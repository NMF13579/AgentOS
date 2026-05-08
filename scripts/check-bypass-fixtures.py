#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

RESULT_OK = "BYPASS_FIXTURES_OK"
RESULT_OK_WARN = "BYPASS_FIXTURES_OK_WITH_WARNINGS"
RESULT_INVALID = "BYPASS_FIXTURES_INVALID"
RESULT_UNSAFE = "BYPASS_FIXTURES_UNSAFE"
RESULT_NEEDS_REVIEW = "BYPASS_FIXTURES_NEEDS_REVIEW"

DEFAULT_ROOTS = [
    "tests/fixtures/m29-m28-context-bypass",
    "tests/fixtures/m29-m27-runtime-bypass",
]

REQUIRED_NON_AUTH_LINES = [
    "Bypass fixture is not approval.",
    "Bypass fixture does not authorize commit, push, merge, release, deployment, or protected changes.",
    "Bypass fixture does not authorize bypassing AgentOS guardrails.",
    "Bypass fixture does not weaken, disable, or reduce any guardrail.",
    "Bypass fixture must not weaken M27 runtime enforcement.",
    "Bypass fixture must not weaken M28 context control.",
    "Human Gate remains approval authority.",
]

ALLOWED_CATEGORIES = {
    "m28_execution_without_context_pack",
    "m28_missing_context_pack_sections",
    "m28_missing_selected_reason",
    "m28_stale_context_accepted",
    "m28_context_pack_claims_approval",
    "m28_compliance_silence_as_pass",
    "m28_verification_without_evidence",
    "m28_lesson_auto_promotion",
    "m28_sqlite_as_source_of_truth",
    "m28_generated_json_as_semantic_authority",
    "m28_false_human_gate_claim",
    "m28_preapproved_context_pack_without_fresh_selection",
    "m27_forbidden_command",
    "m27_write_boundary_violation",
    "m27_direct_push_attempt",
    "m27_protected_branch_mutation",
    "m27_missing_human_gate",
    "m27_retry_limit_bypass",
    "m27_audit_log_tamper_attempt",
    "m27_enforcement_disabled_or_skipped",
    "m27_identity_token_boundary",
    "authority_context_pack_approves_execution",
    "authority_compliance_authorizes_commit",
    "authority_verification_authorizes_merge",
    "authority_lesson_candidate_updates_rules",
    "authority_audit_result_authorizes_execution",
    "authority_evidence_report_starts_next_milestone",
    "authority_completion_review_starts_next_milestone",
    "sot_derived_artifact_overrides_markdown",
    "sot_context_index_overrides_source",
    "sot_context_pack_overrides_policy",
    "sot_sqlite_overrides_context_index",
    "sot_generated_json_claims_semantic_authority",
}

ALLOWED_BOUNDARIES = {
    "m27_runtime_enforcement",
    "m28_context_control",
    "human_gate_approval",
    "protected_action_boundary",
    "source_of_truth_boundary",
    "non_authorization_boundary",
    "optional_sqlite_boundary",
    "audit_evidence_boundary",
}

REQ_SECTIONS = [
    "Simulated Attempt",
    "Expected Guardrail",
    "Expected Result",
    "Evidence Required",
    "Forbidden Real Behavior",
    "Safety Notes",
    "Non-Authorization Statement",
]

DISALLOWED_EXTS = {".sh", ".py", ".bash", ".zsh", ".rb", ".pl"}
FORBIDDEN_EXPECTED = {"BYPASS_ALLOWED", "APPROVED", "AUTHORIZED"}
ALLOWED_STATUSES = {"draft", "needs_review"}
ALLOWED_SAFETY = {"safe_fixture", "static_analysis_only"}

SECRET_PATTERNS = [
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9_]{30,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._=-]{8,}"),
    re.compile(r"password\s*=\s*\S+", re.IGNORECASE),
    re.compile(r"secret\s*=\s*\S+", re.IGNORECASE),
]

PROD_PATTERNS = [
    re.compile(r"https?://(?!example\.com|example\.org|localhost|127\.0\.0\.1)[^\s)]+", re.IGNORECASE),
    re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"),
]

