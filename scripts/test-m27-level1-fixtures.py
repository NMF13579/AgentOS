#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

RESULT_PASS = "LEVEL_1_SMOKE_PASS"
RESULT_PASS_WARN = "LEVEL_1_SMOKE_PASS_WITH_WARNINGS"
RESULT_FAIL = "LEVEL_1_SMOKE_FAIL"
RESULT_REVIEW = "LEVEL_1_SMOKE_NEEDS_REVIEW"

REQUIRED_SCRIPTS = [
    "scripts/agentos-permission-state.py",
    "scripts/agentos-command-guard.py",
    "scripts/agentos-write-guard.py",
    "scripts/agentos-git-guard.py",
    "scripts/agentos-human-gate.py",
    "scripts/agentos-audit-log.py",
    "scripts/agentos-violation-enforce.py",
    "scripts/agentos-retry-enforce.py",
    "scripts/agentos-enforce.py",
]

ALLOWED_RESULTS = {
    "PERMISSION_OK",
    "COMMAND_ALLOWED",
    "WRITE_ALLOWED",
    "GIT_ALLOWED",
    "HUMAN_GATE_APPROVED",
    "AUDIT_OK",
    "RETRY_ALLOWED",
    "ENFORCE_ALLOWED",
}

BLOCK_RESULTS = {
    "COMMAND_BLOCKED",
    "COMMAND_POLICY_VIOLATION",
    "COMMAND_NEEDS_APPROVAL",
    "COMMAND_NEEDS_REVIEW",
    "WRITE_BLOCKED",
    "WRITE_POLICY_VIOLATION",
    "WRITE_NEEDS_APPROVAL",
    "WRITE_NEEDS_REVIEW",
    "GIT_BLOCKED",
    "GIT_POLICY_VIOLATION",
    "GIT_NEEDS_REVIEW",
    "TASK_BLOCKED",
    "AGENT_BLOCKED",
    "RETRY_BLOCKED",
    "RETRY_EXHAUSTED",
    "RETRY_NEEDS_OWNER_REVIEW",
    "NEEDS_OWNER_REVIEW",
    "PERMISSION_BLOCKED",
    "HUMAN_GATE_SIMULATED",
    "AUDIT_TAMPERED",
    "ENFORCE_BLOCKED",
    "ENFORCE_POLICY_VIOLATION",
    "ENFORCE_NEEDS_REVIEW",
}


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


def parse_result(stdout: str):
    for line in stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def run_cmd(cmd, cwd):
    try:
        run = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=False, timeout=20)
    except subprocess.TimeoutExpired:
        return None, 1, "timeout"
    except Exception as e:
        return None, 1, str(e)
    r = parse_result(run.stdout or "")
    return r, run.returncode, (run.stdout.strip() or run.stderr.strip() or "")


