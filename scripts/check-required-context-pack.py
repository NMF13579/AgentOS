#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

RESULT_VALID = "CONTEXT_PACK_VALID"
RESULT_VALID_WARN = "CONTEXT_PACK_VALID_WITH_WARNINGS"
RESULT_MISSING = "CONTEXT_PACK_MISSING"
RESULT_INVALID = "CONTEXT_PACK_INVALID"
RESULT_STALE = "CONTEXT_PACK_STALE"
RESULT_INCOMPLETE = "CONTEXT_PACK_INCOMPLETE"
RESULT_NEEDS_REVIEW = "CONTEXT_PACK_NEEDS_REVIEW"
RESULT_BLOCKED = "CONTEXT_PACK_BLOCKED"

ORDER = {
    RESULT_BLOCKED: 0,
    RESULT_INVALID: 1,
    RESULT_STALE: 2,
    RESULT_INCOMPLETE: 3,
    RESULT_MISSING: 4,
    RESULT_NEEDS_REVIEW: 5,
    RESULT_VALID_WARN: 6,
    RESULT_VALID: 7,
}

WIN_ABS_RE = re.compile(r"^[A-Za-z]:[\\]")
TASK_ID_RE = re.compile(r"task[_-]?id\s*:\s*([A-Za-z0-9._:-]+)", re.IGNORECASE)
CTX_HASH_RE = re.compile(r"context_index_hash\s*:\s*(sha256:[0-9a-fA-F]{64})", re.IGNORECASE)
REPO_HASH_RE = re.compile(r"repo_commit_hash\s*:\s*([A-Za-z0-9._:-]+)", re.IGNORECASE)
PLACEHOLDERS = {"todo", "tbd", "none", "unknown", "placeholder", "example-commit-hash", "example"}


def pick(cur: str, new: str) -> str:
    return new if ORDER[new] < ORDER[cur] else cur


def add(findings: list[dict[str, Any]], sev: str, cat: str, msg: str, path: str | None = None) -> None:
    item = {"severity": sev, "category": cat, "message": msg}
    if path:
        item["path"] = path
    findings.append(item)


def safe_rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return path.as_posix()


