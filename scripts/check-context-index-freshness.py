#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

RESULT_FRESH = "CONTEXT_INDEX_FRESH"
RESULT_FRESH_WARN = "CONTEXT_INDEX_FRESH_WITH_WARNINGS"
RESULT_STALE = "CONTEXT_INDEX_STALE"
RESULT_MISSING = "CONTEXT_INDEX_MISSING"
RESULT_INVALID = "CONTEXT_INDEX_INVALID"
RESULT_INCOMPLETE = "CONTEXT_INDEX_INCOMPLETE"
RESULT_NEEDS_REVIEW = "CONTEXT_INDEX_NEEDS_REVIEW"
RESULT_BLOCKED = "CONTEXT_INDEX_BLOCKED"

DEFAULT_INDEX = "data/context-index.json"
GENERATOR_PATH = "scripts/build-context-index.py"

SHA256_RE = re.compile(r"^sha256:[0-9a-fA-F]{64}$")
WIN_ABS_RE = re.compile(r"^[A-Za-z]:[\\/]")

RESULT_ORDER = {
    RESULT_BLOCKED: 0,
    RESULT_INVALID: 1,
    RESULT_STALE: 2,
    RESULT_INCOMPLETE: 3,
    RESULT_MISSING: 4,
    RESULT_NEEDS_REVIEW: 5,
    RESULT_FRESH_WARN: 6,
    RESULT_FRESH: 7,
}

FORBIDDEN_CLAIMS = (
    "semantic source of truth",
    "overrides markdown",
    "overrides yaml",
    "approves execution",
    "authorizes protected actions",
    "replaces context pack",
    "replaces human gate",
    "sqlite is source of truth",
    "sqlite overrides context-index",
    "freshness check is approval",
)


