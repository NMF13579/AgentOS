#!/usr/bin/env python3
"""False PASS resistance checker.

Validation PASS is not approval.
Validation PASS is not completion.
Human review remains required.
M67 does not start M68.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Validation PASS is not approval.
# Validation PASS is not completion.
# Human review remains required.
# M67 does not start M68.

RESULT_PASS = "M67_FALSE_PASS_CHECK_PASS"
RESULT_PASS_WITH_WARNINGS = "M67_FALSE_PASS_CHECK_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "M67_FALSE_PASS_CHECK_BLOCKED"
RESULT_NOT_ENOUGH_EVIDENCE = "M67_FALSE_PASS_CHECK_NOT_ENOUGH_EVIDENCE"

CONTRACT_VERSION = "1.0.0"
PACKAGE_TYPE = "false_pass_check_input"

ALLOWED_M66_RESULTS = {
    "M66_UNIFIED_RUN_PASS",
    "M66_UNIFIED_RUN_PASS_WITH_WARNINGS",
    "M66_UNIFIED_RUN_BLOCKED",
    "M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE",
}

ALLOWED_HUMAN_REVIEW_STATUSES = {
    "not_requested",
    "pending",
    "reviewed",
    "approved_by_human",
    "rejected_by_human",
    "blocked",
}

ALLOWED_CONTEXT_TYPES = {
    "operative",
    "safe_boundary",
    "documentation_example",
    "fixture_name",
    "negative_fixture_description",
    "policy_explanation",
}

FORBIDDEN_FIELD_NAMES = {
    "approved",
    "task_approved",
    "task_accepted",
    "task_complete",
    "task_completed",
    "completion_approved",
    "completion_authorized",
    "completion_gate_passed",
    "completion_gate_inferred",
    "human_review_not_required",
    "skip_human_review",
    "merge_authorized",
    "push_authorized",
    "release_authorized",
    "deployment_authorized",
    "production_ready",
    "ready_for_production",
    "m68_started_automatically",
    "m68_auto_started",
    "lifecycle_mutated",
    "completion_state_applied",
    "automatic_completion_allowed",
}

FORBIDDEN_PHRASES = {
    "approval": [
        "task approved",
        "task accepted",
        "task accepted by system",
        "approved by system",
        "validation approved task",
        "m66 pass approved task",
        "m67 pass approved task",
        "runner approved task",
        "checker approved task",
        "evidence approved task",
        "evidence report approved task",
        "completion approved by checker",
        "system approval granted",
    ],
    "completion": [
        "task completed",
        "task complete",
        "task marked complete",
        "task moved to complete",
        "completion approved",
        "completion authorized",
        "completion accepted",
        "m66 pass completed task",
        "m67 pass completed task",
        "runner completed task",
        "checker completed task",
        "evidence report completed task",
        "completion review completed task as lifecycle mutation",
        "task can be closed automatically",
        "automatic completion allowed",
    ],
    "completion_gate": [
        "completion gate passed",
        "completion gate approved",
        "completion gate allowed",
        "completion gate authorized",
        "gate passed",
        "gate approved",
        "gate result pass",
        "ready to complete automatically",
        "completion gate satisfied by m66 pass",
        "completion gate satisfied by m67 pass",
        "completion gate inferred from validation",
    ],
    "human_review_waiver": [
        "human review not required",
        "human review waived",
        "human review skipped",
        "skip human review",
        "checker replaces human review",
        "runner replaces human review",
        "fixtures replace human review",
        "evidence report replaces human review",
        "validation pass replaces human review",
        "automatic review accepted",
    ],
    "lifecycle_mutation": [
        "task state updated to complete",
        "task lifecycle mutated",
        "task moved to completed",
        "completion state applied",
        "controlled mutation applied",
        "automatic completion mutation performed",
        "lifecycle transition applied",
        "state machine advanced",
        "task status changed to done",
        "task closed by validation",
    ],
    "merge_push_release": [
        "merge authorized",
        "push authorized",
        "release authorized",
        "deployment authorized",
        "deploy authorized",
        "production ready",
        "ready for production",
        "ship it",
        "safe to deploy",
        "safe to release",
        "ready to merge",
        "ready to push",
    ],
    "m68": [
        "m68 started automatically",
        "ready_for_m68 started m68",
        "m68 implementation authorized",
        "m68 artifacts created by m67",
        "m68 can begin without separate task",
        "m68 may proceed automatically",
        "m68 task chain started",
        "m68 milestone created by this checker",
    ],
}

SAFE_BOUNDARY_PHRASES = {
    "this is not approval.",
    "this does not complete the task.",
    "human review remains required.",
    "validation pass is not approval.",
    "validation pass is not completion.",
    "validation pass is not completion gate pass.",
    "completion gate remains separate.",
    "completion gate was not executed.",
    "completion gate requires explicit policy.",
    "runner proof is evidence, not authorization.",
    "m67 does not start m68.",
    "ready_for_m68 is roadmap readiness only.",
    "m67 result is not approval.",
    "m67 result does not complete tasks.",
    "m67 result does not mutate lifecycle state.",
    "m67 result does not start m68.",
    "m67 result does not authorize merge, push, release, or deployment.",
    "completion gate cannot be inferred from m66 pass.",
    "completion gate cannot be inferred from m67 pass.",
    "completion gate requires explicit human review status.",
}

SAFE_EXAMPLE_MARKERS = {
    "example",
    "unsafe example",
    "forbidden example",
    "negative fixture",
    "expected blocked case",
    "must block",
    "should block",
}

AMBIGUOUS_TERMS = {
    "approved",
    "accepted",
    "complete",
    "completed",
    "waived",
    "authorized",
    "production ready",
    "ready for production",
    "ship it",
    "safe to deploy",
    "safe to release",
    "ready to merge",
    "ready to push",
}

REQUIRED_NON_AUTHORITY_PHRASES = [
    "m67 result is not approval.",
    "m67 result does not complete tasks.",
    "m67 result does not mutate lifecycle state.",
    "m67 result does not start m68.",
    "human review remains required.",
]


def normalize(text: Any) -> str:
    return re.sub(r"[^a-z0-9_]+", " ", str(text).lower()).strip()


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def scan_forbidden_fields(node: Any, path: str = "") -> List[Dict[str, str]]:
    found: List[Dict[str, str]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            key_norm = str(key).lower()
            current_path = f"{path}.{key}" if path else str(key)
            if key_norm in FORBIDDEN_FIELD_NAMES:
                found.append({"path": current_path, "field": str(key)})
            found.extend(scan_forbidden_fields(value, current_path))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            current_path = f"{path}[{index}]"
            found.extend(scan_forbidden_fields(item, current_path))
    return found


def phrase_hits(text: Any, phrases: List[str]) -> List[str]:
    normalized = normalize(text)
    hits = [phrase for phrase in phrases if normalize(phrase) in normalized]
    return hits


def safe_boundary_present(text: Any) -> bool:
    normalized = normalize(text)
    return any(normalize(phrase) in normalized for phrase in SAFE_BOUNDARY_PHRASES)


def example_marker_present(text: Any) -> bool:
    normalized = normalize(text)
    return any(normalize(marker) in normalized for marker in SAFE_EXAMPLE_MARKERS)


def scan_generic_text(
    text: Any,
    path: str,
    *,
    strict: bool,
    warnings: List[str],
    blockers: List[str],
    not_enough: List[str],
    forbidden_claims_found: List[Dict[str, Any]],
    ambiguous_claims: List[Dict[str, Any]],
) -> None:
    if not isinstance(text, str):
        return

    normalized = normalize(text)
    any_hits: List[Tuple[str, str]] = []
    for category, phrases in FORBIDDEN_PHRASES.items():
        for phrase in phrases:
            if normalize(phrase) in normalized:
                any_hits.append((category, phrase))

    if safe_boundary_present(text):
        return

    if any_hits:
        if example_marker_present(text):
            warnings.append(f"{path}: forbidden wording appears in clearly marked example")
            return

        if strict:
            blockers.append(f"{path}: forbidden claim under strict mode")
        else:
            blockers.append(f"{path}: forbidden claim")

        for category, phrase in any_hits:
            forbidden_claims_found.append(
                {
                    "path": path,
                    "category": category,
                    "phrase": phrase,
                    "text": text,
                }
            )
        return

    ambiguous_hits = [term for term in AMBIGUOUS_TERMS if normalize(term) in normalized]
    if ambiguous_hits:
        if strict:
            blockers.append(f"{path}: ambiguous approval/completion wording under strict mode")
        else:
            warnings.append(f"{path}: ambiguous approval/completion wording")
            not_enough.append(f"{path}: ambiguous approval/completion wording")
        ambiguous_claims.append(
            {
                "path": path,
                "text": text,
                "reason": "ambiguous approval/completion wording",
                "matches": ambiguous_hits,
            }
        )


def non_authority_boundary_ok(values: Any) -> Tuple[bool, List[str]]:
    if not isinstance(values, list) or not values:
        return False, []

    normalized_values = [normalize(v) for v in values if isinstance(v, str)]
    matched: List[str] = []
    for phrase in REQUIRED_NON_AUTHORITY_PHRASES:
        if any(normalize(phrase) in item for item in normalized_values):
            matched.append(phrase)
    return len(matched) == len(REQUIRED_NON_AUTHORITY_PHRASES), matched


def validate_claims(
    claims: Any,
    *,
    strict: bool,
    warnings: List[str],
    blockers: List[str],
    not_enough: List[str],
    forbidden_claims_found: List[Dict[str, Any]],
    ambiguous_claims: List[Dict[str, Any]],
    safe_context_detected: List[bool],
) -> None:
    if claims is None:
        blockers.append("claims missing")
        return
    if not isinstance(claims, list):
        blockers.append("claims wrong type")
        return
    if not claims:
        not_enough.append("claims empty")
        return

    for index, claim in enumerate(claims):
        path = f"claims[{index}]"
        if not isinstance(claim, dict):
            blockers.append(f"{path} wrong type")
            continue

        claim_id = claim.get("claim_id")
        source = claim.get("source")
        text = claim.get("text")
        context_type = claim.get("context_type")

        if claim_id is None or source is None or text is None or context_type is None:
            blockers.append(f"{path} missing required fields")
            continue
        if not is_non_empty_string(text) or not is_non_empty_string(context_type):
            blockers.append(f"{path} invalid text or context_type")
            continue
        if context_type not in ALLOWED_CONTEXT_TYPES:
            blockers.append(f"{path} invalid context_type: {context_type}")
            continue

        if context_type in {
            "safe_boundary",
            "documentation_example",
            "fixture_name",
            "negative_fixture_description",
            "policy_explanation",
        }:
            safe_context_detected[0] = True

        if context_type == "operative":
            normalized = normalize(text)
            hits = []
            for category, phrases in FORBIDDEN_PHRASES.items():
                for phrase in phrases:
                    if normalize(phrase) in normalized:
                        hits.append((category, phrase))
            if hits:
                for category, phrase in hits:
                    forbidden_claims_found.append(
                        {
                            "claim_id": claim_id,
                            "source": source,
                            "context_type": context_type,
                            "category": category,
                            "phrase": phrase,
                            "text": text,
                        }
                    )
                blockers.append(f"{path} contains forbidden operative claim")
            continue

        if context_type == "safe_boundary":
            if safe_boundary_present(text):
                continue
            if any(normalize(phrase) in normalize(text) for phrase in sum(FORBIDDEN_PHRASES.values(), [])) or any(
                normalize(term) in normalize(text) for term in AMBIGUOUS_TERMS
            ):
                if strict:
                    blockers.append(f"{path} unsafe boundary wording under strict mode")
                else:
                    ambiguous_claims.append(
                        {
                            "claim_id": claim_id,
                            "source": source,
                            "context_type": context_type,
                            "text": text,
                            "reason": "unsafe boundary wording not clearly marked",
                        }
                    )
                    not_enough.append(f"{path}: unsafe boundary wording not clearly marked")
            continue

        if context_type == "documentation_example":
            if example_marker_present(text) or safe_boundary_present(text):
                continue
            if any(normalize(phrase) in normalize(text) for phrase in sum(FORBIDDEN_PHRASES.values(), [])) or any(
                normalize(term) in normalize(text) for term in AMBIGUOUS_TERMS
            ):
                if strict:
                    blockers.append(f"{path} ambiguous documentation example under strict mode")
                else:
                    ambiguous_claims.append(
                        {
                            "claim_id": claim_id,
                            "source": source,
                            "context_type": context_type,
                            "text": text,
                            "reason": "documentation example is not clearly marked",
                        }
                    )
                    not_enough.append(f"{path}: documentation example is not clearly marked")
            continue

        if context_type in {"fixture_name", "negative_fixture_description", "policy_explanation"}:
            continue


def validate_completion_gate(
    completion_gate: Any,
    *,
    strict: bool,
    warnings: List[str],
    blockers: List[str],
    not_enough: List[str],
    forbidden_claims_found: List[Dict[str, Any]],
    ambiguous_claims: List[Dict[str, Any]],
) -> Tuple[bool, bool, bool]:
    """Return (requested, evidence_present, human_approved)."""
    if completion_gate is None:
        not_enough.append("completion_gate missing")
        return False, False, False
    if not isinstance(completion_gate, dict):
        blockers.append("completion_gate wrong type")
        return False, False, False

    requested = completion_gate.get("completion_gate_requested")
    allowed = completion_gate.get("completion_gate_allowed")
    result = completion_gate.get("completion_gate_result")
    evidence = completion_gate.get("completion_gate_evidence")
    policy_ref = completion_gate.get("completion_gate_policy_reference")

    if requested is None:
        not_enough.append("completion_gate_requested missing")
    elif not isinstance(requested, bool):
        blockers.append("completion_gate_requested wrong type")

    if result is not None and not isinstance(result, str):
        blockers.append("completion_gate_result wrong type")

    if allowed is not None and not isinstance(allowed, bool):
        blockers.append("completion_gate_allowed wrong type")

    evidence_present = is_non_empty_string(evidence) or is_non_empty_string(policy_ref)
    human_approved = False
    if isinstance(completion_gate.get("human_review_status"), str):
        human_approved = completion_gate.get("human_review_status") == "approved_by_human"

    if requested is True and not evidence_present:
        not_enough.append("completion_gate requested but evidence missing")

    if requested is False and result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
        blockers.append("completion gate pass inferred without request")

    if result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
        if not evidence_present or not human_approved:
            blockers.append("completion gate pass claimed without explicit evidence and human approval")
        if allowed is True and (not evidence_present or not human_approved):
            blockers.append("completion_gate_allowed true without explicit gate evidence and human approval evidence")

    if allowed is True and (not evidence_present or not human_approved):
        blockers.append("completion_gate_allowed true without explicit gate evidence and human approval evidence")

    # Scan any extra strings in the completion gate object, but keep explicit enum fields permissive.
    for key, value in completion_gate.items():
        if key in {"completion_gate_requested", "completion_gate_allowed", "completion_gate_result"}:
            continue
        if isinstance(value, str):
            scan_generic_text(
                value,
                f"completion_gate.{key}",
                strict=strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )
        elif isinstance(value, (dict, list)):
            scan_nested_generic(
                value,
                f"completion_gate.{key}",
                strict=strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )

    return requested is True, evidence_present, human_approved


def validate_human_review(
    human_review: Any,
    *,
    strict: bool,
    warnings: List[str],
    blockers: List[str],
    not_enough: List[str],
    forbidden_claims_found: List[Dict[str, Any]],
    ambiguous_claims: List[Dict[str, Any]],
) -> Optional[str]:
    if human_review is None:
        not_enough.append("human_review missing")
        return None
    if not isinstance(human_review, dict):
        blockers.append("human_review wrong type")
        return None

    required = human_review.get("human_review_required")
    status = human_review.get("human_review_status")

    if required is not True:
        blockers.append("human_review_required must be true")

    if status is None:
        not_enough.append("human_review_status missing")
        return None
    if not isinstance(status, str):
        blockers.append("human_review_status wrong type")
        return None
    if status not in ALLOWED_HUMAN_REVIEW_STATUSES:
        blockers.append(f"human_review_status invalid: {status}")

    evidence = human_review.get("human_review_evidence")
    if isinstance(evidence, str):
        scan_generic_text(
            evidence,
            "human_review.human_review_evidence",
            strict=strict,
            warnings=warnings,
            blockers=blockers,
            not_enough=not_enough,
            forbidden_claims_found=forbidden_claims_found,
            ambiguous_claims=ambiguous_claims,
        )
    elif isinstance(evidence, (dict, list)):
        scan_nested_generic(
            evidence,
            "human_review.human_review_evidence",
            strict=strict,
            warnings=warnings,
            blockers=blockers,
            not_enough=not_enough,
            forbidden_claims_found=forbidden_claims_found,
            ambiguous_claims=ambiguous_claims,
        )

    return status


def scan_nested_generic(
    node: Any,
    path: str,
    *,
    strict: bool,
    warnings: List[str],
    blockers: List[str],
    not_enough: List[str],
    forbidden_claims_found: List[Dict[str, Any]],
    ambiguous_claims: List[Dict[str, Any]],
) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            current_path = f"{path}.{key}"
            if str(key).lower() in FORBIDDEN_FIELD_NAMES:
                forbidden_claims_found.append(
                    {"path": current_path, "field": str(key), "reason": "forbidden operative field"}
                )
                blockers.append(f"{current_path} forbidden operative field")
            if isinstance(value, str):
                scan_generic_text(
                    value,
                    current_path,
                    strict=strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )
            elif isinstance(value, (dict, list)):
                scan_nested_generic(
                    value,
                    current_path,
                    strict=strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )
    elif isinstance(node, list):
        for index, value in enumerate(node):
            current_path = f"{path}[{index}]"
            if isinstance(value, str):
                scan_generic_text(
                    value,
                    current_path,
                    strict=strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )
            elif isinstance(value, (dict, list)):
                scan_nested_generic(
                    value,
                    current_path,
                    strict=strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )


def determine_result(
    blockers: List[str],
    not_enough: List[str],
    warnings: List[str],
) -> str:
    if blockers:
        return RESULT_BLOCKED
    if not_enough:
        return RESULT_NOT_ENOUGH_EVIDENCE
    if warnings:
        return RESULT_PASS_WITH_WARNINGS
    return RESULT_PASS


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only false PASS resistance checker."
    )
    parser.add_argument("--input", required=True, help="Path to the false PASS check input JSON.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Enable stricter ambiguous-claim handling.")

    args = parser.parse_args()

    if not args.json:
        print("error: --json is required", file=sys.stderr)
        return 2

    input_path = Path(args.input)
    if not input_path.exists():
        payload = {
            "result": RESULT_BLOCKED,
            "task_id": None,
            "human_review_required": True,
            "warnings": [],
            "blockers": [f"input file missing: {input_path}"],
            "not_enough_evidence": [],
            "forbidden_claims_found": [],
            "forbidden_fields_found": [],
            "safe_context_detected": False,
            "ambiguous_claims": [],
            "non_authority_boundary": [],
            "exit_code": 1,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 1

    try:
        data = json.loads(input_path.read_text())
    except json.JSONDecodeError as exc:
        payload = {
            "result": RESULT_BLOCKED,
            "task_id": None,
            "human_review_required": True,
            "warnings": [],
            "blockers": [f"invalid JSON: {exc.msg}"],
            "not_enough_evidence": [],
            "forbidden_claims_found": [],
            "forbidden_fields_found": [],
            "safe_context_detected": False,
            "ambiguous_claims": [],
            "non_authority_boundary": [],
            "exit_code": 1,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 1

    except Exception:
        if args.json:
            payload = {
                "result": RESULT_BLOCKED,
                "task_id": None,
                "human_review_required": True,
                "warnings": [],
                "blockers": ["internal checker error while reading input"],
                "not_enough_evidence": [],
                "forbidden_claims_found": [],
                "forbidden_fields_found": [],
                "safe_context_detected": False,
                "ambiguous_claims": [],
                "non_authority_boundary": [],
                "exit_code": 2,
            }
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            print("internal checker error", file=sys.stderr)
        return 2

    blockers: List[str] = []
    not_enough: List[str] = []
    warnings: List[str] = []
    forbidden_claims_found: List[Dict[str, Any]] = []
    forbidden_fields_found: List[Dict[str, str]] = []
    ambiguous_claims: List[Dict[str, Any]] = []
    safe_context_detected = [False]

    if not isinstance(data, dict):
        payload = {
            "result": RESULT_BLOCKED,
            "task_id": None,
            "human_review_required": True,
            "warnings": [],
            "blockers": ["root JSON value must be an object"],
            "not_enough_evidence": [],
            "forbidden_claims_found": [],
            "forbidden_fields_found": [],
            "safe_context_detected": False,
            "ambiguous_claims": [],
            "non_authority_boundary": [],
            "exit_code": 1,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 1

    root_forbidden_fields = scan_forbidden_fields(data, "root")
    forbidden_fields_found.extend(root_forbidden_fields)
    for item in root_forbidden_fields:
        blockers.append(f"{item['path']} forbidden operative field")

    contract_version = data.get("contract_version")
    package_type = data.get("package_type")
    task_id = data.get("task_id")
    m66_result = data.get("m66_result")
    claims = data.get("claims")
    operative_fields = data.get("operative_fields")
    completion_gate = data.get("completion_gate")
    human_review = data.get("human_review")
    non_authority_boundary = data.get("non_authority_boundary")
    input_warnings = data.get("warnings")
    input_blockers = data.get("blockers")

    # Validate fixed package identity.
    if contract_version != CONTRACT_VERSION:
        blockers.append("invalid contract_version")
    if package_type != PACKAGE_TYPE:
        blockers.append("invalid package_type")
    if not is_non_empty_string(task_id):
        blockers.append("task_id missing or empty")

    if m66_result not in ALLOWED_M66_RESULTS:
        blockers.append("m66_result missing or invalid")

    # Preserve top-level warnings/blockers if present.
    if input_warnings is None:
        not_enough.append("warnings missing")
    elif isinstance(input_warnings, list):
        for index, item in enumerate(input_warnings):
            if not isinstance(item, str):
                blockers.append(f"warnings[{index}] wrong type")
            else:
                warnings.append(item)
                scan_generic_text(
                    item,
                    f"warnings[{index}]",
                    strict=args.strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )
    else:
        blockers.append("warnings wrong type")

    if input_blockers is None:
        not_enough.append("blockers missing")
    elif isinstance(input_blockers, list):
        for index, item in enumerate(input_blockers):
            if not isinstance(item, str):
                blockers.append(f"blockers[{index}] wrong type")
            else:
                blockers.append(item)
                scan_generic_text(
                    item,
                    f"blockers[{index}]",
                    strict=args.strict,
                    warnings=warnings,
                    blockers=blockers,
                    not_enough=not_enough,
                    forbidden_claims_found=forbidden_claims_found,
                    ambiguous_claims=ambiguous_claims,
                )
    else:
        blockers.append("blockers wrong type")

    # Claims are scanned by context.
    validate_claims(
        claims,
        strict=args.strict,
        warnings=warnings,
        blockers=blockers,
        not_enough=not_enough,
        forbidden_claims_found=forbidden_claims_found,
        ambiguous_claims=ambiguous_claims,
        safe_context_detected=safe_context_detected,
    )

    # Operative fields are required and must be a dictionary.
    if operative_fields is None:
        not_enough.append("operative_fields missing")
    elif not isinstance(operative_fields, dict):
        blockers.append("operative_fields wrong type")
    else:
        operative_forbidden_fields = scan_forbidden_fields(operative_fields, "operative_fields")
        forbidden_fields_found.extend(operative_forbidden_fields)
        for item in operative_forbidden_fields:
            blockers.append(f"{item['path']} forbidden operative field")
        scan_nested_generic(
            operative_fields,
            "operative_fields",
            strict=args.strict,
            warnings=warnings,
            blockers=blockers,
            not_enough=not_enough,
            forbidden_claims_found=forbidden_claims_found,
            ambiguous_claims=ambiguous_claims,
        )

    # Completion gate and human review are the policy boundary.
    if completion_gate is None:
        not_enough.append("completion_gate missing")
    else:
        if not isinstance(completion_gate, dict):
            blockers.append("completion_gate wrong type")
        else:
            requested = completion_gate.get("completion_gate_requested")
            allowed = completion_gate.get("completion_gate_allowed")
            result = completion_gate.get("completion_gate_result")
            evidence = completion_gate.get("completion_gate_evidence")
            policy_ref = completion_gate.get("completion_gate_policy_reference")

            gate_evidence_present = is_non_empty_string(evidence) or is_non_empty_string(policy_ref)

            if requested is None:
                not_enough.append("completion_gate_requested missing")
            elif not isinstance(requested, bool):
                blockers.append("completion_gate_requested wrong type")

            if allowed is not None and not isinstance(allowed, bool):
                blockers.append("completion_gate_allowed wrong type")

            if result is not None and not isinstance(result, str):
                blockers.append("completion_gate_result wrong type")

            if requested is True and result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
                if not gate_evidence_present:
                    blockers.append("completion gate pass claimed without explicit evidence")
                if allowed is not True:
                    blockers.append("completion_gate_allowed must be true for pass claims")

            if requested is True and allowed is True and not gate_evidence_present:
                blockers.append("completion_gate_allowed true without explicit gate evidence")

            if requested is False and result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
                blockers.append("completion gate pass inferred without request")

            if requested is True and not gate_evidence_present and result not in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
                not_enough.append("completion gate requested but evidence missing")

            scan_nested_generic(
                completion_gate,
                "completion_gate",
                strict=args.strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )

    # Human review boundary.
    human_review_status = None
    if human_review is None:
        not_enough.append("human_review missing")
    elif not isinstance(human_review, dict):
        blockers.append("human_review wrong type")
    else:
        human_required = human_review.get("human_review_required")
        human_review_status = human_review.get("human_review_status")
        human_review_evidence = human_review.get("human_review_evidence")

        if human_required is False:
            blockers.append("human_review_required must be true")
        elif human_required is None:
            not_enough.append("human_review_required missing")
        elif not isinstance(human_required, bool):
            blockers.append("human_review_required wrong type")

        if human_review_status is None:
            not_enough.append("human_review_status missing")
        elif not isinstance(human_review_status, str):
            blockers.append("human_review_status wrong type")
        elif human_review_status not in ALLOWED_HUMAN_REVIEW_STATUSES:
            blockers.append("human_review_status invalid")

        if isinstance(human_review_evidence, str):
            scan_generic_text(
                human_review_evidence,
                "human_review.human_review_evidence",
                strict=args.strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )
        elif isinstance(human_review_evidence, (dict, list)):
            scan_nested_generic(
                human_review_evidence,
                "human_review.human_review_evidence",
                strict=args.strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )

    # Completion gate claims must also respect the human review status.
    if isinstance(completion_gate, dict):
        requested = completion_gate.get("completion_gate_requested")
        allowed = completion_gate.get("completion_gate_allowed")
        result = completion_gate.get("completion_gate_result")
        gate_evidence_present = is_non_empty_string(completion_gate.get("completion_gate_evidence")) or is_non_empty_string(
            completion_gate.get("completion_gate_policy_reference")
        )

        if requested is True and result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
            if human_review_status != "approved_by_human":
                blockers.append("completion gate pass claimed without approved_by_human human review")
            if not gate_evidence_present:
                blockers.append("completion gate pass claimed without explicit evidence")

        if requested is True and allowed is True:
            if human_review_status != "approved_by_human":
                blockers.append("completion_gate_allowed true without approved_by_human human review")
            if not gate_evidence_present:
                blockers.append("completion_gate_allowed true without explicit gate evidence")

        if requested is False and result in {"COMPLETION_GATE_PASS", "COMPLETION_GATE_PASS_WITH_WARNINGS"}:
            blockers.append("completion gate pass inferred without request")

    # Validate required non-authority boundary statements.
    boundary_ok, matched_boundary = non_authority_boundary_ok(non_authority_boundary)
    if not boundary_ok:
        blockers.append("non_authority_boundary missing required statements")
    else:
        safe_context_detected[0] = True

    # A few top-level strings that may still carry claim-like content.
    for field_name in ("m66_result_source",):
        value = data.get(field_name)
        if isinstance(value, str):
            scan_generic_text(
                value,
                field_name,
                strict=args.strict,
                warnings=warnings,
                blockers=blockers,
                not_enough=not_enough,
                forbidden_claims_found=forbidden_claims_found,
                ambiguous_claims=ambiguous_claims,
            )

    # Determine final result.
    result = determine_result(blockers, not_enough, warnings)
    exit_code = 0 if result in {RESULT_PASS, RESULT_PASS_WITH_WARNINGS} else 1

    if result == RESULT_BLOCKED and "internal checker error" in " ".join(blockers):
        exit_code = 2

    payload = {
        "result": result,
        "task_id": task_id,
        "human_review_required": True if human_review is None else bool(human_review.get("human_review_required", True)),
        "warnings": warnings,
        "blockers": blockers,
        "not_enough_evidence": not_enough,
        "forbidden_claims_found": forbidden_claims_found,
        "forbidden_fields_found": forbidden_fields_found,
        "safe_context_detected": bool(safe_context_detected[0]),
        "ambiguous_claims": ambiguous_claims,
        "non_authority_boundary": matched_boundary if matched_boundary else [
            "M67 result is not approval.",
            "M67 result does not complete tasks.",
            "M67 result does not mutate lifecycle state.",
            "M67 result does not start M68.",
            "Human review remains required.",
        ],
        "exit_code": exit_code,
    }

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(result)

    return exit_code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception:
        print("internal checker error", file=sys.stderr)
        raise SystemExit(2)
