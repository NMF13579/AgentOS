#!/usr/bin/env python3
"""M52 task contract candidate validator (read-only MVP)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOK_OK = "TASK_CONTRACT_CANDIDATE_VALIDATION_OK"
TOK_OK_LIM = "TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS"
TOK_FAIL = "TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED"
TOK_BLOCK = "TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED"

NON_AUTH_MARKERS = [
    "CANDIDATE_VALIDATION_IS_NOT_APPROVAL",
    "CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_EXECUTION",
    "CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_QUEUE_PLACEMENT",
    "CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_ACTIVE_TASK_REPLACEMENT",
    "CANDIDATE_VALIDATION_DOES_NOT_CREATE_LIFECYCLE_STATE",
    "CANDIDATE_VALIDATION_REQUIRES_M53_PLACEMENT_REVIEW",
]

SOURCE_ORIGIN = "M51_GENERATED_STAGING_ARTIFACT"


def _false_authority_fields() -> Dict[str, bool]:
    return {
        "placement_authorized": False,
        "execution_authorized": False,
        "active_task_write_allowed": False,
        "queue_write_allowed": False,
        "approval_record_creation_allowed": False,
    }


def _boundary_flags() -> Dict[str, bool]:
    return {
        "validation_only": True,
        "placement_authorized": False,
        "execution_authorized": False,
        "queue_write_allowed": False,
        "active_task_write_allowed": False,
        "approval_record_creation_allowed": False,
    }


def _result(
    token: str,
    checked_path: str,
    candidate_id: str,
    source_generated_artifact: str,
    source_traceability: Dict[str, str],
    required_sections: Dict[str, bool],
    carry_forward: Dict[str, List[str]],
    findings: List[str],
    warnings: List[str],
    blockers: List[str],
) -> Dict[str, Any]:
    if token in (TOK_OK, TOK_OK_LIM):
        exit_code = 0
        validated = True
        m53_input = True
    elif token == TOK_FAIL:
        exit_code = 1
        validated = False
        m53_input = False
    else:
        exit_code = 2
        validated = False
        m53_input = False

    payload = {
        "candidate_validation_result": {
            "result": token,
            "exit_code": exit_code,
            "validated": validated,
            "checked_path": checked_path,
            "candidate_id": candidate_id,
            "source_generated_artifact": source_generated_artifact,
            "source_candidate_origin": SOURCE_ORIGIN,
            "source_traceability": source_traceability,
            "required_sections": required_sections,
            "carry_forward": carry_forward,
            "boundary_flags": _boundary_flags(),
            "findings": findings,
            "warnings": warnings,
            "blockers": blockers,
            "non_authority_markers": NON_AUTH_MARKERS,
            "m53_review_input_candidate": m53_input,
            **_false_authority_fields(),
        }
    }
    return payload


def _default_traceability(source: str = "") -> Dict[str, str]:
    return {
        "source_proposal": "",
        "source_authorization": "",
        "source_conversion_package": "",
        "source_generated_artifact": source,
        "source_candidate_origin": SOURCE_ORIGIN,
        "m50_traceability": "",
        "m51_generator_evidence": "",
    }


def _default_sections() -> Dict[str, bool]:
    return {
        "goal": False,
        "scope": False,
        "allowed_changes": False,
        "forbidden_changes": False,
        "validation": False,
        "expected_final_report": False,
    }


def _default_carry() -> Dict[str, List[str]]:
    return {
        "accepted_limitations": [],
        "open_questions": [],
        "downstream_limits": [],
        "non_authority_boundary": [],
    }


def _extract_yaml_block(text: str, key: str) -> str:
    pattern = rf"(?ms)^```yaml\s.*?^{re.escape(key)}:\n(.*?)^```"
    m = re.search(pattern, text)
    if m:
        return f"{key}:\n{m.group(1)}"
    return ""


def _has_marker(text: str, marker: str) -> bool:
    return marker in text


def _extract_list_items(text: str, key: str) -> List[str]:
    # MVP parser: collect '- item' lines under a YAML key.
    lines = text.splitlines()
    items: List[str] = []
    in_block = False
    base_indent = None
    for line in lines:
        if re.match(rf"^\s*{re.escape(key)}:\s*$", line):
            in_block = True
            base_indent = len(line) - len(line.lstrip(" "))
            continue
        if not in_block:
            continue
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= (base_indent or 0):
            break
        s = line.strip()
        if s.startswith("- "):
            items.append(s[2:].strip())
    return items


def _validate_candidate(path: Path) -> Dict[str, Any]:
    checked_path = str(path)
    trace = _default_traceability(checked_path)
    sections = _default_sections()
    carry = _default_carry()

    if not path.exists() or not path.is_file():
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["source generated artifact missing"],
        )

    text = path.read_text(encoding="utf-8", errors="replace")

    if "conversion_package:" not in text:
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["expected conversion package wrapper missing"],
        )

    if "task_contract_candidate:" not in text:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=["task_contract_candidate missing"],
            warnings=[],
            blockers=[],
        )

    if "candidate_output:" in text and "examples/task-contract-candidate" in text:
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=[
                "standalone candidate-only file submitted as primary artifact"
            ],
        )

    candidate = _extract_yaml_block(text, "task_contract_candidate")
    source = _extract_yaml_block(text, "conversion_package")
    data = candidate or text

    required_markers = {
        "goal": "goal:",
        "scope": "scope:",
        "allowed_changes": "allowed_changes:",
        "forbidden_changes": "forbidden_changes:",
        "validation": "validation:",
        "expected_final_report": "expected_final_report:",
    }
    missing = []
    for k, marker in required_markers.items():
        ok = _has_marker(data, marker)
        sections[k] = ok
        if not ok:
            missing.append(k)

    carry_required = [
        "accepted_limitations:",
        "open_questions:",
        "downstream_limits:",
        "non_authority_boundary:",
    ]
    carry_missing = [m[:-1] for m in carry_required if m not in data and m not in source]

    if "mode: EXECUTION" in data:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=["mode EXECUTION used instead of EXECUTION_SHAPE"],
            warnings=[],
            blockers=[],
        )

    if "M51_GENERATED_STAGING_ARTIFACT" not in text and "source_candidate_origin:" in text:
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["source_candidate_origin unsupported or unknown"],
        )

    if "source_generator_evidence:" not in text:
        # For candidate mode, infer M51 evidence from generator artifact markers.
        if "human_authorization:" not in text and "source_readiness_report:" not in text:
            return _result(
                TOK_BLOCK,
                checked_path,
                "",
                checked_path,
                trace,
                sections,
                carry,
                findings=[],
                warnings=[],
                blockers=["M51-origin evidence missing for M51 candidate"],
            )

    forbidden_true_flags = [
        "placement_authorized: true",
        "execution_authorized: true",
        "queue_write_allowed: true",
        "active_task_write_allowed: true",
        "approval_record_creation_allowed: true",
    ]
    hit_true = [f for f in forbidden_true_flags if f in text]
    if hit_true:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=["authority flag is true"],
            warnings=[],
            blockers=[],
        )

    # Fill traceability from obvious known markers.
    for key in trace:
        m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", text)
        if m:
            trace[key] = m.group(1).strip().strip("`")

    carry["accepted_limitations"] = _extract_list_items(text, "accepted_limitations")
    carry["open_questions"] = _extract_list_items(text, "open_questions")
    carry["downstream_limits"] = _extract_list_items(text, "downstream_limits")
    carry["non_authority_boundary"] = _extract_list_items(text, "non_authority_boundary")

    missing_trace = [k for k, v in trace.items() if not v]
    if missing_trace and any(trace.values()):
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=["required traceability fields missing while source lineage is known"],
            warnings=[],
            blockers=[],
        )
    if missing_trace and not any(trace.values()):
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["source lineage cannot be safely determined"],
        )

    if missing or carry_missing:
        messages = [f"missing {m}" for m in missing] + [f"missing {m}" for m in carry_missing]
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=messages,
            warnings=[],
            blockers=[],
        )

    warnings: List[str] = []
    if carry["accepted_limitations"] or carry["open_questions"]:
        warnings.append("accepted_limitations and/or open_questions remain present")
        return _result(
            TOK_OK_LIM,
            checked_path,
            "",
            checked_path,
            trace,
            sections,
            carry,
            findings=["candidate structurally valid"],
            warnings=warnings,
            blockers=[],
        )

    return _result(
        TOK_OK,
        checked_path,
        "",
        checked_path,
        trace,
        sections,
        carry,
        findings=["candidate structurally valid"],
        warnings=[],
        blockers=[],
    )


def _validate_input(path: Path) -> Dict[str, Any]:
    checked_path = str(path)
    trace = _default_traceability("")
    sections = _default_sections()
    carry = _default_carry()

    if not path.exists() or not path.is_file():
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            "",
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["input package missing"],
        )

    text = path.read_text(encoding="utf-8", errors="replace")
    if "candidate_validation_input:" not in text:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            "",
            trace,
            sections,
            carry,
            findings=["candidate_validation_input missing"],
            warnings=[],
            blockers=[],
        )

    required_kv = [
        "source_candidate_origin: M51_GENERATED_STAGING_ARTIFACT",
        "validation_mode: M52_CANDIDATE_READINESS_VALIDATION",
        "expected_candidate_shape: generated_conversion_package_with_embedded_candidate",
        "downstream_target: M53_PLACEMENT_REVIEW",
        "m51_origin:",
        "required: true",
        "validation_only: true",
        "queue_write_allowed: false",
        "active_task_write_allowed: false",
        "execution_authorized: false",
        "approval_record_creation_allowed: false",
        "placement_authorized: false",
    ]
    missing = [k for k in required_kv if k not in text]
    if missing:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            "",
            trace,
            sections,
            carry,
            findings=[f"missing input marker: {m}" for m in missing],
            warnings=[],
            blockers=[],
        )

    m = re.search(r"(?m)^\s*source_generated_artifact:\s*(.+?)\s*$", text)
    source_art = m.group(1).strip() if m else ""
    trace = _default_traceability(source_art)

    if not source_art:
        return _result(
            TOK_FAIL,
            checked_path,
            "",
            source_art,
            trace,
            sections,
            carry,
            findings=["source_generated_artifact missing"],
            warnings=[],
            blockers=[],
        )

    if not Path(source_art).exists():
        return _result(
            TOK_BLOCK,
            checked_path,
            "",
            source_art,
            trace,
            sections,
            carry,
            findings=[],
            warnings=[],
            blockers=["source generated artifact missing"],
        )

    # Input package valid for M52 read-only MVP.
    return _result(
        TOK_OK,
        checked_path,
        "",
        source_art,
        trace,
        sections,
        carry,
        findings=["input package structurally valid"],
        warnings=[],
        blockers=[],
    )


def _fixtures_mode() -> Dict[str, Any]:
    fixture_dir = Path("tests/fixtures/task-contract-candidate-validation")
    if not fixture_dir.exists():
        return _result(
            TOK_BLOCK,
            str(fixture_dir),
            "",
            "",
            _default_traceability(""),
            _default_sections(),
            _default_carry(),
            findings=[],
            warnings=[],
            blockers=["fixture directory absent for --fixtures mode"],
        )

    return _result(
        TOK_OK,
        str(fixture_dir),
        "",
        "",
        _default_traceability(""),
        _default_sections(),
        _default_carry(),
        findings=["fixture directory discovered"],
        warnings=[],
        blockers=[],
    )


def _explain_text() -> str:
    return "\n".join(
        [
            "M52 candidate validator CLI (read-only)",
            "Modes: --candidate <path> | --input <path> | --fixtures | --explain | --json",
            f"Result tokens: {TOK_OK}, {TOK_OK_LIM}, {TOK_FAIL}, {TOK_BLOCK}",
            "Exit codes: OK/OK_WITH_LIMITATIONS=0, FAILED=1, BLOCKED=2",
            "Read-only boundary: no file writes, no queue placement, no active-task replacement, no execution authorization.",
            "Non-authority markers:",
            *NON_AUTH_MARKERS,
        ]
    )


def _print_text(result: Dict[str, Any]) -> None:
    r = result["candidate_validation_result"]
    print(f"result: {r['result']}")
    print(f"exit_code: {r['exit_code']}")
    print(f"validated: {str(r['validated']).lower()}")
    if r["findings"]:
        print("findings:")
        for item in r["findings"]:
            print(f"- {item}")
    if r["warnings"]:
        print("warnings:")
        for item in r["warnings"]:
            print(f"- {item}")
    if r["blockers"]:
        print("blockers:")
        for item in r["blockers"]:
            print(f"- {item}")
    print("non_authority_markers:")
    print("- CANDIDATE_VALIDATION_IS_NOT_APPROVAL")
    print("- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_EXECUTION")
    print("- CANDIDATE_VALIDATION_REQUIRES_M53_PLACEMENT_REVIEW")


def _blocked(msg: str, path: str = "") -> Dict[str, Any]:
    return _result(
        TOK_BLOCK,
        path,
        "",
        path,
        _default_traceability(path),
        _default_sections(),
        _default_carry(),
        findings=[],
        warnings=[],
        blockers=[msg],
    )


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--candidate")
    parser.add_argument("--input")
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    ns = _parse_args(argv)

    if ns.explain:
        print(_explain_text())
        return 0

    if ns.candidate and ns.input:
        result = _blocked("both --candidate and --input are provided")
    elif ns.fixtures:
        result = _fixtures_mode()
    elif ns.candidate:
        result = _validate_candidate(Path(ns.candidate))
    elif ns.input:
        result = _validate_input(Path(ns.input))
    else:
        result = _blocked("no actionable mode provided")

    if ns.as_json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        _print_text(result)

    return int(result["candidate_validation_result"]["exit_code"])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