def rel_for_output(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return path.as_posix()


def add_finding(findings: list[dict[str, Any]], severity: str, category: str, message: str, path: str | None = None) -> None:
    item: dict[str, Any] = {
        "severity": severity,
        "category": category,
        "message": message,
    }
    if path:
        item["path"] = path
    findings.append(item)


def choose_result(current: str, new: str) -> str:
    return new if RESULT_ORDER[new] < RESULT_ORDER[current] else current


def is_unsafe_path(raw: str) -> tuple[bool, str]:
    p = raw.strip()
    if not p:
        return True, "empty"
    if p.startswith("/"):
        return True, "absolute_path"
    if p.startswith("~"):
        return True, "home_path"
    if WIN_ABS_RE.match(p):
        return True, "absolute_path"
    normalized = Path(p)
    if ".." in normalized.parts:
        return True, "path_escape"
    return False, ""


def file_sha256(path: Path) -> str:
    data = path.read_bytes()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception as exc:
        return None, f"read_failed:{exc}"
    try:
        obj = json.loads(raw)
    except Exception as exc:
        return None, f"invalid_json:{exc}"
    if not isinstance(obj, dict):
        return None, "top_level_not_object"
    return obj, None


def validate_structure(index: dict[str, Any], findings: list[dict[str, Any]], root: Path) -> tuple[str, list[dict[str, Any]]]:
    result = RESULT_FRESH
    entries = index.get("entries")
    if entries is None:
        add_finding(findings, "error", "index_invalid_json", "missing entries array")
        return RESULT_INVALID, []
    if not isinstance(entries, list):
        add_finding(findings, "error", "index_invalid_json", "entries must be an array")
        return RESULT_INVALID, []

    for key in ("generated_at", "generator", "schema_version"):
        if key not in index:
            add_finding(findings, "needs_review", "needs_review", f"missing metadata field: {key}")
            result = choose_result(result, RESULT_NEEDS_REVIEW)

    serialized = json.dumps(index, ensure_ascii=False).lower()
    for token in FORBIDDEN_CLAIMS:
        if token in serialized:
            add_finding(findings, "blocking", "source_of_truth_violation", f"forbidden authority claim detected: {token}")
            result = choose_result(result, RESULT_BLOCKED)

    if "sqlite" in serialized and "source of truth" in serialized:
        add_finding(findings, "blocking", "sqlite_authority_violation", "SQLite authority claim detected")
        result = choose_result(result, RESULT_BLOCKED)

    checked_entries: list[dict[str, Any]] = []
    for idx, entry in enumerate(entries):
        if not isinstance(entry, dict):
            add_finding(findings, "error", "index_invalid_json", f"entry {idx} is not object")
            result = choose_result(result, RESULT_INVALID)
            continue

        raw_path = entry.get("path")
        if not isinstance(raw_path, str):
            add_finding(findings, "error", "index_invalid_json", f"entry {idx} missing path")
            result = choose_result(result, RESULT_INVALID)
            continue

        unsafe, reason = is_unsafe_path(raw_path)
        if unsafe:
            cat = "absolute_path" if reason in ("absolute_path", "home_path") else "path_escape"
            add_finding(findings, "error", cat, f"unsafe path: {raw_path}", raw_path)
            result = choose_result(result, RESULT_INVALID)
            continue

        source_path = root / raw_path
        try:
            resolved = source_path.resolve()
            root_resolved = root.resolve()
            if root_resolved not in resolved.parents and resolved != root_resolved:
                add_finding(findings, "error", "path_escape", f"path escapes repository root: {raw_path}", raw_path)
                result = choose_result(result, RESULT_INVALID)
                continue
        except Exception:
            add_finding(findings, "needs_review", "needs_review", f"cannot resolve path: {raw_path}", raw_path)
            result = choose_result(result, RESULT_NEEDS_REVIEW)

        checked_entries.append(entry)
    return result, checked_entries


def run_hash_check(root: Path, index_path: Path, findings: list[dict[str, Any]]) -> tuple[str, int]:
    if not index_path.exists():
        add_finding(findings, "error", "index_missing", "context index file is missing", rel_for_output(index_path, root))
        return RESULT_MISSING, 0

    index_obj, err = load_json(index_path)
    if err:
        add_finding(findings, "error", "index_invalid_json", f"context index JSON parse failure: {err}")
        return RESULT_INVALID, 0
    assert index_obj is not None

    result, checked_entries = validate_structure(index_obj, findings, root)
    if RESULT_ORDER[result] <= RESULT_ORDER[RESULT_INVALID]:
        return result, len(checked_entries)

    checked_count = 0
    for entry in checked_entries:
        raw_path = entry.get("path")
        if not isinstance(raw_path, str):
            continue

        source = root / raw_path
        checked_count += 1

        if not source.exists():
            add_finding(findings, "error", "source_file_missing", "source file referenced by index is missing", raw_path)
            result = choose_result(result, RESULT_INVALID)
            continue

        src_hash = entry.get("source_hash")
        if src_hash is None:
            add_finding(findings, "needs_review", "source_hash_missing", "required source_hash is missing", raw_path)
            result = choose_result(result, RESULT_NEEDS_REVIEW)
            continue

        if not isinstance(src_hash, str) or not SHA256_RE.match(src_hash):
            add_finding(findings, "needs_review", "source_hash_missing", "source_hash format must be sha256:<hex>", raw_path)
            result = choose_result(result, RESULT_NEEDS_REVIEW)
            continue

        current_hash = file_sha256(source)
        if current_hash != src_hash:
            add_finding(findings, "error", "source_hash_mismatch", "source hash mismatch; index is stale", raw_path)
            result = choose_result(result, RESULT_STALE)
        else:
            add_finding(findings, "info", "source_hash_ok", "source hash matches committed context index", raw_path)

    return result, checked_count


def canonicalize_json(obj: dict[str, Any]) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)


def run_generator_in_temp(root: Path, out_path: Path) -> tuple[int, str, str]:
    temp_root = Path(tempfile.mkdtemp(prefix="m30-index-check-"))
    temp_repo = temp_root / "repo"
    shutil.copytree(root, temp_repo, symlinks=True, ignore=shutil.ignore_patterns(".git"))

    cmd = [sys.executable, str((temp_repo / GENERATOR_PATH).resolve()), "--root", str(temp_repo), "--json"]
    proc = subprocess.run(cmd, cwd=str(temp_repo), capture_output=True, text=True)
    generated_index = temp_repo / DEFAULT_INDEX
    if generated_index.exists():
        out_path.write_text(generated_index.read_text(encoding="utf-8"), encoding="utf-8")
    shutil.rmtree(temp_root, ignore_errors=True)
    return proc.returncode, proc.stdout, proc.stderr


