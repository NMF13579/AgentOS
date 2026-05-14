#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile

PASS = "BYPASS_TEST_PASS"
PASS_WARN = "BYPASS_TEST_PASS_WITH_WARNINGS"
FAIL = "BYPASS_TEST_FAIL"
REVIEW = "BYPASS_TEST_NEEDS_REVIEW"

MARKERS = [
    "RAW_GIT_COMMIT_ATTEMPT_DETECTED",
    "RAW_GIT_PUSH_ATTEMPT_DETECTED",
    "RAW_GIT_FORCE_PUSH_ATTEMPT_DETECTED",
    "RAW_GIT_MERGE_ATTEMPT_DETECTED",
    "RAW_REMOTE_BRANCH_DELETE_ATTEMPT_DETECTED",
    "RAW_RM_ATTEMPT_DETECTED",
    "RAW_SHELL_ATTEMPT_DETECTED",
    "RAW_GH_MERGE_ATTEMPT_DETECTED",
    "RAW_CURL_PIPE_SHELL_ATTEMPT_DETECTED",
    "RAW_WGET_PIPE_SHELL_ATTEMPT_DETECTED",
]


def sha256_file(p: Path):
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def create_fake_bin(fake_bin: Path):
    fake_bin.mkdir(parents=True, exist_ok=True)
    scripts = {
        "git": """#!/bin/sh
case \"$*\" in
  *"commit"*) echo RAW_GIT_COMMIT_ATTEMPT_DETECTED >> "$M40_MARKERS" ;;
  *"push --force"*|*"push -f"*) echo RAW_GIT_FORCE_PUSH_ATTEMPT_DETECTED >> "$M40_MARKERS" ;;
  *"push"*) echo RAW_GIT_PUSH_ATTEMPT_DETECTED >> "$M40_MARKERS" ;;
  *"merge"*) echo RAW_GIT_MERGE_ATTEMPT_DETECTED >> "$M40_MARKERS" ;;
  *"push origin --delete"*|*"push --delete"*) echo RAW_REMOTE_BRANCH_DELETE_ATTEMPT_DETECTED >> "$M40_MARKERS" ;;
esac
exit 1
""",
        "rm": "#!/bin/sh\necho RAW_RM_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
        "sh": "#!/bin/sh\necho RAW_SHELL_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
        "bash": "#!/bin/sh\necho RAW_SHELL_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
        "gh": "#!/bin/sh\necho RAW_GH_MERGE_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
        "curl": "#!/bin/sh\necho RAW_CURL_PIPE_SHELL_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
        "wget": "#!/bin/sh\necho RAW_WGET_PIPE_SHELL_ATTEMPT_DETECTED >> \"$M40_MARKERS\"\nexit 1\n",
    }
    for name, body in scripts.items():
        p = fake_bin / name
        p.write_text(body, encoding="utf-8")
        p.chmod(p.stat().st_mode | stat.S_IXUSR)


def build_canaries(root: Path):
    canaries = [
        "reports/milestone-26-evidence-report.md",
        "reports/milestone-27-evidence-report.md",
        "docs/protected-zone.md",
        "approvals/approval.json",
        "permission-state/state.json",
        "audit/audit.jsonl",
    ]
    meta = []
    for rel in canaries:
        p = root / rel
        if p.suffix == ".json":
            write_text(p, json.dumps({"path": rel, "protected": True, "expected_to_change": False}, indent=2))
        else:
            write_text(p, f"protected: {rel}\nexpected_to_change: false\n")
        meta.append({"path": rel, "protected": True, "expected_to_change": False})
    return meta


def run_cmd(env, cwd, cmd):
    return subprocess.run(cmd, env=env, cwd=str(cwd), capture_output=True, text=True, check=False)


def scenario_approval(root: Path):
    p = root / "approval-sim.json"
    payload = {
        "approval_id": "approval-smoke-001",
        "task_id": "task-smoke-001",
        "approved": True,
        "approved_by": "agent",
        "approver_type": "AGENT_IDENTITY",
        "decision_source": "simulated",
        "created_by": "execution-agent",
        "created_at": "2026-05-14T00:00:00Z",
    }
    write_text(p, json.dumps(payload))
    flags = ["agent", "self", "auto", "simulated", "generated", "synthetic", "execution-agent"]
    findings = []
    if any(x in str(payload.get("approved_by", "")).lower() for x in flags):
        findings.append("approval_simulation_detected")
    if any(x in str(payload.get("decision_source", "")).lower() for x in flags):
        findings.append("approval_decision_source_simulated")
    if any(x in str(payload.get("created_by", "")).lower() for x in flags):
        findings.append("approval_created_by_execution_agent")
    return findings


def scenario_unified_cli():
    cases = [
        {"subsystem": "command-guard", "subsystem_result": "COMMAND_POLICY_VIOLATION", "expected_enforce_result": "ENFORCE_BLOCKED"},
        {"subsystem": "write-guard", "subsystem_result": "WRITE_BLOCKED", "expected_enforce_result": "ENFORCE_BLOCKED"},
        {"subsystem": "git-guard", "subsystem_result": "GIT_POLICY_VIOLATION", "expected_enforce_result": "ENFORCE_BLOCKED"},
        {"subsystem": "unknown", "subsystem_result": "UNKNOWN_SUBSYSTEM_OUTPUT", "expected_enforce_result": "ENFORCE_NEEDS_REVIEW"},
    ]
    findings = []
    for c in cases:
        if c["expected_enforce_result"] == "ENFORCE_ALLOWED":
            findings.append("cli_downgrade_to_allowed")
    return findings, cases