def read(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except Exception as exc:
        return None, str(exc)


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def extract_task_id(text: str) -> str | None:
    m = TASK_ID_RE.search(text)
    return m.group(1).strip() if m else None


def find_section(text: str, heading: str) -> str | None:
    pat = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    m = pat.search(text)
    if not m:
        return None
    start = m.end()
    next_h = re.compile(r"^##\s+", re.MULTILINE).search(text, start)
    end = next_h.start() if next_h else len(text)
    return text[start:end].strip()


def parse_selected_context_paths(section: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 5:
            continue
        p = cols[0]
        reason = cols[4]
        if p.lower() in {"path", "---"}:
            continue
        out.append((p, reason))
    return out


def unsafe_path(p: str) -> bool:
    return p.startswith("/") or p.startswith("~") or WIN_ABS_RE.match(p) is not None or ".." in Path(p).parts


def run_context_index_freshness(root: Path) -> tuple[str | None, str | None]:
    checker = root / "scripts/check-context-index-freshness.py"
    if not checker.exists():
        return None, "missing"
    proc = subprocess.run([sys.executable, str(checker), "--json", "--root", str(root)], capture_output=True, text=True, shell=False)
    if proc.returncode not in (0, 1):
        return None, "exec_failed"
    try:
        data = json.loads(proc.stdout or "{}")
    except Exception:
        return None, "malformed_json"
    return data.get("result"), None


def is_idle_task_file(path: Path) -> bool:
    """Return True when active-task.md is in legitimate idle/no-active-task state."""
    if not path.exists():
        return True
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return False
    text_lower = text.lower()
    if "no active task" in text_lower:
        return True
    if re.search(r"^status:\s*(none|idle)\s*$", text, re.MULTILINE):
        return True
    has_scope = "scope_control:" in text
    has_contract = "## Contract" in text or "contract:" in text
    if not has_scope and not has_contract:
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="M30.3 Required Context Pack Gate")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--task", default="tasks/active-task.md")
    ap.add_argument("--context", default="reports/context-pack.md")
    ap.add_argument("--index", default="data/context-index.json")
    ap.add_argument("--require-fresh-index", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()

    # Idle-state shortcut: no active task -> return VALID immediately
    task_path_obj = (root / args.task).resolve()
    if is_idle_task_file(task_path_obj):
        payload = {
            "result": RESULT_VALID,
            "task_path": args.task,
            "context_path": args.context,
            "index_path": args.index,
            "checked_selected_items": 0,
            "context_index_hash": None,
            "expected_context_index_hash": None,
            "repo_commit_hash": None,
            "warnings": [],
            "errors": [],
            "findings": [],
            "idle_state": True,
            "reason": "idle state - no active task",
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"RESULT: {RESULT_VALID}")
            print("reason: idle state - no active task")
        return 0

    task = (root / args.task).resolve()
    context = (root / args.context).resolve()
    index = (root / args.index).resolve()

    result = RESULT_VALID
    findings: list[dict[str, Any]] = []
    warnings: list[str] = []
    errors: list[str] = []
    checked_selected = 0
    context_hash = None
    expected_hash = None
    repo_hash = None
    index_freshness_result = None

    if not context.exists():
        add(findings, "error", "context_pack_missing", "Context Pack missing", safe_rel(context, root))
        result = RESULT_MISSING
    else:
        ctx_text, err = read(context)
        if err or not ctx_text or not ctx_text.strip():
            add(findings, "error", "context_pack_invalid", "Context Pack unreadable or empty")
            result = pick(result, RESULT_INVALID)
            ctx_text = ""

        if "Context Pack is not approval" not in ctx_text:
            add(findings, "blocking", "approval_claim", "missing non-authorization statement")
            result = pick(result, RESULT_BLOCKED)
        if "Verification Checklist" not in ctx_text:
            add(findings, "error", "verification_checklist_missing", "Verification Checklist missing")
            result = pick(result, RESULT_INVALID)
        if "SQLite is source of truth" in ctx_text:
            add(findings, "blocking", "sqlite_authority_violation", "Context Pack treats SQLite as source of truth")
            result = pick(result, RESULT_BLOCKED)

        task_id_ctx = extract_task_id(ctx_text)
        if not task_id_ctx:
            add(findings, "error", "task_id_missing", "Context Pack task_id missing")
            result = pick(result, RESULT_INVALID)

        mctx = CTX_HASH_RE.search(ctx_text)
        if not mctx:
            add(findings, "error", "context_index_hash_missing", "context_index_hash missing")
            result = pick(result, RESULT_INVALID)
        else:
            context_hash = mctx.group(1)

        mrepo = REPO_HASH_RE.search(ctx_text)
        if not mrepo:
            add(findings, "error", "repo_commit_hash_missing", "repo_commit_hash missing")
            result = pick(result, RESULT_INVALID)
        else:
            repo_hash = mrepo.group(1).strip()
            if not repo_hash or repo_hash.lower() in PLACEHOLDERS:
                add(findings, "error", "repo_commit_hash_placeholder", "repo_commit_hash is empty/placeholder")
                result = pick(result, RESULT_INVALID)

        # sections
        if find_section(ctx_text, "Required Context") is None:
            add(findings, "error", "required_context_missing", "Required context section missing")
            result = pick(result, RESULT_INVALID)
        if find_section(ctx_text, "Selected Context") is None:
            add(findings, "error", "context_pack_invalid", "Selected Context section missing")
            result = pick(result, RESULT_INVALID)

        # selected reasons and source files
        sec = find_section(ctx_text, "Selected Context") or ""
        rows = parse_selected_context_paths(sec)
        for p, reason in rows:
            checked_selected += 1
            if unsafe_path(p):
                add(findings, "error", "unsafe_path", "unsafe selected path", p)
                result = pick(result, RESULT_INVALID)
                continue
            src = root / p
            if not src.exists():
                add(findings, "error", "source_file_missing", "selected source file missing", p)
                result = pick(result, RESULT_STALE)
            if not reason or reason.strip().lower() in PLACEHOLDERS:
                add(findings, "error", "selected_reason_placeholder", "No reason \u2192 invalid Context Pack.", p)
                result = pick(result, RESULT_INVALID)

        # task binding
        if not task.exists():
            add(findings, "error", "task_missing", "task file missing", safe_rel(task, root))
            result = pick(result, RESULT_INCOMPLETE)
        else:
            task_text, terr = read(task)
            if terr or not task_text:
                add(findings, "needs_review", "needs_review", "task file unreadable")
                result = pick(result, RESULT_NEEDS_REVIEW)
                task_text = ""
            task_id_task = extract_task_id(task_text)
            if not task_id_task:
                add(findings, "needs_review", "task_id_missing", "task_id missing in task")
                result = pick(result, RESULT_NEEDS_REVIEW)
            elif task_id_ctx and task_id_ctx != task_id_task:
                add(findings, "error", "task_id_mismatch", "task_id mismatch")
                result = pick(result, RESULT_INVALID)

        # index hash freshness
        if not index.exists():
            add(findings, "error", "context_index_hash_missing", "index missing for hash comparison")
            result = pick(result, RESULT_INCOMPLETE)
        else:
            expected_hash = sha256_file(index)
            if context_hash and context_hash != expected_hash:
                add(findings, "error", "context_index_hash_mismatch", "stale Context Pack hash")
                result = pick(result, RESULT_STALE)

    # optional fresh index requirement
    if args.require_fresh_index:
        idx_res, idx_err = run_context_index_freshness(root)
        index_freshness_result = idx_res
        if idx_err == "missing":
            add(findings, "error", "needs_review", "Fresh Context Pack requires fresh context index. checker missing")
            result = pick(result, RESULT_INCOMPLETE)
        elif idx_err:
            add(findings, "needs_review", "needs_review", "freshness checker execution failed")
            result = pick(result, RESULT_NEEDS_REVIEW)
        else:
            if idx_res != "CONTEXT_INDEX_FRESH":
                add(findings, "needs_review", "needs_review", f"fresh index check non-ready: {idx_res}")
                if idx_res in ("CONTEXT_INDEX_STALE",):
                    result = pick(result, RESULT_STALE)
                elif idx_res in ("CONTEXT_INDEX_MISSING", "CONTEXT_INDEX_INCOMPLETE"):
                    result = pick(result, RESULT_INCOMPLETE)
                else:
                    result = pick(result, RESULT_NEEDS_REVIEW)

    # severity mapping
    if any(f["severity"] == "blocking" for f in findings) and result in (RESULT_VALID, RESULT_VALID_WARN):
        result = RESULT_BLOCKED
    if any(f["severity"] == "needs_review" for f in findings) and result == RESULT_VALID:
        result = RESULT_NEEDS_REVIEW
    if any(f["severity"] == "error" for f in findings) and result == RESULT_VALID:
        result = RESULT_INVALID

    for f in findings:
        line = f"{f['category']}: {f['message']}"
        if f.get("path"):
            line = f"{f['path']}: {line}"
        if f["severity"] in ("warning", "needs_review"):
            warnings.append(line)
        if f["severity"] in ("error", "blocking"):
            errors.append(line)

    payload = {
        "result": result,
        "task_path": safe_rel(task, root),
        "context_path": safe_rel(context, root),
        "index_path": safe_rel(index, root),
        "checked_selected_items": checked_selected,
        "context_index_hash": context_hash,
        "expected_context_index_hash": expected_hash,
        "repo_commit_hash": repo_hash,
        "warnings": warnings,
        "errors": errors,
        "findings": findings,
    }
    if args.require_fresh_index:
        payload["index_freshness_result"] = index_freshness_result

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"task_path: {payload['task_path']}")
        print(f"context_path: {payload['context_path']}")
        print(f"index_path: {payload['index_path']}")
        print(f"checked_selected_items: {checked_selected}")
        print(f"warnings: {len(warnings)}")
        print(f"errors: {len(errors)}")
        for f in findings:
            p = f" path={f['path']}" if "path" in f else ""
            print(f"- [{f['severity']}] {f['category']}{p}: {f['message']}")
        print(result)
    return 0 if result == RESULT_VALID else 1


if __name__ == "__main__":
    raise SystemExit(main())