def run_compare_after_rebuild(root: Path, index_path: Path, findings: list[dict[str, Any]]) -> tuple[str, int]:
    if not index_path.exists():
        add_finding(findings, "error", "index_missing", "context index file is missing", rel_for_output(index_path, root))
        return RESULT_MISSING, 0

    generator = root / GENERATOR_PATH
    if not generator.exists():
        add_finding(findings, "error", "generator_missing", "context index generator script is missing")
        return RESULT_INCOMPLETE, 0

    try:
        committed_obj, err = load_json(index_path)
        if err:
            add_finding(findings, "error", "index_invalid_json", f"committed index parse error: {err}")
            return RESULT_INVALID, 0
        assert committed_obj is not None

        with tempfile.TemporaryDirectory() as tmp:
            out1 = Path(tmp) / "gen1.json"
            out2 = Path(tmp) / "gen2.json"

            code1, _, _ = run_generator_in_temp(root, out1)
            if code1 != 0:
                add_finding(findings, "needs_review", "generator_failed", "generator exists but failed unexpectedly")
                return RESULT_NEEDS_REVIEW, len(committed_obj.get("entries", []))

            if not out1.exists():
                add_finding(findings, "needs_review", "generator_failed", "generator did not produce context index output")
                return RESULT_NEEDS_REVIEW, len(committed_obj.get("entries", []))

            gen1_obj, err1 = load_json(out1)
            if err1:
                add_finding(findings, "needs_review", "generator_failed", f"generated index invalid JSON: {err1}")
                return RESULT_NEEDS_REVIEW, len(committed_obj.get("entries", []))
            assert gen1_obj is not None

            # Nondeterminism check (two consecutive rebuilds)
            code2, _, _ = run_generator_in_temp(root, out2)
            if code2 != 0 or not out2.exists():
                add_finding(findings, "needs_review", "generator_failed", "second generator run failed unexpectedly")
                return RESULT_NEEDS_REVIEW, len(committed_obj.get("entries", []))
            gen2_obj, err2 = load_json(out2)
            if err2:
                add_finding(findings, "needs_review", "generator_failed", f"second generated index invalid JSON: {err2}")
                return RESULT_NEEDS_REVIEW, len(committed_obj.get("entries", []))
            assert gen2_obj is not None

            if canonicalize_json(gen1_obj) != canonicalize_json(gen2_obj):
                add_finding(findings, "needs_review", "nondeterministic_output", "generator output is nondeterministic across consecutive runs")
                return RESULT_NEEDS_REVIEW, len(gen1_obj.get("entries", []))

            vres, _ = validate_structure(gen1_obj, findings, root)
            if RESULT_ORDER[vres] <= RESULT_ORDER[RESULT_INVALID]:
                return vres, len(gen1_obj.get("entries", []))

            if canonicalize_json(committed_obj) != canonicalize_json(gen1_obj):
                add_finding(findings, "error", "rebuild_diff_detected", "Diff after rebuild means stale index.")
                return RESULT_STALE, len(gen1_obj.get("entries", []))

            add_finding(findings, "info", "entry_checked", "committed index matches deterministic rebuild")
            return RESULT_FRESH, len(gen1_obj.get("entries", []))
    except Exception as exc:
        add_finding(findings, "needs_review", "needs_review", f"compare-after-rebuild failed unexpectedly: {exc}")
        return RESULT_NEEDS_REVIEW, 0


def enforce_result_from_findings(result: str, findings: list[dict[str, Any]]) -> str:
    has_blocking = any(f.get("severity") == "blocking" for f in findings)
    has_needs_review = any(f.get("severity") == "needs_review" for f in findings)
    has_error = any(f.get("severity") == "error" for f in findings)

    if has_blocking and result in (RESULT_FRESH, RESULT_FRESH_WARN):
        return RESULT_BLOCKED
    if has_needs_review and result == RESULT_FRESH:
        return RESULT_NEEDS_REVIEW
    if has_error and result == RESULT_FRESH:
        return RESULT_INVALID
    return result


