"""Requirement tests: only tested language detections map to supported locales."""

import asyncio
import json

import pytest

from app import gemini_service
from app.config import SUPPORTED_LANGS, get_default_language, map_detected_language


@pytest.mark.parametrize(
    ("model_language", "expected_code"),
    [
        ("hi", "hi-IN"),
        ("Tamil", "ta-IN"),
        ("te-IN", "te-IN"),
        ("বাংলা", "bn-IN"),
        ("मराठी", "mr-IN"),
        ("ಕನ್ನಡ", "kn-IN"),
    ],
)
def test_detected_language_maps_to_each_tested_locale(
    model_language: str, expected_code: str, monkeypatch
) -> None:
    assert expected_code in SUPPORTED_LANGS
    assert SUPPORTED_LANGS[expected_code]["native_name"]
    assert SUPPORTED_LANGS[expected_code]["greeting"]

    def fake_generate(prompt: str, **kwargs: object) -> str:
        return json.dumps({"detected_lang": model_language, "answer": True})

    monkeypatch.setattr(
        gemini_service, "_generate_structured_content_sync", fake_generate
    )
    result = asyncio.run(
        gemini_service.understand(
            audio_b64=None,
            mime=None,
            text="answer",
            lang_hint=None,
            question={"id": "q", "type": "yes_no", "text_key": "q"},
        )
    )

    assert result.detected_lang == expected_code


def test_unsupported_detection_falls_back_to_default_lang(monkeypatch) -> None:
    monkeypatch.setenv("DEFAULT_LANG", "kn-IN")

    assert map_detected_language("en-US") == "kn-IN"


def test_unsupported_or_invalid_default_uses_safe_supported_fallback(
    monkeypatch,
) -> None:
    monkeypatch.setenv("DEFAULT_LANG", "xx-XX")

    assert get_default_language() == "hi-IN"
    assert map_detected_language("English", "xx-XX") == "hi-IN"


def test_transient_gemini_rate_limit_retries_with_short_backoff(monkeypatch) -> None:
    calls = 0
    delays: list[float] = []

    def fake_generate(prompt: str, **kwargs: object) -> str:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise RuntimeError("429 rate limit")
        return json.dumps({"detected_lang": "hi-IN", "answer": True})

    async def fake_sleep(delay: float) -> None:
        delays.append(delay)

    monkeypatch.setattr(
        gemini_service, "_generate_structured_content_sync", fake_generate
    )
    monkeypatch.setattr(gemini_service.asyncio, "sleep", fake_sleep)
    result = asyncio.run(
        gemini_service.understand(
            audio_b64=None,
            mime=None,
            text="yes",
            lang_hint="hi-IN",
            question={"id": "q", "type": "yes_no", "text_key": "q"},
        )
    )

    assert result.detected_lang == "hi-IN"
    assert calls == 2
    assert delays == [gemini_service.BACKOFF_SECONDS]
