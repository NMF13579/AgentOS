#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

VIOLATION_CATEGORIES = {
    "SCOPE_VIOLATION",
    "FORBIDDEN_COMMAND",
    "FORBIDDEN_WRITE",
    "UNAPPROVED_PUSH",
    "DIRECT_PROTECTED_BRANCH_PUSH",
    "FORCE_PUSH_ATTEMPT",
    "REMOTE_BRANCH_DELETE_ATTEMPT",
    "VALIDATION_BYPASS",
    "EVIDENCE_TAMPERING",
    "PERMISSION_ESCALATION_ATTEMPT",
    "APPROVAL_SIMULATION",
    "AUTO_MERGE_ATTEMPT",
    "REPEATED_FAILURE",
    "UNBOUNDED_RETRY",
    "HUMAN_IMPERSONATION",
    "AGENT_ADMIN_TOKEN_EXPOSURE",
    "RUNNER_CREDENTIAL_LEAK",
    "UNKNOWN_VIOLATION",
}
SEVERITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL", "UNKNOWN"}
SANCTIONS = {
    "RECORD_ONLY",
    "REQUIRE_HUMAN_REVIEW",
    "REDUCE_TO_READ_ONLY",
    "BLOCK_TASK",
    "RESET_TO_LAST_SAFE_STATE",
    "RETRY_WITH_REDUCED_PERMISSIONS",
    "ESCALATE_TO_OWNER",
    "DISALLOW_AUTOPILOT",
    "BLOCK_AGENT",
}

REQUIRED_FIELDS = [
    "schema_version",
    "violation_id",
    "task_id",
    "agent_id",
    "violation_category",
    "severity",
    "detected_at",
    "detected_by",
    "evidence",
    "attempted_action",
    "policy_reference",
    "current_permission",
    "requested_permission",
    "open_state",
    "prior_attempts",
    "non_authorization_warning",
]

EXIT0 = {"SANCTION_REQUIRED", "SANCTION_APPLIED"}


