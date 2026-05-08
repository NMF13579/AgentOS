#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

READY = "CONTEXT_PIPELINE_READY"
READY_WARN = "CONTEXT_PIPELINE_READY_WITH_WARNINGS"
MISSING = "CONTEXT_PIPELINE_MISSING"
INVALID = "CONTEXT_PIPELINE_INVALID"
STALE = "CONTEXT_PIPELINE_STALE"
VIOLATION = "CONTEXT_PIPELINE_VIOLATION"
INCOMPLETE = "CONTEXT_PIPELINE_INCOMPLETE"
NEEDS_REVIEW = "CONTEXT_PIPELINE_NEEDS_REVIEW"
BLOCKED = "CONTEXT_PIPELINE_BLOCKED"
OK = "CONTEXT_PIPELINE_OK"

ORDER = {BLOCKED: 0, VIOLATION: 1, INVALID: 2, STALE: 3, INCOMPLETE: 4, MISSING: 5, NEEDS_REVIEW: 6, READY_WARN: 7, READY: 8}

INDEX_MAP = {
    "CONTEXT_INDEX_FRESH": READY,
    "CONTEXT_INDEX_FRESH_WITH_WARNINGS": READY_WARN,
    "CONTEXT_INDEX_STALE": STALE,
    "CONTEXT_INDEX_MISSING": MISSING,
    "CONTEXT_INDEX_INVALID": INVALID,
    "CONTEXT_INDEX_INCOMPLETE": INCOMPLETE,
    "CONTEXT_INDEX_NEEDS_REVIEW": NEEDS_REVIEW,
    "CONTEXT_INDEX_BLOCKED": BLOCKED,
}
PACK_MAP = {
    "CONTEXT_PACK_VALID": READY,
    "CONTEXT_PACK_VALID_WITH_WARNINGS": READY_WARN,
    "CONTEXT_PACK_MISSING": MISSING,
    "CONTEXT_PACK_INVALID": INVALID,
    "CONTEXT_PACK_STALE": STALE,
    "CONTEXT_PACK_INCOMPLETE": INCOMPLETE,
    "CONTEXT_PACK_NEEDS_REVIEW": NEEDS_REVIEW,
    "CONTEXT_PACK_BLOCKED": BLOCKED,
}
COMP_MAP = {
    "CONTEXT_COMPLIANCE_PASS": READY,
    "CONTEXT_COMPLIANCE_PASS_WITH_WARNINGS": READY_WARN,
    "CONTEXT_COMPLIANCE_MISSING": MISSING,
    "CONTEXT_COMPLIANCE_INVALID": INVALID,
    "CONTEXT_COMPLIANCE_VIOLATION": VIOLATION,
    "CONTEXT_COMPLIANCE_INCOMPLETE": INCOMPLETE,
    "CONTEXT_COMPLIANCE_NEEDS_REVIEW": NEEDS_REVIEW,
    "CONTEXT_COMPLIANCE_BLOCKED": BLOCKED,
}


def pick(a: str, b: str) -> str:
    return b if ORDER[b] < ORDER[a] else a


def run_gate(cmd: list[str], timeout: int = 30) -> tuple[int, dict[str, Any] | None, str | None]:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, shell=False, timeout=timeout)
    except subprocess.TimeoutExpired:
        return 124, None, "timeout"
    except Exception as exc:
        return 125, None, f"exec_failed:{exc}"

    try:
        data = json.loads(proc.stdout or "{}")
    except Exception:
        return proc.returncode, None, "malformed_json"

    return proc.returncode, data, None


def parse_active_task(root: Path, task_rel: str) -> tuple[str, list[str]]:
    state = "unknown"
    allowed: list[str] = []
    p = root / task_rel
    if not p.exists():
        return state, allowed
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^state:\s*([A-Za-z0-9_-]+)\s*$", text, re.MULTILINE)
    if m:
        state = m.group(1).strip()

    m2 = re.search(r"allowed_paths:\s*\n((?:\s+-\s*.+\n)+)", text)
    if m2:
        for line in m2.group(1).splitlines():
            line = line.strip()
            if line.startswith("-"):
                allowed.append(line[1:].strip())
    return state, allowed


