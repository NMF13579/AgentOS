#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

RESULTS = {"PASS", "WARN", "FAIL", "ERROR"}
CHECK_STATUSES = {"PASS", "WARN", "FAIL", "NOT_RUN", "NOT_IMPLEMENTED", "ERROR"}

BOUNDARY_LINES = [
    "RELEASE_READINESS_AUDIT_BOUNDARY: PASS does not mark AgentOS as MVP-ready.",
    "RELEASE_READINESS_AUDIT_BOUNDARY: WARN does not mark AgentOS as MVP-ready.",
    "RELEASE_READINESS_AUDIT_BOUNDARY: Final MVP readiness decision must come from Milestone 20 completion review.",
]

REQUIRED_ARTIFACTS = [
    "docs/STABLE-MVP-RELEASE-READINESS.md",
    "VERSION",
    "CHANGELOG.md",
    "docs/release-checklist.md",
    "templates/release-notes.md",
    "scripts/check-template-integrity.py",
    "docs/TEMPLATE-INTEGRITY.md",
    "scripts/test-template-integrity-fixtures.py",
    "tests/fixtures/template-integrity/",
    "docs/architecture.md",
    "docs/guardrails.md",
    "docs/limitations.md",
    "docs/troubleshooting.md",
    "docs/mvp-checklist.md",
    "examples/scenarios/simple-docs-change.md",
    "examples/scenarios/risky-deploy-change.md",
    "examples/scenarios/dangerous-command-detected.md",
    "examples/scenarios/failed-verification.md",
    "examples/scenarios/repeated-feedback-detected.md",
    "examples/scenarios/handoff-between-sessions.md",
    "prompts/cursor.md",
    "prompts/claude-code.md",
    "prompts/codex.md",
    "prompts/generic-agent.md",
    "docs/UNIFIED-GATE-CONTRACT.md",
    "docs/GATE-RESULT-SEMANTICS.md",
    "docs/GATE-OUTPUT-CONTRACT.md",
    "scripts/validate-gate-contract.py",
    "scripts/test-gate-regression-fixtures.py",
    "scripts/audit-gate-contract.py",
    "scripts/test-unified-gate-smoke.py",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Read-only release readiness audit runner")
    p.add_argument("--json", action="store_true", dest="json_mode", help="JSON output")
    p.add_argument("--strict", action="store_true", help="Exit 0 only for PASS")
    return p.parse_args()


def run_cmd(cmd, cwd: Path):
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def extract_marker(text: str, key: str):
    prefix = key + ":"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return None


def add_check(checks, name: str, status: str, reason: str):
    if status not in CHECK_STATUSES:
        status = "ERROR"
    checks.append({"name": name, "status": status, "reason": reason})


def artifact_exists(root: Path, rel: str) -> bool:
    p = root / rel
    if rel.endswith("/"):
        return p.exists() and p.is_dir()
    return p.exists() and p.is_file()


def evaluate(root: Path):
    checks = []

    for rel in REQUIRED_ARTIFACTS:
        status = "PASS" if artifact_exists(root, rel) else "FAIL"
        reason = "present" if status == "PASS" else "missing required artifact"
        add_check(checks, f"artifact:{rel}", status, reason)

    # Required command checks
    required_commands = [
        (["python3", "-m", "py_compile", "scripts/check-template-integrity.py"], "cmd:py_compile:check-template-integrity"),
        (["python3", "-m", "py_compile", "scripts/test-template-integrity-fixtures.py"], "cmd:py_compile:test-template-integrity-fixtures"),
        (["python3", "scripts/check-template-integrity.py"], "cmd:run:check-template-integrity"),
        (["python3", "scripts/test-template-integrity-fixtures.py"], "cmd:run:test-template-integrity-fixtures"),
    ]

    for cmd, name in required_commands:
        rc, out = run_cmd(cmd, root)
        if name == "cmd:run:check-template-integrity":
            marker = extract_marker(out, "TEMPLATE_INTEGRITY_RESULT")
            if marker is None:
                add_check(checks, name, "FAIL", "missing TEMPLATE_INTEGRITY_RESULT marker")
            elif marker in {"PASS", "WARN", "NOT_IMPLEMENTED"} and rc == 0:
                add_check(checks, name, "PASS", f"TEMPLATE_INTEGRITY_RESULT={marker}")
            elif marker in {"FAIL", "ERROR"}:
                add_check(checks, name, "FAIL", f"TEMPLATE_INTEGRITY_RESULT={marker}")
            else:
                add_check(checks, name, "ERROR", f"unexpected marker/exit combination: marker={marker}, rc={rc}")
            continue

        if name == "cmd:run:test-template-integrity-fixtures":
            marker = extract_marker(out, "TEMPLATE_INTEGRITY_FIXTURES_RESULT")
            if marker is None:
                if (root / "scripts/test-template-integrity-fixtures.py").exists():
                    add_check(checks, name, "FAIL", "missing TEMPLATE_INTEGRITY_FIXTURES_RESULT marker")
                else:
                    add_check(checks, name, "FAIL", "required script missing")
            elif marker == "PASS" and rc == 0:
                add_check(checks, name, "PASS", "fixture runner PASS")
            else:
                add_check(checks, name, "FAIL", f"fixture runner non-pass marker={marker}, rc={rc}")
            continue

        if rc == 0:
            add_check(checks, name, "PASS", "command passed")
        else:
            add_check(checks, name, "FAIL", f"command failed with rc={rc}")

    # Optional M19 checks
    optional_checks = [
        ("scripts/test-unified-gate-smoke.py", ["python3", "scripts/test-unified-gate-smoke.py"], "cmd:optional:test-unified-gate-smoke"),
        ("scripts/audit-gate-contract.py", ["python3", "scripts/audit-gate-contract.py"], "cmd:optional:audit-gate-contract"),
    ]

    for rel, cmd, name in optional_checks:
        p = root / rel
        if not p.exists():
            add_check(checks, name, "NOT_IMPLEMENTED", "optional script missing")
            continue
        rc, out = run_cmd(cmd, root)
        if rc == 0:
            add_check(checks, name, "PASS", "optional check passed")
        else:
            if "Traceback" in out:
                add_check(checks, name, "FAIL", "optional check failed with traceback")
            else:
                add_check(checks, name, "FAIL", f"optional check failed with rc={rc}")

    # Summaries
    checks_run = len(checks)
    checks_passed = sum(1 for c in checks if c["status"] == "PASS")
    checks_warned = sum(1 for c in checks if c["status"] == "WARN")
    checks_failed = sum(1 for c in checks if c["status"] in {"FAIL", "ERROR"})
    checks_not_run = sum(1 for c in checks if c["status"] == "NOT_RUN")
    checks_not_implemented = sum(1 for c in checks if c["status"] == "NOT_IMPLEMENTED")

    if checks_failed > 0:
        result = "FAIL"
        reason = "One or more required checks failed"
    elif checks_warned > 0 or checks_not_run > 0 or checks_not_implemented > 0:
        result = "WARN"
        reason = "Required checks passed but warnings/not-run/not-implemented remain"
    else:
        result = "PASS"
        reason = "All checks passed with no warnings"

    payload = {
        "audit": "release-readiness",
        "result": result,
        "checks_run": checks_run,
        "checks_passed": checks_passed,
        "checks_warned": checks_warned,
        "checks_failed": checks_failed,
        "checks_not_run": checks_not_run,
        "checks_not_implemented": checks_not_implemented,
        "reason": reason,
        "checks": checks,
    }
    return payload


def print_text(payload: dict):
    print("RELEASE_READINESS_AUDIT: run")
    print(f"RELEASE_READINESS_AUDIT_RESULT: {payload['result']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_RUN: {payload['checks_run']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_PASSED: {payload['checks_passed']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_WARNED: {payload['checks_warned']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_FAILED: {payload['checks_failed']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_NOT_RUN: {payload['checks_not_run']}")
    print(f"RELEASE_READINESS_AUDIT_CHECKS_NOT_IMPLEMENTED: {payload['checks_not_implemented']}")
    print(f"RELEASE_READINESS_AUDIT_REASON: {payload['reason']}")
    for c in payload["checks"]:
        print(f"RELEASE_READINESS_AUDIT_CHECK: {c['name']} {c['status']} {c['reason']}")
    for line in BOUNDARY_LINES:
        print(line)


def exit_code(result: str, strict: bool) -> int:
    if strict:
        return 0 if result == "PASS" else 1
    return 0 if result in {"PASS", "WARN"} else 1


def main() -> int:
    args = parse_args()
    payload = evaluate(Path.cwd())

    if payload["result"] not in RESULTS:
        payload["result"] = "ERROR"
        payload["reason"] = "Invalid internal audit result"

    if args.json_mode:
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print_text(payload)

    return exit_code(payload["result"], args.strict)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        error_payload = {
            "audit": "release-readiness",
            "result": "ERROR",
            "checks_run": 0,
            "checks_passed": 0,
            "checks_warned": 0,
            "checks_failed": 1,
            "checks_not_run": 0,
            "checks_not_implemented": 0,
            "reason": f"Unhandled exception: {exc.__class__.__name__}",
            "checks": [],
        }
        if "--json" in sys.argv[1:]:
            print(json.dumps(error_payload, ensure_ascii=False))
        else:
            print("RELEASE_READINESS_AUDIT: run")
            print("RELEASE_READINESS_AUDIT_RESULT: ERROR")
            print("RELEASE_READINESS_AUDIT_CHECKS_RUN: 0")
            print("RELEASE_READINESS_AUDIT_CHECKS_PASSED: 0")
            print("RELEASE_READINESS_AUDIT_CHECKS_WARNED: 0")
            print("RELEASE_READINESS_AUDIT_CHECKS_FAILED: 1")
            print("RELEASE_READINESS_AUDIT_CHECKS_NOT_RUN: 0")
            print("RELEASE_READINESS_AUDIT_CHECKS_NOT_IMPLEMENTED: 0")
            print(f"RELEASE_READINESS_AUDIT_REASON: Unhandled exception: {exc.__class__.__name__}")
            for line in BOUNDARY_LINES:
                print(line)
        sys.exit(1)