def emit(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def load_json(path: str):
    p = Path(path)
    if not p.exists():
        return None, "VIOLATION_INVALID", "file missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None, "VIOLATION_INVALID", "invalid json"
    if not isinstance(data, dict):
        return None, "VIOLATION_INVALID", "record must be object"
    return data, None, None


def parse_result(stdout: str):
    for line in stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def validate_permission_state(path: str):
    script = Path("scripts/agentos-permission-state.py")
    if not script.exists():
        return "PERMISSION_INVALID", "permission checker missing"
    try:
        run = subprocess.run(
            ["python3", "scripts/agentos-permission-state.py", "validate", path],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except Exception:
        return "PERMISSION_INVALID", "permission check failed"
    res = parse_result(run.stdout or "")
    if res == "PERMISSION_OK":
        return "PERMISSION_OK", "permission state valid"
    if res == "PERMISSION_BLOCKED":
        return "TASK_BLOCKED", "permission already blocked"
    return "PERMISSION_INVALID", "permission state invalid"


def validate_human_gate(path: str):
    script = Path("scripts/agentos-human-gate.py")
    if not script.exists():
        return "NEEDS_HUMAN_REVIEW", "human gate checker missing"
    try:
        run = subprocess.run(
            ["python3", "scripts/agentos-human-gate.py", "validate", path],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except Exception:
        return "NEEDS_HUMAN_REVIEW", "human gate validation failed"
    res = parse_result(run.stdout or "")
    if res == "HUMAN_GATE_APPROVED":
        return "OK", "human gate approved"
    return "NEEDS_HUMAN_REVIEW", "human gate not approved"


def append_audit(audit_log: str, violation: dict, sanctions: list, result: str):
    script = Path("scripts/agentos-audit-log.py")
    if not script.exists():
        return False, "audit script missing"
    payload = {
        "violation_id": violation.get("violation_id"),
        "violation_category": violation.get("violation_category"),
        "severity": violation.get("severity"),
        "sanctions": sanctions,
        "result": result,
    }
    cmd = [
        "python3",
        "scripts/agentos-audit-log.py",
        "append",
        audit_log,
        "--actor-id",
        "runtime-system",
        "--actor-type",
        "RUNTIME_SYSTEM_IDENTITY",
        "--action-type",
        "VIOLATION_DECISION",
        "--task-id",
        str(violation.get("task_id", "unknown")),
        "--decision",
        result,
        "--reason",
        "violation enforcement decision",
        "--payload-json",
        json.dumps(payload, ensure_ascii=True),
    ]
    try:
        run = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=12)
    except Exception:
        return False, "audit append failed"
    r = parse_result(run.stdout or "")
    return (r == "AUDIT_APPENDED"), (run.stdout.strip() or run.stderr.strip() or "audit append failed")


def detect_forbidden_attempts(v: dict):
    action = str(v.get("attempted_action", "")).lower()
    if "clear violation" in action or "clear_violation" in action:
        return "NEEDS_OWNER_REVIEW", "self-clear attempt detected"
    if "downgrade" in action and "severity" in action:
        return "NEEDS_OWNER_REVIEW", "severity downgrade attempt detected"
    if "false positive" in action or "false_positive" in action:
        return "NEEDS_OWNER_REVIEW", "false-positive marking attempt detected"
    return None, None


def map_sanctions(category: str, severity: str):
    sanctions = []

    if severity == "LOW":
        sanctions.append("RECORD_ONLY")
    elif severity == "MEDIUM":
        sanctions.append("REQUIRE_HUMAN_REVIEW")
    elif severity == "HIGH":
        sanctions.extend(["REDUCE_TO_READ_ONLY", "REQUIRE_HUMAN_REVIEW"])
    elif severity == "CRITICAL":
        sanctions.extend(["BLOCK_TASK", "ESCALATE_TO_OWNER"])
    else:
        return None

    if category == "UNBOUNDED_RETRY":
        if "DISALLOW_AUTOPILOT" not in sanctions:
            sanctions.append("DISALLOW_AUTOPILOT")
        if "REQUIRE_HUMAN_REVIEW" not in sanctions:
            sanctions.append("REQUIRE_HUMAN_REVIEW")

    if category in {"EVIDENCE_TAMPERING", "APPROVAL_SIMULATION", "HUMAN_IMPERSONATION", "AGENT_ADMIN_TOKEN_EXPOSURE", "DIRECT_PROTECTED_BRANCH_PUSH"}:
        sanctions = ["BLOCK_TASK", "ESCALATE_TO_OWNER"]

    if category == "RUNNER_CREDENTIAL_LEAK":
        sanctions = ["BLOCK_AGENT", "ESCALATE_TO_OWNER"]

    if category == "FORCE_PUSH_ATTEMPT" and severity not in {"HIGH", "CRITICAL"}:
        sanctions = ["REQUIRE_HUMAN_REVIEW", "DISALLOW_AUTOPILOT"]

    dedup = []
    for s in sanctions:
        if s not in dedup:
            dedup.append(s)
    return dedup


def compute_result(sanctions: list):
    if "BLOCK_AGENT" in sanctions:
        return "AGENT_BLOCKED", "critical sanction requires blocking agent"
    if "BLOCK_TASK" in sanctions:
        return "TASK_BLOCKED", "critical sanction requires blocking task"
    return "SANCTION_REQUIRED", "sanction computed"


def apply_state(violation: dict, sanctions: list, state_in: dict):
    out = json.loads(json.dumps(state_in))
    out.setdefault("open_violations", [])
    if violation["violation_id"] not in out["open_violations"]:
        out["open_violations"].append(violation["violation_id"])

    if "BLOCK_AGENT" in sanctions or "BLOCK_TASK" in sanctions:
        out["blocked_state"] = True
        out["current_permission"] = "BLOCKED"
    elif "REDUCE_TO_READ_ONLY" in sanctions:
        out["current_permission"] = "READ_ONLY"

    # never increase permission, never reset retry_count
    return out


def evaluate_core(v: dict):
    for f in REQUIRED_FIELDS:
        if f not in v:
            return None, "VIOLATION_INVALID", f"missing required field: {f}"

    if v["violation_category"] not in VIOLATION_CATEGORIES:
        return None, "VIOLATION_NEEDS_REVIEW", "unknown violation category"
    if v["severity"] not in SEVERITIES:
        return None, "VIOLATION_NEEDS_REVIEW", "unknown severity"

    if v["open_state"] is False:
        return None, "VIOLATION_NEEDS_REVIEW", "closed violation requires owner/human resolution evidence"

    fr, rr = detect_forbidden_attempts(v)
    if fr:
        return None, fr, rr

    # category-severity hard rules
    if v["violation_category"] in {"EVIDENCE_TAMPERING", "APPROVAL_SIMULATION", "HUMAN_IMPERSONATION", "AGENT_ADMIN_TOKEN_EXPOSURE", "DIRECT_PROTECTED_BRANCH_PUSH"} and v["severity"] != "CRITICAL":
        return None, "VIOLATION_NEEDS_REVIEW", "category requires CRITICAL severity"

    sanctions = map_sanctions(v["violation_category"], v["severity"])
    if not sanctions:
        return None, "VIOLATION_NEEDS_REVIEW", "failed to map sanctions"

    result, reason = compute_result(sanctions)
    return sanctions, result, reason


def cmd_show_sanctions(as_json=False):
    mapping = {
        "LOW": ["RECORD_ONLY"],
        "MEDIUM": ["REQUIRE_HUMAN_REVIEW"],
        "HIGH": ["REDUCE_TO_READ_ONLY", "REQUIRE_HUMAN_REVIEW"],
        "CRITICAL": ["BLOCK_TASK", "ESCALATE_TO_OWNER"],
    }
    if as_json:
        print(json.dumps(mapping, ensure_ascii=True))
    else:
        for k, v in mapping.items():
            print(f"{k}: {', '.join(v)}")
    emit("SANCTION_REQUIRED", "sanction map shown", as_json)
    return 0


def main():
    parser = argparse.ArgumentParser(description="M27 violation enforcement runtime")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pe = sub.add_parser("evaluate")
    pe.add_argument("--violation", required=True)
    pe.add_argument("--permission-state")
    pe.add_argument("--human-gate-record")
    pe.add_argument("--audit-log")

    pa = sub.add_parser("apply")
    pa.add_argument("--violation", required=True)
    pa.add_argument("--permission-state", required=True)
    pa.add_argument("--state-out")
    pa.add_argument("--human-gate-record")
    pa.add_argument("--audit-log")

    sub.add_parser("show-sanctions")

    args = parser.parse_args()

    if args.cmd == "show-sanctions":
        return cmd_show_sanctions(args.json)

    v, er, rs = load_json(args.violation)
    if er:
        emit(er, rs, args.json)
        return 1

    sanctions, result, reason = evaluate_core(v)
    if sanctions is None:
        emit(result, reason, args.json)
        return 1

    if args.permission_state:
        ps, pr = validate_permission_state(args.permission_state)
        if ps == "TASK_BLOCKED":
            emit("TASK_BLOCKED", pr, args.json)
            return 1
        if ps != "PERMISSION_OK":
            emit("PERMISSION_INVALID", pr, args.json)
            return 1

    if args.human_gate_record:
        hs, hr = validate_human_gate(args.human_gate_record)
        if hs != "OK":
            emit("NEEDS_HUMAN_REVIEW", hr, args.json)
            return 1

    if args.cmd == "evaluate":
        final_res = result
        final_reason = reason
        if final_res == "NEEDS_OWNER_REVIEW" and "ESCALATE_TO_OWNER" in sanctions:
            final_reason = "owner review required"

        if args.audit_log:
            ok, audit_msg = append_audit(args.audit_log, v, sanctions, final_res)
            if not ok:
                emit("VIOLATION_NEEDS_REVIEW", f"audit append failed: {audit_msg}", args.json)
                return 1
        emit(final_res, final_reason, args.json)
        return 0 if final_res in EXIT0 else 1

    # apply path
    if not args.state_out:
        emit("VIOLATION_INVALID", "apply requires --state-out", args.json)
        return 1

    state_in, ser, srs = load_json(args.permission_state)
    if ser:
        emit("PERMISSION_INVALID", "input permission state missing/invalid", args.json)
        return 1

    new_state = apply_state(v, sanctions, state_in)
    outp = Path(args.state_out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(new_state, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    final_res = "SANCTION_APPLIED"
    final_reason = "sanction state written"
    if "BLOCK_AGENT" in sanctions:
        final_res = "AGENT_BLOCKED"
        final_reason = "agent blocked state written"
    elif "BLOCK_TASK" in sanctions:
        final_res = "TASK_BLOCKED"
        final_reason = "task blocked state written"

    if args.audit_log:
        ok, audit_msg = append_audit(args.audit_log, v, sanctions, final_res)
        if not ok:
            emit("VIOLATION_NEEDS_REVIEW", f"audit append failed: {audit_msg}", args.json)
            return 1

    emit(final_res, final_reason, args.json)
    return 0 if final_res in EXIT0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
