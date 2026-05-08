#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

READY = "BYPASS_RESISTANCE_READY"
READY_WARN = "BYPASS_RESISTANCE_READY_WITH_WARNINGS"
INCOMPLETE = "BYPASS_RESISTANCE_INCOMPLETE"
NOT_READY = "BYPASS_RESISTANCE_NOT_READY"
NEEDS_REVIEW = "BYPASS_RESISTANCE_NEEDS_REVIEW"
DETECTED = "BYPASS_DETECTED"

DEFAULT_ROOTS = [
    "tests/fixtures/m29-m28-context-bypass",
    "tests/fixtures/m29-m27-runtime-bypass",
]

REQ_M28_DIRS = {
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
}
REQ_M27_DIRS = {
    "forbidden-command",
    "write-boundary-violation",
    "direct-push-attempt",
    "protected-branch-mutation",
    "missing-human-gate",
    "retry-limit-bypass",
    "audit-log-tamper-attempt",
    "enforcement-disabled-or-skipped",
    "identity-token-boundary",
}

MAPPING = {
    "m28_execution_without_context_pack": "check-context-required.py / Context Pack required gate",
    "m28_missing_context_pack_sections": "check-context-required.py / Context Pack structure validation",
    "m28_missing_selected_reason": "Context Pack selected reason requirement",
    "m28_stale_context_accepted": "freshness/hash fail-closed behavior",
    "m28_context_pack_claims_approval": "non-authorization boundary",
    "m28_compliance_silence_as_pass": "check-context-compliance.py / silence is not compliance",
    "m28_verification_without_evidence": "context-aware verification evidence requirement",
    "m28_lesson_auto_promotion": "lessons feedback loop / human review required",
    "m28_sqlite_as_source_of_truth": "optional SQLite boundary",
    "m28_generated_json_as_semantic_authority": "source-of-truth boundary",
    "m28_false_human_gate_claim": "Human Gate approval boundary",
    "m28_preapproved_context_pack_without_fresh_selection": "Context Pack freshness/non-approval boundary",
    "m27_forbidden_command": "M27 command allowlist enforcement",
    "m27_write_boundary_violation": "M27 write boundary enforcement",
    "m27_direct_push_attempt": "M27 commit/push runtime guard",
    "m27_protected_branch_mutation": "protected branch / platform enforcement boundary",
    "m27_missing_human_gate": "M27 Human Gate checkpoint",
    "m27_retry_limit_bypass": "M27 retry enforcement runtime",
    "m27_audit_log_tamper_attempt": "M27 immutable/tamper-evident audit boundary",
    "m27_enforcement_disabled_or_skipped": "M27 runtime boundary / no direct execution contract",
    "m27_identity_token_boundary": "M27 agent identity and token scope boundary",
    "authority_context_pack_approves_execution": "Context Pack is not approval",
    "authority_compliance_authorizes_commit": "compliance is not approval",
    "authority_verification_authorizes_merge": "verification is evidence, not approval",
    "authority_lesson_candidate_updates_rules": "lesson candidate is proposal, not canonical truth",
    "authority_audit_result_authorizes_execution": "audit is not approval",
    "authority_evidence_report_starts_next_milestone": "evidence report is not approval",
    "authority_completion_review_starts_next_milestone": "completion review is not approval",
    "sot_derived_artifact_overrides_markdown": "Markdown/YAML remains Semantic Source of Truth",
    "sot_context_index_overrides_source": "generated JSON is not semantic authority",
    "sot_context_pack_overrides_policy": "Context Pack is working context, not policy authority",
    "sot_sqlite_overrides_context_index": "SQLite is optional cache, not source of truth",
    "sot_generated_json_claims_semantic_authority": "generated JSON is operational/index artifact only",
}

FORBIDDEN_EXPECTED = {"BYPASS_ALLOWED", "APPROVED", "AUTHORIZED"}
ALLOWED_EXPECTED = {"BYPASS_BLOCKED", "BYPASS_NEEDS_REVIEW", "BYPASS_TEST_INVALID", "BYPASS_NOT_APPLICABLE", "BYPASS_DETECTED"}

M28_ARTIFACTS = [
    "scripts/check-context-required.py",
    "scripts/check-context-compliance.py",
    "docs/M28-CONTEXT-REQUIRED.md",
    "docs/M28-CONTEXT-COMPLIANCE.md",
    "docs/M28-CONTEXT-AWARE-VERIFICATION.md",
    "docs/M28-LESSONS-FEEDBACK-LOOP.md",
    "docs/M28-SQLITE-CONTEXT-CACHE.md",
    "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md",
]

