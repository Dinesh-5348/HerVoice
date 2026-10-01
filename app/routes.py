"""Requirement: connect the stateless turn API to Gemini and deterministic rules."""

from typing import Any

from fastapi import APIRouter

from app.config import get_default_language
from app.gemini_service import UnderstandingError, respond, understand
from app.rules import evaluate_eligibility, load_scheme, next_unanswered_question
from app.schemas import TurnRequest, TurnResponse, TurnState

router = APIRouter()
SCHEME_ID = "ujjwala"
RETRY_REPLIES = {
	"hi-IN": "कृपया फिर से कोशिश करें।",
	"ta-IN": "தயவுசெய்து மீண்டும் முயற்சிக்கவும்.",
	"te-IN": "దయచేసి మళ్లీ ప్రయత్నించండి.",
	"bn-IN": "দয়া করে আবার চেষ্টা করুন।",
	"mr-IN": "कृपया पुन्हा प्रयत्न करा.",
	"kn-IN": "ದಯವಿಟ್ಟು ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
}


def _step_for(scheme: dict[str, Any], question: dict[str, Any] | None) -> int:
	if question is None:
		return len(scheme["questions"])
	return next(
		index
		for index, item in enumerate(scheme["questions"])
		if item["id"] == question["id"]
	)


def _retry_response(language: str, state: TurnState) -> TurnResponse:
	return TurnResponse(
		lang=language,
		reply_text=RETRY_REPLIES[language],
		state=state,
		done=False,
		checklist=[],
	)


@router.post("/api/turn", response_model=TurnResponse)
async def api_turn(turn: TurnRequest) -> TurnResponse:
	scheme = load_scheme(SCHEME_ID)
	answers = dict(turn.state.answers)
	language = turn.lang_hint or get_default_language()
	question = next_unanswered_question(scheme, answers)

	if question is not None:
		try:
			understanding = await understand(
				audio_b64=turn.audio_b64,
				mime=turn.mime,
				text=turn.text,
				lang_hint=turn.lang_hint,
				question=question,
			)
			language = understanding.detected_lang
			if understanding.answer is None:
				return _retry_response(language, turn.state)
			answers[question["id"]] = understanding.answer
		except (UnderstandingError, ValueError):
			return _retry_response(language, turn.state)

	result = evaluate_eligibility(scheme, answers)
	if result["verdict"] == "need_more_info":
		next_question = next_unanswered_question(scheme, answers)
		if next_question is None:
			return _retry_response(language, turn.state)
		done = False
		reply_question = next_question
		checklist: list[dict[str, str]] = []
	else:
		done = True
		reply_question = None
		checklist = scheme["documents"] if result["verdict"] == "eligible" else []

	response_state = TurnState(
		answers=answers,
		step=_step_for(scheme, next_question if not done else None),
	)
	try:
		reply = await respond(
			lang=language,
			scheme=scheme,
			question=reply_question,
			verdict=result["verdict"] if done else None,
			reasons=result["reasons"],
		)
	except Exception:
		return _retry_response(language, turn.state)
	return TurnResponse(
		lang=language,
		reply_text=reply,
		state=response_state,
		done=done,
		checklist=checklist,
	)