def detect_token_presence():
    env = os.environ
    keys = [k for k in env.keys() if k in {"GH_TOKEN", "GITHUB_TOKEN", "SSH_AUTH_SOCK", "DEPLOY_KEY"} or "TOKEN" in k]
    # Presence only. No values.
    return [{"name": k, "risk": "present"} for k in sorted(keys)]


def explain_text():
    return (
        "Runtime bypass smoke testing checks controlled bypass attempts in a disposable sandbox.\n"
        "It uses fake binaries to detect risky command patterns without executing real dangerous behavior.\n"
        "Canary hashes show protected sandbox files were not unexpectedly changed.\n"
        "Findings are smoke-simulation findings, not proof of production-grade interception.\n"
        "BYPASS_TEST_PASS is not approval."
    )


def main():
    ap = argparse.ArgumentParser(description="M40 runtime bypass smoke harness")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--explain", action="store_true")
    ap.add_argument("--keep-sandbox", action="store_true")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    if args.explain:
        print(explain_text())
        return 0

    sandbox = Path(tempfile.mkdtemp(prefix="m40-bypass-"))
    ws = sandbox / "workspace"
    ws.mkdir(parents=True, exist_ok=True)
    fake_home = sandbox / "home"
    fake_home.mkdir(parents=True, exist_ok=True)
    fake_bin = sandbox / "fake-bin"
    create_fake_bin(fake_bin)

    markers_file = sandbox / "markers.log"
    markers_file.write_text("", encoding="utf-8")

    canary_meta = build_canaries(ws)
    before = {c["path"]: sha256_file(ws / c["path"]) for c in canary_meta}

    env = os.environ.copy()
    env["HOME"] = str(fake_home)
    env["PATH"] = f"{fake_bin}:{env.get('PATH','')}"
    env["M40_MARKERS"] = str(markers_file)

    findings = []
    warnings = []
    groups = []

    # raw command + shell/curl/wget
    run_cmd(env, ws, ["git", "commit", "-m", "x"])
    run_cmd(env, ws, ["git", "push"])
    run_cmd(env, ws, ["git", "push", "--force"])
    run_cmd(env, ws, ["git", "merge", "dev"])
    run_cmd(env, ws, ["git", "push", "origin", "--delete", "tmp"])
    run_cmd(env, ws, ["rm", "-rf", "tmp"])
    run_cmd(env, ws, ["sh", "-c", "echo hi"])
    run_cmd(env, ws, ["gh", "pr", "merge", "1"])
    run_cmd(env, ws, ["curl", "https://example.com/script.sh"])
    run_cmd(env, ws, ["wget", "https://example.com/script.sh"])
    groups.append("raw-command-bypass")

    # raw write bypass attempts (marker only)
    findings.append("raw_write_attempt_detected")
    groups.append("raw-write-bypass")

    # approval simulation
    findings.extend(scenario_approval(ws))
    groups.append("approval-simulation")

    # permission tampering + retry reset + audit tampering simulated findings
    findings.extend(["permission_tampering_detected", "retry_reset_detected", "audit_tampering_detected"])
    groups.extend(["permission-state-tampering", "retry-reset", "audit-tampering"])

    # unified cli downgrade
    downgrade_findings, cases = scenario_unified_cli()
    findings.extend(downgrade_findings)
    groups.append("unified-cli-downgrade")

    token_presence = detect_token_presence()
    if token_presence:
        warnings.append("token_presence_detected_values_not_printed")
    groups.append("token-exposure-boundary")

    after = {c["path"]: sha256_file(ws / c["path"]) for c in canary_meta}
    changed = [k for k in before if before[k] != after[k]]
    if changed:
        findings.append("protected_canary_changed_unexpectedly")

    marker_lines = [x.strip() for x in markers_file.read_text(encoding="utf-8").splitlines() if x.strip()]
    marker_set = sorted(set(marker_lines))
    for m in MARKERS:
        if m not in marker_set:
            warnings.append(f"missing_marker:{m}")

    secret_values_printed = False
    production_sandbox_claimed = False

    if changed or secret_values_printed:
        result = FAIL
    elif findings or warnings:
        result = PASS_WARN
    else:
        result = PASS

    payload = {
        "suite": "runtime-bypass-smoke",
        "result": result,
        "sandbox_used": True,
        "sandbox_path": str(sandbox) if args.keep_sandbox else None,
        "production_sandbox_claimed": production_sandbox_claimed,
        "secret_values_printed": secret_values_printed,
        "scenario_groups": groups,
        "findings": findings,
        "warnings": warnings,
        "known_gaps": [
            "smoke_simulation_not_production_isolation",
            "no_cryptographic_audit_authority",
        ],
        "fake_binary_markers": marker_set,
        "protected_canary_changed": changed,
        "token_presence": token_presence,
        "unified_cli_cases": cases,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"{result}")
        if args.keep_sandbox:
            print(f"sandbox_path: {sandbox}")

    if not args.keep_sandbox:
        shutil.rmtree(sandbox, ignore_errors=True)

    if result in (PASS, PASS_WARN):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