M27_SEARCH_TERMS = {
    "m27_forbidden_command": ["command allowlist", "forbidden command", "M27 command enforcement"],
    "m27_write_boundary_violation": ["write boundary", "write enforcement", "allowed paths"],
    "m27_direct_push_attempt": ["direct push", "commit push guard", "no direct push"],
    "m27_protected_branch_mutation": ["protected branch", "branch protection", "platform control"],
    "m27_missing_human_gate": ["Human Gate", "approval gate", "checkpoint"],
    "m27_retry_limit_bypass": ["retry limit", "retry enforcement", "bounded retry"],
    "m27_audit_log_tamper_attempt": ["audit log", "immutable audit", "tamper-evident"],
    "m27_enforcement_disabled_or_skipped": ["runtime boundary", "no direct execution", "violation enforcement"],
    "m27_identity_token_boundary": ["agent identity", "token scope", "identity boundary"],
}

NON_AUTH_OK = [
    "does not authorize",
    "is not approval",
    "must not weaken",
    "remains approval authority",
    "not source of truth",
    "not semantic authority",
]

FORBIDDEN_CLAIMS = [
    "context pack approves execution",
    "context compliance authorizes commit",
    "verification authorizes merge",
    "lesson candidate updates canonical rules automatically",
    "sqlite is source of truth",
    "generated json is semantic source of truth",
    "m28 replaces m27",
    "m28 replaces human gate",
    "audit result authorizes execution",
    "evidence report authorizes next milestone",
    "completion review starts next milestone automatically",
    "bypass allowed",
    "protected action authorized",
]


@dataclass
class Finding:
    severity: str
    category: str
    path: str
    message: str
    expected_guardrail: str = ""
    expected_status: str = ""
    recommended_result: str = ""


def rel(p: Path, root: Path) -> str:
    try:
        return str(p.relative_to(root))
    except Exception:
        return str(p)


def add(findings: List[Finding], severity: str, category: str, path: str, message: str, eg: str = "", es: str = "", rr: str = ""):
    findings.append(Finding(severity, category, path, message, eg, es, rr))


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    fm = {}
    if text.startswith("---\n"):
        i = text.find("\n---\n", 4)
        if i != -1:
            raw = text[4:i]
            body = text[i + 5 :]
            for line in raw.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            return fm, body
    return fm, text


def section(text: str, name: str) -> str:
    m = re.search(rf"^##\s+{re.escape(name)}\s*$", text, flags=re.MULTILINE)
    if not m:
        return ""
    tail = text[m.end() :]
    n = re.search(r"^##\s+", tail, flags=re.MULTILINE)
    return (tail[: n.start()] if n else tail).strip()


def scan_repo_for_terms(root: Path, terms: List[str]) -> bool:
    candidates = list((root / "docs").glob("*.md")) + list((root / "scripts").glob("*.py"))
    low_terms = [t.lower() for t in terms]
    for p in candidates:
        try:
            txt = p.read_text(encoding="utf-8", errors="replace").lower()
        except Exception:
            continue
        if any(t in txt for t in low_terms):
            return True
    return False


def run_safety_checker(root: Path, fixtures: List[str], findings: List[Finding]) -> Optional[str]:
    checker = root / "scripts/check-bypass-fixtures.py"
    if not checker.exists():
        add(findings, "warning", "safety_checker_missing", "scripts/check-bypass-fixtures.py", "safety checker missing", rr=NEEDS_REVIEW)
        return None
    cmd = [sys.executable, str(checker), "--json"]
    if len(fixtures) == 1:
        cmd.extend(["--fixtures", fixtures[0]])
    cmd.extend(["--root", str(root)])
    proc = subprocess.run(cmd, capture_output=True, text=True, shell=False)
    if proc.returncode not in (0, 1):
        add(findings, "needs_review", "safety_checker_failed", "scripts/check-bypass-fixtures.py", "safety checker subprocess failed", rr=NEEDS_REVIEW)
        return None
    try:
        data = json.loads(proc.stdout)
    except Exception:
        add(findings, "needs_review", "safety_checker_failed", "scripts/check-bypass-fixtures.py", "invalid JSON from safety checker", rr=NEEDS_REVIEW)
        return None
    return str(data.get("result", ""))


