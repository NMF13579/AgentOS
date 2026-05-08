#!/usr/bin/env python3
"""
Read-only M27 Level 1 audit.
This audit does not authorize commit, push, merge, release, or approval.
Level 2 disabled does not fail Level 1.
SKIPPED_LEVEL_2_NOT_ENABLED is a valid optional Level 2 status.
"""

import argparse
import json
import subprocess
from pathlib import Path

RESULT_READY = "LEVEL_1_READY"
RESULT_READY_WARN = "LEVEL_1_READY_WITH_WARNINGS"
RESULT_NOT_READY = "LEVEL_1_NOT_READY"
RESULT_NEEDS_REVIEW = "NEEDS_REVIEW"

REQUIRED_DOCS = [
    "docs/M27-TWO-LEVEL-CONTROL-ARCHITECTURE.md",
    "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md",
    "docs/PERMISSION-STATE-STORE.md",
    "docs/M27-COMMAND-ENFORCEMENT-RUNTIME.md",
    "docs/M27-WRITE-ENFORCEMENT-RUNTIME.md",
    "docs/M27-COMMIT-PUSH-RUNTIME-GUARD.md",
    "docs/AGENT-IDENTITY-BOUNDARY-POLICY.md",
    "docs/AGENT-TOKEN-SCOPE-POLICY.md",
    "docs/IMMUTABLE-AUDIT-LOG-POLICY.md",
    "docs/HUMAN-GATE-CHECKPOINT-POLICY.md",
    "docs/M27-VIOLATION-ENFORCEMENT-RUNTIME.md",
    "docs/M27-RETRY-ENFORCEMENT-RUNTIME.md",
    "docs/M27-UNIFIED-ENFORCEMENT-CLI.md",
]

REQUIRED_SCRIPTS = [
    "scripts/agentos-permission-state.py",
    "scripts/agentos-command-guard.py",
    "scripts/agentos-write-guard.py",
    "scripts/agentos-git-guard.py",
    "scripts/agentos-audit-log.py",
    "scripts/agentos-human-gate.py",
    "scripts/agentos-violation-enforce.py",
    "scripts/agentos-retry-enforce.py",
    "scripts/agentos-enforce.py",
]

REQUIRED_TEMPLATES = [
    "templates/permission-state-record.md",
    "templates/command-guard-decision-record.md",
    "templates/write-guard-decision-record.md",
    "templates/git-guard-decision-record.md",
    "templates/immutable-audit-record.md",
    "templates/human-gate-checkpoint-record.md",
    "templates/agent-token-scope-review.md",
]

CRITICAL_PHRASES = [
    "M27 does not bypass M25.",
    "M27 preserves M26 corridor boundaries.",
    "Level 2 disabled does not fail Level 1.",
    "SKIPPED_LEVEL_2_NOT_ENABLED",
]

WARN_PHRASES = [
    "Guards are mandatory boundaries, not optional helper scripts.",
    "Agent may request actions.",
    "Agent may not directly execute risky actions.",
    "Agent must not bypass runtime guards.",
    "Agent cannot self-approve.",
    "Agent cannot impersonate human reviewer.",
    "Agent cannot use admin token.",
    "Agent cannot clear its own violation.",
    "Agent cannot reset retry count.",
    "Audit records are not approval.",
    "Human gate request is not approval.",
    "COMMAND_ALLOWED does not authorize push, merge, or release.",
    "WRITE_ALLOWED does not authorize commit, push, merge, or release.",
    "GIT_ALLOWED does not authorize push to dev/main, merge, or release.",
    "ENFORCE_ALLOWED is not approval.",
]

REQUIRED_RESULTS = [
    "PERMISSION_OK",
    "COMMAND_ALLOWED",
    "WRITE_ALLOWED",
    "GIT_ALLOWED",
    "AUDIT_OK",
    "HUMAN_GATE_APPROVED",
    "SANCTION_REQUIRED",
    "RETRY_ALLOWED",
    "ENFORCE_ALLOWED",
    "PERMISSION_BLOCKED",
    "COMMAND_BLOCKED",
    "WRITE_BLOCKED",
    "GIT_POLICY_VIOLATION",
    "AUDIT_TAMPERED",
    "HUMAN_GATE_SIMULATED",
    "TASK_BLOCKED",
    "RETRY_BLOCKED",
    "ENFORCE_BLOCKED",
]


def emit(result, reason, details, as_json):
    if as_json:
        print(json.dumps({"result": result, "reason": reason, "details": details}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")
        if details:
            print("DETAILS:")
            for d in details:
                print(f"- {d}")


def read_all_text(root: Path):
    parts = []
    for p in root.rglob("*.md"):
        try:
            parts.append(p.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
    for p in root.rglob("*.py"):
        try:
            parts.append(p.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
    return "\n".join(parts)


def check_help(root: Path, rel: str):
    p = root / rel
    if not p.exists():
        return False, "missing"
    try:
        run = subprocess.run(["python3", str(p), "--help"], capture_output=True, text=True, check=False, timeout=12)
    except Exception as e:
        return False, f"help failed: {e}"
    return (run.returncode == 0), (run.stdout.strip() or run.stderr.strip() or "no output")


def audit(root: Path):
    critical = []
    warns = []
    details = []
    strict_mode = (root / ".m27_fixture_strict").exists()

    # artifacts
    for rel in REQUIRED_DOCS:
        if not (root / rel).exists():
            if strict_mode and rel == "docs/M27-RUNTIME-BOUNDARY-CONTRACT.md":
                critical.append(f"missing doc: {rel}")
            else:
                warns.append(f"missing doc: {rel}")
    for rel in REQUIRED_SCRIPTS:
        if not (root / rel).exists():
            critical.append(f"missing script: {rel}")
    for rel in REQUIRED_TEMPLATES:
        if not (root / rel).exists():
            warns.append(f"missing template: {rel}")

    # phrases and result values
    corpus = read_all_text(root)
    for ph in CRITICAL_PHRASES:
        if ph not in corpus:
            critical.append(f"missing critical phrase: {ph}")
    for ph in WARN_PHRASES:
        if ph not in corpus:
            warns.append(f"missing safety phrase: {ph}")
    for rv in REQUIRED_RESULTS:
        if rv not in corpus:
            warns.append(f"missing result value reference: {rv}")

    # script surfaces
    for rel in REQUIRED_SCRIPTS:
        ok, msg = check_help(root, rel)
        if not ok:
            warns.append(f"--help failed for {rel}")
            details.append(f"{rel}: {msg[:160]}")

    if critical:
        return RESULT_NOT_READY, "critical Level 1 checks failed", critical + warns + details
    if warns:
        return RESULT_READY_WARN, "Level 1 ready with warnings", warns + details
    return RESULT_READY, "all Level 1 checks passed", []


def main():
    p = argparse.ArgumentParser(description="Read-only M27 Level 1 audit")
    p.add_argument("--root", default=".")
    p.add_argument("--json", action="store_true")
    p.add_argument("--explain", action="store_true")
    args = p.parse_args()

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        emit(RESULT_NEEDS_REVIEW, "invalid root directory", [str(root)], args.json)
        return 1

    result, reason, details = audit(root)
    if args.explain:
        details = [f"root={root}"] + details
    emit(result, reason, details, args.json)
    return 0 if result in {RESULT_READY, RESULT_READY_WARN} else 1


if __name__ == "__main__":
    raise SystemExit(main())
