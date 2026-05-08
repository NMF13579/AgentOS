#!/usr/bin/env python3
"""Validate Context Pack availability and structure for M28 required-check."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

OK = "CONTEXT_REQUIRED_OK"
MISSING = "CONTEXT_REQUIRED_MISSING"
INVALID = "CONTEXT_REQUIRED_INVALID"
NEEDS_REVIEW = "CONTEXT_REQUIRED_NEEDS_REVIEW"

EXIT = {OK: 0, MISSING: 1, INVALID: 1, NEEDS_REVIEW: 1}

REQ_FM_FIELDS = [
    "type",
    "task_id",
    "status",
    "generated_by",
    "generated_at",
    "context_index_path",
    "context_index_hash",
    "repo_commit_hash",
]
ALLOWED_STATUS = {"generated", "stale", "invalid", "needs_review"}
REQUIRED_HEADINGS = [
    "# Context Pack",
    "## Task Summary",
    "## Selected Context",
    "## Required Context",
    "## Supporting Context",
    "## Relevant Rules",
    "## Relevant Lessons",
    "## Relevant Policies",
    "## Out-of-Scope Context",
    "## Context Risks",
    "## Source Integrity",
    "## Non-Authorization Warning",
    "## Verification Checklist",
]
NON_AUTH_BLOCK = [
    "Context Pack is not approval.",
    "Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.",
    "Context Pack does not replace M27 runtime enforcement.",
    "Context Pack does not replace Human Gate approval.",
    "Freshness check is not approval.",
    "Integrity check is not approval.",
]
HASH_RE = re.compile(r"^sha256:[0-9a-fA-F]+$")
WIN_ABS_RE = re.compile(r"^[A-Za-z]:[\\/]")


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Check Context Pack required precondition.")
    p.add_argument("--task", required=True)
    p.add_argument("--context", required=True)
    p.add_argument("--selection")
    p.add_argument("--json", action="store_true")
    p.add_argument("--root", default=".")
    return p.parse_args(argv)


def resolve(root: Path, raw: str) -> Path:
    p = Path(raw)
    return p if p.is_absolute() else (root / p)


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_abs_path_like(value: str) -> bool:
    return value.startswith("/") or bool(WIN_ABS_RE.match(value))


def split_frontmatter(text: str) -> tuple[dict[str, Any] | None, str, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, "missing_frontmatter"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text, "unclosed_frontmatter"
    block = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(block)
    except Exception as exc:
        return None, text, f"invalid_frontmatter_yaml:{exc}"
    if not isinstance(data, dict):
        return None, text, "frontmatter_not_object"
    body = "\n".join(lines[end + 1 :])
    return data, body, None


def get_section_lines(body: str, heading: str) -> list[str]:
    lines = body.splitlines()
    try:
        idx = [i for i, ln in enumerate(lines) if ln.strip() == heading][0]
    except IndexError:
        return []
    out: list[str] = []
    for ln in lines[idx + 1 :]:
        s = ln.strip()
        if s.startswith("## ") and s != heading:
            break
        out.append(ln)
    return out


def extract_task_id(task_text: str) -> tuple[str | None, str | None]:
    fm, body, err = split_frontmatter(task_text)
    if fm is not None:
        if isinstance(fm.get("task_id"), str) and fm.get("task_id").strip():
            return fm["task_id"].strip(), None
        task_obj = fm.get("task")
        if isinstance(task_obj, dict) and isinstance(task_obj.get("id"), str) and task_obj.get("id").strip():
            return task_obj["id"].strip(), None

    m = re.search(r"^Task ID:\s*([A-Za-z0-9._:-]+)\s*$", task_text, re.MULTILINE)
    if m:
        return m.group(1), None

    for ln in task_text.splitlines():
        s = ln.strip()
        if s.startswith("#"):
            t = s.lstrip("#").strip()
            m1 = re.match(r"^Task\s+([A-Za-z0-9._:-]+)$", t)
            m2 = re.match(r"^([A-Za-z0-9._:-]+)\s+[—-]\s+", t)
            if m1:
                return m1.group(1), None
            if m2:
                return m2.group(1), None

    return None, "task_id could not be extracted"


def git_head(root: Path) -> tuple[str | None, str | None]:
    try:
        p = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(root), capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return None, "git_not_found"
    if p.returncode != 0:
        return None, "git_rev_parse_failed"
    head = p.stdout.strip()
    if not head:
        return None, "git_head_empty"
    return head, None


def find_non_auth_block(body: str) -> bool:
    lines = [ln.rstrip() for ln in body.splitlines()]
    idxs = [i for i, ln in enumerate(lines) if ln.strip() == NON_AUTH_BLOCK[0]]
    for start in idxs:
        j = start
        ok = True
        for sentence in NON_AUTH_BLOCK[1:]:
            blanks = 0
            j += 1
            while j < len(lines) and lines[j].strip() == "":
                blanks += 1
                j += 1
            if blanks > 2:
                ok = False
                break
            if j >= len(lines) or lines[j].strip() != sentence:
                ok = False
                break
        if ok:
            return True
    return False


def parse_selected_table(selected_lines: list[str]) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    table_rows = [ln.strip() for ln in selected_lines if ln.strip().startswith("|")]
    if len(table_rows) < 2:
        return rows, errors
    header = [x.strip().lower() for x in table_rows[0].strip("|").split("|")]
    for ln in table_rows[2:]:
        cols = [x.strip() for x in ln.strip("|").split("|")]
        if len(cols) != len(header):
            continue
        d = dict(zip(header, cols))
        rows.append(d)
    return rows, errors


def extract_selected_hashes(source_integrity_lines: list[str]) -> dict[str, str]:
    m: dict[str, str] = {}
    in_block = False
    for ln in source_integrity_lines:
        stripped = ln.strip()
        if stripped == "- selected_source_hashes:":
            in_block = True
            continue
        if not in_block:
            continue
        # Keep only nested bullet items under selected_source_hashes.
        if not ln.startswith("  - "):
            if stripped.startswith("- "):
                in_block = False
            continue
        item = ln.strip()[2:].strip()
        if ": " not in item:
            continue
        left, right = item.split(": ", 1)
        m[left.strip()] = right.strip()
    return m


def check_required(
    root: Path,
    task_path_raw: str,
    context_path_raw: str,
    selection_path_raw: str | None,
) -> tuple[str, list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    result = OK

    task_path = resolve(root, task_path_raw)
    context_path = resolve(root, context_path_raw)
    selection_path = resolve(root, selection_path_raw) if selection_path_raw else None

    if not task_path.exists():
        return MISSING, warnings, ["task_missing"]
    if not context_path.exists():
        return MISSING, warnings, ["context_pack_missing"]
    if selection_path_raw and selection_path and not selection_path.exists():
        return MISSING, warnings, ["selection_record_missing"]

    task_text = task_path.read_text(encoding="utf-8")
    task_id, task_id_warn = extract_task_id(task_text)
    if task_id_warn:
        warnings.append("task_id could not be extracted")
        result = NEEDS_REVIEW

    cp_text = context_path.read_text(encoding="utf-8")
    cp_fm, cp_body, cp_err = split_frontmatter(cp_text)
    if cp_err or cp_fm is None:
        return INVALID, warnings, [f"context_pack_frontmatter_invalid:{cp_err}"]

    for f in REQ_FM_FIELDS:
        if f not in cp_fm:
            errors.append(f"missing_frontmatter_field:{f}")

    if cp_fm.get("type") != "context-pack":
        errors.append("invalid_type")

    status = cp_fm.get("status")
    if status not in ALLOWED_STATUS:
        errors.append("invalid_status")
    elif status == "stale":
        result = NEEDS_REVIEW
    elif status == "invalid":
        result = INVALID
    elif status == "needs_review":
        result = NEEDS_REVIEW

    rch = cp_fm.get("repo_commit_hash")
    if not isinstance(rch, str) or not rch.strip():
        errors.append("repo_commit_hash_invalid")

    cih = cp_fm.get("context_index_hash")
    if not isinstance(cih, str) or not HASH_RE.match(cih):
        errors.append("context_index_hash_invalid")

    cip = cp_fm.get("context_index_path")
    if not isinstance(cip, str) or not cip.strip():
        errors.append("context_index_path_invalid")
    else:
        idx_path = resolve(root, cip)
        if not idx_path.exists():
            errors.append("context_index_path_missing")
        else:
            idx_hash = sha256_text(idx_path.read_text(encoding="utf-8"))
            if isinstance(cih, str) and idx_hash != cih:
                warnings.append("context_index_hash_mismatch")
                if result != INVALID:
                    result = NEEDS_REVIEW

    for h in REQUIRED_HEADINGS:
        if not any(ln.strip() == h for ln in cp_body.splitlines()):
            errors.append(f"missing_heading:{h}")

    if errors:
        return INVALID, warnings, errors

    if task_id is not None and str(cp_fm.get("task_id")) != task_id:
        return INVALID, warnings, ["task_id_mismatch"]

    rel_task = task_path.relative_to(root).as_posix() if task_path.is_relative_to(root) else task_path.as_posix()
    if f"source_task_path: {rel_task}" not in cp_body and task_id and task_id not in cp_body:
        warnings.append("task_linkage_uncertain")
        if result == OK:
            result = NEEDS_REVIEW

    selected_lines = get_section_lines(cp_body, "## Selected Context")
    selected_rows, _ = parse_selected_table(selected_lines)
    explicit_needs_review = "CONTEXT_NEEDS_REVIEW" in cp_body

    if not selected_rows and not explicit_needs_review:
        errors.append("no_selected_context_items")

    for row in selected_rows:
        p = row.get("path", "")
        reason = row.get("reason", "")
        if not reason.strip():
            errors.append("selected_item_missing_reason")
        if is_abs_path_like(p):
            errors.append("selected_item_absolute_path")

    src_int_lines = get_section_lines(cp_body, "## Source Integrity")
    src_map = extract_selected_hashes(src_int_lines)
    for p, h in src_map.items():
        if not HASH_RE.match(h):
            errors.append("bad_source_hash_format")
            continue
        if is_abs_path_like(p):
            errors.append("selected_item_absolute_path")
            continue
        fp = resolve(root, p)
        if not fp.exists():
            errors.append("selected_source_file_missing")
            continue
        actual = sha256_text(fp.read_text(encoding="utf-8"))
        if actual != h:
            warnings.append("selected_source_hash_mismatch")
            if result != INVALID:
                result = NEEDS_REVIEW

    if not find_non_auth_block(cp_body):
        errors.append("missing_or_modified_non_authorization_block")

    checklist = get_section_lines(cp_body, "## Verification Checklist")
    if not checklist:
        errors.append("missing_verification_checklist")
    else:
        check_text = "\n".join(checklist).lower()
        concepts = [
            "selected rules",
            "selected policies",
            "selected lessons",
            "out-of-scope",
            "approval",
            "m27",
            "needs_review",
        ]
        for c in concepts:
            if c not in check_text:
                errors.append(f"missing_checklist_concept:{c}")

    head, git_err = git_head(root)
    if git_err:
        warnings.append(git_err)
        if result != INVALID:
            result = NEEDS_REVIEW
    else:
        if isinstance(rch, str) and rch.strip() and rch.strip() != head:
            warnings.append("repo_commit_hash_mismatch")
            if result != INVALID:
                result = NEEDS_REVIEW

    if selection_path is not None:
        sel_text = selection_path.read_text(encoding="utf-8")
        if "## selected_items" not in sel_text:
            errors.append("selection_missing_selected_items")
        if "## excluded_items" not in sel_text:
            errors.append("selection_missing_excluded_items")
        if "matched_signals" not in sel_text and "- none" not in get_section_lines(sel_text, "## selected_items"):
            warnings.append("selection_missing_matched_signals")
            if result != INVALID:
                result = NEEDS_REVIEW
        m = re.search(r"^- result:\s*(\S+)\s*$", sel_text, re.MULTILINE)
        if not m:
            errors.append("selection_result_missing")
        else:
            sres = m.group(1)
            allowed = {"CONTEXT_SELECTED", "CONTEXT_SELECTED_WITH_WARNINGS", "CONTEXT_NEEDS_REVIEW", "CONTEXT_INVALID"}
            if sres not in allowed:
                errors.append("selection_result_invalid")
            elif sres == "CONTEXT_SELECTED_WITH_WARNINGS":
                if result != INVALID:
                    result = NEEDS_REVIEW
            elif sres == "CONTEXT_NEEDS_REVIEW":
                if result != INVALID:
                    result = NEEDS_REVIEW
            elif sres == "CONTEXT_INVALID":
                result = INVALID

    if errors:
        return INVALID, warnings, errors
    return result, warnings, errors


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()

    result, warnings, errors = check_required(root, args.task, args.context, args.selection)

    payload = {
        "result": result,
        "task_path": args.task,
        "context_path": args.context,
        "selection_path": args.selection,
        "warnings": warnings,
        "errors": errors,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print(result)
        if warnings:
            print("warnings:")
            for w in warnings:
                print(f"- {w}")
        if errors:
            print("errors:")
            for e in errors:
                print(f"- {e}")

    return EXIT[result]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