BYPASS_GUIDE_PATTERNS = [
    re.compile(r"run this command", re.IGNORECASE),
    re.compile(r"disable enforcement by", re.IGNORECASE),
    re.compile(r"turn off guardrail", re.IGNORECASE),
    re.compile(r"use this token", re.IGNORECASE),
    re.compile(r"push directly to", re.IGNORECASE),
    re.compile(r"delete audit log", re.IGNORECASE),
    re.compile(r"skip Human Gate by", re.IGNORECASE),
    re.compile(r"exfiltrate", re.IGNORECASE),
    re.compile(r"curl\s+http", re.IGNORECASE),
    re.compile(r"\bssh\s", re.IGNORECASE),
    re.compile(r"chmod\s+\+x", re.IGNORECASE),
    re.compile(r"rm\s+-rf", re.IGNORECASE),
]


@dataclass
class Finding:
    severity: str
    category: str
    path: str
    message: str


def relpath(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root))
    except Exception:
        return str(p)


def add(findings: List[Finding], severity: str, category: str, path: str, message: str) -> None:
    findings.append(Finding(severity, category, path, message))


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, str]], str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_raw = text[4:end]
    body = text[end + 5 :]
    fm: Dict[str, str] = {}
    for line in fm_raw.splitlines():
        if not line.strip() or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def sections(text: str) -> Dict[str, str]:
    chunks: Dict[str, str] = {}
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunks[name] = text[start:end].strip()
    return chunks


def is_defensive_context(text: str, match_start: int) -> bool:
    window = text[max(0, match_start - 300) : match_start].lower()
    defensive_markers = [
        "forbidden real behavior",
        "safety notes",
        "non-authorization statement",
        "inert",
        "not executable",
        "fixture-only",
        "does not authorize",
        "must not",
    ]
    return any(m in window for m in defensive_markers)


def redact(s: str) -> str:
    return re.sub(r"[A-Za-z0-9]{6,}", "[REDACTED]", s)


def check_file_safety(path: Path, root: Path, findings: List[Finding]) -> None:
    rp = relpath(path, root)
    if path.is_symlink():
        add(findings, "unsafe", "symlink_detected", rp, "symlinks are not allowed")
        return
    st = path.stat()
    if st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):
        add(findings, "unsafe", "executable_bit", rp, "executable bit set")
    if path.suffix.lower() in DISALLOWED_EXTS:
        add(findings, "unsafe", "disallowed_file_type", rp, "disallowed script extension")
    if path.suffix.lower() not in {".md", ".json"}:
        add(findings, "unsafe", "disallowed_file_type", rp, "only .md/.json allowed")
    data = path.read_bytes()
    if b"\x00" in data:
        add(findings, "unsafe", "disallowed_file_type", rp, "binary file detected")
        return
    text = data.decode("utf-8", errors="replace")
    if text.startswith("#!"):
        add(findings, "unsafe", "shebang_detected", rp, "shebang not allowed")

    for pat in SECRET_PATTERNS:
        for m in pat.finditer(text):
            msg = f"secret-like pattern detected: {redact(m.group(0))}"
            sev = "needs_review" if is_defensive_context(text, m.start()) else "unsafe"
            add(findings, sev, "secret_pattern_detected", rp, msg)

    for pat in PROD_PATTERNS:
        for m in pat.finditer(text):
            token = m.group(0)
            if token in {"127.0.0.1"}:
                continue
            if "example.com" in token or "example.org" in token or "localhost" in token:
                continue
            sev = "needs_review"
            add(findings, sev, "production_target_detected", rp, f"possible external/production target: {redact(token)}")

    for pat in BYPASS_GUIDE_PATTERNS:
        for m in pat.finditer(text):
            sev = "needs_review" if is_defensive_context(text, m.start()) else "unsafe"
            add(findings, sev, "bypass_guide_pattern", rp, f"bypass-guide pattern found: {pat.pattern}")


def check_non_auth(text: str, rp: str, findings: List[Finding]) -> None:
    missing = [line for line in REQUIRED_NON_AUTH_LINES if line not in text]
    if missing:
        add(findings, "error", "missing_non_authorization", rp, "missing required non-authorization block lines")

    for line in text.splitlines():
        l = line.lower().strip()
        if "does not authorize" in l or "is not approval" in l or "must not weaken" in l or "remains approval authority" in l:
            continue
        if "authorizes bypassing" in l or "approves execution" in l or "authorizes protected actions" in l or "bypass allowed" in l:
            add(findings, "unsafe", "forbidden_authority_claim", rp, "forbidden authority/approval claim found")


