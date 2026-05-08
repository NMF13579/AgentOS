#!/usr/bin/env python3
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REASONS = {
    "TASK_FAILURE",
    "VALIDATION_FAILURE",
    "SAME_FAILURE",
    "WARNING",
    "VIOLATION",
    "CRITICAL_VIOLATION",
    "BLOCKED_STATE",
    "HUMAN_REVIEW_RETRY",
    "OWNER_RESTORATION_RETRY",
    "UNKNOWN_REASON",
}

REQUIRED_FIELDS = [
    "schema_version",
    "retry_id",
    "task_id",
    "agent_id",
    "retry_reason",
    "failure_type",
    "failure_signature",
    "attempt_number",
    "retry_count",
    "same_failure_count",
    "prior_warning",
    "prior_violation",
    "prior_critical_violation",
    "blocked_state",
    "requested_permission",
    "current_permission",
    "previous_task_id",
    "created_at",
    "last_attempt_at",
    "non_authorization_warning",
]

EXIT0 = {"RETRY_ALLOWED"}


def emit(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def parse_iso(value: str):
    if value is None:
        return None
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(value)
    except Exception:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def get_now(override: str):
    if not override:
        return datetime.now(timezone.utc), None
    dt = parse_iso(override)
    if dt is None:
        return None, "invalid --now value"
    return dt, None


def load_json(path: str):
    p = Path(path)
    if not p.exists():
        return None, "RETRY_INVALID", "file missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None, "RETRY_INVALID", "invalid json"
    if not isinstance(data, dict):
        return None, "RETRY_INVALID", "record must be object"
    return data, None, None


def parse_result(stdout: str):
    for line in stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def validate_permission(path: str):
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
        return "PERMISSION_INVALID", "permission validation failed"

    res = parse_result(run.stdout or "")
    if res == "PERMISSION_OK":
        return "PERMISSION_OK", "permission state valid"
    if res == "PERMISSION_BLOCKED":
        return "PERMISSION_BLOCKED", "permission is blocked"
    if res == "PERMISSION_DENIED":
        return "PERMISSION_DENIED", "permission denied"
    return "PERMISSION_INVALID", "permission state invalid"


def validate_human_gate(path: str):
    script = Path("scripts/agentos-human-gate.py")
    if not script.exists():
        return "RETRY_NEEDS_HUMAN_REVIEW", "human gate checker missing"
    try:
        run = subprocess.run(
            ["python3", "scripts/agentos-human-gate.py", "validate", path],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except Exception:
        return "RETRY_NEEDS_HUMAN_REVIEW", "human gate validation failed"
    res = parse_result(run.stdout or "")
    if res == "HUMAN_GATE_APPROVED":
        return "OK", "human gate approved"
    return "RETRY_NEEDS_HUMAN_REVIEW", "human gate not approved"


def append_audit(audit_log: str, rec: dict, result: str):
    script = Path("scripts/agentos-audit-log.py")
    if not script.exists():
        return False, "audit script missing"
    payload = {
        "retry_id": rec.get("retry_id"),
        "retry_reason": rec.get("retry_reason"),
        "retry_count": rec.get("retry_count"),
        "same_failure_count": rec.get("same_failure_count"),
        "result": result,
    }
    cmd = [
        "python3", "scripts/agentos-audit-log.py", "append", audit_log,
        "--actor-id", "runtime-system",
        "--actor-type", "RUNTIME_SYSTEM_IDENTITY",
        "--action-type", "RETRY_DECISION",
        "--task-id", str(rec.get("task_id", "unknown")),
        "--decision", result,
        "--reason", "retry enforcement decision",
        "--payload-json", json.dumps(payload, ensure_ascii=True),
    ]
    try:
        run = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=12)
    except Exception:
        return False, "audit append failed"
    res = parse_result(run.stdout or "")
    return res == "AUDIT_APPENDED", (run.stdout.strip() or run.stderr.strip() or "audit append failed")


def evaluate_retry(rec: dict, human_gate_ok: bool, now_dt: datetime):
    for f in REQUIRED_FIELDS:
        if f not in rec:
            return "RETRY_INVALID", f"missing required field: {f}"

    if rec["retry_reason"] not in REASONS:
        return "RETRY_INVALID", "unknown retry_reason"

    if rec["failure_type"] in (None, "", "UNKNOWN"):
        return "RETRY_INVALID", "ambiguous failure_type"

    if rec["retry_reason"] == "SAME_FAILURE" and not rec.get("failure_signature"):
        return "RETRY_INVALID", "missing failure_signature for SAME_FAILURE"

    if not isinstance(rec["retry_count"], int) or rec["retry_count"] < 0:
        return "RETRY_INVALID", "retry_count must be integer >= 0"
    if not isinstance(rec["same_failure_count"], int) or rec["same_failure_count"] < 0:
        return "RETRY_INVALID", "same_failure_count must be integer >= 0"
    if not isinstance(rec["attempt_number"], int) or rec["attempt_number"] < 1:
        return "RETRY_INVALID", "attempt_number must be integer >= 1"

    if rec["attempt_number"] != rec["retry_count"] + 1:
        return "RETRY_INVALID", "attempt_number inconsistent with retry_count"

    # Optional time-based retry window.
    retry_window_seconds = rec.get("retry_window_seconds")
    if retry_window_seconds is not None:
        if not isinstance(retry_window_seconds, int) or retry_window_seconds <= 0:
            return "RETRY_INVALID", "retry_window_seconds must be integer > 0"
        last_attempt = parse_iso(rec.get("last_attempt_at"))
        if last_attempt is None:
            return "RETRY_INVALID", "invalid last_attempt_at"
        window_end = last_attempt.timestamp() + retry_window_seconds
        if now_dt.timestamp() >= window_end:
            return "RETRY_WINDOW_EXPIRED", "retry window expired"

    # reset detection using previous_task_id convention in fixtures
    if rec["retry_count"] < int(rec.get("prior_retry_count", rec["retry_count"])):
        return "RETRY_POLICY_VIOLATION", "retry_count reset attempt detected"
    if rec["same_failure_count"] < int(rec.get("prior_same_failure_count", rec["same_failure_count"])):
        return "RETRY_POLICY_VIOLATION", "same_failure_count reset attempt detected"
    if rec.get("previous_task_id") and rec.get("previous_task_id") != rec.get("task_id") and rec.get("failure_signature") == rec.get("prior_failure_signature", rec.get("failure_signature")):
        return "RETRY_POLICY_VIOLATION", "new-task reset attempt detected"

    if rec["retry_count"] >= 3:
        return "RETRY_EXHAUSTED", "max attempts per task reached"
    if rec["same_failure_count"] >= 2:
        return "RETRY_EXHAUSTED", "same failure limit reached"

    if rec["prior_critical_violation"] is True:
        return "RETRY_NEEDS_OWNER_REVIEW", "critical violation requires owner/admin gate"

    if rec["blocked_state"] is True or rec["retry_reason"] == "BLOCKED_STATE":
        return "RETRY_NEEDS_OWNER_REVIEW", "blocked state requires owner/admin gate"

    if rec["prior_warning"] is True and rec["retry_count"] >= 1 and not human_gate_ok:
        return "RETRY_NEEDS_HUMAN_REVIEW", "warning retry requires human review"

    if rec["prior_violation"] is True:
        if rec["requested_permission"] in {"COMMIT_REQUEST", "PUSH_REQUEST"} and not human_gate_ok:
            if rec["requested_permission"] == "PUSH_REQUEST":
                return "RETRY_NEEDS_OWNER_REVIEW", "push retry after violation requires owner/admin gate"
            return "RETRY_NEEDS_HUMAN_REVIEW", "commit retry after violation requires human gate"
        if not human_gate_ok:
            return "RETRY_BLOCKED", "retry after violation blocked without human gate"

    return "RETRY_ALLOWED", "retry permitted within bounds"


def apply_state(permission_state: dict, retry_record: dict):
    out = json.loads(json.dumps(permission_state))
    out["retry_count"] = retry_record["retry_count"] + 1
    return out


def show_limits(as_json=False):
    limits = {
        "max_attempts_per_task": 3,
        "same_failure_max": 2,
        "after_warning_without_human_review": 1,
        "after_violation_without_human_review": 0,
        "after_critical_violation": 0,
        "after_blocked_state_without_owner_review": 0,
    }
    if as_json:
        print(json.dumps(limits, ensure_ascii=True))
    else:
        for k, v in limits.items():
            print(f"{k}: {v}")
    emit("RETRY_ALLOWED", "limits shown", as_json)
    return 0


def main():
    parser = argparse.ArgumentParser(description="M27 retry enforcement runtime")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--now")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pcheck = sub.add_parser("check")
    pcheck.add_argument("--retry-record", required=True)
    pcheck.add_argument("--permission-state")
    pcheck.add_argument("--human-gate-record")
    pcheck.add_argument("--audit-log")

    papply = sub.add_parser("apply")
    papply.add_argument("--retry-record", required=True)
    papply.add_argument("--permission-state", required=True)
    papply.add_argument("--state-out")
    papply.add_argument("--human-gate-record")
    papply.add_argument("--audit-log")

    sub.add_parser("show-limits")

    args = parser.parse_args()

    now_dt, now_err = get_now(args.now)
    if now_err:
        emit("RETRY_INVALID", now_err, args.json)
        return 1
    _ = now_dt  # reserved for future cooldown/window checks

    if args.cmd == "show-limits":
        return show_limits(args.json)

    rec, er, rs = load_json(args.retry_record)
    if er:
        emit(er, rs, args.json)
        return 1

    human_gate_ok = False
    if args.human_gate_record:
        hr, hreason = validate_human_gate(args.human_gate_record)
        if hr == "OK":
            human_gate_ok = True
        else:
            emit(hr, hreason, args.json)
            return 1

    if args.permission_state:
        pr, preason = validate_permission(args.permission_state)
        if pr == "PERMISSION_BLOCKED":
            emit("PERMISSION_BLOCKED", preason, args.json)
            return 1
        if pr != "PERMISSION_OK":
            emit("PERMISSION_INVALID", preason, args.json)
            return 1

    result, reason = evaluate_retry(rec, human_gate_ok, now_dt)

    if args.cmd == "check":
        if args.audit_log:
            ok, msg = append_audit(args.audit_log, rec, result)
            if not ok:
                emit("RETRY_NEEDS_HUMAN_REVIEW", f"audit append failed: {msg}", args.json)
                return 1
        emit(result, reason, args.json)
        return 0 if result in EXIT0 else 1

    # apply
    if not args.state_out:
        emit("RETRY_INVALID", "apply requires --state-out", args.json)
        return 1

    if result != "RETRY_ALLOWED":
        emit(result, reason, args.json)
        return 1

    pst, per, prs = load_json(args.permission_state)
    if per:
        emit("PERMISSION_INVALID", "input permission state missing/invalid", args.json)
        return 1

    new_state = apply_state(pst, rec)
    out = Path(args.state_out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(new_state, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    if args.audit_log:
        ok, msg = append_audit(args.audit_log, rec, "RETRY_ALLOWED")
        if not ok:
            emit("RETRY_NEEDS_HUMAN_REVIEW", f"audit append failed: {msg}", args.json)
            return 1

    emit("RETRY_ALLOWED", "retry allowed and state-out written", args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
