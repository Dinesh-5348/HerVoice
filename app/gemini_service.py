"""Requirement: understand turns and phrase grounded replies with Gemini."""

import asyncio
import base64
import json
from typing import Any

from pydantic import ValidationError

from app.config import (
	SUPPORTED_LANGS,
	get_gemini_api_key,
	get_gemini_model,
	map_detected_language,
)
from app.schemas import LocalizedReply, UnderstandingResult


class UnderstandingError(RuntimeError):
	"""Raised when Gemini cannot return a valid answer for the current question."""


GENERATION_ATTEMPTS = 3
BACKOFF_SECONDS = 0.2


def _generate_structured_content_sync(
	prompt: str,
	*,
	audio_bytes: bytes | None,
	mime: str | None,
	text: str | None = None,
	response_schema: type[UnderstandingResult] | type[LocalizedReply],
) -> str:
	from google import genai
	from google.genai import types

	content: list[str | types.Part] = [prompt]
	if audio_bytes is not None:
		content.append(
			types.Part.from_bytes(data=audio_bytes, mime_type=mime or "audio/webm")
		)
	elif text is not None:
		content.append(types.Part.from_text(text=text))
	response = genai.Client(api_key=get_gemini_api_key()).models.generate_content(
		model=get_gemini_model(),
		contents=content,
		config=types.GenerateContentConfig(
			response_mime_type="application/json",
			response_schema=response_schema,
		),
	)
	return response.text or ""


async def _generate_with_retry(*args: Any, **kwargs: Any) -> str:
	"""Retry transient Gemini request failures with a short exponential backoff."""
	for attempt in range(GENERATION_ATTEMPTS):
		try:
			return await asyncio.to_thread(
				_generate_structured_content_sync, *args, **kwargs
			)
		except Exception:
			if attempt + 1 == GENERATION_ATTEMPTS:
				raise
			await asyncio.sleep(BACKOFF_SECONDS * (2**attempt))
	raise AssertionError("Gemini retry loop ended unexpectedly.")


def _validate_answer_type(answer: Any, question: dict[str, Any]) -> None:
	if answer is None:
		raise ValueError("No answer was understood.")
	if question["type"] == "yes_no" and not isinstance(answer, bool):
		raise ValueError("Expected a yes/no answer.")
	if question["type"] == "number" and (
		not isinstance(answer, (int, float)) or isinstance(answer, bool)
	):
		raise ValueError("Expected a number answer.")


async def understand(
	*,
	audio_b64: str | None,
	mime: str | None,
	text: str | None,
	lang_hint: str | None,
	question: dict[str, Any],
) -> UnderstandingResult:
	"""Understand direct audio or text and validate one answer, retrying bad JSON once."""
	audio_bytes = base64.b64decode(audio_b64, validate=True) if audio_b64 else None
	hint = lang_hint or "not provided"
	prompt = (
		"You are HerVoice's answer parser. Detect the user's spoken or written "
		f"language using only: {', '.join(SUPPORTED_LANGS)}. The language hint "
		f"is {hint}; use it only if it matches the input. The current question is "
		f"{json.dumps(question, ensure_ascii=False)}. Return only detected_lang and "
		"the answer to this question. Return a boolean for type yes_no, a number "
		"for type number, and null only when the input does not answer the question. "
		"Do not infer answers from unrelated input."
	)
	last_error: Exception | None = None
	for attempt in range(2):
		retry_prompt = prompt
		if attempt:
			retry_prompt += " Your previous output was invalid; return valid matching JSON."
		try:
			raw_result = await _generate_with_retry(
				retry_prompt,
				audio_bytes=audio_bytes,
				mime=mime,
				text=text,
				response_schema=UnderstandingResult,
			)
			understood = UnderstandingResult.model_validate_json(raw_result)
			understood.detected_lang = map_detected_language(
				understood.detected_lang, lang_hint
			)
			_validate_answer_type(understood.answer, question)
			return understood
		except (ValidationError, ValueError) as error:
			last_error = error
		except Exception as error:
			raise UnderstandingError("Gemini understanding failed.") from error
	raise UnderstandingError("Gemini returned invalid understanding JSON.") from last_error


async def respond(
	*,
	lang: str,
	scheme: dict[str, Any],
	question: dict[str, Any] | None,
	verdict: str | None,
	reasons: list[dict[str, Any]],
) -> str:
	"""Phrase a simple localized question or verdict from scheme JSON facts only."""
	facts = {
		"name": scheme["name"],
		"short_description": scheme["short_description"],
		"criteria": scheme["criteria"],
		"documents": scheme["documents"],
		"where_to_apply": scheme["where_to_apply"],
		"source_url": scheme["source_url"],
	}
	prompt = (
		f"Write a short, very simple reply in locale {lang}. Use only facts from this "
		f"scheme JSON: {json.dumps(facts, ensure_ascii=False)}. Do not add facts, "
		"advice, steps, fees, promises, or eligibility rules not present there. "
	)
	if question is not None:
		task = {
			"task": "Ask exactly the next question in simple language.",
			"question": {
				"id": question["id"],
				"type": question["type"],
				"text_key": question["text_key"],
			},
		}
	else:
		task = {
			"task": "State the deterministic eligibility verdict simply.",
			"verdict": verdict,
			"reason_keys": [reason["text_key"] for reason in reasons],
		}
	prompt += f" Task: {json.dumps(task, ensure_ascii=False)}"
	try:
		raw_reply = await _generate_with_retry(
			prompt,
			audio_bytes=None,
			mime=None,
			text=None,
			response_schema=LocalizedReply,
		)
		return LocalizedReply.model_validate_json(raw_reply).reply_text
	except Exception as error:
		raise RuntimeError("Gemini response phrasing failed.") from error