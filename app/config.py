"""Requirement: configure supported languages and Gemini from environment variables."""

import os

SUPPORTED_LANGS = {
	"hi-IN": {"native_name": "हिन्दी", "greeting": "नमस्ते।"},
	"ta-IN": {"native_name": "தமிழ்", "greeting": "வணக்கம்."},
	"te-IN": {"native_name": "తెలుగు", "greeting": "నమస్కారం."},
	"bn-IN": {"native_name": "বাংলা", "greeting": "নমস্কার।"},
	"mr-IN": {"native_name": "मराठी", "greeting": "नमस्कार."},
	"kn-IN": {"native_name": "ಕನ್ನಡ", "greeting": "ನಮಸ್ಕಾರ."},
}
SUPPORTED_LANGUAGES = tuple(SUPPORTED_LANGS)
LANGUAGE_ALIASES = {
	"hindi": "hi-IN",
	"tamil": "ta-IN",
	"telugu": "te-IN",
	"bengali": "bn-IN",
	"marathi": "mr-IN",
	"kannada": "kn-IN",
}
LANGUAGE_ALIASES.update(
	{details["native_name"].casefold(): code for code, details in SUPPORTED_LANGS.items()}
)


def get_gemini_api_key() -> str:
	"""Return the configured Google AI Studio API key without a code fallback."""
	api_key = os.getenv("GEMINI_API_KEY", "").strip()
	if not api_key:
		raise RuntimeError("GEMINI_API_KEY is not configured.")
	return api_key


def get_gemini_model() -> str:
	"""Return the selected Gemini model; never supply a hardcoded model ID."""
	model = os.getenv("GEMINI_MODEL", "").strip()
	if not model:
		raise RuntimeError("GEMINI_MODEL is not configured.")
	return model


def get_default_language() -> str:
	"""Return DEFAULT_LANG when supported, otherwise use the Hindi locale."""
	language = os.getenv("DEFAULT_LANG", "hi-IN").strip()
	return language if language in SUPPORTED_LANGS else "hi-IN"


def map_detected_language(detected: str | None, default: str | None = None) -> str:
	"""Map model output to a supported locale, safely falling back to DEFAULT_LANG."""
	candidate = detected.strip().casefold().replace("_", "-") if detected else ""
	for code in SUPPORTED_LANGS:
		if candidate == code.casefold() or candidate == code.split("-")[0]:
			return code
	if candidate in LANGUAGE_ALIASES:
		return LANGUAGE_ALIASES[candidate]

	safe_default = default or get_default_language()
	return safe_default if safe_default in SUPPORTED_LANGS else "hi-IN"