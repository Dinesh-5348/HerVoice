"""Requirement: connect stateless turns to Gemini and deterministic scheme rules."""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from app.config import (
    get_default_language,
    get_gemini_api_key,
    get_language_message,
)
from app.gemini_service import (
    GeminiServiceError,
    MalformedModelOutput,
    gemini_health_check,
    respond,
    synthesize_speech,
    understand,
)
from app.rules import evaluate_eligibility, load_scheme, next_unanswered_question
from app.schemas import SpeechRequest, TurnRequest, TurnResponse, TurnState

logger = logging.getLogger(__name__)
router = APIRouter()
SCHEME_ID = "ujjwala"


def _step_for(scheme: dict[str, Any], question: dict[str, Any] | None) -> int:
    if question is None:
        return len(scheme["questions"])
    return next(
        index
        for index, item in enumerate(scheme["questions"])
        if item["id"] == question["id"]
    )


def _append_recent_turns(
    state: TurnState, user_text: str | None, reply: str
) -> list[dict[str, str]]:
    recent_turns = [turn.model_dump() for turn in state.recent_turns]
    if user_text:
        recent_turns.append({"role": "user", "text": user_text[:1200]})
    recent_turns.append({"role": "assistant", "text": reply[:1200]})
    return recent_turns[-4:]


def _log_stage_error(stage: str, error: Exception, turn: TurnRequest) -> None:
    message = str(error)
    try:
        api_key = get_gemini_api_key()
    except RuntimeError:
        api_key = ""
    if api_key:
        message = message.replace(api_key, "[redacted]")
    private_texts = [turn.text or ""] + [item.text for item in turn.state.recent_turns]
    for private_text in private_texts:
        if private_text:
            message = message.replace(private_text, "[user text redacted]")
    message = " ".join(message.split())[:400]
    logger.error(
        "turn stage=%s exception_type=%s message=%s",
        stage,
        type(error).__name__,
        message,
    )


def _localized_error(
    language: str,
    state: TurnState,
    error: Exception,
) -> JSONResponse:
    if isinstance(error, MalformedModelOutput):
        code = "malformed_output"
        status_code = 200
        message_key = "unclear"
    elif isinstance(error, GeminiServiceError):
        if error.kind == "malformed_output":
            code, status_code, message_key = "malformed_output", 200, "unclear"
        elif error.kind == "invalid_key":
            code, status_code, message_key = "invalid_key", 503, "invalid_key"
        elif error.kind == "invalid_model":
            code, status_code, message_key = "invalid_model", 503, "invalid_model"
        elif error.kind == "rate_limited":
            code, status_code, message_key = "rate_limited", 429, "rate_limited"
        else:
            code, status_code, message_key = "unavailable", 503, "unavailable"
    else:
        code, status_code, message_key = "unavailable", 503, "unavailable"

    response = TurnResponse(
        lang=language,
        reply_text=get_language_message(language, message_key),
        state=state,
        done=False,
        error_code=code,
    )
    return JSONResponse(
        status_code=status_code,
        content=response.model_dump(mode="json"),
        headers={"Cache-Control": "no-store"},
    )


@router.post("/api/turn", response_model=TurnResponse)
async def api_turn(turn: TurnRequest) -> TurnResponse | JSONResponse:
    language = turn.lang_hint or get_default_language()
    try:
        scheme = load_scheme(SCHEME_ID)
        answers = dict(turn.state.answers)
        question = next_unanswered_question(scheme, answers)
    except Exception as error:
        _log_stage_error("rules", error, turn)
        return _localized_error(language, turn.state, error)

    if question is None:
        return _localized_error(
            language,
            turn.state,
            ValueError("No unanswered scheme question remains."),
        )

    try:
        understanding = await understand(
            audio_b64=turn.audio_b64,
            mime=turn.mime,
            text=turn.text,
            lang_hint=turn.lang_hint,
            question=question,
            recent_turns=[item.model_dump() for item in turn.state.recent_turns],
        )
        language = understanding.detected_lang
    except Exception as error:
        _log_stage_error("understand", error, turn)
        return _localized_error(language, turn.state, error)

    intent = understanding.intent
    if intent == "answer" and understanding.answer is None:
        intent = "unclear"

    if intent != "answer":
        try:
            reply = await respond(
                lang=language,
                scheme=scheme,
                question=question,
                verdict=None,
                reasons=[],
                intent=intent,
                user_text=turn.text,
                recent_turns=[item.model_dump() for item in turn.state.recent_turns],
            )
        except Exception as error:
            _log_stage_error("respond", error, turn)
            return _localized_error(language, turn.state, error)
        response_state = TurnState(
            answers=answers,
            step=_step_for(scheme, question),
            recent_turns=_append_recent_turns(turn.state, turn.text, reply),
        )
        return TurnResponse(
            lang=language,
            reply_text=reply,
            state=response_state,
            done=False,
            speech_cache_key=question["id"],
            question_id=question["id"],
            question_type=question["type"],
        )

    try:
        answers[question["id"]] = understanding.answer
        result = evaluate_eligibility(scheme, answers)
        next_question = (
            next_unanswered_question(scheme, answers)
            if result["verdict"] == "need_more_info"
            else None
        )
    except Exception as error:
        _log_stage_error("rules", error, turn)
        return _localized_error(language, turn.state, error)

    done = result["verdict"] != "need_more_info"
    checklist = scheme["documents"] if result["verdict"] == "eligible" else []
    try:
        reply = await respond(
            lang=language,
            scheme=scheme,
            question=next_question,
            verdict=result["verdict"] if done else None,
            reasons=result["reasons"],
            intent="answer",
            recent_turns=[item.model_dump() for item in turn.state.recent_turns],
        )
    except Exception as error:
        _log_stage_error("respond", error, turn)
        return _localized_error(language, turn.state, error)

    response_state = TurnState(
        answers=answers,
        step=_step_for(scheme, next_question),
        recent_turns=_append_recent_turns(
            turn.state,
            turn.text if turn.text is not None else str(understanding.answer),
            reply,
        ),
    )
    return TurnResponse(
        lang=language,
        reply_text=reply,
        state=response_state,
        done=done,
        checklist=checklist,
        speech_cache_key=next_question["id"] if next_question is not None else None,
        question_id=next_question["id"] if next_question is not None else None,
        question_type=next_question["type"] if next_question is not None else None,
    )


@router.post("/api/speak")
async def api_speak(request: SpeechRequest) -> Response:
    try:
        audio = await synthesize_speech(request.text, request.lang)
    except Exception as error:
        logger.error("speech generation failed: %s", error)
        raise HTTPException(
            status_code=503, detail="Speech generation failed."
        ) from error
    return Response(
        content=audio,
        media_type="audio/wav",
        headers={"Cache-Control": "no-store"},
    )


@router.get("/healthz/gemini")
async def gemini_health() -> dict[str, bool | str]:
    try:
        await gemini_health_check()
    except Exception as error:
        return {"ok": False, "error_type": type(error).__name__}
    return {"ok": True}