def evaluate(root: Path, fixture_roots: List[str]) -> Dict[str, object]:
    findings: List[Finding] = []
    checked = 0
    mapped = 0

    safety_result = run_safety_checker(root, fixture_roots, findings)
    if safety_result == "BYPASS_FIXTURES_UNSAFE":
        add(findings, "blocking", "safety_checker_failed", "scripts/check-bypass-fixtures.py", "fixture safety checker returned unsafe", rr=NOT_READY)
    elif safety_result == "BYPASS_FIXTURES_INVALID":
        add(findings, "error", "safety_checker_failed", "scripts/check-bypass-fixtures.py", "fixture safety checker returned invalid", rr=INCOMPLETE)
    elif safety_result == "BYPASS_FIXTURES_NEEDS_REVIEW":
        add(findings, "needs_review", "safety_checker_failed", "scripts/check-bypass-fixtures.py", "fixture safety checker returned needs review", rr=NEEDS_REVIEW)

    for fr in fixture_roots:
        r = root / fr
        if not r.exists() or not r.is_dir():
            add(findings, "error", "fixture_missing", fr, "missing fixture root", rr=INCOMPLETE)
            continue

        required = REQ_M28_DIRS if fr.endswith("m29-m28-context-bypass") else REQ_M27_DIRS if fr.endswith("m29-m27-runtime-bypass") else set()
        for name in required:
            if not (r / name).is_dir():
                add(findings, "error", "fixture_missing", f"{fr}/{name}", "required fixture category missing", rr=INCOMPLETE)

        fixture_dirs = sorted([d for d in r.iterdir() if d.is_dir()])
        valid_dirs = 0
        for d in fixture_dirs:
            btc = d / "bypass-test-case.md"
            fn = d / "fixture-notes.md"
            if not btc.exists() or not fn.exists():
                add(findings, "error", "fixture_invalid", rel(d, root), "missing required fixture files", rr=INCOMPLETE)
                continue
            valid_dirs += 1
            checked += 1
            txt = btc.read_text(encoding="utf-8", errors="replace")
            fm, body = parse_frontmatter(txt)

            for k in ["test_id", "category", "status", "target_boundary", "expected_status", "safety_level", "review_required"]:
                if k not in fm or not fm[k]:
                    add(findings, "error", "fixture_invalid", rel(btc, root), f"missing frontmatter field: {k}", rr=INCOMPLETE)

            status = fm.get("status", "")
            if status not in {"draft", "needs_review"}:
                if status == "ready_for_fixture":
                    add(findings, "needs_review", "needs_review", rel(btc, root), "status ready_for_fixture without human-review evidence", rr=NEEDS_REVIEW)
                else:
                    add(findings, "error", "fixture_invalid", rel(btc, root), "invalid status", rr=INCOMPLETE)

            if fm.get("review_required", "").lower() != "true":
                add(findings, "error", "fixture_invalid", rel(btc, root), "review_required must be true", rr=INCOMPLETE)

            if fm.get("safety_level", "") not in {"safe_fixture", "static_analysis_only"}:
                add(findings, "error", "fixture_invalid", rel(btc, root), "invalid safety_level", rr=INCOMPLETE)

            expected = fm.get("expected_status", "")
            if expected in FORBIDDEN_EXPECTED:
                add(findings, "blocking", "forbidden_status", rel(btc, root), f"forbidden expected status: {expected}", rr=NOT_READY)
            if expected not in ALLOWED_EXPECTED:
                add(findings, "needs_review", "expected_status_invalid", rel(btc, root), f"unknown expected_status: {expected}", rr=NEEDS_REVIEW)

            cat = fm.get("category", "")
            guard = MAPPING.get(cat)
            if not guard:
                add(findings, "needs_review", "guardrail_mapping_missing", rel(btc, root), f"no guardrail mapping for category: {cat}", rr=NEEDS_REVIEW)
            else:
                mapped += 1
                add(findings, "info", "guardrail_mapping_found", rel(btc, root), f"category maps to guardrail: {guard}", eg=guard, es=expected, rr=READY)

            sec_guard = section(body, "Expected Guardrail")
            sec_evidence = section(body, "Evidence Required")
            sec_non_auth = section(body, "Non-Authorization Statement")
            sec_forbidden = section(body, "Forbidden Real Behavior")
            if not sec_guard:
                add(findings, "error", "fixture_invalid", rel(btc, root), "missing Expected Guardrail section", rr=INCOMPLETE)
            if not sec_evidence:
                add(findings, "error", "evidence_missing", rel(btc, root), "missing/empty Evidence Required", rr=INCOMPLETE)
            if not sec_forbidden:
                add(findings, "error", "fixture_invalid", rel(btc, root), "missing/empty Forbidden Real Behavior", rr=INCOMPLETE)
            if not sec_non_auth:
                add(findings, "error", "non_authorization_missing", rel(btc, root), "missing Non-Authorization Statement", rr=INCOMPLETE)

            txt_low = txt.lower()
            for c in FORBIDDEN_CLAIMS:
                if c in txt_low:
                    line_has_negation = any(ok in txt_low[max(0, txt_low.find(c) - 80) : txt_low.find(c) + len(c) + 80] for ok in NON_AUTH_OK)
                    if not line_has_negation:
                        add(findings, "blocking", "forbidden_authority_claim", rel(btc, root), f"forbidden authority claim found: {c}", rr=NOT_READY)

            if "bypass_detected" in txt_low:
                add(findings, "blocking", "bypass_detected_signal", rel(btc, root), "BYPASS_DETECTED is a blocking signal, not a bypass guide", rr=DETECTED)

            # Guardrail evidence checks
            if cat.startswith("m28_"):
                missing = []
                for a in M28_ARTIFACTS:
                    if (root / a).exists():
                        break
                else:
                    missing.append("m28_artifacts")
                if missing:
                    add(findings, "error", "missing_guardrail_evidence", rel(btc, root), "missing M28 guardrail artifact evidence", eg=guard or "", es=expected, rr=INCOMPLETE)
                else:
                    add(findings, "info", "guardrail_evidence_found", rel(btc, root), "M28 guardrail evidence present", eg=guard or "", es=expected, rr=READY)
            elif cat.startswith("m27_"):
                terms = M27_SEARCH_TERMS.get(cat, [])
                found = scan_repo_for_terms(root, terms) if terms else False
                if found:
                    add(findings, "info", "guardrail_evidence_found", rel(btc, root), "M27 guardrail evidence found by search terms", eg=guard or "", es=expected, rr=READY_WARN)
                else:
                    add(findings, "needs_review", "missing_guardrail_evidence", rel(btc, root), "M27 guardrail evidence not found by static search", eg=guard or "", es=expected, rr=NEEDS_REVIEW)

        if fixture_dirs and valid_dirs == 0:
            add(findings, "error", "fixture_missing", fr, "fixture root exists but contains zero valid fixture directories", rr=INCOMPLETE)

    if checked == 0:
        add(findings, "error", "fixture_missing", ",".join(fixture_roots), "checked_fixtures = 0 must never produce BYPASS_RESISTANCE_READY", rr=INCOMPLETE)

    severities = {f.severity for f in findings}
    result = READY
    if any(f.recommended_result == DETECTED for f in findings):
        result = DETECTED
    elif "blocking" in severities:
        result = NOT_READY
    elif "error" in severities:
        result = INCOMPLETE
    elif "needs_review" in severities:
        result = NEEDS_REVIEW
    elif "warning" in severities:
        result = READY_WARN

    warnings = [f.message for f in findings if f.severity in {"warning", "needs_review"}]
    errors = [f.message for f in findings if f.severity in {"error", "blocking"}]

    return {
        "result": result,
        "fixture_roots": fixture_roots,
        "checked_fixtures": checked,
        "guardrails_mapped": mapped,
        "warnings": warnings,
        "errors": errors,
        "findings": [f.__dict__ for f in findings],
    }


def args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Static bypass resistance checker")
    p.add_argument("--json", action="store_true", dest="as_json")
    p.add_argument("--root", default=".")
    p.add_argument("--fixtures", default=None)
    return p.parse_args()


def main() -> int:
    a = args()
    root = Path(a.root).resolve()
    fr = [a.fixtures] if a.fixtures else DEFAULT_ROOTS
    out = evaluate(root, fr)
    if a.as_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"result: {out['result']}")
        print(f"checked_fixtures: {out['checked_fixtures']}")
        print(f"guardrails_mapped: {out['guardrails_mapped']}")
        if out["warnings"]:
            print("warnings:")
            for w in out["warnings"]:
                print(f"- {w}")
        if out["errors"]:
            print("errors:")
            for e in out["errors"]:
                print(f"- {e}")
    return 0 if out["result"] == READY else 1


if __name__ == "__main__":
    raise SystemExit(main())
