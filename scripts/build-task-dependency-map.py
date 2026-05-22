#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

TASK_DEPENDENCY_MAP_DRY_RUN_OK = "TASK_DEPENDENCY_MAP_DRY_RUN_OK"
TASK_DEPENDENCY_MAP_WRITE_OK = "TASK_DEPENDENCY_MAP_WRITE_OK"
TASK_DEPENDENCY_MAP_BLOCKED_CIRCULAR_DEPENDENCY = "TASK_DEPENDENCY_MAP_BLOCKED_CIRCULAR_DEPENDENCY"
TASK_DEPENDENCY_MAP_BLOCKED_MISSING_DEPENDENCY = "TASK_DEPENDENCY_MAP_BLOCKED_MISSING_DEPENDENCY"
TASK_DEPENDENCY_MAP_BLOCKED_DUPLICATE_TASK_ID = "TASK_DEPENDENCY_MAP_BLOCKED_DUPLICATE_TASK_ID"
TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK = "TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK"
TASK_DEPENDENCY_MAP_NEEDS_REVIEW = "TASK_DEPENDENCY_MAP_NEEDS_REVIEW"
TASK_DEPENDENCY_MAP_FAILED = "TASK_DEPENDENCY_MAP_FAILED"

NON_APPROVAL_WARNING = [
    "Dependency map does not approve work",
    "Dependency map does not authorize execution",
    "Dependency map does not authorize commit, push, merge, or deploy",
    "Dependency map does not replace HumanApprovalGate",
    "Dependency map does not mark tasks ready in the real queue",
    "Queue placement does not authorize execution",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build task dependency map from task frontmatter files")
    parser.add_argument("--input", required=True, help="Directory with task markdown files")
    parser.add_argument("--out", help="Output directory for --write mode")
    parser.add_argument("--dry-run", action="store_true", help="Print dependency map to stdout")
    parser.add_argument("--write", action="store_true", help="Write dependency-map.md into --out directory")
    parser.add_argument("--json", action="store_true", dest="json_mode", help="Emit JSON summary")
    return parser.parse_args()


def read_frontmatter(path: Path) -> Dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("missing_frontmatter_start")

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("missing_frontmatter_end")

    body = lines[1:end_idx]
    data: Dict[str, object] = {}
    i = 0
    while i < len(body):
        line = body[i]
        if not line.strip():
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()

        if value == "[]":
            data[key] = []
            i += 1
            continue

        if value:
            data[key] = value
            i += 1
            continue

        items: List[str] = []
        j = i + 1
        while j < len(body):
            candidate = body[j]
            stripped = candidate.strip()
            if not stripped:
                j += 1
                continue
            if stripped.startswith("- "):
                items.append(stripped[2:].strip())
                j += 1
                continue
            break
        data[key] = items if items else ""
        i = j

    return data


def ensure_list(value: object) -> List[str]:
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned in ("", "[]"):
            return []
        return [cleaned]
    return []


def fail(token: str, msg: str, json_mode: bool, extra: Dict[str, object] | None = None) -> int:
    payload = {
        "result": token,
        "message": msg,
        "non_approval_warning": "Dependency map does not authorize execution.",
    }
    if extra:
        payload.update(extra)
    if json_mode:
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(token)
        print(msg)
    return 1


def protected_out_path(out_path: Path, repo_root: Path) -> bool:
    reports_path = (repo_root / "reports").resolve()
    queue_path = (repo_root / "tasks/queue").resolve()
    out_resolved = out_path.resolve()
    try:
        common_reports = Path(os.path.commonpath([str(reports_path), str(out_resolved)]))
        common_queue = Path(os.path.commonpath([str(queue_path), str(out_resolved)]))
    except ValueError:
        return False
    return common_reports == reports_path or common_queue == queue_path


def detect_cycle(task_ids: List[str], depends_on: Dict[str, List[str]]) -> bool:
    visiting = set()
    visited = set()

    def dfs(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for nxt in depends_on.get(node, []):
            if dfs(nxt):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    for tid in sorted(task_ids):
        if dfs(tid):
            return True
    return False


def build_entries(tasks: Dict[str, Dict[str, object]]) -> List[Dict[str, object]]:
    depends = {tid: ensure_list(meta.get("depends_on")) for tid, meta in tasks.items()}
    blocked = {tid: ensure_list(meta.get("blocked_by")) for tid, meta in tasks.items()}

    reverse: Dict[str, List[str]] = {tid: [] for tid in tasks}
    for tid, deps in depends.items():
        for dep in deps:
            reverse[dep].append(tid)
    for tid in reverse:
        reverse[tid] = sorted(reverse[tid])

    hints: Dict[str, int | None] = {tid: None for tid in tasks}
    ready = {tid for tid in tasks if not blocked[tid]}

    # Priority does not override blocked_by or depends_on
    ordered: List[str] = []
    remaining = set(ready)
    order = 1
    while True:
        progressed = False
        for tid in sorted(remaining):
            deps = depends[tid]
            if all((dep in ordered) for dep in deps if dep in ready) and all(dep in tasks for dep in deps):
                hints[tid] = order
                order += 1
                ordered.append(tid)
                progressed = True
        for tid in ordered:
            remaining.discard(tid)
        if not progressed:
            break

    entries: List[Dict[str, object]] = []
    for tid in sorted(tasks):
        readiness = "blocked" if blocked[tid] else ("ready" if hints[tid] is not None else "blocked")
        entries.append(
            {
                "task_id": tid,
                "depends_on": depends[tid],
                "blocked_by": blocked[tid],
                "priority": tasks[tid]["priority"],
                "risk_level": tasks[tid]["risk_level"],
                "readiness": readiness,
                "execution_order_hint": hints[tid],
                "unblocks": reverse[tid],
            }
        )
    return entries


def render_markdown(result: str, entries: List[Dict[str, object]]) -> str:
    lines = [
        f"Result: {result}",
        "",
        "Dependency map orders work.",
        "Dependency map does not approve work.",
        "Dependency map does not authorize execution.",
        "Priority does not override blocked_by.",
        "HIGH priority blocked task remains blocked.",
        "",
    ]
    for entry in entries:
        lines.append(f"- task_id: {entry['task_id']}")
        lines.append(f"  readiness: {entry['readiness']}")
        hint = "null" if entry["execution_order_hint"] is None else str(entry["execution_order_hint"])
        lines.append(f"  execution_order_hint: {hint}")
        lines.append(f"  depends_on: {entry['depends_on']}")
        lines.append(f"  blocked_by: {entry['blocked_by']}")
        lines.append("  unblocks:")
        for u in entry["unblocks"]:
            lines.append(f"    - {u}")
        if not entry["unblocks"]:
            lines.append("    -")
    lines.append("")
    lines.extend(NON_APPROVAL_WARNING)
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()

    if not args.dry_run and not args.write:
        args.dry_run = True

    if args.json_mode and args.write:
        return fail(
            TASK_DEPENDENCY_MAP_FAILED,
            "--json and --write together are not supported in this MVP",
            args.json_mode,
            {"failed_check": "mode_check"},
        )

    input_dir = Path(args.input)
    if not input_dir.exists() or not input_dir.is_dir():
        return fail(TASK_DEPENDENCY_MAP_FAILED, "--input must be an existing directory", args.json_mode, {"failed_check": "input_check"})

    if args.write and not args.out:
        return fail(TASK_DEPENDENCY_MAP_FAILED, "--write requires --out", args.json_mode, {"failed_check": "write_precheck"})

    out_dir = Path(args.out) if args.out else None
    if args.write and out_dir:
        if out_dir.exists() and out_dir.is_file():
            return fail(TASK_DEPENDENCY_MAP_FAILED, "--out points to an existing file", args.json_mode, {"failed_check": "out_type_check"})

        repo_root = Path.cwd().resolve()
        if protected_out_path(out_dir, repo_root):
            return fail(TASK_DEPENDENCY_MAP_FAILED, "protected output path refused", args.json_mode, {"failed_check": "protected_path_check"})

    files = sorted(input_dir.rglob("*.md"))
    tasks: Dict[str, Dict[str, object]] = {}

    for fp in files:
        try:
            meta = read_frontmatter(fp)
        except Exception:
            return fail(TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK, f"invalid frontmatter: {fp.as_posix()}", args.json_mode, {"failed_check": "frontmatter_parse"})

        task_id = str(meta.get("task_id", "")).strip()
        if not task_id:
            return fail(TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK, f"missing task_id: {fp.as_posix()}", args.json_mode, {"failed_check": "task_validation"})

        if task_id in tasks:
            return fail(TASK_DEPENDENCY_MAP_BLOCKED_DUPLICATE_TASK_ID, f"duplicate task_id: {task_id}", args.json_mode, {"failed_check": "duplicate_task_id", "task_id": task_id})

        priority = str(meta.get("priority", "")).strip()
        risk_level = str(meta.get("risk_level", "")).strip()
        if priority not in {"high", "normal", "low"}:
            return fail(TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK, f"invalid priority in {fp.as_posix()}", args.json_mode, {"failed_check": "task_validation"})
        if risk_level not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            return fail(TASK_DEPENDENCY_MAP_BLOCKED_INVALID_TASK, f"invalid risk_level in {fp.as_posix()}", args.json_mode, {"failed_check": "task_validation"})

        tasks[task_id] = {
            "task_id": task_id,
            "depends_on": ensure_list(meta.get("depends_on")),
            "blocked_by": ensure_list(meta.get("blocked_by")),
            "priority": priority,
            "risk_level": risk_level,
        }

    for tid, meta in tasks.items():
        for dep in ensure_list(meta.get("depends_on")):
            if dep not in tasks:
                return fail(
                    TASK_DEPENDENCY_MAP_BLOCKED_MISSING_DEPENDENCY,
                    f"missing dependency: {tid} -> {dep}",
                    args.json_mode,
                    {"failed_check": "missing_dependency", "task_id": tid, "missing_dependency": dep},
                )

    depends_map = {tid: ensure_list(meta.get("depends_on")) for tid, meta in tasks.items()}
    if detect_cycle(sorted(tasks.keys()), depends_map):
        return fail(
            TASK_DEPENDENCY_MAP_BLOCKED_CIRCULAR_DEPENDENCY,
            "circular dependency detected",
            args.json_mode,
            {"failed_check": "circular_dependency"},
        )

    entries = build_entries(tasks)

    if args.json_mode:
        print(
            json.dumps(
                {
                    "result": TASK_DEPENDENCY_MAP_DRY_RUN_OK,
                    "entries": entries,
                    "non_approval_warning": "Dependency map does not authorize execution.",
                },
                ensure_ascii=False,
            )
        )
        return 0

    if args.write and out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "dependency-map.md"
        if out_file.exists():
            return fail(
                TASK_DEPENDENCY_MAP_FAILED,
                "Write mode must refuse to overwrite an existing dependency-map.md",
                args.json_mode,
                {"failed_check": "overwrite_protection"},
            )
        content = render_markdown(TASK_DEPENDENCY_MAP_WRITE_OK, entries)
        out_file.write_text(content, encoding="utf-8")
        print(content, end="")
        return 0

    print(render_markdown(TASK_DEPENDENCY_MAP_DRY_RUN_OK, entries), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
