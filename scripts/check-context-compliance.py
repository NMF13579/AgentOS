#!/usr/bin/env python3
"""M28 context compliance checker (read-only)."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import yaml

CONTEXT_COMPLIANT = "CONTEXT_COMPLIANT"
CONTEXT_COMPLIANT_WITH_WARNINGS = "CONTEXT_COMPLIANT_WITH_WARNINGS"
CONTEXT_VIOLATION = "CONTEXT_VIOLATION"
CONTEXT_NEEDS_REVIEW = "CONTEXT_NEEDS_REVIEW"
CONTEXT_MISSING = "CONTEXT_MISSING"

EXIT_CODE = {
    CONTEXT_COMPLIANT: 0,
    CONTEXT_COMPLIANT_WITH_WARNINGS: 1,
    CONTEXT_VIOLATION: 1,
    CONTEXT_NEEDS_REVIEW: 1,
    CONTEXT_MISSING: 1,
}

NON_AUTH_SENTENCES = [
    "Context Pack is not approval.",
    "Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.",
    "Context Pack does not replace M27 runtime enforcement.",
    "Context Pack does not replace Human Gate approval.",
    "Freshness check is not approval.",
    "Integrity check is not approval.",
]

REQUIRED_HEADERS = [
    "# Context Pack",
    "## Selected Context",
    "## Required Context",
    "## Relevant Rules",
    "## Relevant Lessons",
    "## Relevant Policies",
    "## Out-of-Scope Context",
    "## Context Risks",
    "## Non-Authorization Warning",
    "## Verification Checklist",
]

PROTECTED_APPROVAL_CLAIMS = [
    "context pack approves execution",
    "context pack authorizes commit",
    "context pack authorizes push",
    "context pack authorizes merge",
    "context pack authorizes release",
    "context pack authorizes deployment",
    "context pack authorizes protected changes",
    "context pack replaces human gate",
    "context pack replaces m27",
    "freshness check is approval",
    "integrity check is approval",
    "context compliance is approval",
    "compliance result authorizes",
]

WIN_ABS_RE = re.compile(r"^[A-Za-z]:[\\/]")


@dataclass
class Finding:
    severity: str
    category: str
    message: str
    source: str
    affected_path: str | None
    result_impact: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate plan/verification alignment with Context Pack.")
    p.add_argument("--context", required=True)
    p.add_argument("--plan")
    p.add_argument("--verification")
    p.add_argument("--changed-files")
    p.add_argument("--json", action="store_true")
    p.add_argument("--root", default=".")
    return p.parse_args(argv)


def resolve(root: Path, raw: str | None) -> Path | None:
    if raw is None:
        return None
    p = Path(raw)
    return p if p.is_absolute() else (root / p)


def sha256_text(text: str) -> str:
    import hashlib

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
        return None, text, f"invalid_frontmatter:{exc}"
    if not isinstance(data, dict):
        return None, text, "frontmatter_not_object"
    body = "\n".join(lines[end + 1 :])
    return data, body, None


def section_lines(body: str, heading: str) -> list[str]:
    lines = body.splitlines()
    idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == heading:
            idx = i
            break
    if idx is None:
        return []
    out = []
    for ln in lines[idx + 1 :]:
        if ln.strip().startswith("## "):
            break
        out.append(ln)
    return out


def normalize_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def contains_non_auth_block(body: str) -> bool:
    lines = [ln.rstrip() for ln in body.splitlines()]
    starts = [i for i, ln in enumerate(lines) if ln.strip() == NON_AUTH_SENTENCES[0]]
    for st in starts:
        i = st
        ok = True
        for sentence in NON_AUTH_SENTENCES[1:]:
            i += 1
            blanks = 0
            while i < len(lines) and lines[i].strip() == "":
                blanks += 1
                i += 1
            if blanks > 2:
                ok = False
                break
            if i >= len(lines) or lines[i].strip() != sentence:
                ok = False
                break
        if ok:
            return True
    return False


def extract_selected_items(body: str) -> list[dict[str, str]]:
    lines = section_lines(body, "## Selected Context")
    table = [ln.strip() for ln in lines if ln.strip().startswith("|")]
    items: list[dict[str, str]] = []
    if len(table) < 3:
        return items
    header = [x.strip().lower() for x in table[0].strip("|").split("|")]
    for row in table[2:]:
        cols = [x.strip() for x in row.strip("|").split("|")]
        if len(cols) != len(header):
            continue
        items.append(dict(zip(header, cols)))
    return items


def extract_list_items(lines: list[str]) -> list[str]:
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
    return out


def parse_changed_files(path: Path) -> tuple[list[str] | None, list[Finding], str | None]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        findings.append(Finding("needs_review", "changed_files_conflict", f"changed-files unreadable: {exc}", str(path), None, CONTEXT_NEEDS_REVIEW))
        return None, findings, CONTEXT_NEEDS_REVIEW

    out: list[str] = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if is_abs_path_like(s):
            findings.append(Finding("violation", "changed_files_conflict", "absolute path in changed-files", str(path), s, CONTEXT_VIOLATION))
            return None, findings, CONTEXT_VIOLATION
        if s.startswith("..") or "/../" in s or "\\..\\" in s:
            findings.append(Finding("violation", "changed_files_conflict", "repo escape path in changed-files", str(path), s, CONTEXT_VIOLATION))
            return None, findings, CONTEXT_VIOLATION
        out.append(s)
    return out, findings, None


def status_rank(result: str) -> int:
    order = {
        CONTEXT_COMPLIANT: 0,
        CONTEXT_COMPLIANT_WITH_WARNINGS: 1,
        CONTEXT_NEEDS_REVIEW: 2,
        CONTEXT_VIOLATION: 3,
        CONTEXT_MISSING: 4,
    }
    return order[result]


def combine(current: str, new: str) -> str:
    return new if status_rank(new) > status_rank(current) else current


def check_context_pack(root: Path, context_path: Path) -> tuple[str, dict[str, Any] | None, str, list[Finding]]:
    findings: list[Finding] = []
    if not context_path.exists():
        findings.append(Finding("warning", "missing_context", "context pack file is missing", str(context_path), None, CONTEXT_MISSING))
        return CONTEXT_MISSING, None, "", findings

    text = context_path.read_text(encoding="utf-8")
    fm, body, err = split_frontmatter(text)
    if err or fm is None:
        findings.append(Finding("violation", "missing_context", f"invalid context frontmatter: {err}", str(context_path), None, CONTEXT_MISSING))
        return CONTEXT_MISSING, None, body, findings

    for h in REQUIRED_HEADERS:
        if not any(ln.strip() == h for ln in body.splitlines()):
            findings.append(Finding("violation", "missing_context", f"missing required heading: {h}", str(context_path), None, CONTEXT_NEEDS_REVIEW))

    st = str(fm.get("status", "")).strip().lower()
    result = CONTEXT_COMPLIANT
    if st == "stale":
        findings.append(Finding("needs_review", "stale_context", "context pack status is stale", str(context_path), None, CONTEXT_NEEDS_REVIEW))
        result = CONTEXT_NEEDS_REVIEW
    elif st in {"invalid", "needs_review"}:
        findings.append(Finding("needs_review", "stale_context", f"context pack status is {st}", str(context_path), None, CONTEXT_NEEDS_REVIEW))
        result = CONTEXT_NEEDS_REVIEW

    if not contains_non_auth_block(body):
        findings.append(Finding("violation", "non_authorization_violation", "missing or modified non-authorization block", str(context_path), None, CONTEXT_VIOLATION))
        result = combine(result, CONTEXT_VIOLATION)

    selected = extract_selected_items(body)
    for item in selected:
        reason = item.get("reason", "").strip()
        if not reason:
            findings.append(Finding("needs_review", "selected_rule_missing", "selected context item has no reason", str(context_path), item.get("path"), CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    # Freshness checks (lightweight)
    idx_path = fm.get("context_index_path")
    idx_hash = fm.get("context_index_hash")
    if isinstance(idx_path, str) and idx_path:
        p = resolve(root, idx_path)
        if p and p.exists() and isinstance(idx_hash, str) and idx_hash.startswith("sha256:"):
            actual = sha256_text(p.read_text(encoding="utf-8"))
            if actual != idx_hash:
                findings.append(Finding("needs_review", "stale_context", "context_index_hash mismatch", str(context_path), idx_path, CONTEXT_NEEDS_REVIEW))
                result = combine(result, CONTEXT_NEEDS_REVIEW)

    repo_hash = fm.get("repo_commit_hash")
    if isinstance(repo_hash, str) and repo_hash:
        try:
            cp = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(root), capture_output=True, text=True, check=False)
            if cp.returncode == 0:
                head = cp.stdout.strip()
                if head and head != repo_hash:
                    findings.append(Finding("needs_review", "stale_context", "repo_commit_hash mismatch", str(context_path), None, CONTEXT_NEEDS_REVIEW))
                    result = combine(result, CONTEXT_NEEDS_REVIEW)
        except FileNotFoundError:
            findings.append(Finding("needs_review", "stale_context", "git unavailable for freshness check", str(context_path), None, CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    if any(f.result_impact == CONTEXT_NEEDS_REVIEW for f in findings) and result == CONTEXT_COMPLIANT:
        result = CONTEXT_COMPLIANT_WITH_WARNINGS
    return result, fm, body, findings


def has_phrase(text: str, phrase: str) -> bool:
    return phrase in normalize_text(text)


def check_non_auth_violations(text: str, source: str) -> tuple[str, list[Finding]]:
    findings: list[Finding] = []
    norm = normalize_text(text)
    result = CONTEXT_COMPLIANT
    for phrase in PROTECTED_APPROVAL_CLAIMS:
        if phrase in norm:
            findings.append(Finding("violation", "non_authorization_violation", f"forbidden approval claim: {phrase}", source, None, CONTEXT_VIOLATION))
            result = CONTEXT_VIOLATION
    return result, findings


def check_plan(plan_text: str, context_body: str, source: str) -> tuple[str, list[Finding]]:
    findings: list[Finding] = []
    result = CONTEXT_COMPLIANT
    plan_norm = normalize_text(plan_text)

    selected = extract_selected_items(context_body)
    required_paths = extract_list_items(section_lines(context_body, "## Required Context"))
    policy_items = extract_list_items(section_lines(context_body, "## Relevant Policies"))
    lesson_lines = extract_list_items(section_lines(context_body, "## Relevant Lessons"))

    # Acknowledgements
    if required_paths and required_paths != ["none"]:
        acknowledged = any(p.lower() in plan_norm for p in required_paths)
        if not acknowledged:
            findings.append(Finding("needs_review", "selected_rule_missing", "plan does not acknowledge required context paths", source, None, CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    if policy_items and policy_items != ["none"]:
        acknowledged = any(p.lower() in plan_norm for p in policy_items)
        if not acknowledged:
            findings.append(Finding("needs_review", "selected_policy_missing", "plan does not acknowledge selected policies", source, None, CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    if lesson_lines and lesson_lines != ["none"]:
        if "lesson" not in plan_norm:
            findings.append(Finding("needs_review", "lesson_not_acknowledged", "plan does not acknowledge relevant lessons", source, None, CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    # Contradiction heuristics
    if "bypass m27" in plan_norm or "ignore m27" in plan_norm:
        findings.append(Finding("violation", "selected_rule_contradicted", "plan explicitly bypasses M27", source, None, CONTEXT_VIOLATION))
        result = combine(result, CONTEXT_VIOLATION)

    if "repeat known lesson" in plan_norm:
        findings.append(Finding("violation", "lesson_repeated", "plan repeats known lesson pattern", source, None, CONTEXT_VIOLATION))
        result = combine(result, CONTEXT_VIOLATION)

    non_auth_result, na_findings = check_non_auth_violations(plan_text, source)
    findings.extend(na_findings)
    result = combine(result, non_auth_result)

    if result == CONTEXT_COMPLIANT and findings:
        result = CONTEXT_COMPLIANT_WITH_WARNINGS
    return result, findings


def check_verification(verification_text: str, context_body: str, source: str) -> tuple[str, list[Finding]]:
    findings: list[Finding] = []
    result = CONTEXT_COMPLIANT
    ver_norm = normalize_text(verification_text)

    needed = [
        "selected rules",
        "selected policies",
        "selected lessons",
        "out-of-scope",
        "context pack did not grant approval",
        "m27",
    ]
    for k in needed:
        if k not in ver_norm:
            findings.append(Finding("needs_review", "insufficient_verification", f"verification missing context-aware check: {k}", source, None, CONTEXT_NEEDS_REVIEW))
            result = combine(result, CONTEXT_NEEDS_REVIEW)

    if "success" in ver_norm and "selected context" not in ver_norm:
        findings.append(Finding("needs_review", "insufficient_verification", "verification claims success without selected context proof", source, None, CONTEXT_NEEDS_REVIEW))
        result = combine(result, CONTEXT_NEEDS_REVIEW)

    if "contradict" in ver_norm and "selected" in ver_norm:
        findings.append(Finding("violation", "selected_rule_contradicted", "verification admits contradiction of selected context", source, None, CONTEXT_VIOLATION))
        result = combine(result, CONTEXT_VIOLATION)

    if "repeat known lesson" in ver_norm:
        findings.append(Finding("violation", "lesson_repeated", "verification repeats known lesson pattern", source, None, CONTEXT_VIOLATION))
        result = combine(result, CONTEXT_VIOLATION)

    non_auth_result, na_findings = check_non_auth_violations(verification_text, source)
    findings.extend(na_findings)
    result = combine(result, non_auth_result)

    if result == CONTEXT_COMPLIANT and findings:
        result = CONTEXT_COMPLIANT_WITH_WARNINGS
    return result, findings


def check_changed_files(changed: list[str], context_body: str, source: str) -> tuple[str, list[Finding]]:
    findings: list[Finding] = []
    result = CONTEXT_COMPLIANT

    out_scope_lines = section_lines(context_body, "## Out-of-Scope Context")
    out_scope_text = "\n".join(out_scope_lines).lower()
    out_scope_tokens: list[str] = []
    for ln in out_scope_lines:
        s = ln.strip().lower()
        if "path_or_category:" in s:
            tok = s.split("path_or_category:", 1)[1].strip()
            if tok:
                out_scope_tokens.append(tok)

    for p in changed:
        if is_abs_path_like(p):
            findings.append(Finding("violation", "changed_files_conflict", "absolute path in changed-files", source, p, CONTEXT_VIOLATION))
            result = combine(result, CONTEXT_VIOLATION)
            continue
        if p.startswith("..") or "/../" in p or "\\..\\" in p:
            findings.append(Finding("violation", "changed_files_conflict", "repo escape path in changed-files", source, p, CONTEXT_VIOLATION))
            result = combine(result, CONTEXT_VIOLATION)
            continue
        # explicit out-of-scope match by text mention
        p_low = p.lower()
        explicit_match = p_low in out_scope_text
        prefix_match = any(
            (tok.endswith("/") and p_low.startswith(tok))
            or (tok and p_low == tok)
            for tok in out_scope_tokens
        )
        if explicit_match or prefix_match:
            findings.append(Finding("violation", "out_of_scope_touched", "changed path is explicitly out-of-scope", source, p, CONTEXT_VIOLATION))
            result = combine(result, CONTEXT_VIOLATION)

    return result, findings


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()

    context_path = resolve(root, args.context)
    plan_path = resolve(root, args.plan)
    verification_path = resolve(root, args.verification)
    changed_path = resolve(root, args.changed_files)

    findings: list[Finding] = []
    warnings: list[str] = []
    errors: list[str] = []

    if not any([plan_path, verification_path, changed_path]):
        result = CONTEXT_MISSING
        errors.append("Missing required compliance input must return CONTEXT_MISSING")
    else:
        result = CONTEXT_COMPLIANT

    if context_path is None or not context_path.exists():
        result = CONTEXT_MISSING
        errors.append("context pack missing")

    if plan_path is not None and not plan_path.exists():
        result = CONTEXT_MISSING
        errors.append("plan missing")
    if verification_path is not None and not verification_path.exists():
        result = CONTEXT_MISSING
        errors.append("verification missing")
    if changed_path is not None and not changed_path.exists():
        result = CONTEXT_MISSING
        errors.append("changed-files missing")

    context_fm: dict[str, Any] | None = None
    context_body = ""
    if result != CONTEXT_MISSING and context_path is not None:
        r, context_fm, context_body, f = check_context_pack(root, context_path)
        findings.extend(f)
        result = combine(result, r)

    # Plan check
    if result != CONTEXT_MISSING and plan_path is not None:
        plan_text = plan_path.read_text(encoding="utf-8")
        r, f = check_plan(plan_text, context_body, plan_path.as_posix())
        findings.extend(f)
        result = combine(result, r)

    # Verification check
    if result != CONTEXT_MISSING and verification_path is not None:
        ver_text = verification_path.read_text(encoding="utf-8")
        r, f = check_verification(ver_text, context_body, verification_path.as_posix())
        findings.extend(f)
        result = combine(result, r)

    # Changed files check
    if result != CONTEXT_MISSING and changed_path is not None:
        changed, f1, force = parse_changed_files(changed_path)
        findings.extend(f1)
        if force is not None:
            result = combine(result, force)
        elif changed is not None:
            r, f2 = check_changed_files(changed, context_body, changed_path.as_posix())
            findings.extend(f2)
            result = combine(result, r)

    if result == CONTEXT_COMPLIANT:
        # If warnings-like findings are present, downgrade to warning result.
        if any(f.severity in {"warning", "needs_review"} for f in findings):
            result = CONTEXT_COMPLIANT_WITH_WARNINGS

    # collect plain warnings/errors arrays
    for f in findings:
        if f.severity in {"warning", "needs_review"}:
            warnings.append(f.message)
        if f.severity == "violation":
            errors.append(f.message)

    payload = {
        "result": result,
        "context_path": args.context,
        "plan_path": args.plan,
        "verification_path": args.verification,
        "changed_files_path": args.changed_files,
        "warnings": warnings,
        "errors": errors,
        "findings": [asdict(x) for x in findings],
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

    return EXIT_CODE[result]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
