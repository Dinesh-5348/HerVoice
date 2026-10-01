"""Requirement tests: the turn API uses mocked Gemini and stores no server state."""

import asyncio
import base64

from fastapi.testclient import TestClient

from app import gemini_service, routes
from app.gemini_service import UnderstandingError
from app.main import app
from app.schemas import UnderstandingResult

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
    assert payload["state"] == {"answers": {"applicant_is_woman": True}, "step": 1}
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


def test_understanding_failure_returns_localized_repeat_and_keeps_state(monkeypatch) -> None:
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
    assert response.json()["reply_text"] == "தயவுசெய்து மீண்டும் முயற்சிக்கவும்."
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

    assert response.status_code == 200
    assert response.json()["reply_text"] == "தயவுசெய்து மீண்டும் முயற்சிக்கவும்."
    assert response.json()["state"] == prior_state


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
            question={"id": "applicant_is_woman", "type": "yes_no", "text_key": "applicant_is_woman"},
        )
    )

    assert calls == 2
    assert result.answer is True


def test_invalid_turn_input_is_rejected_before_gemini() -> None:
    response = client.post("/api/turn", json={"text": " ", "lang_hint": "hi-IN"})

    assert response.status_code == 422


def test_input_length_is_limited() -> None:
    response = client.post("/api/turn", json={"text": "x" * 4001})

    assert response.status_code == 422