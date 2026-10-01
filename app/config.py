"""Requirement: configure supported languages and Gemini from environment variables."""

import os

from dotenv import load_dotenv

load_dotenv()

SUPPORTED_LANGS = {
    "hi-IN": {
        "native_name": "हिन्दी",
        "greeting": "नमस्ते।",
        "unclear": "मैं समझ नहीं पाई।",
        "off_topic": "मैं केवल उज्ज्वला योजना की जानकारी में मदद कर सकती हूँ।",
        "retry": "कृपया फिर से कोशिश करें।",
        "unavailable": "सेवा अभी उपलब्ध नहीं है। कृपया बाद में कोशिश करें।",
        "rate_limited": "अभी बहुत अनुरोध हैं। कृपया थोड़ी देर बाद कोशिश करें।",
        "invalid_model": "सेवा का मॉडल अभी उपलब्ध नहीं है। कृपया बाद में कोशिश करें।",
        "invalid_key": "सेवा की अनुमति में समस्या है। कृपया LPG वितरक से पूछें।",
        "ask_distributor": "इसकी जानकारी यहाँ नहीं है। कृपया LPG वितरक से पूछें।",
        "yes_variants": ["yes", "yeah", "yep", "haan", "han", "हाँ", "हां", "जी"],
        "no_variants": ["no", "nope", "nahi", "nahin", "नहीं", "नही", "ना"],
    },
    "ta-IN": {
        "native_name": "தமிழ்",
        "greeting": "வணக்கம்.",
        "unclear": "எனக்குப் புரியவில்லை.",
        "off_topic": "உஜ்வாலா திட்டம் பற்றிய தகவலில் மட்டுமே உதவ முடியும்.",
        "retry": "மீண்டும் சொல்லுங்கள்.",
        "unavailable": "சேவை இப்போது கிடைக்கவில்லை. பின்னர் முயற்சிக்கவும்.",
        "rate_limited": "இப்போது பல கோரிக்கைகள் உள்ளன. சிறிது நேரம் கழித்து முயற்சிக்கவும்.",
        "invalid_model": "சேவை இப்போது கிடைக்கவில்லை. பின்னர் முயற்சிக்கவும்.",
        "invalid_key": "சேவை அனுமதியில் சிக்கல் உள்ளது. LPG விநியோகஸ்தரிடம் கேளுங்கள்.",
        "ask_distributor": "இந்தத் தகவல் இங்கே இல்லை. LPG விநியோகஸ்தரிடம் கேளுங்கள்.",
        "yes_variants": ["yes", "haan", "ஆம்", "ஆமாம்", "சரி"],
        "no_variants": ["no", "nahi", "இல்லை", "இல்ல"],
    },
    "te-IN": {
        "native_name": "తెలుగు",
        "greeting": "నమస్కారం.",
        "unclear": "నాకు అర్థం కాలేదు.",
        "off_topic": "ఉజ్వల పథకం సమాచారం కోసం మాత్రమే సహాయం చేయగలను.",
        "retry": "దయచేసి మళ్లీ చెప్పండి.",
        "unavailable": "సేవ ఇప్పుడు అందుబాటులో లేదు. తర్వాత ప్రయత్నించండి.",
        "rate_limited": "ఇప్పుడు చాలా అభ్యర్థనలు ఉన్నాయి. కొద్దిసేపటి తర్వాత ప్రయత్నించండి.",
        "invalid_model": "సేవ ఇప్పుడు అందుబాటులో లేదు. తర్వాత ప్రయత్నించండి.",
        "invalid_key": "సేవ అనుమతిలో సమస్య ఉంది. LPG పంపిణీదారుని అడగండి.",
        "ask_distributor": "ఈ సమాచారం ఇక్కడ లేదు. LPG పంపిణీదారుని అడగండి.",
        "yes_variants": ["yes", "haan", "అవును", "అవునండి", "సరే"],
        "no_variants": ["no", "nahi", "కాదు", "లేదు"],
    },
    "bn-IN": {
        "native_name": "বাংলা",
        "greeting": "নমস্কার।",
        "unclear": "আমি বুঝতে পারিনি।",
        "off_topic": "আমি শুধু উজ্জ্বলা যোজনার তথ্য দিতে পারি।",
        "retry": "দয়া করে আবার বলুন।",
        "unavailable": "পরিষেবা এখন পাওয়া যাচ্ছে না। পরে চেষ্টা করুন।",
        "rate_limited": "এখন অনেক অনুরোধ আসছে। একটু পরে চেষ্টা করুন।",
        "invalid_model": "পরিষেবা এখন পাওয়া যাচ্ছে না। পরে চেষ্টা করুন।",
        "invalid_key": "পরিষেবার অনুমতিতে সমস্যা হয়েছে। LPG পরিবেশকের কাছে জিজ্ঞাসা করুন।",
        "ask_distributor": "এই তথ্য এখানে নেই। LPG পরিবেশকের কাছে জিজ্ঞাসা করুন।",
        "yes_variants": ["yes", "haan", "হ্যাঁ", "হ্যা", "জি"],
        "no_variants": ["no", "nahi", "না", "নয়"],
    },
    "mr-IN": {
        "native_name": "मराठी",
        "greeting": "नमस्कार.",
        "unclear": "मला समजले नाही.",
        "off_topic": "मी फक्त उज्ज्वला योजनेची माहिती देऊ शकते.",
        "retry": "कृपया पुन्हा सांगा.",
        "unavailable": "सेवा आत्ता उपलब्ध नाही. नंतर प्रयत्न करा.",
        "rate_limited": "आत्ता खूप विनंत्या आहेत. थोड्या वेळाने प्रयत्न करा.",
        "invalid_model": "सेवा आत्ता उपलब्ध नाही. नंतर प्रयत्न करा.",
        "invalid_key": "सेवेच्या परवानगीची अडचण आहे. LPG वितरकाला विचारा.",
        "ask_distributor": "ही माहिती इथे नाही. LPG वितरकाला विचारा.",
        "yes_variants": ["yes", "haan", "हो", "होय", "जी"],
        "no_variants": ["no", "nahi", "नाही", "नाय"],
    },
    "kn-IN": {
        "native_name": "ಕನ್ನಡ",
        "greeting": "ನಮಸ್ಕಾರ.",
        "unclear": "ನನಗೆ ಅರ್ಥವಾಗಲಿಲ್ಲ.",
        "off_topic": "ಉಜ್ವಲ ಯೋಜನೆಯ ಮಾಹಿತಿಗೆ ಮಾತ್ರ ಸಹಾಯ ಮಾಡಬಲ್ಲೆ.",
        "retry": "ದಯವಿಟ್ಟು ಮತ್ತೆ ಹೇಳಿ.",
        "unavailable": "ಸೇವೆ ಈಗ ಲಭ್ಯವಿಲ್ಲ. ನಂತರ ಪ್ರಯತ್ನಿಸಿ.",
        "rate_limited": "ಈಗ ಹಲವು ವಿನಂತಿಗಳಿವೆ. ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಪ್ರಯತ್ನಿಸಿ.",
        "invalid_model": "ಸೇವೆ ಈಗ ಲಭ್ಯವಿಲ್ಲ. ನಂತರ ಪ್ರಯತ್ನಿಸಿ.",
        "invalid_key": "ಸೇವೆಯ ಅನುಮತಿಯಲ್ಲಿ ತೊಂದರೆ ಇದೆ. LPG ವಿತರಕರನ್ನು ಕೇಳಿ.",
        "ask_distributor": "ಈ ಮಾಹಿತಿ ಇಲ್ಲಿಲ್ಲ. LPG ವಿತರಕರನ್ನು ಕೇಳಿ.",
        "yes_variants": ["yes", "haan", "ಹೌದು", "ಹೌದ", "ಸರಿ"],
        "no_variants": ["no", "nahi", "ಇಲ್ಲ", "ಅಲ್ಲ"],
    },
}
LANGUAGE_ALIASES = {
    "hindi": "hi-IN",
    "tamil": "ta-IN",
    "telugu": "te-IN",
    "bengali": "bn-IN",
    "marathi": "mr-IN",
    "kannada": "kn-IN",
}
LANGUAGE_ALIASES.update(
    {
        details["native_name"].casefold(): code
        for code, details in SUPPORTED_LANGS.items()
    }
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


def get_gemini_tts_model() -> str:
    """Return the configured free-tier Gemini speech-generation model."""
    model = os.getenv("GEMINI_TTS_MODEL", "").strip()
    if not model:
        raise RuntimeError("GEMINI_TTS_MODEL is not configured.")
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


def get_rate_limit() -> int:
    """Return the per-process limit, using a safe fallback for bad configuration."""
    try:
        return max(1, int(os.getenv("RATE_LIMIT_PER_MINUTE", "30")))
    except ValueError:
        return 30


def get_language_message(language: str, key: str) -> str:
    """Return a localized message for a supported language."""
    selected = language if language in SUPPORTED_LANGS else get_default_language()
    return SUPPORTED_LANGS[selected][key]