def read_changed_files(root: Path, rel: str) -> list[str]:
    p = root / rel
    if not p.exists():
        return []
    return [x.strip() for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def file_invalid_json(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        json.loads(path.read_text(encoding="utf-8"))
        return False
    except Exception:
        return True


def outside_allowed(path: str, allowed_paths: list[str]) -> bool:
    if not allowed_paths:
        return True
    for a in allowed_paths:
        if a.endswith("/"):
            if path.startswith(a):
                return False
        elif path == a:
            return False
    return True


def legacy_result(index_r: str, pack_r: str, comp_r: str) -> str:
    result = READY
    result = pick(result, INDEX_MAP.get(index_r, INCOMPLETE))
    result = pick(result, PACK_MAP.get(pack_r, INCOMPLETE))
    result = pick(result, COMP_MAP.get(comp_r, INCOMPLETE))
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description="Unified Context Pipeline Check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--task", default="tasks/active-task.md")
    ap.add_argument("--index", default="data/context-index.json")
    ap.add_argument("--context", default="reports/context-pack.md")
    ap.add_argument("--plan", default="reports/plan.md")
    ap.add_argument("--verification", default="reports/context-verification.md")
    ap.add_argument("--changed-files", default="reports/changed-files.txt")
    ap.add_argument("--mode", choices=["plan", "verification", "both"], default="both")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--advisory", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    findings: list[dict[str, Any]] = []

    gate_cmds = {
        "index": [sys.executable, "scripts/check-context-index-freshness.py", "--json", "--root", str(root), "--index", args.index],
        "pack": [sys.executable, "scripts/check-required-context-pack.py", "--json", "--root", str(root), "--task", args.task, "--context", args.context, "--index", args.index],
        "compliance": [sys.executable, "scripts/check-required-context-compliance.py", "--json", "--root", str(root), "--task", args.task, "--context", args.context, "--plan", args.plan, "--verification", args.verification, "--changed-files", args.changed_files, "--mode", args.mode],
    }

    gate_results: dict[str, dict[str, Any]] = {}
    for key, cmd in gate_cmds.items():
        rc, data, err = run_gate(cmd)
        gate_results[key] = {"exit_code": rc, "data": data, "error": err, "command": " ".join(cmd)}

    idx_raw = (gate_results["index"]["data"] or {}).get("result")
    pack_raw = (gate_results["pack"]["data"] or {}).get("result")
    comp_raw = (gate_results["compliance"]["data"] or {}).get("result")

    state, allowed_paths = parse_active_task(root, args.task)
    changed_files = read_changed_files(root, args.changed_files)
    has_scope_violation = any(outside_allowed(f, allowed_paths) for f in changed_files)

    # BLOCKING classification
    blocking: list[str] = []

    if file_invalid_json(root / "data/context-index.json"):
        blocking.append("invalid JSON: data/context-index.json")
    if file_invalid_json(root / "data/context-pack.json"):
        blocking.append("invalid JSON: data/context-pack.json")

    idx_err = gate_results["index"]["error"]
    if idx_err and idx_err.startswith("exec_failed"):
        blocking.append("generator/checker execution failure with Python exception")

    if comp_raw == "CONTEXT_COMPLIANCE_VIOLATION" and has_scope_violation:
        blocking.append("context compliance violation with out-of-scope files")

    if state not in ("completed", "idle", "none") and has_scope_violation:
        blocking.append("active-task state != completed with simultaneous scope violation")

    # ADVISORY classification
    advisory: list[str] = []

    if pack_raw == "CONTEXT_PACK_STALE":
        advisory.append("context pack stale hash")
    if idx_raw == "CONTEXT_INDEX_NEEDS_REVIEW":
        advisory.append("context index needs review (non-critical metadata/frontmatter issues)")

    comp_data = gate_results["compliance"]["data"] or {}
    for f in comp_data.get("findings", []) if isinstance(comp_data.get("findings"), list) else []:
        msg = str(f.get("message", ""))
        cat = str(f.get("category", ""))
        if "required context not acknowledged" in msg or cat == "required_context_unacknowledged":
            advisory.append("required context not acknowledged")
        if "verification missing" in msg or cat == "verification_missing":
            advisory.append("verification missing")
        if "Undeclared changed files" in msg and not has_scope_violation:
            advisory.append("undeclared changed files inside allowed_paths")

    if state == "completed":
        advisory.append("active-task state completed treated as advisory context")

    # Compose result by mode
    mode = "legacy"
    if args.strict:
        mode = "strict"
    if args.advisory:
        mode = "advisory"

    if args.strict and args.advisory:
        mode = "strict+advisory"

    if mode == "strict":
        result = OK if not blocking else BLOCKED
        exit_code = 0 if not blocking else 1
    elif mode == "advisory":
        result = READY_WARN if advisory else READY
        exit_code = 0
    else:
        # backward-compatible: legacy aggregation
        result = legacy_result(str(idx_raw), str(pack_raw), str(comp_raw))
        exit_code = 0 if result == READY else 1

    for b in blocking:
        findings.append({"severity": "blocking", "category": "blocking", "message": b})
    for w in advisory:
        findings.append({"severity": "warning", "category": "advisory", "message": w})

    payload = {
        "result": result,
        "mode": mode,
        "task_path": args.task,
        "index_path": args.index,
        "context_path": args.context,
        "plan_path": args.plan,
        "verification_path": args.verification,
        "changed_files_path": args.changed_files,
        "active_task_state": state,
        "allowed_paths": allowed_paths,
        "scope_violation": has_scope_violation,
        "blocking_reasons": blocking,
        "advisory_reasons": advisory,
        "gate_results": {
            "index": {"result": idx_raw, "exit_code": gate_results["index"]["exit_code"], "error": gate_results["index"]["error"]},
            "pack": {"result": pack_raw, "exit_code": gate_results["pack"]["exit_code"], "error": gate_results["pack"]["error"]},
            "compliance": {"result": comp_raw, "exit_code": gate_results["compliance"]["exit_code"], "error": gate_results["compliance"]["error"]},
        },
        "findings": findings,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"mode: {mode}")
        print(f"blocking: {len(blocking)}")
        print(f"advisory: {len(advisory)}")
        print(result)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
