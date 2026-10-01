"""Requirement: load scheme JSON and decide eligibility with deterministic rules."""

import json
import operator
import re
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, Literal, TypedDict

Verdict = Literal["eligible", "not_eligible", "need_more_info"]
AnswerValue = bool | int | float | None


class EligibilityReason(TypedDict):
	question_id: str
	text_key: str
	kind: Literal["criterion_not_met", "missing_answer"]
	expected: AnswerValue
	actual: AnswerValue


class EligibilityResult(TypedDict):
	verdict: Verdict
	reasons: list[EligibilityReason]


SCHEMES_DIR = Path(__file__).resolve().parent.parent / "data" / "schemes"
COMPARATORS: dict[str, Callable[[Any, Any], bool]] = {
	"eq": operator.eq,
	"ne": operator.ne,
	"gt": operator.gt,
	"gte": operator.ge,
	"lt": operator.lt,
	"lte": operator.le,
}
SCHEME_ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9_-]*\Z")


def load_scheme(scheme_id: str, schemes_dir: Path | None = None) -> dict[str, Any]:
	"""Load and validate one scheme file from the configured schemes directory."""
	if not SCHEME_ID_PATTERN.fullmatch(scheme_id):
		raise ValueError("Scheme ID must contain only lowercase letters, digits, _ or -.")

	directory = schemes_dir or SCHEMES_DIR
	scheme_path = directory / f"{scheme_id}.json"
	with scheme_path.open(encoding="utf-8") as scheme_file:
		scheme = json.load(scheme_file)
	_question_map(scheme)
	return scheme


def next_unanswered_question(
	scheme: Mapping[str, Any], answers: Mapping[str, Any] | None = None
) -> dict[str, Any] | None:
	"""Return the first unanswered question in the scheme's declared order."""
	question_map = _question_map(scheme)
	valid_answers = _validated_answers(question_map, answers or {})
	for question in scheme["questions"]:
		if question["id"] not in valid_answers:
			return question
	return None


def evaluate_eligibility(
	scheme: Mapping[str, Any], answers: Mapping[str, Any]
) -> EligibilityResult:
	"""Evaluate every supplied answer against the scheme's declared criteria."""
	question_map = _question_map(scheme)
	valid_answers = _validated_answers(question_map, answers)
	failed_criteria: list[EligibilityReason] = []

	for criterion in scheme["criteria"]:
		question_id = criterion["question_id"]
		if question_id not in valid_answers:
			continue
		answer = valid_answers[question_id]
		if not _criterion_matches(answer, criterion["operator"], criterion["value"]):
			failed_criteria.append(
				{
					"question_id": question_id,
					"text_key": question_map[question_id]["text_key"],
					"kind": "criterion_not_met",
					"expected": criterion["value"],
					"actual": answer,
				}
			)

	if failed_criteria:
		return {"verdict": "not_eligible", "reasons": failed_criteria}

	missing_reasons: list[EligibilityReason] = []
	for question in scheme["questions"]:
		question_id = question["id"]
		if question_id not in valid_answers:
			missing_reasons.append(
				{
					"question_id": question_id,
					"text_key": question["text_key"],
					"kind": "missing_answer",
					"expected": None,
					"actual": None,
				}
			)

	if missing_reasons:
		return {"verdict": "need_more_info", "reasons": missing_reasons}
	return {"verdict": "eligible", "reasons": []}


def _question_map(scheme: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
	questions = scheme.get("questions")
	criteria = scheme.get("criteria")
	if not isinstance(questions, list) or not isinstance(criteria, list):
		raise ValueError("Scheme must define question and criteria lists.")

	question_map: dict[str, Mapping[str, Any]] = {}
	for question in questions:
		if not isinstance(question, Mapping):
			raise ValueError("Each question must be an object.")
		question_id = question.get("id")
		question_type = question.get("type")
		if not isinstance(question_id, str) or not question_id:
			raise ValueError("Each question must have a non-empty ID.")
		if question_id in question_map:
			raise ValueError(f"Duplicate question ID: {question_id}")
		if question_type not in {"yes_no", "number"}:
			raise ValueError(f"Unsupported question type for {question_id}.")
		if not isinstance(question.get("text_key"), str):
			raise ValueError(f"Question {question_id} must have a text key.")
		question_map[question_id] = question

	for criterion in criteria:
		if not isinstance(criterion, Mapping):
			raise ValueError("Each criterion must be an object.")
		question_id = criterion.get("question_id")
		operation = criterion.get("operator")
		if question_id not in question_map:
			raise ValueError(f"Criterion references unknown question: {question_id}")
		if operation not in COMPARATORS:
			raise ValueError(f"Unsupported criterion operator: {operation}")
		expected = criterion.get("value")
		question_type = question_map[question_id]["type"]
		if question_type == "yes_no" and not isinstance(expected, bool):
			raise ValueError(f"Criterion for {question_id} must use a boolean value.")
		if question_type == "number" and (
			not isinstance(expected, (int, float)) or isinstance(expected, bool)
		):
			raise ValueError(f"Criterion for {question_id} must use a numeric value.")
	return question_map


def _validated_answers(
	question_map: Mapping[str, Mapping[str, Any]], answers: Mapping[str, Any]
) -> dict[str, AnswerValue]:
	if not isinstance(answers, Mapping):
		raise ValueError("Answers must be an object keyed by question ID.")

	valid_answers: dict[str, AnswerValue] = {}
	for question_id, answer in answers.items():
		if question_id not in question_map or answer is None:
			continue
		question_type = question_map[question_id]["type"]
		if question_type == "yes_no" and not isinstance(answer, bool):
			raise ValueError(f"Answer for {question_id} must be yes/no (boolean).")
		if question_type == "number" and (
			not isinstance(answer, (int, float)) or isinstance(answer, bool)
		):
			raise ValueError(f"Answer for {question_id} must be numeric.")
		valid_answers[question_id] = answer
	return valid_answers


def _criterion_matches(answer: AnswerValue, operation: str, expected: Any) -> bool:
	try:
		return COMPARATORS[operation](answer, expected)
	except TypeError as error:
		raise ValueError("Criterion compares incompatible values.") from error