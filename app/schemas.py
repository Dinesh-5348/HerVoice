"""Requirement: validate bounded stateless API turns and their responses."""

import base64
import binascii
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    model_validator,
)

LanguageCode = Literal["hi-IN", "ta-IN", "te-IN", "bn-IN", "mr-IN", "kn-IN"]
Intent = Literal["answer", "question", "greeting", "unclear", "off_topic"]
TurnErrorCode = Literal[
    "invalid_key",
    "invalid_model",
    "rate_limited",
    "malformed_output",
    "unavailable",
]
SpeechCacheKey = Literal[
    "greeting",
    "applicant_is_woman",
    "applicant_age",
    "poor_household",
    "household_has_lpg",
]
AnswerValue = StrictBool | StrictInt | StrictFloat


class ConversationTurn(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Literal["user", "assistant"]
    text: str = Field(min_length=1, max_length=1200)


class TurnState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answers: dict[str, AnswerValue] = Field(default_factory=dict, max_length=50)
    step: int = Field(default=0, ge=0, le=50)
    recent_turns: list[ConversationTurn] = Field(default_factory=list, max_length=4)


class TurnRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audio_b64: str | None = Field(default=None, max_length=11_184_812)
    mime: str | None = Field(default=None, max_length=100)
    text: str | None = Field(default=None, max_length=4000)
    lang_hint: LanguageCode | None = None
    state: TurnState = Field(default_factory=TurnState)

    @model_validator(mode="after")
    def validate_input(self) -> "TurnRequest":
        has_audio = self.audio_b64 is not None
        has_text = self.text is not None and bool(self.text.strip())
        if has_audio == has_text:
            raise ValueError("Provide exactly one of audio_b64 or text.")
        if has_audio:
            if not self.mime or not self.mime.startswith("audio/"):
                raise ValueError("Audio input requires an audio MIME type.")
            try:
                audio = base64.b64decode(self.audio_b64 or "", validate=True)
            except (binascii.Error, ValueError) as error:
                raise ValueError("audio_b64 must contain valid base64.") from error
            if len(audio) > 8 * 1024 * 1024:
                raise ValueError("Audio must not exceed 8 MB.")
        elif self.mime is not None:
            raise ValueError("mime is only valid with audio_b64.")
        return self


class UnderstandingResult(BaseModel):
    """Requirement: constrain Gemini understanding to language and one typed answer."""

    model_config = ConfigDict(extra="forbid")

    detected_lang: str = Field(min_length=2, max_length=40)
    intent: Intent = "answer"
    answer: AnswerValue | None = None


class GeminiUnderstandingSchema(BaseModel):
    """Requirement: provide a Gemini-compatible structured output schema."""

    detected_lang: str = Field(min_length=2, max_length=40)
    intent: Intent
    answer: AnswerValue | None


class ChecklistItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    icon_name: str
    label: str


class TurnResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lang: LanguageCode
    reply_text: str = Field(min_length=1, max_length=4000)
    state: TurnState
    done: bool
    checklist: list[ChecklistItem] = Field(default_factory=list, max_length=50)
    speech_cache_key: SpeechCacheKey | None = None
    question_id: str | None = None
    question_type: Literal["yes_no", "number"] | None = None
    error_code: TurnErrorCode | None = None


class SpeechRequest(BaseModel):
    """Requirement: bound text and locale for the no-device-voice speech fallback."""

    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1, max_length=4000)
    lang: LanguageCode


class LocalizedReply(BaseModel):
    """Requirement: validate Gemini's simple-language response text."""

    model_config = ConfigDict(extra="forbid")

    reply_text: str = Field(min_length=1, max_length=4000)


class GeminiReplySchema(BaseModel):
    """Requirement: provide a Gemini-compatible localized reply schema."""

    reply_text: str = Field(min_length=1, max_length=4000)