def summarize(findings: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    for item in findings:
        sev = item.get("severity")
        msg = item.get("message", "")
        cat = item.get("category", "")
        p = item.get("path")
        line = f"{cat}: {msg}" if cat else msg
        if p:
            line = f"{p}: {line}"
        if sev in ("warning", "needs_review"):
            warnings.append(line)
        if sev in ("error", "blocking"):
            errors.append(line)
    return warnings, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="M30.2 Context Index Freshness Gate")
    parser.add_argument("--json", action="store_true", help="print JSON output")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--index", default=DEFAULT_INDEX, help="context index path")
    parser.add_argument(
        "--mode",
        choices=["hash-check", "compare-after-rebuild", "auto"],
        default="auto",
        help="freshness mode",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    index_path = (root / args.index).resolve()

    findings: list[dict[str, Any]] = []
    mode_used = args.mode
    checked_entries = 0
    result = RESULT_INCOMPLETE

    if args.mode == "hash-check":
        result, checked_entries = run_hash_check(root, index_path, findings)

    elif args.mode == "compare-after-rebuild":
        result, checked_entries = run_compare_after_rebuild(root, index_path, findings)

    else:  # auto
        generator_exists = (root / GENERATOR_PATH).exists()
        if generator_exists:
            mode_used = "compare-after-rebuild"
            result_compare, count_compare = run_compare_after_rebuild(root, index_path, findings)
            checked_entries = count_compare
            if result_compare in (RESULT_NEEDS_REVIEW, RESULT_INCOMPLETE):
                add_finding(findings, "needs_review", "generator_failed", "auto mode: generator failure must not silently fall back to hash-check")
                result = result_compare
            else:
                result = result_compare
                # additionally detect disagreement only when both are available and successful-ish
                result_hash, count_hash = run_hash_check(root, index_path, findings)
                checked_entries = max(checked_entries, count_hash)
                if result_hash in (RESULT_FRESH, RESULT_STALE, RESULT_INVALID, RESULT_MISSING, RESULT_NEEDS_REVIEW):
                    if result_hash != result_compare:
                        add_finding(findings, "needs_review", "mode_disagreement", "If both modes are available and disagree, result is needs_review")
                        result = RESULT_NEEDS_REVIEW
                    else:
                        add_finding(findings, "info", "entry_checked", "auto mode: both modes agreed")
                else:
                    add_finding(findings, "warning", "needs_review", "auto mode: secondary hash-check unavailable")
        else:
            mode_used = "hash-check"
            add_finding(findings, "warning", "generator_missing", "If the context index generator script is missing, the gate must fail with INCOMPLETE, not skip silently.")
            result_hash, checked_entries = run_hash_check(root, index_path, findings)
            if result_hash == RESULT_FRESH:
                result = RESULT_FRESH_WARN
            elif result_hash == RESULT_NEEDS_REVIEW:
                result = RESULT_INCOMPLETE
            else:
                result = result_hash

    result = enforce_result_from_findings(result, findings)
    warnings, errors = summarize(findings)

    payload: dict[str, Any] = {
        "result": result,
        "mode": mode_used,
        "index_path": rel_for_output(index_path, root),
        "checked_entries": checked_entries,
        "warnings": warnings,
        "errors": errors,
        "findings": findings,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"mode: {mode_used}")
        print(f"index_path: {payload['index_path']}")
        print(f"checked_entries: {checked_entries}")
        print(f"warnings: {len(warnings)}")
        print(f"errors: {len(errors)}")
        print("findings:")
        for f in findings:
            p = f" path={f['path']}" if "path" in f else ""
            print(f"- [{f['severity']}] {f['category']}{p}: {f['message']}")
        print(result)

    return 0 if result == RESULT_FRESH else 1


if __name__ == "__main__":
    raise SystemExit(main())
