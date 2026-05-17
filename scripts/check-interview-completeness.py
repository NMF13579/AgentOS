#!/usr/bin/env python3
"""M45 Interview completeness checker.

All expected checker output, including RESULT, must be written to stdout.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATUSES = {
    "INTERVIEW_DRAFT",
    "INTERVIEW_NEEDS_CLARIFICATION",
    "INTERVIEW_READY_FOR_SPEC",
    "INTERVIEW_BLOCKED",
}

REQUIRED_FIELDS = [
    "interview_id",
    "created_at",
    "interview_status",
    "source_user_input",
    "idea_summary",
    "problem_summary",
    "target_users",
    "current_workaround",
    "desired_outcome",
    "success_criteria",
    "constraints",
    "risks",
    "non_goals",
    "unknowns",
    "assumptions",
    "answered_questions",
    "unanswered_questions",
    "follow_up_questions",
    "non_approval_warning",
]

REQUIRED_COMPLETENESS_FIELDS = [
    "problem_summary",
    "target_users",
    "desired_outcome",
    "success_criteria",
]

BOUNDARY_FIELDS = ["constraints", "risks", "non_goals"]

NON_APPROVAL_WARNING_CONST = (
    "Interview evidence is not approval. Interview readiness does not authorize "
    "implementation, task creation, queue entry creation, autopilot, commit, push, "
    "merge, release, or deployment."
)

RESULT_EXIT = {
    "COMPLETENESS_COMPLETE": 0,
    "COMPLETENESS_INCOMPLETE": 1,
    "COMPLETENESS_NEEDS_CLARIFICATION": 1,
    "COMPLETENESS_BLOCKED": 1,
    "COMPLETENESS_CHECK_FAILED": 2,
}

REASON_DRAFT = (
    "If interview_status is INTERVIEW_DRAFT and no higher-priority failure exists, "
    "result must be COMPLETENESS_NEEDS_CLARIFICATION."
)
REASON_CLAR = (
    "If interview_status is INTERVIEW_NEEDS_CLARIFICATION and no higher-priority "
    "failure exists, result must be COMPLETENESS_NEEDS_CLARIFICATION."
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Check interview answer record completeness")
    p.add_argument("record_path", help="Path to interview answer record JSON")
    p.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    p.add_argument("--explain", action="store_true", help="Print detailed explanation")
    p.add_argument("--strict", action="store_true", help="Reserved strict mode flag")
    return p.parse_args()


def _is_missing_text(value: Any) -> bool:
    return not isinstance(value, str) or value.strip() == "" or value == "MISSING_FROM_INTERVIEW"


def build_result(record_path: Path) -> dict[str, Any]:
    result = {
        "result": "COMPLETENESS_CHECK_FAILED",
        "record_path": str(record_path),
        "interview_status": "UNKNOWN",
        "missing_fields": [],
        "incomplete_fields": [],
        "unknown_without_followup": False,
        "blockers": [],
        "warnings": [],
    }

    if not record_path.exists() or not record_path.is_file():
        result["blockers"].append("Record path does not exist or is not a file")
        return result

    try:
        data = json.loads(record_path.read_text(encoding="utf-8"))
    except Exception as exc:  # malformed / unreadable
        result["blockers"].append(f"Malformed JSON: {exc}")
        return result

    if not isinstance(data, dict):
        result["blockers"].append("Record root must be a JSON object")
        return result

    missing_fields = [f for f in REQUIRED_FIELDS if f not in data]
    result["missing_fields"] = missing_fields
    if missing_fields:
        result["blockers"].append("Required fields are missing")
        return result

    status = data.get("interview_status")
    result["interview_status"] = str(status)

    if status not in ALLOWED_STATUSES:
        result["blockers"].append("Invalid interview_status")
        return result

    if data.get("non_approval_warning") != NON_APPROVAL_WARNING_CONST:
        result["blockers"].append("non_approval_warning is missing or not exact")
        return result

    # basic type checks for required arrays
    for arr_field in [
        "unknowns",
        "assumptions",
        "answered_questions",
        "unanswered_questions",
        "follow_up_questions",
    ]:
        if not isinstance(data.get(arr_field), list):
            result["missing_fields"].append(arr_field)

    if result["missing_fields"]:
        result["blockers"].append("Required list fields are not arrays")
        result["result"] = "COMPLETENESS_CHECK_FAILED"
        return result

    if status == "INTERVIEW_BLOCKED":
        result["result"] = "COMPLETENESS_BLOCKED"
        result["blockers"].append("Interview status is INTERVIEW_BLOCKED")
        return result

    incomplete_fields: list[str] = []

    for fld in REQUIRED_COMPLETENESS_FIELDS:
        if _is_missing_text(data.get(fld)):
            incomplete_fields.append(fld)

    for fld in BOUNDARY_FIELDS:
        val = data.get(fld)
        if _is_missing_text(val):
            incomplete_fields.append(fld)

    result["incomplete_fields"] = incomplete_fields

    unknowns = data.get("unknowns", [])
    follow_up = data.get("follow_up_questions", [])
    if isinstance(unknowns, list) and len(unknowns) > 0 and isinstance(follow_up, list) and len(follow_up) == 0:
        result["unknown_without_followup"] = True

    # priority order after CHECK_FAILED/BLOCKED
    if result["unknown_without_followup"]:
        result["result"] = "COMPLETENESS_INCOMPLETE"
        result["warnings"].append("Unknowns without follow_up_questions are incomplete interview evidence")
        return result

    if incomplete_fields:
        result["result"] = "COMPLETENESS_NEEDS_CLARIFICATION"
        result["warnings"].append("Interview status cannot override missing information")
        return result

    if status == "INTERVIEW_DRAFT":
        result["result"] = "COMPLETENESS_NEEDS_CLARIFICATION"
        result["warnings"].append(REASON_DRAFT)
        return result

    if status == "INTERVIEW_NEEDS_CLARIFICATION":
        result["result"] = "COMPLETENESS_NEEDS_CLARIFICATION"
        result["warnings"].append(REASON_CLAR)
        return result

    # only status left is INTERVIEW_READY_FOR_SPEC and all checks pass
    result["result"] = "COMPLETENESS_COMPLETE"
    return result


def print_text_output(payload: dict[str, Any], explain: bool) -> None:
    print(f"RESULT: {payload['result']}")
    print(f"INTERVIEW_STATUS: {payload['interview_status']}")
    print(f"RECORD_PATH: {payload['record_path']}")

    if payload["missing_fields"]:
        print("MISSING_FIELDS:")
        for item in payload["missing_fields"]:
            print(f"- {item}")

    if payload["incomplete_fields"]:
        print("INCOMPLETE_FIELDS:")
        for item in payload["incomplete_fields"]:
            print(f"- {item}")

    if payload["unknown_without_followup"]:
        print("UNKNOWN_WITHOUT_FOLLOWUP:")
        print("- true")

    if payload["blockers"]:
        print("BLOCKERS:")
        for item in payload["blockers"]:
            print(f"- {item}")

    if payload["warnings"]:
        print("WARNINGS:")
        for item in payload["warnings"]:
            print(f"- {item}")

    if explain:
        print("EXPLAIN:")
        print("- Completeness check is not approval.")
        print("- Completeness check does not authorize implementation.")
        print("- Completeness check does not authorize M46 by itself.")


def main() -> int:
    args = parse_args()
    payload = build_result(Path(args.record_path))

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_text_output(payload, args.explain)

    return RESULT_EXIT[payload["result"]]


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # unexpected internal diagnostics only
        print(f"UNEXPECTED_INTERNAL_ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
