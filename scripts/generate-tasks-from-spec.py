#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

TOKEN_DRY_RUN_OK = "SPEC_TO_TASK_DRY_RUN_OK"
TOKEN_WRITE_OK = "SPEC_TO_TASK_WRITE_OK"
TOKEN_BLOCKED_NOT_APPROVED = "SPEC_TO_TASK_BLOCKED_SPEC_NOT_APPROVED"
TOKEN_BLOCKED_INVALID_SPEC = "SPEC_TO_TASK_BLOCKED_INVALID_SPEC"
TOKEN_NEEDS_REVIEW = "SPEC_TO_TASK_NEEDS_REVIEW"
TOKEN_FAILED = "SPEC_TO_TASK_FAILED"

NON_APPROVAL_WARNING = [
    "This generated Task Contract is not approval.",
    "This generated Task Contract does not authorize execution.",
    "This generated Task Contract does not authorize commit, push, merge, deploy, or release.",
    "This generated Task Contract does not replace HumanApprovalGate.",
]


class SpecParseError(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate candidate Task Contract v2 from approved Spec markdown")
    parser.add_argument("--spec", required=True, help="Path to Spec markdown file")
    parser.add_argument("--out", help="Output directory for --write mode")
    parser.add_argument("--dry-run", action="store_true", help="Print candidate contract to stdout")
    parser.add_argument("--write", action="store_true", help="Write candidate contract file")
    parser.add_argument("--json", action="store_true", dest="json_mode", help="Emit JSON summary")
    return parser.parse_args()


def now_utc_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-") or "generated-task"


def read_spec(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SpecParseError(f"cannot read spec: {exc}") from exc


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
            heading = line.lstrip("#").strip()
            current = heading
            sections.setdefault(current, [])
            continue
        if current:
            sections[current].append(line)
    return sections


def clean_list(lines: List[str]) -> List[str]:
    items: List[str] = []
    for line in lines:
        text = line.strip()
        if not text:
            continue
        if text.startswith("- "):
            text = text[2:].strip()
        items.append(text)
    return items


def first_non_empty(lines: List[str]) -> str:
    for line in lines:
        text = line.strip()
        if text:
            return text
    return ""


def evaluate_spec(front: Dict[str, str]) -> str:
    status = front.get("status", "").strip()
    if status != "APPROVED":
        return TOKEN_BLOCKED_NOT_APPROVED
    spec_id = front.get("spec_id", "").strip()
    title = front.get("title", "").strip()
    if not spec_id and not title:
        return TOKEN_BLOCKED_INVALID_SPEC
    return "OK"


def validate_priority(priority: str) -> str:
    value = (priority or "").strip().lower()
    if value in {"high", "normal", "low"}:
        return value
    return "normal"


def validate_risk_level(risk_level: str) -> str:
    value = (risk_level or "").strip().upper()
    if value in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        return value
    return "MEDIUM"


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def build_candidate(spec_path: Path, front: Dict[str, str], sections: Dict[str, List[str]], result_token: str) -> Tuple[str, str]:
    spec_id = front.get("spec_id", "").strip()
    title = front.get("title", "").strip()
    task_id_base = spec_id or slugify(title) or slugify(spec_path.stem)
    task_id = slugify(task_id_base)

    goal = first_non_empty(sections.get("Goal", [])) or title or "TODO"
    functional_items = clean_list(sections.get("Functional Requirements", []))
    expected_result = functional_items[0] if functional_items else "TODO"
    in_scope = functional_items or ["TODO"]

    out_scope = clean_list(sections.get("Out of Scope", [])) or ["TODO"]
    acceptance = clean_list(sections.get("Acceptance Criteria", [])) or ["TODO"]
    validation = clean_list(sections.get("Validation Plan", [])) or ["TODO"]

    known_risks = clean_list(sections.get("Known Risks", []))
    risk_reason = known_risks[0] if known_risks else "Generator default risk reason"

    risk_level = validate_risk_level(front.get("risk_level", ""))
    priority = validate_priority(front.get("priority", ""))

    human_approval_required = risk_level in {"HIGH", "CRITICAL"}
    owner_review_required = risk_level == "CRITICAL"

    created_at = now_utc_z()

    def yaml_list(items: List[str]) -> str:
        if not items:
            return "[]"
        return "\n" + "\n".join(f"  - {item}" for item in items)

    body = f"""---
contract_version: 2
task_id: {task_id}
source_spec: {spec_path.as_posix()}
source_ux: TODO
source_ui_contract: TODO
goal: {goal}
expected_result: {expected_result}
in_scope:{yaml_list(in_scope)}
out_of_scope:{yaml_list(out_scope)}
affected_paths:
  - TODO
forbidden_paths:
  - tasks/active-task.md
  - tasks/queue/
dependencies: []
blocked_by: []
priority: {priority}
risk_level: {risk_level}
risk_reason: {risk_reason}
acceptance_criteria:{yaml_list(acceptance)}
validation_plan:{yaml_list(validation)}
rollback_plan: TODO
human_approval_required: {bool_text(human_approval_required)}
owner_review_required: {bool_text(owner_review_required)}
context_required: true
created_at: {created_at}
---

result_token: {result_token}

## Summary
Candidate Task Contract v2 generated from approved Spec input.

## Source References
- source_spec: {spec_path.as_posix()}
- source_ux: TODO
- source_ui_contract: TODO

## Goal
{goal}

## Expected Result
{expected_result}

## In Scope
"""
    for item in in_scope:
        body += f"- {item}\n"

    body += "\n## Out of Scope\n"
    for item in out_scope:
        body += f"- {item}\n"

    body += "\n## Acceptance Criteria\n"
    for item in acceptance:
        body += f"- {item}\n"

    body += "\n## Validation Plan\n"
    for item in validation:
        body += f"- {item}\n"

    body += "\n## Rollback Plan\n- TODO\n\n## Non-Approval Warning\n"
    for line in NON_APPROVAL_WARNING:
        body += f"{line}\n"

    body += (
        "\n## Known Gaps\n"
        "source_ux: TODO and source_ui_contract: TODO are MVP placeholders.\n"
        "Future task linting may classify these placeholders as TASK_LINT_WARNING or TASK_LINT_NEEDS_REVIEW.\n"
        "These placeholders do not authorize execution and do not make the task queue-ready by themselves.\n"
    )

    return task_id, body


def fail_json(spec_path: Path, token: str, message: str, warnings: List[str] | None = None) -> str:
    payload = {
        "result": token,
        "spec_path": spec_path.as_posix(),
        "message": message,
        "warnings": warnings or [],
        "non_approval_warning": "Generated task contracts are candidate contracts only and are not approval.",
    }
    return json.dumps(payload, ensure_ascii=False)


def is_queue_path(path: Path) -> bool:
    queue_root = Path("tasks/queue").resolve()
    target = path.resolve()
    return target == queue_root or queue_root in target.parents


def main() -> int:
    args = parse_args()

    if not args.dry_run and not args.write:
        args.dry_run = True

    spec_path = Path(args.spec)
    if not spec_path.exists():
        token = TOKEN_FAILED
        message = "spec file does not exist"
        if args.json_mode:
            print(fail_json(spec_path, token, message))
        else:
            print(token)
            print(message)
        return 1

    if args.write and not args.out:
        token = TOKEN_FAILED
        message = "--write requires --out"
        if args.json_mode:
            print(fail_json(spec_path, token, message))
        else:
            print(token)
            print(message)
        return 1

    if args.write and args.out:
        out_dir = Path(args.out)
        if is_queue_path(out_dir):
            token = TOKEN_FAILED
            message = "refusing to write into tasks/queue/"
            if args.json_mode:
                print(fail_json(spec_path, token, message))
            else:
                print(token)
                print(message)
            return 1

    try:
        text = read_spec(spec_path)
    except SpecParseError as exc:
        token = TOKEN_FAILED
        if args.json_mode:
            print(fail_json(spec_path, token, str(exc)))
        else:
            print(token)
            print(str(exc))
        return 1

    lines = text.splitlines(keepends=True)
    front, body_start = parse_frontmatter_like(lines)
    sections = parse_sections(lines, body_start)

    readiness = evaluate_spec(front)
    if readiness == TOKEN_BLOCKED_NOT_APPROVED:
        msg = "Spec status must be exactly APPROVED"
        if args.json_mode:
            print(fail_json(spec_path, readiness, msg))
        else:
            print(readiness)
            print(msg)
        return 1

    if readiness == TOKEN_BLOCKED_INVALID_SPEC:
        msg = "APPROVED Spec must include spec_id or title"
        if args.json_mode:
            print(fail_json(spec_path, readiness, msg))
        else:
            print(readiness)
            print(msg)
        return 1

    result_token = TOKEN_DRY_RUN_OK if args.dry_run and not args.write else TOKEN_WRITE_OK
    task_id, markdown = build_candidate(spec_path, front, sections, result_token)

    warnings = [
        "Generated Task Contracts are candidate contracts only.",
        "source_ux: TODO and source_ui_contract: TODO are MVP placeholders.",
    ]

    if args.write:
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{task_id}.md"
        if out_file.exists():
            token = TOKEN_FAILED
            message = f"output file already exists: {out_file.as_posix()}"
            if args.json_mode:
                print(fail_json(spec_path, token, message, warnings))
            else:
                print(token)
                print(message)
            return 1
        out_file.write_text(markdown, encoding="utf-8")

        if args.json_mode:
            payload = {
                "result": TOKEN_WRITE_OK,
                "spec_path": spec_path.as_posix(),
                "written_path": out_file.as_posix(),
                "generated_task_id": task_id,
                "warnings": warnings,
                "non_approval_warning": "Generated task contracts are candidate contracts only and are not approval.",
            }
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print(TOKEN_WRITE_OK)
            print(out_file.as_posix())
        return 0

    if args.json_mode:
        payload = {
            "result": TOKEN_DRY_RUN_OK,
            "spec_path": spec_path.as_posix(),
            "would_write": f"{task_id}.md",
            "generated_task_id": task_id,
            "warnings": warnings,
            "non_approval_warning": "Generated task contracts are candidate contracts only and are not approval.",
        }
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(markdown)

    return 0


if __name__ == "__main__":
    sys.exit(main())
