"""Requirement tests: the turn API uses mocked Gemini and stores no server state."""

import asyncio
import base64
import json

import pytest
from fastapi.testclient import TestClient

from app import gemini_service, routes
from app.config import get_gemini_tts_model
from app.gemini_service import (
    GeminiServiceError,
    MalformedModelOutput,
    UnderstandingError,
)
from app.main import app
from app.rules import load_scheme
from app.schemas import (
    GeminiReplySchema,
    GeminiUnderstandingSchema,
    UnderstandingResult,
)

client = TestClient(app)


def _mock_understanding(language: str, answer: bool | int):
    async def understand(**kwargs):
        return UnderstandingResult(detected_lang=language, answer=answer)

    return understand


def _mock_response(text: str = "localized reply"):
    async def respond(**kwargs):
        return text

    return respond


def test_text_turn_advances_with_mocked_gemini(monkeypatch) -> None:
    monkeypatch.setattr(routes, "understand", _mock_understanding("hi-IN", True))
    monkeypatch.setattr(routes, "respond", _mock_response("अगला सवाल"))

    response = client.post("/api/turn", json={"text": "हाँ", "lang_hint": "hi-IN"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["lang"] == "hi-IN"
    assert payload["reply_text"] == "अगला सवाल"
    assert payload["state"]["answers"] == {"applicant_is_woman": True}
    assert payload["state"]["step"] == 1
    assert len(payload["state"]["recent_turns"]) == 2
    assert payload["done"] is False
    assert payload["checklist"] == []


def test_audio_turn_passes_recording_directly_to_gemini(monkeypatch) -> None:
    received: dict = {}

    async def mock_understand(**kwargs):
        received.update(kwargs)
        return UnderstandingResult(detected_lang="ta-IN", answer=True)

    monkeypatch.setattr(routes, "understand", mock_understand)
    monkeypatch.setattr(routes, "respond", _mock_response("அடுத்த கேள்வி"))
    recording = base64.b64encode(b"recorded audio").decode("ascii")

    response = client.post(
        "/api/turn",
        json={
            "audio_b64": recording,
            "mime": "audio/webm",
            "lang_hint": "ta-IN",
        },
    )

    assert response.status_code == 200
    assert received["audio_b64"] == recording
    assert received["mime"] == "audio/webm"
    assert received["text"] is None


def test_final_answer_uses_rules_and_returns_checklist(monkeypatch) -> None:
    monkeypatch.setattr(routes, "understand", _mock_understanding("kn-IN", False))
    monkeypatch.setattr(routes, "respond", _mock_response("ಮಾಹಿತಿ ಪೂರ್ಣವಾಗಿದೆ"))
    state = {
        "answers": {
            "applicant_is_woman": True,
            "applicant_age": 30,
            "poor_household": True,
        },
        "step": 3,
    }

    response = client.post(
        "/api/turn", json={"text": "ಇಲ್ಲ", "state": state, "lang_hint": "kn-IN"}
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["done"] is True
    assert payload["state"]["answers"]["household_has_lpg"] is False
    assert len(payload["checklist"]) == 7


def test_ineligible_answer_completes_without_checklist(monkeypatch) -> None:
    monkeypatch.setattr(routes, "understand", _mock_understanding("mr-IN", True))
    monkeypatch.setattr(routes, "respond", _mock_response("निकष पूर्ण होत नाहीत"))
    state = {
        "answers": {
            "applicant_is_woman": True,
            "applicant_age": 30,
            "poor_household": True,
        },
        "step": 3,
    }

    response = client.post(
        "/api/turn", json={"text": "नाही", "state": state, "lang_hint": "mr-IN"}
    )

    assert response.status_code == 200
    assert response.json()["done"] is True
    assert response.json()["checklist"] == []


def test_understanding_failure_returns_localized_repeat_and_keeps_state(
    monkeypatch,
) -> None:
    async def failed_understanding(**kwargs):
        raise UnderstandingError("invalid model output")

    monkeypatch.setattr(routes, "understand", failed_understanding)

    response = client.post(
        "/api/turn",
        json={
            "text": "எனக்குப் புரியவில்லை",
            "lang_hint": "ta-IN",
            "state": {"answers": {}, "step": 0},
        },
    )

    assert response.status_code == 200
    assert response.json()["error_code"] == "malformed_output"
    assert response.json()["reply_text"] == "எனக்குப் புரியவில்லை."
    assert response.json()["state"] == {"answers": {}, "step": 0}
    assert response.json()["done"] is False


def test_response_failure_returns_localized_retry_and_keeps_state(monkeypatch) -> None:
    monkeypatch.setattr(routes, "understand", _mock_understanding("ta-IN", True))

    async def failed_response(**kwargs):
        raise RuntimeError("Gemini unavailable")

    monkeypatch.setattr(routes, "respond", failed_response)
    prior_state = {"answers": {}, "step": 0}

    response = client.post(
        "/api/turn",
        json={"text": "ஆம்", "lang_hint": "ta-IN", "state": prior_state},
    )

    assert response.status_code == 503
    assert response.json()["error_code"] == "unavailable"
    assert response.json()["reply_text"] == "சேவை இப்போது கிடைக்கவில்லை. பின்னர் முயற்சிக்கவும்."
    assert response.json()["state"] == prior_state


@pytest.mark.parametrize(
    ("failure", "status", "error_code", "message"),
    [
        (
            GeminiServiceError("invalid_key", "hidden detail", 503),
            503,
            "invalid_key",
            "सेवा की अनुमति में समस्या है। कृपया LPG वितरक से पूछें।",
        ),
        (
            GeminiServiceError("invalid_model", "hidden detail", 503),
            503,
            "invalid_model",
            "सेवा का मॉडल अभी उपलब्ध नहीं है। कृपया बाद में कोशिश करें।",
        ),
        (
            GeminiServiceError("rate_limited", "hidden detail", 429),
            429,
            "rate_limited",
            "अभी बहुत अनुरोध हैं। कृपया थोड़ी देर बाद कोशिश करें।",
        ),
        (MalformedModelOutput(), 200, "malformed_output", "मैं समझ नहीं पाई।"),
    ],
)
def test_gemini_failure_types_return_localized_messages(
    monkeypatch, failure, status: int, error_code: str, message: str
) -> None:
    async def failed_understanding(**kwargs):
        raise failure

    monkeypatch.setattr(routes, "understand", failed_understanding)

    response = client.post(
        "/api/turn", json={"text": "yes", "lang_hint": "hi-IN"}
    )

    assert response.status_code == status
    assert response.json()["error_code"] == error_code
    assert response.json()["reply_text"] == message


def test_gemini_health_check_has_no_sensitive_error_details(monkeypatch) -> None:
    async def failed_health_check():
        raise GeminiServiceError("invalid_key", "secret error details", 503)

    monkeypatch.setattr(routes, "gemini_health_check", failed_health_check)

    response = client.get("/healthz/gemini")

    assert response.status_code == 200
    assert response.json() == {"ok": False, "error_type": "GeminiServiceError"}


def test_bad_gemini_json_gets_one_retry(monkeypatch) -> None:
    outputs = iter(
        [
            '{"detected_lang":"hi-IN","answer":"yes"}',
            '{"detected_lang":"hi-IN","answer":true}',
        ]
    )
    calls = 0

    def generate(prompt, **kwargs):
        nonlocal calls
        calls += 1
        return next(outputs)

    monkeypatch.setattr(gemini_service, "_generate_structured_content_sync", generate)

    result = asyncio.run(
        gemini_service.understand(
            audio_b64=None,
            mime=None,
            text="हाँ",
            lang_hint="hi-IN",
            question={
                "id": "applicant_is_woman",
                "type": "yes_no",
                "text_key": "applicant_is_woman",
            },
        )
    )

    assert calls == 2
    assert result.answer is True


def test_response_prompt_uses_question_and_facts_from_scheme_json(monkeypatch) -> None:
    prompts: list[str] = []

    def generate(prompt: str, **kwargs: object) -> str:
        prompts.append(prompt)
        return json.dumps({"reply_text": "अगला सवाल"}, ensure_ascii=False)

    monkeypatch.setattr(gemini_service, "_generate_structured_content_sync", generate)
    scheme = load_scheme("ujjwala")
    question = scheme["questions"][2]

    reply = asyncio.run(
        gemini_service.respond(
            lang="hi-IN",
            scheme=scheme,
            question=question,
            verdict=None,
            reasons=[],
        )
    )

    assert reply == "अगला सवाल"
    assert len(prompts) == 1
    assert question["text"] in prompts[0]
    assert scheme["source_url"] in prompts[0]
    assert scheme["documents"][0]["label"] in prompts[0]
    assert scheme["where_to_apply"] in prompts[0]


def test_gemini_response_schemas_avoid_unsupported_additional_properties() -> None:
    assert "additionalProperties" not in GeminiUnderstandingSchema.model_json_schema()
    assert "additionalProperties" not in GeminiReplySchema.model_json_schema()


def test_invalid_turn_input_is_rejected_before_gemini() -> None:
    response = client.post("/api/turn", json={"text": " ", "lang_hint": "hi-IN"})

    assert response.status_code == 422


def test_input_length_is_limited() -> None:
    response = client.post("/api/turn", json={"text": "x" * 4001})

    assert response.status_code == 422


def test_speak_endpoint_returns_mocked_audio_without_gemini(monkeypatch) -> None:
    received: dict[str, str] = {}

    async def mock_speech(text: str, language: str) -> bytes:
        received.update(text=text, language=language)
        return b"RIFF-test-wave"

    monkeypatch.setattr(routes, "synthesize_speech", mock_speech)

    response = client.post("/api/speak", json={"text": "नमस्ते।", "lang": "hi-IN"})

    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/wav"
    assert response.headers["cache-control"] == "no-store"
    assert response.content == b"RIFF-test-wave"
    assert received == {"text": "नमस्ते।", "language": "hi-IN"}


def test_speak_endpoint_rejects_oversized_text() -> None:
    response = client.post("/api/speak", json={"text": "x" * 4001, "lang": "hi-IN"})

    assert response.status_code == 422


def test_tts_model_is_required_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("GEMINI_TTS_MODEL", "gemini-3.8-flash-lite-tts")

    assert get_gemini_tts_model() == "gemini-3.8-flash-lite-tts"
