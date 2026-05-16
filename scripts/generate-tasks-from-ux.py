#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

UX_TO_TASK_DRY_RUN_OK = "UX_TO_TASK_DRY_RUN_OK"
UX_TO_TASK_WRITE_OK = "UX_TO_TASK_WRITE_OK"
UX_TO_TASK_BLOCKED_UX_NOT_APPROVED = "UX_TO_TASK_BLOCKED_UX_NOT_APPROVED"
UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT = "UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT"
UX_TO_TASK_BLOCKED_INVALID_UX = "UX_TO_TASK_BLOCKED_INVALID_UX"
UX_TO_TASK_NEEDS_REVIEW = "UX_TO_TASK_NEEDS_REVIEW"
UX_TO_TASK_FAILED = "UX_TO_TASK_FAILED"

VALIDATION_ORDER = [
    "approval_check",
    "ui_contract_check",
    "ux_structure_check",
    "candidate_generation",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate candidate Task Contract v2 from approved UX markdown")
    parser.add_argument("--ux", required=True, help="Path to UX markdown")
    parser.add_argument("--out", help="Output directory for write mode")
    parser.add_argument("--dry-run", action="store_true", help="Print candidate to stdout")
    parser.add_argument("--write", action="store_true", help="Write candidate file")
    parser.add_argument("--json", action="store_true", dest="json_mode", help="Emit JSON summary")
    return parser.parse_args()


def parse_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def now_utc_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_ux_id(ux_id: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", ux_id.lower())
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter_like(lines: List[str]) -> Tuple[Dict[str, str], int]:
    data: Dict[str, str] = {}
    idx = 0
    for idx, raw in enumerate(lines):
        line = raw.rstrip("\n")
        if not line.strip():
            return data, idx + 1
        if ":" not in line:
            return data, idx
        key, value = line.split(":", 1)
        key = key.strip()
        if not key:
            return data, idx
        data[key] = value.strip()
    return data, len(lines)


def parse_sections(lines: List[str], start: int) -> Dict[str, List[str]]:
    sections: Dict[str, List[str]] = {}
    current = ""
    for raw in lines[start:]:
        line = raw.rstrip("\n")
        if line.startswith("#"):
            current = line.lstrip("#").strip()
            sections.setdefault(current, [])
            continue
        if current:
            sections[current].append(line)
    return sections


def to_list(lines: List[str]) -> List[str]:
    out: List[str] = []
    for line in lines:
        text = line.strip()
        if not text:
            continue
        if text.startswith("- "):
            text = text[2:].strip()
        out.append(text)
    return out


def first_text(lines: List[str]) -> str:
    for line in lines:
        text = line.strip()
        if text:
            return text[2:].strip() if text.startswith("- ") else text
    return ""


def build_json(
    result: str,
    ux_path: Path,
    front: Dict[str, str],
    warnings: List[str],
    failed_check: str | None = None,
    generated_task_id: str | None = None,
    would_write: str | None = None,
    written_path: str | None = None,
) -> str:
    payload = {
        "result": result,
        "ux_path": ux_path.as_posix(),
        "ui_contract_required": parse_bool(front.get("ui_contract_required", "false")),
        "ui_contract_present": parse_bool(front.get("ui_contract_present", "false")),
        "ui_contract_reference": front.get("ui_contract_reference", ""),
        "ui_contract_reference_checked_on_disk": False,
        "validation_order": VALIDATION_ORDER,
        "failed_check": failed_check,
        "generated_task_id": generated_task_id,
        "would_write": would_write,
        "written_path": written_path,
        "warnings": warnings,
        "non_approval_warning": "Generated UX task contracts are candidate contracts only and are not approval.",
    }
    return json.dumps(payload, ensure_ascii=False)


def check_out_path(out_dir: Path, repo_root: Path) -> bool:
    queue_path = (repo_root / "tasks/queue").resolve()
    out_resolved = out_dir.resolve()
    try:
        common = Path(__import__("os").path.commonpath([str(queue_path), str(out_resolved)]))
    except ValueError:
        return False
    return common == queue_path


def make_contract(ux_path: Path, front: Dict[str, str], sections: Dict[str, List[str]], result_line: str) -> Tuple[str, str]:
    ux_id = front.get("ux_id", "").strip()
    normalized = normalize_ux_id(ux_id)
    generated_task_id = f"ux_{normalized}_task_contract"

    title = front.get("title", "").strip()
    goal = first_text(sections.get("UX Goal", [])) or title or "TODO"

    screens = to_list(sections.get("Screens", []))
    flows = to_list(sections.get("User Flows", []))
    state_matrix = to_list(sections.get("State and Error Matrix", []))
    access = to_list(sections.get("Accessibility Notes", []))
    responsive = to_list(sections.get("Responsive Behavior", []))
    ux_copy = to_list(sections.get("UX Copy", []))
    acceptance = to_list(sections.get("UX Acceptance Criteria", [])) or ["TODO"]

    expected_result = acceptance[0] if acceptance else "TODO"
    in_scope = screens + flows + state_matrix + access + responsive + ux_copy
    if not in_scope:
        in_scope = ["TODO"]

    out_of_scope = to_list(sections.get("Out of Scope", [])) or ["TODO"]
    known_risks = to_list(sections.get("Known Risks", []))
    risk_reason = known_risks[0] if known_risks else "Generator default risk reason"

    priority = front.get("priority", "normal").strip().lower()
    if priority not in {"high", "normal", "low"}:
        priority = "normal"

    risk_level = front.get("risk_level", "MEDIUM").strip().upper()
    if risk_level not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        risk_level = "MEDIUM"

    human_approval_required = risk_level in {"HIGH", "CRITICAL"}
    owner_review_required = risk_level == "CRITICAL"
    created_at = now_utc_z()

    source_ui_contract = front.get("ui_contract_reference", "TODO") or "TODO"

    def yaml_list(items: List[str]) -> str:
        return "\n" + "\n".join(f"  - {item}" for item in items)

    md = f"""---
contract_version: 2
task_id: {generated_task_id}
source_spec: TODO
source_ux: {ux_path.as_posix()}
source_ui_contract: {source_ui_contract}
goal: {goal}
expected_result: {expected_result}
in_scope:{yaml_list(in_scope)}
out_of_scope:{yaml_list(out_of_scope)}
affected_paths:
  - TODO
forbidden_paths:
  - tasks/active-task.md
  - tasks/queue/
  - components/ui/*
  - @radix-ui/*
dependencies: []
blocked_by: []
priority: {priority}
risk_level: {risk_level}
risk_reason: {risk_reason}
acceptance_criteria:{yaml_list(acceptance)}
validation_plan:
  - TODO
  - UI Contract compliance check placeholder
rollback_plan: TODO
human_approval_required: {str(human_approval_required).lower()}
owner_review_required: {str(owner_review_required).lower()}
context_required: true
created_at: {created_at}
---

Result: {result_line}

## Summary
Candidate UX Task Contract generated from approved UX artifact.

## Source References
- source_spec: TODO
- source_ux: {ux_path.as_posix()}
- source_ui_contract: {source_ui_contract}

## UX Goal
{goal}

## Screens
"""
    for i in screens:
        md += f"- {i}\n"
    if not screens:
        md += "- TODO\n"

    md += "\n## User Flows\n"
    for i in flows:
        md += f"- {i}\n"
    if not flows:
        md += "- TODO\n"

    md += "\n## State and Error Matrix\n"
    for i in state_matrix:
        md += f"- {i}\n"
    if not state_matrix:
        md += "- TODO\n"

    md += "\n## UX Acceptance Criteria\n"
    for i in acceptance:
        md += f"- {i}\n"

    md += "\n## Accessibility Notes\n"
    for i in access:
        md += f"- {i}\n"
    if not access:
        md += "- TODO\n"

    md += "\n## Responsive Behavior\n"
    for i in responsive:
        md += f"- {i}\n"
    if not responsive:
        md += "- TODO\n"

    md += "\n## UX Copy\n"
    for i in ux_copy:
        md += f"- {i}\n"
    if not ux_copy:
        md += "- TODO\n"

    md += """
## UI Contract Boundary
- UX intent must be implemented through semantic application components or approved UI contract abstractions.
- Do not import components/ui/* directly from generated feature code unless a later UI rule explicitly allows it.
- Do not import @radix-ui/* directly from generated feature code unless a later UI rule explicitly allows it.
- Do not hardcode colors, spacing, typography, animation, or visual identity from UX prose.
- UX prose describes user experience intent, not direct implementation authority.
- Missing UI Contract blocks UI task readiness.
- ui_contract_present: true in UX frontmatter does not prove the referenced UI Contract file exists on disk.

## In Scope
"""
    for i in in_scope:
        md += f"- {i}\n"

    md += "\n## Out of Scope\n"
    for i in out_of_scope:
        md += f"- {i}\n"

    md += """
## Validation Plan
- TODO
- UI Contract compliance check placeholder

## Rollback Plan
- TODO

## Non-Approval Warning
This generated UX Task Contract is not approval.
This generated UX Task Contract does not authorize execution.
This generated UX Task Contract does not authorize raw styling or direct UI library use.
This generated UX Task Contract does not authorize commit, push, merge, deploy, or release.
This generated UX Task Contract does not replace HumanApprovalGate.

## Known Gaps
source_spec: TODO is an MVP placeholder.
affected_paths: TODO may require later human or lint review.
Future task linting may classify these placeholders as TASK_LINT_WARNING or TASK_LINT_NEEDS_REVIEW.
These placeholders do not authorize execution and do not make the task queue-ready by themselves.
ui_contract_present: true is trusted from UX frontmatter in this MVP.
The generator does not verify that ui_contract_reference exists on disk.
Referenced UI Contract artifact existence must be validated later by task linting / UI task decomposition checks.
"""

    return generated_task_id, md


def main() -> int:
    args = parse_args()

    if not args.dry_run and not args.write:
        args.dry_run = True

    ux_path = Path(args.ux)
    if not ux_path.exists():
        payload = build_json(UX_TO_TASK_FAILED, ux_path, {}, ["ux file does not exist"], failed_check="input_path_check")
        print(payload if args.json_mode else f"{UX_TO_TASK_FAILED}\nux file does not exist")
        return 1

    if args.write and not args.out:
        payload = build_json(UX_TO_TASK_FAILED, ux_path, {}, ["--write requires --out"], failed_check="write_mode_precheck")
        print(payload if args.json_mode else f"{UX_TO_TASK_FAILED}\n--write requires --out")
        return 1

    if args.write and args.out:
        out_path = Path(args.out)
        if out_path.exists() and out_path.is_file():
            payload = build_json(UX_TO_TASK_FAILED, ux_path, {}, ["--out exists as a file"], failed_check="output_path_type_check")
            print(payload if args.json_mode else f"{UX_TO_TASK_FAILED}\n--out exists as a file")
            return 1

        repo_root = Path.cwd().resolve()
        if check_out_path(out_path, repo_root):
            payload = build_json(UX_TO_TASK_FAILED, ux_path, {}, ["refusing tasks/queue boundary"], failed_check="queue_boundary_check")
            print(payload if args.json_mode else f"{UX_TO_TASK_FAILED}\nrefusing to write into tasks/queue/")
            return 1

    text = read_text(ux_path)
    lines = text.splitlines(keepends=True)
    front, start = parse_frontmatter_like(lines)
    sections = parse_sections(lines, start)

    status = front.get("status", "").strip()
    if status != "APPROVED":
        payload = build_json(
            UX_TO_TASK_BLOCKED_UX_NOT_APPROVED,
            ux_path,
            front,
            ["status must be APPROVED"],
            failed_check="approval_check",
        )
        print(payload if args.json_mode else f"{UX_TO_TASK_BLOCKED_UX_NOT_APPROVED}\nstatus must be APPROVED")
        return 1

    ui_contract_required = parse_bool(front.get("ui_contract_required", "false"))
    ui_contract_present = parse_bool(front.get("ui_contract_present", "false"))
    if ui_contract_required and not ui_contract_present:
        payload = build_json(
            UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT,
            ux_path,
            front,
            ["ui contract required but not present"],
            failed_check="ui_contract_check",
        )
        print(payload if args.json_mode else f"{UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT}\nui contract required but not present")
        return 1

    ux_id = front.get("ux_id", "").strip()
    title = front.get("title", "").strip()
    if not ux_id and not title:
        payload = build_json(
            UX_TO_TASK_BLOCKED_INVALID_UX,
            ux_path,
            front,
            ["ux_id and title are both empty"],
            failed_check="ux_structure_check",
        )
        print(payload if args.json_mode else f"{UX_TO_TASK_BLOCKED_INVALID_UX}\nux_id and title are both empty")
        return 1

    normalized = normalize_ux_id(ux_id)
    if not normalized:
        payload = build_json(
            UX_TO_TASK_BLOCKED_INVALID_UX,
            ux_path,
            front,
            ["normalized ux_id is empty"],
            failed_check="ux_structure_check",
        )
        print(payload if args.json_mode else f"{UX_TO_TASK_BLOCKED_INVALID_UX}\nnormalized ux_id is empty")
        return 1

    screens = to_list(sections.get("Screens", []))
    if not screens:
        payload = build_json(
            UX_TO_TASK_BLOCKED_INVALID_UX,
            ux_path,
            front,
            ["Screens section is missing or empty"],
            failed_check="ux_structure_check",
        )
        print(payload if args.json_mode else f"{UX_TO_TASK_BLOCKED_INVALID_UX}\nScreens section is missing or empty")
        return 1

    if args.json_mode and not args.write:
        generated_task_id = f"ux_{normalized}_task_contract"
        payload = build_json(
            UX_TO_TASK_DRY_RUN_OK,
            ux_path,
            front,
            [
                "Generated UX Task Contracts are candidate contracts only.",
                "ui_contract_reference_checked_on_disk is false in MVP.",
            ],
            generated_task_id=generated_task_id,
            would_write=f"{generated_task_id}.md",
        )
        print(payload)
        return 0

    generated_task_id, markdown = make_contract(ux_path, front, sections, UX_TO_TASK_DRY_RUN_OK if not args.write else UX_TO_TASK_WRITE_OK)

    if args.write:
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{generated_task_id}.md"
        if out_file.exists():
            payload = build_json(
                UX_TO_TASK_FAILED,
                ux_path,
                front,
                ["output file already exists"],
                failed_check="write_collision_check",
                generated_task_id=generated_task_id,
            )
            print(payload if args.json_mode else f"{UX_TO_TASK_FAILED}\noutput file already exists: {out_file.as_posix()}")
            return 1

        out_file.write_text(markdown, encoding="utf-8")

        if args.json_mode:
            payload = build_json(
                UX_TO_TASK_WRITE_OK,
                ux_path,
                front,
                ["write mode created candidate file"],
                generated_task_id=generated_task_id,
                written_path=out_file.as_posix(),
            )
            print(payload)
        else:
            print(UX_TO_TASK_WRITE_OK)
            print(out_file.as_posix())
        return 0

    print(markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