def build_cases(repo_root: Path, fixture_root: Path):
    p = fixture_root
    valid_audit = repo_root / "tests/fixtures/immutable-audit-log/valid-two-record-chain/audit.jsonl"
    tampered_audit = repo_root / "tests/fixtures/immutable-audit-log/tampered-payload/audit.jsonl"
    return [
        ("permission-state-read-only-ok", ["python3", "scripts/agentos-permission-state.py", "validate", str(p / "permission/valid-read-only.json")], "PERMISSION_OK", 0),
        ("safe-read-command-allowed", ["python3", "scripts/agentos-command-guard.py", "check", "--category", "SAFE_READ", "--command", "git status"], "COMMAND_ALLOWED", 0),
        ("safe-validate-command-allowed", ["python3", "scripts/agentos-command-guard.py", "check", "--category", "SAFE_VALIDATE", "--command", "python3 -V"], "COMMAND_ALLOWED", 0),
        ("in-scope-write-allowed", ["python3", "scripts/agentos-write-guard.py", "check", "--path", "docs/example.md", "--operation", "modify", "--path-class", "ALLOWED_WRITE_PATH"], "WRITE_ALLOWED", 0),
        ("status-git-check-allowed", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "status", "--target", "local"], "GIT_ALLOWED", 0),
        ("human-gate-approved-valid", ["python3", "scripts/agentos-human-gate.py", "validate", str(p / "human-gate/approved.json")], "HUMAN_GATE_APPROVED", 0),
        ("audit-valid-chain-ok", ["python3", "scripts/agentos-audit-log.py", "validate", str(valid_audit)], "AUDIT_OK", 0),
        ("retry-first-failure-allowed", ["python3", "scripts/agentos-retry-enforce.py", "check", "--retry-record", str(p / "retry/first-allowed.json")], "RETRY_ALLOWED", 0),
        ("unified-cli-safe-command-allowed", ["python3", "scripts/agentos-enforce.py", "check-command", "--category", "SAFE_READ", "--command", "git status"], "ENFORCE_ALLOWED", 0),

        ("command-forbidden-blocked", ["python3", "scripts/agentos-command-guard.py", "check", "--category", "FORBIDDEN", "--command", "rm -rf /"], "COMMAND_POLICY_VIOLATION", 1),
        ("command-unknown-needs-review", ["python3", "scripts/agentos-command-guard.py", "check", "--category", "UNKNOWN", "--command", "something"], "COMMAND_NEEDS_REVIEW", 1),
        ("dangerous-command-without-approval-blocked", ["python3", "scripts/agentos-command-guard.py", "check", "--category", "DANGEROUS", "--command", "rm -rf tmp"], "COMMAND_NEEDS_APPROVAL", 1),
        ("write-out-of-scope-blocked", ["python3", "scripts/agentos-write-guard.py", "check", "--path", "unknown/file.md", "--operation", "modify", "--path-class", "UNKNOWN_PATH"], "WRITE_NEEDS_REVIEW", 1),
        ("write-evidence-artifact-blocked", ["python3", "scripts/agentos-write-guard.py", "check", "--path", "reports/milestone-26-evidence-report.md", "--operation", "modify", "--path-class", "EVIDENCE_ARTIFACT"], "WRITE_POLICY_VIOLATION", 1),
        ("write-protected-zone-needs-approval", ["python3", "scripts/agentos-write-guard.py", "check", "--path", "core-rules/MAIN.md", "--operation", "modify", "--path-class", "PROTECTED_ZONE"], "WRITE_NEEDS_APPROVAL", 1),
        ("commit-without-preconditions-blocked", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "commit", "--target", "local", "--commit-message", "feat: x", "--task-id", "27.15.1"], "GIT_NEEDS_REVIEW", 1),
        ("push-without-approval-blocked", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "push", "--target", "feature_branch", "--branch", "feature/x"], "GIT_NEEDS_REVIEW", 1),
        ("push-to-dev-blocked", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "push", "--target", "dev", "--branch", "dev"], "GIT_POLICY_VIOLATION", 1),
        ("force-push-blocked", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "force-push", "--target", "feature_branch", "--branch", "feature/x"], "GIT_POLICY_VIOLATION", 1),
        ("remote-branch-delete-blocked", ["python3", "scripts/agentos-git-guard.py", "check", "--action", "remote-delete", "--target", "feature_branch", "--branch", "feature/x"], "GIT_POLICY_VIOLATION", 1),
        ("retry-after-critical-blocked", ["python3", "scripts/agentos-retry-enforce.py", "check", "--retry-record", str(p / "retry/critical-blocked.json")], "RETRY_NEEDS_OWNER_REVIEW", 1),
        ("retry-count-exhausted", ["python3", "scripts/agentos-retry-enforce.py", "check", "--retry-record", str(p / "retry/exhausted.json")], "RETRY_EXHAUSTED", 1),
        ("agent-self-clears-violation-blocked", ["python3", "scripts/agentos-violation-enforce.py", "evaluate", "--violation", str(p / "violation/self-clear.json")], "NEEDS_OWNER_REVIEW", 1),
        ("permission-escalation-without-record-blocked", ["python3", "scripts/agentos-violation-enforce.py", "evaluate", "--violation", str(p / "violation/perm-escalation.json")], "SANCTION_REQUIRED", 0),
        ("blocked-permission-denies-action", ["python3", "scripts/agentos-permission-state.py", "validate", str(p / "permission/blocked.json")], "PERMISSION_BLOCKED", 1),
        ("human-gate-self-approval-simulated", ["python3", "scripts/agentos-human-gate.py", "validate", str(p / "human-gate/self-simulated.json")], "HUMAN_GATE_SIMULATED", 1),
        ("audit-tampered-payload-detected", ["python3", "scripts/agentos-audit-log.py", "validate", str(tampered_audit)], "AUDIT_TAMPERED", 1),
        ("unified-cli-blocked-command-blocked", ["python3", "scripts/agentos-enforce.py", "check-command", "--category", "FORBIDDEN", "--command", "rm -rf /"], "ENFORCE_POLICY_VIOLATION", 1),
        ("level2-disabled-does-not-fail-level1", ["python3", "scripts/check-github-platform-enforcement.py", "check", "--level-2-enabled", "false"], "SKIPPED_LEVEL_2_NOT_ENABLED", 0),
    ]


def main():
    ap = argparse.ArgumentParser(description="M27 Level 1 smoke fixtures runner")
    ap.add_argument("--root", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--explain", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    details = []

    # support both:
    # 1) --root <repo-root>
    # 2) --root tests/fixtures/m27-level1
    if (root / "scripts").exists():
        repo_root = root
    else:
        repo_root = Path(__file__).resolve().parents[1]
    fixture_root = root if (root / "permission").exists() else (repo_root / "tests/fixtures/m27-level1")

    # required scripts existence
    for rel in REQUIRED_SCRIPTS:
        if not (repo_root / rel).exists():
            emit(RESULT_FAIL, f"missing required script: {rel}", details, args.json)
            return 1

    cases = build_cases(repo_root, fixture_root)
    if not cases:
        emit(RESULT_REVIEW, "unsupported fixture shape", details, args.json)
        return 1

    failures = []
    warnings = []
    for name, cmd, exp_res, exp_code in cases:
        res, code, out = run_cmd(cmd, repo_root)
        if res is None:
            failures.append(f"{name}: no RESULT parsed ({out[:120]})")
            continue
        if res != exp_res or code != exp_code:
            failures.append(f"{name}: expected ({exp_res},{exp_code}) got ({res},{code})")
            continue
        # sanity checks to avoid unexpected allow on unsafe names
        unsafe_keywords = ["forbidden", "blocked", "needs-review", "critical", "tampered", "self-approval"]
        if any(k in name for k in unsafe_keywords) and res in ALLOWED_RESULTS:
            failures.append(f"{name}: unsafe case returned allowed result {res}")

    if failures:
        emit(RESULT_FAIL, "one or more smoke cases failed", failures, args.json)
        return 1

    if warnings:
        emit(RESULT_PASS_WARN, "smoke passed with warnings", warnings, args.json)
        return 0

    emit(RESULT_PASS, "all smoke cases passed", details if args.explain else [], args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