def check_sections(text: str, rp: str, findings: List[Finding]) -> None:
    sec = sections(text)
    for s in REQ_SECTIONS:
        if s not in sec:
            add(findings, "error", "required_section_missing", rp, f"missing section: {s}")
    ev = sec.get("Evidence Required", "").strip()
    frb = sec.get("Forbidden Real Behavior", "").strip()
    sn = sec.get("Safety Notes", "").strip()
    if not ev:
        add(findings, "error", "evidence_missing", rp, "empty Evidence Required section")
    else:
        if "guardrail" not in ev.lower() and "boundary" not in ev.lower() and "checker" not in ev.lower() and "audit" not in ev.lower():
            add(findings, "warning", "evidence_generic", rp, "Evidence Required should reference specific guardrail or boundary")
        if "tests passed" in ev.lower():
            add(findings, "warning", "evidence_generic", rp, "generic 'tests passed' is insufficient")
    if not frb:
        add(findings, "error", "required_section_missing", rp, "empty Forbidden Real Behavior section")
    if not sn:
        add(findings, "needs_review", "needs_review", rp, "empty Safety Notes section")


def check_frontmatter(fm: Dict[str, str], rp: str, findings: List[Finding], seen_ids: Dict[str, str]) -> None:
    required = [
        "type",
        "test_id",
        "status",
        "category",
        "target_boundary",
        "expected_status",
        "safety_level",
        "created_by",
        "created_at",
        "review_required",
    ]
    for k in required:
        if k not in fm or not fm[k]:
            add(findings, "error", "invalid_frontmatter", rp, f"missing frontmatter field: {k}")

    if fm.get("type") != "bypass-test-case":
        add(findings, "error", "invalid_frontmatter", rp, "type must be bypass-test-case")

    tid = fm.get("test_id", "")
    if tid:
        if tid in seen_ids:
            add(findings, "error", "invalid_frontmatter", rp, f"duplicate test_id values: {tid}")
        else:
            seen_ids[tid] = rp

    status = fm.get("status", "")
    if status not in ALLOWED_STATUSES:
        if status == "ready_for_fixture":
            add(findings, "needs_review", "needs_review", rp, "ready_for_fixture without human-review evidence")
        else:
            add(findings, "error", "invalid_frontmatter", rp, "status must be draft or needs_review")

    if fm.get("review_required", "").lower() != "true":
        add(findings, "error", "invalid_frontmatter", rp, "review_required must be true")

    expected = fm.get("expected_status", "")
    if expected in FORBIDDEN_EXPECTED:
        add(findings, "unsafe", "forbidden_status", rp, f"forbidden expected_status: {expected}")

    safety = fm.get("safety_level", "")
    if safety not in ALLOWED_SAFETY:
        add(findings, "error", "invalid_frontmatter", rp, "safety_level must be safe_fixture or static_analysis_only")

    created_by = fm.get("created_by", "")
    if created_by in {"<agent-id or human-username>", "", "placeholder", "unknown"}:
        add(findings, "needs_review", "invalid_frontmatter", rp, "created_by must not retain template placeholder value")

    created_at = fm.get("created_at", "")
    if created_at:
        try:
            dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            if dt > datetime.now(timezone.utc):
                add(findings, "needs_review", "invalid_frontmatter", rp, "created_at must not be in the future")
        except Exception:
            add(findings, "error", "invalid_frontmatter", rp, "invalid created_at format")

    cat = fm.get("category", "")
    if cat not in ALLOWED_CATEGORIES:
        add(findings, "needs_review", "unknown_category", rp, f"unknown category: {cat}")

    boundary = fm.get("target_boundary", "")
    if boundary not in ALLOWED_BOUNDARIES:
        add(findings, "needs_review", "unknown_boundary", rp, f"unknown target boundary: {boundary}")


def required_dirs_for_root(root: str) -> Optional[List[str]]:
    if root.endswith("m29-m28-context-bypass"):
        return [
            "execution-without-context-pack",
            "missing-context-pack-sections",
            "missing-selected-reason",
            "stale-context-accepted",
            "context-pack-claims-approval",
            "compliance-silence-as-pass",
            "verification-without-evidence",
            "lesson-auto-promotion",
            "sqlite-as-source-of-truth",
            "generated-json-as-semantic-authority",
            "false-human-gate-claim",
            "preapproved-context-pack-without-fresh-selection",
        ]
    if root.endswith("m29-m27-runtime-bypass"):
        return [
            "forbidden-command",
            "write-boundary-violation",
            "direct-push-attempt",
            "protected-branch-mutation",
            "missing-human-gate",
            "retry-limit-bypass",
            "audit-log-tamper-attempt",
            "enforcement-disabled-or-skipped",
            "identity-token-boundary",
        ]
    return None


