"""Requirement tests: scheme JSON drives deterministic eligibility decisions."""

import json

import pytest

from app.rules import (
    evaluate_eligibility,
    load_scheme,
    next_unanswered_question,
)


@pytest.fixture
def scheme() -> dict:
    return load_scheme("ujjwala")


def eligible_answers() -> dict[str, bool | int]:
    return {
        "applicant_is_woman": True,
        "applicant_age": 30,
        "poor_household": True,
        "household_has_lpg": False,
    }


def test_all_matching_criteria_are_eligible(scheme: dict) -> None:
    result = evaluate_eligibility(scheme, eligible_answers())

    assert result == {"verdict": "eligible", "reasons": []}


def test_failed_criterion_is_not_eligible(scheme: dict) -> None:
    answers = eligible_answers() | {"applicant_age": 17}

    result = evaluate_eligibility(scheme, answers)

    assert result["verdict"] == "not_eligible"
    assert result["reasons"] == [
        {
            "question_id": "applicant_age",
            "text_key": "applicant_age",
            "kind": "criterion_not_met",
            "expected": 18,
            "actual": 17,
        }
    ]


def test_missing_answers_need_more_info(scheme: dict) -> None:
    result = evaluate_eligibility(scheme, {"applicant_is_woman": True})

    assert result["verdict"] == "need_more_info"
    assert [reason["question_id"] for reason in result["reasons"]] == [
        "applicant_age",
        "poor_household",
        "household_has_lpg",
    ]


def test_next_question_skips_answered_questions(scheme: dict) -> None:
    question = next_unanswered_question(
        scheme, {"applicant_is_woman": False, "applicant_age": 42}
    )

    assert question is not None
    assert question["id"] == "poor_household"


def test_no_next_question_when_all_answers_are_present(scheme: dict) -> None:
    assert next_unanswered_question(scheme, eligible_answers()) is None


def test_unknown_answer_keys_are_ignored(scheme: dict) -> None:
    result = evaluate_eligibility(scheme, {"unlisted_question": True})

    assert result["verdict"] == "need_more_info"
    assert result["reasons"][0]["question_id"] == "applicant_is_woman"


def test_answer_type_must_match_question_type(scheme: dict) -> None:
    with pytest.raises(ValueError, match="boolean"):
        evaluate_eligibility(scheme, {"applicant_is_woman": "yes"})

    with pytest.raises(ValueError, match="numeric"):
        evaluate_eligibility(scheme, {"applicant_age": True})


def test_scheme_id_cannot_escape_schemes_directory() -> None:
    with pytest.raises(ValueError, match="Scheme ID"):
        load_scheme("../secret")


def test_new_scheme_json_uses_the_same_engine(tmp_path) -> None:
    new_scheme = {
        "id": "sample",
        "questions": [{"id": "count", "type": "number", "text_key": "count"}],
        "criteria": [{"question_id": "count", "operator": "gte", "value": 2}],
    }
    (tmp_path / "sample.json").write_text(json.dumps(new_scheme), encoding="utf-8")

    loaded_scheme = load_scheme("sample", tmp_path)

    assert evaluate_eligibility(loaded_scheme, {"count": 2}) == {
        "verdict": "eligible",
        "reasons": [],
    }
