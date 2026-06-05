#!/usr/bin/env python3
"""M65 acceptance criteria checker (read-only).

M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE maps to exit 1 because automated
 evaluation is inconclusive and must not allow the pipeline to proceed without
 human review. This is a conservative fail-closed mapping, not a claim that the
 task failed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PASS = "M65_ACCEPTANCE_CHECK_PASS"
PASS_WARN = "M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS"
BLOCKED = "M65_ACCEPTANCE_CHECK_BLOCKED"
NEE = "M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE"

CRIT_STATES = {
    "SATISFIED",
    "SATISFIED_WITH_WARNINGS",
    "NOT_SATISFIED",
    "NOT_ENOUGH_EVIDENCE",
    "NOT_EVALUABLE",
    "BLOCKED",
}

CHECK_METHODS = {
    "artifact_presence",
    "validation_output",
    "declared_change",
    "manual_review_required",
}

VALIDATION_RESULTS = {
    "PASS",
    "PASS_WITH_WARNINGS",
    "FAIL",
    "BLOCKED",
    "NOT_RUN",
    "UNKNOWN",
}

EVIDENCE_RESULTS = {
    "M64_EVIDENCE_CHECK_PASS",
    "M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS",
    "M64_EVIDENCE_CHECK_BLOCKED",
    "M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE",
    "UNKNOWN",
}

FORBIDDEN_FIELDS = {
    "approved",
    "task_approved",
    "task_complete",
    "task_completed",
    "accepted_by_system",
    "completion_approved",
    "completion_authorized",
    "completion_gate_passed",
    "human_review_not_required",
    "skip_human_review",
    "merge_authorized",
    "push_authorized",
    "release_authorized",
    "production_ready",
    "ready_for_production",
    "m66_started_automatically",
    "m67_started_automatically",
}

FORBIDDEN_CLAIMS = [
    "task approved",
    "task accepted by system",
    "completion approved",
    "human review not required",
    "merge authorized",
    "push authorized",
    "release authorized",
    "production ready",
    "ready for production",
    "completion gate passed",
    "m66 started automatically",
    "m67 started automatically",
]

REQUIRED_TOP_LEVEL = {
    "contract_version",
    "package_type",
    "task_id",
    "task_brief_path",
    "acceptance_criteria",
    "expected_artifacts",
    "actual_artifacts",
    "changed_files",
    "evidence_result",
    "validation_outputs",
    "known_limitations",
    "warnings",
    "blockers",
    "human_review_required",
    "non_authority_boundary",
}


def strict_bool(v: Any) -> bool:
    return type(v) is bool


def is_non_empty_str(v: Any) -> bool:
    return isinstance(v, str) and len(v.strip()) > 0


def normalize_path_item(item: Any) -> Optional[str]:
    if isinstance(item, str) and item.strip():
        return item.strip()
    if isinstance(item, dict):
        p = item.get("path")
        if isinstance(p, str) and p.strip():
            return p.strip()
    return None


def is_negated_policy_context(text: str) -> bool:
    t = text.lower()
    return (
        "not approval" in t
        or "does not complete" in t
        or "must not" in t
        or "forbidden claim" in t
        or "is not approval" in t
    )


def json_output(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M65 acceptance criteria checker (read-only)")
    parser.add_argument("--package", required=True, help="Path to acceptance criteria check package JSON")
    parser.add_argument("--json", action="store_true", help="Emit JSON output (required)")
    parser.add_argument("--strict", action="store_true", help="Enable stricter checks")
    args = parser.parse_args()
    if not args.json:
        parser.error("--json is required")
    return args


def default_payload(package_path: str, strict: bool) -> Dict[str, Any]:
    return {
        "result": BLOCKED,
        "package_path": package_path,
        "contract_version": None,
        "package_type": None,
        "task_id": None,
        "human_review_required": True,
        "criteria_summary": {
            "total": 0,
            "required": 0,
            "optional": 0,
            "satisfied": 0,
            "satisfied_with_warnings": 0,
            "not_satisfied": 0,
            "not_enough_evidence": 0,
            "not_evaluable": 0,
            "blocked": 0,
        },
        "criterion_results": [],
        "findings": {
            "blockers": [],
            "not_enough_evidence": [],
            "warnings": [],
        },
        "forbidden_claims_found": [],
        "forbidden_fields_found": [],
        "non_authority_boundary_present": False,
        "final_decision_reason": "",
        "exit_code": 1,
        "strict": strict,
    }


def add_unique(lst: List[str], msg: str) -> None:
    if msg not in lst:
        lst.append(msg)


def validate_top_level(data: Dict[str, Any], out: Dict[str, Any], strict: bool) -> Tuple[bool, Dict[str, Any]]:
    blockers = out["findings"]["blockers"]
    warnings = out["findings"]["warnings"]

    missing = sorted(REQUIRED_TOP_LEVEL - set(data.keys()))
    if missing:
        add_unique(blockers, f"Missing required top-level fields: {', '.join(missing)}")

    if strict:
        extra = sorted(set(data.keys()) - REQUIRED_TOP_LEVEL)
        if extra:
            add_unique(warnings, f"Unknown top-level fields in strict mode: {', '.join(extra)}")

    if data.get("contract_version") != "1.0.0":
        add_unique(blockers, "contract_version must be '1.0.0'")
    if data.get("package_type") != "acceptance_criteria_check_package":
        add_unique(blockers, "package_type must be 'acceptance_criteria_check_package'")

    if not is_non_empty_str(data.get("task_id")):
        add_unique(blockers, "task_id must be non-empty string")
    if not is_non_empty_str(data.get("task_brief_path")):
        add_unique(blockers, "task_brief_path must be non-empty string")

    ac = data.get("acceptance_criteria")
    if not isinstance(ac, list) or len(ac) == 0:
        add_unique(blockers, "acceptance_criteria must be non-empty array")

    for key in ["expected_artifacts", "actual_artifacts", "changed_files", "validation_outputs", "known_limitations", "warnings", "blockers"]:
        if not isinstance(data.get(key), list):
            add_unique(blockers, f"{key} must be array")

    if not isinstance(data.get("evidence_result"), dict):
        add_unique(blockers, "evidence_result must be object")

    hr = data.get("human_review_required")
    if not strict_bool(hr):
        add_unique(blockers, "human_review_required must be strict JSON boolean")
    elif hr is not True:
        add_unique(blockers, "human_review_required must be true")
    out["human_review_required"] = True

    nab = data.get("non_authority_boundary")
    if not isinstance(nab, list):
        add_unique(blockers, "non_authority_boundary must be array")
    elif len(nab) == 0:
        add_unique(blockers, "non_authority_boundary must be non-empty")
    else:
        out["non_authority_boundary_present"] = True
        for i, item in enumerate(nab):
            if not isinstance(item, str):
                add_unique(blockers, f"non_authority_boundary[{i}] must be string")

        joined = " ".join([x.lower() for x in nab if isinstance(x, str)])
        if "human review remains required" not in joined:
            add_unique(warnings, "non_authority_boundary does not clearly state human review remains required")
        if "not approval" not in joined and "is not approval" not in joined:
            add_unique(warnings, "non_authority_boundary does not clearly negate approval")
        if "does not complete" not in joined:
            add_unique(warnings, "non_authority_boundary does not clearly negate completion")

    out["contract_version"] = data.get("contract_version")
    out["package_type"] = data.get("package_type")
    out["task_id"] = data.get("task_id")
    return (len(blockers) == 0), out


def collect_paths(data: Dict[str, Any]) -> Tuple[set[str], set[str], set[str], set[str]]:
    expected_paths = set()
    actual_paths = set()
    changed_paths = set()
    required_expected_paths = set()

    for item in data.get("expected_artifacts", []):
        if isinstance(item, dict):
            p = item.get("path")
            if isinstance(p, str) and p.strip():
                path = p.strip()
                expected_paths.add(path)
                if type(item.get("required")) is bool and item.get("required") is True:
                    required_expected_paths.add(path)

    for item in data.get("actual_artifacts", []):
        p = normalize_path_item(item)
        if p:
            actual_paths.add(p)

    for item in data.get("changed_files", []):
        p = normalize_path_item(item)
        if p:
            changed_paths.add(p)

    return expected_paths, actual_paths, changed_paths, required_expected_paths


def find_correlated_validation_outputs(criterion_id: str, expected_evidence: List[str], validation_outputs: List[Any]) -> List[Dict[str, Any]]:
    matches: List[Dict[str, Any]] = []
    for item in validation_outputs:
        if not isinstance(item, dict):
            continue
        corr = item.get("correlates_to_criteria")
        if isinstance(corr, list) and any(isinstance(x, str) and x == criterion_id for x in corr):
            matches.append(item)
            continue
        name = item.get("name")
        output_path = item.get("output_path")
        if isinstance(name, str) and any(name == ev for ev in expected_evidence):
            matches.append(item)
            continue
        if isinstance(output_path, str) and any(output_path == ev for ev in expected_evidence):
            matches.append(item)
            continue
    return matches


def evaluate_criteria(data: Dict[str, Any], out: Dict[str, Any], strict: bool) -> None:
    blockers = out["findings"]["blockers"]
    warnings = out["findings"]["warnings"]
    nees = out["findings"]["not_enough_evidence"]

    expected_paths, actual_paths, changed_paths, required_expected_paths = collect_paths(data)
    validation_outputs = data.get("validation_outputs", []) if isinstance(data.get("validation_outputs"), list) else []

    all_manual = True
    has_required = False

    for i, c in enumerate(data.get("acceptance_criteria", [])):
        crit_res: Dict[str, Any] = {
            "criterion_id": None,
            "state": "BLOCKED",
            "reason": "",
            "required": None,
            "check_method": None,
        }

        if not isinstance(c, dict):
            add_unique(blockers, f"criterion[{i}] must be object")
            crit_res["reason"] = "criterion must be object"
            out["criterion_results"].append(crit_res)
            continue

        req_fields = ["criterion_id", "description", "required", "check_method", "expected_evidence", "notes"]
        missing = [f for f in req_fields if f not in c]
        if missing:
            add_unique(blockers, f"criterion[{i}] missing required fields: {', '.join(missing)}")

        criterion_id = c.get("criterion_id")
        description = c.get("description")
        required = c.get("required")
        method = c.get("check_method")
        expected_evidence = c.get("expected_evidence")
        notes = c.get("notes")

        crit_res["criterion_id"] = criterion_id
        crit_res["required"] = required
        crit_res["check_method"] = method

        malformed = False
        if not is_non_empty_str(criterion_id):
            add_unique(blockers, f"criterion[{i}].criterion_id must be non-empty string")
            malformed = True
        if not is_non_empty_str(description):
            add_unique(blockers, f"criterion[{i}].description must be non-empty string")
            malformed = True
        if not strict_bool(required):
            add_unique(blockers, f"criterion[{i}].required must be strict JSON boolean")
            malformed = True
        if not isinstance(method, str) or method not in CHECK_METHODS:
            if strict_bool(required) and required is True:
                add_unique(blockers, f"criterion[{i}] required unsupported check_method")
            else:
                add_unique(warnings, f"criterion[{i}] unsupported check_method")
            malformed = True
        if not isinstance(expected_evidence, list) or any(not isinstance(x, str) for x in expected_evidence):
            add_unique(blockers, f"criterion[{i}].expected_evidence must be array of strings")
            malformed = True
        if not isinstance(notes, str):
            add_unique(blockers, f"criterion[{i}].notes must be string")
            malformed = True

        if method != "manual_review_required":
            all_manual = False
        if strict_bool(required) and required is True:
            has_required = True

        if malformed:
            crit_res["state"] = "BLOCKED"
            crit_res["reason"] = "malformed criterion"
            out["criterion_results"].append(crit_res)
            continue

        assert isinstance(criterion_id, str)
        assert isinstance(expected_evidence, list)

        if method == "manual_review_required":
            if required is True:
                add_unique(blockers, f"required manual_review_required criterion blocked: {criterion_id}")
                crit_res["state"] = "BLOCKED"
                crit_res["reason"] = "required manual review criterion"
            else:
                add_unique(warnings, f"optional manual_review_required criterion: {criterion_id}")
                crit_res["state"] = "SATISFIED_WITH_WARNINGS"
                crit_res["reason"] = "optional manual review criterion"

        elif method == "artifact_presence":
            missing_required = []
            for ev in expected_evidence:
                if not isinstance(ev, str) or not ev.strip():
                    continue
                path = ev.strip()
                in_any = path in actual_paths or path in changed_paths
                if required is True and not in_any:
                    missing_required.append(path)
                elif required is False and not in_any:
                    add_unique(warnings, f"optional artifact evidence missing for {criterion_id}: {path}")

            if required is True:
                for p in expected_evidence:
                    if isinstance(p, str) and p.strip() and p.strip() in required_expected_paths:
                        if p.strip() not in actual_paths and p.strip() not in changed_paths:
                            if p.strip() not in missing_required:
                                missing_required.append(p.strip())

            if missing_required:
                add_unique(blockers, f"required artifact evidence missing for {criterion_id}: {', '.join(sorted(set(missing_required)))}")
                crit_res["state"] = "BLOCKED"
                crit_res["reason"] = "required artifact missing"
            else:
                crit_res["state"] = "SATISFIED" if required else "SATISFIED_WITH_WARNINGS" if any(
                    isinstance(ev, str) and ev.strip() and ev.strip() not in actual_paths and ev.strip() not in changed_paths
                    for ev in expected_evidence
                ) else "SATISFIED"
                crit_res["reason"] = "artifact presence check"

        elif method == "validation_output":
            correlated = find_correlated_validation_outputs(criterion_id, [x for x in expected_evidence if isinstance(x, str)], validation_outputs)
            if not correlated:
                if required is True:
                    add_unique(blockers, f"required criterion missing correlated validation output: {criterion_id}")
                    crit_res["state"] = "BLOCKED"
                    crit_res["reason"] = "required validation output missing"
                else:
                    if strict:
                        add_unique(nees, f"optional criterion missing correlated validation output: {criterion_id}")
                        crit_res["state"] = "NOT_ENOUGH_EVIDENCE"
                        crit_res["reason"] = "optional validation output missing"
                    else:
                        add_unique(warnings, f"optional criterion missing correlated validation output: {criterion_id}")
                        crit_res["state"] = "SATISFIED_WITH_WARNINGS"
                        crit_res["reason"] = "optional validation output missing"
            else:
                worst = "PASS"
                for v in correlated:
                    result = v.get("result")
                    if result not in VALIDATION_RESULTS:
                        if required is True:
                            add_unique(blockers, f"required criterion invalid validation result: {criterion_id}")
                            worst = "FAIL"
                        else:
                            add_unique(warnings, f"optional criterion invalid validation result: {criterion_id}")
                        continue
                    if result in {"FAIL", "BLOCKED", "NOT_RUN", "UNKNOWN"}:
                        if result == "FAIL":
                            worst = "FAIL"
                        elif result == "BLOCKED" and worst != "FAIL":
                            worst = "BLOCKED"
                        elif result == "NOT_RUN" and worst not in {"FAIL", "BLOCKED"}:
                            worst = "NOT_RUN"
                        elif result == "UNKNOWN" and worst not in {"FAIL", "BLOCKED", "NOT_RUN"}:
                            worst = "UNKNOWN"

                if required is True and worst in {"FAIL", "BLOCKED", "NOT_RUN", "UNKNOWN"}:
                    add_unique(blockers, f"required validation output failed or unavailable for {criterion_id}: {worst}")
                    crit_res["state"] = "BLOCKED"
                    crit_res["reason"] = f"required validation result {worst}"
                elif required is False and worst in {"FAIL", "BLOCKED", "NOT_RUN", "UNKNOWN"}:
                    if strict or worst == "UNKNOWN":
                        add_unique(nees, f"optional validation output inconclusive for {criterion_id}: {worst}")
                        crit_res["state"] = "NOT_ENOUGH_EVIDENCE"
                        crit_res["reason"] = f"optional validation result {worst}"
                    else:
                        add_unique(warnings, f"optional validation output issue for {criterion_id}: {worst}")
                        crit_res["state"] = "SATISFIED_WITH_WARNINGS"
                        crit_res["reason"] = f"optional validation result {worst}"
                else:
                    crit_res["state"] = "SATISFIED"
                    crit_res["reason"] = "validation output check"

        elif method == "declared_change":
            missing = []
            for ev in expected_evidence:
                if not isinstance(ev, str) or not ev.strip():
                    continue
                path = ev.strip()
                if path not in changed_paths and path not in actual_paths:
                    missing.append(path)

            if required is True and missing:
                add_unique(blockers, f"required declared change missing for {criterion_id}: {', '.join(sorted(set(missing)))}")
                crit_res["state"] = "BLOCKED"
                crit_res["reason"] = "required declared change missing"
            elif required is False and missing:
                if strict:
                    add_unique(nees, f"optional declared change missing for {criterion_id}")
                    crit_res["state"] = "NOT_ENOUGH_EVIDENCE"
                    crit_res["reason"] = "optional declared change missing"
                else:
                    add_unique(warnings, f"optional declared change missing for {criterion_id}")
                    crit_res["state"] = "SATISFIED_WITH_WARNINGS"
                    crit_res["reason"] = "optional declared change missing"
            else:
                crit_res["state"] = "SATISFIED"
                crit_res["reason"] = "declared change check"

        out["criterion_results"].append(crit_res)

    if all_manual and has_required:
        add_unique(blockers, "All criteria are manual_review_required and at least one is required")

    # Non-correlated validation outputs warning
    criterion_ids = {
        c.get("criterion_id")
        for c in data.get("acceptance_criteria", [])
        if isinstance(c, dict) and isinstance(c.get("criterion_id"), str)
    }
    for v in validation_outputs:
        if not isinstance(v, dict):
            continue
        corr = v.get("correlates_to_criteria")
        if isinstance(corr, list):
            has_match = any(isinstance(x, str) and x in criterion_ids for x in corr)
            if not has_match:
                add_unique(warnings, f"validation output not correlated to any criterion: {v.get('name', '<unnamed>')}")

    # Extra actual artifacts warning
    extras = sorted(actual_paths - expected_paths)
    if extras:
        add_unique(warnings, f"extra actual artifacts not in expected_artifacts: {', '.join(extras)}")
        if strict:
            add_unique(nees, "strict mode: extra actual artifacts require manual follow-up")


def evaluate_evidence_result(data: Dict[str, Any], out: Dict[str, Any], strict: bool) -> None:
    blockers = out["findings"]["blockers"]
    warnings = out["findings"]["warnings"]
    nees = out["findings"]["not_enough_evidence"]

    ev = data.get("evidence_result")
    if not isinstance(ev, dict):
        add_unique(blockers, "evidence_result must be object")
        return

    source = ev.get("source_path")
    if not is_non_empty_str(source):
        add_unique(blockers, "evidence_result.source_path must be non-empty string")

    result = ev.get("result")
    if result not in EVIDENCE_RESULTS:
        add_unique(blockers, "evidence_result.result is invalid")
        return

    if result == "M64_EVIDENCE_CHECK_BLOCKED":
        add_unique(blockers, "evidence_result is M64_EVIDENCE_CHECK_BLOCKED")
    elif result == "M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE":
        required_exists = any(
            isinstance(c, dict) and strict_bool(c.get("required")) and c.get("required") is True
            for c in data.get("acceptance_criteria", [])
        )
        if required_exists and strict:
            add_unique(blockers, "required criteria depend on inconclusive M64 evidence_result")
        else:
            add_unique(nees, "evidence_result is M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE")
    elif result == "M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS":
        add_unique(warnings, "evidence_result is M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS")
    elif result == "UNKNOWN":
        if strict:
            add_unique(nees, "evidence_result is UNKNOWN")
        else:
            add_unique(warnings, "evidence_result is UNKNOWN")


def scan_forbidden_fields_and_claims(data: Any, out: Dict[str, Any], in_non_authority_boundary: bool = False) -> None:
    blockers = out["findings"]["blockers"]

    def walk(node: Any, in_nab: bool = False) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                kl = k.lower()
                if kl in FORBIDDEN_FIELDS:
                    add_unique(out["forbidden_fields_found"], k)
                    add_unique(blockers, f"forbidden operative field found: {k}")
                walk(v, in_nab or (k == "non_authority_boundary"))
        elif isinstance(node, list):
            for item in node:
                walk(item, in_nab)
        elif isinstance(node, str):
            s = node.strip()
            lower = s.lower()
            for claim in FORBIDDEN_CLAIMS:
                if claim in lower:
                    if in_nab and is_negated_policy_context(lower):
                        continue
                    add_unique(out["forbidden_claims_found"], claim)
                    add_unique(blockers, f"forbidden operative claim found: {claim}")

    walk(data, in_non_authority_boundary)


def evaluate_known_lists(data: Dict[str, Any], out: Dict[str, Any], strict: bool) -> None:
    blockers = out["findings"]["blockers"]
    warnings = out["findings"]["warnings"]

    pkg_blockers = data.get("blockers", [])
    pkg_warnings = data.get("warnings", [])
    known_limitations = data.get("known_limitations", [])

    if isinstance(pkg_blockers, list) and any(isinstance(x, str) and x.strip() for x in pkg_blockers):
        add_unique(blockers, "package blockers is non-empty")

    if isinstance(pkg_warnings, list) and any(isinstance(x, str) and x.strip() for x in pkg_warnings):
        add_unique(warnings, "package warnings is non-empty")

    required_ids = {
        c.get("criterion_id")
        for c in data.get("acceptance_criteria", [])
        if isinstance(c, dict) and c.get("required") is True and isinstance(c.get("criterion_id"), str)
    }

    if isinstance(known_limitations, list):
        for entry in known_limitations:
            if not isinstance(entry, str):
                add_unique(blockers, "known_limitations items must be strings")
                continue
            lower = entry.lower()
            affects_required = any(cid.lower() in lower for cid in required_ids)
            if affects_required:
                add_unique(blockers, f"known_limitation references required criterion: {entry}")
            else:
                if strict:
                    add_unique(warnings, f"known_limitation requires review: {entry}")
                elif entry.strip():
                    add_unique(warnings, "known_limitations is non-empty")
                    break


def finalize(out: Dict[str, Any]) -> None:
    blockers = out["findings"]["blockers"]
    warnings = out["findings"]["warnings"]
    nees = out["findings"]["not_enough_evidence"]

    # summarize criterion states
    for item in out["criterion_results"]:
        state = item.get("state")
        if state not in CRIT_STATES:
            continue
        if state == "SATISFIED":
            out["criteria_summary"]["satisfied"] += 1
        elif state == "SATISFIED_WITH_WARNINGS":
            out["criteria_summary"]["satisfied_with_warnings"] += 1
        elif state == "NOT_SATISFIED":
            out["criteria_summary"]["not_satisfied"] += 1
        elif state == "NOT_ENOUGH_EVIDENCE":
            out["criteria_summary"]["not_enough_evidence"] += 1
        elif state == "NOT_EVALUABLE":
            out["criteria_summary"]["not_evaluable"] += 1
        elif state == "BLOCKED":
            out["criteria_summary"]["blocked"] += 1

    if blockers:
        out["result"] = BLOCKED
        out["exit_code"] = 1
        out["final_decision_reason"] = "blocker conditions found"
        return

    if nees:
        out["result"] = NEE
        out["exit_code"] = 1
        out["final_decision_reason"] = "not enough evidence conditions found"
        return

    if warnings:
        out["result"] = PASS_WARN
        out["exit_code"] = 0
        out["final_decision_reason"] = "warning conditions found"
        return

    out["result"] = PASS
    out["exit_code"] = 0
    out["final_decision_reason"] = "all deterministic checks satisfied"


def run_checker(args: argparse.Namespace) -> Tuple[Dict[str, Any], int]:
    out = default_payload(args.package, args.strict)

    p = Path(args.package)
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"package file not found: {args.package}")

    try:
        raw = p.read_text(encoding="utf-8")
    except OSError as exc:
        raise OSError(f"cannot read package file: {exc}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        out["findings"]["blockers"].append("package JSON is invalid")
        out["result"] = BLOCKED
        out["final_decision_reason"] = "invalid JSON"
        out["exit_code"] = 1
        return out, 1

    if not isinstance(data, dict):
        out["findings"]["blockers"].append("top-level package must be object")
        out["result"] = BLOCKED
        out["final_decision_reason"] = "invalid top-level type"
        out["exit_code"] = 1
        return out, 1

    validate_top_level(data, out, args.strict)

    ac = data.get("acceptance_criteria")
    if isinstance(ac, list):
        out["criteria_summary"]["total"] = len(ac)
        req_count = 0
        for c in ac:
            if isinstance(c, dict) and strict_bool(c.get("required")) and c.get("required") is True:
                req_count += 1
        out["criteria_summary"]["required"] = req_count
        out["criteria_summary"]["optional"] = len(ac) - req_count

    evaluate_evidence_result(data, out, args.strict)
    evaluate_criteria(data, out, args.strict)
    evaluate_known_lists(data, out, args.strict)
    scan_forbidden_fields_and_claims(data, out)

    finalize(out)
    return out, int(out["exit_code"])


def main() -> int:
    try:
        args = parse_args()
    except SystemExit as exc:
        return int(exc.code)

    try:
        out, code = run_checker(args)
        json_output(out)
        return code
    except (FileNotFoundError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # fail-closed
        print(f"ERROR: internal checker error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