def evaluate(root: Path, fixture_roots: List[str]) -> Dict[str, object]:
    findings: List[Finding] = []
    seen_ids: Dict[str, str] = {}
    checked_files = 0

    for r in fixture_roots:
        rp = root / r
        if not rp.exists() or not rp.is_dir():
            add(findings, "error", "fixture_missing", r, "fixture root is missing")
            continue
        if not (rp / "README.md").exists():
            add(findings, "error", "required_file_missing", r, "root README.md is missing")

        req = required_dirs_for_root(r)
        if req:
            for d in req:
                if not (rp / d).is_dir():
                    add(findings, "error", "fixture_missing", f"{r}/{d}", "required fixture directory missing")

        dirs = sorted([p for p in rp.iterdir() if p.is_dir()])
        if not dirs:
            add(findings, "error", "fixture_missing", r, "fixture root exists but contains zero fixture directories")

        for d in dirs:
            btc = d / "bypass-test-case.md"
            fn = d / "fixture-notes.md"
            if not btc.exists():
                add(findings, "error", "required_file_missing", relpath(btc, root), "missing bypass-test-case.md")
            if not fn.exists():
                add(findings, "error", "required_file_missing", relpath(fn, root), "missing fixture-notes.md")

            for f in d.rglob("*"):
                if not f.is_file():
                    continue
                checked_files += 1
                check_file_safety(f, root, findings)

            if btc.exists():
                text = btc.read_text(encoding="utf-8", errors="replace")
                fm, body = parse_frontmatter(text)
                rp_btc = relpath(btc, root)
                if fm is None:
                    add(findings, "error", "invalid_frontmatter", rp_btc, "missing or malformed frontmatter")
                else:
                    check_frontmatter(fm, rp_btc, findings, seen_ids)
                check_sections(body if fm else text, rp_btc, findings)
                check_non_auth(text, rp_btc, findings)
                add(findings, "info", "fixture_checked", rp_btc, "fixture passed static parse checks")

            if fn.exists():
                text = fn.read_text(encoding="utf-8", errors="replace")
                rp_fn = relpath(fn, root)
                check_sections(text, rp_fn, findings)
                check_non_auth(text, rp_fn, findings)
                add(findings, "info", "fixture_checked", rp_fn, "fixture notes passed static parse checks")

    severities = {f.severity for f in findings}
    if "unsafe" in severities:
        result = RESULT_UNSAFE
    elif "error" in severities:
        result = RESULT_INVALID
    elif "needs_review" in severities:
        result = RESULT_NEEDS_REVIEW
    elif "warning" in severities:
        result = RESULT_OK_WARN
    else:
        result = RESULT_OK

    warnings = [f.message for f in findings if f.severity in {"warning", "needs_review"}]
    errors = [f.message for f in findings if f.severity in {"error", "unsafe"}]

    return {
        "result": result,
        "fixture_roots": fixture_roots,
        "checked_files": checked_files,
        "warnings": warnings,
        "errors": errors,
        "findings": [f.__dict__ for f in findings],
    }


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Static bypass fixture safety checker")
    ap.add_argument("--json", action="store_true", dest="as_json", help="print JSON output")
    ap.add_argument("--root", default=".", help="repository root")
    ap.add_argument("--fixtures", default=None, help="single fixture root to check")
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    fixtures = [args.fixtures] if args.fixtures else DEFAULT_ROOTS
    data = evaluate(root, fixtures)

    if args.as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"result: {data['result']}")
        print(f"fixture_roots: {', '.join(data['fixture_roots'])}")
        print(f"checked_files: {data['checked_files']}")
        if data["warnings"]:
            print("warnings:")
            for w in data["warnings"]:
                print(f"- {w}")
        if data["errors"]:
            print("errors:")
            for e in data["errors"]:
                print(f"- {e}")

    return 0 if data["result"] == RESULT_OK else 1


if __name__ == "__main__":
    raise SystemExit(main())
