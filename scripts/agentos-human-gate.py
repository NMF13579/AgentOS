#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

DECISIONS = {"APPROVED", "REJECTED", "NEEDS_CLARIFICATION", "EXPIRED", "INVALID", "SIMULATED", "UNKNOWN"}
REQUIRED_FOR = {
    "DANGEROUS_COMMAND",
    "PROTECTED_ZONE_WRITE",
    "EVIDENCE_ARTIFACT_ACCESS",
    "COMMIT_REQUEST_ESCALATION",
    "PUSH_REQUEST_ESCALATION",
    "PUSH_APPROVAL",
    "RETRY_AFTER_VIOLATION",
    "EXIT_FROM_BLOCKED",
    "M25_OVERRIDE",
    "BRANCH_PROTECTION_OR_WORKFLOW_MODIFICATION",
    "TOKEN_SCOPE_ESCALATION",
    "IDENTITY_BOUNDARY_EXCEPTION",
    "VIOLATION_SEVERITY_REDUCTION",
    "PERMISSION_RESTORATION_AFTER_VIOLATION",
    "MERGE_APPROVAL",
}
ALLOWED_DECIDER_TYPES = {"HUMAN_REVIEWER_IDENTITY", "OWNER_ADMIN_IDENTITY"}
FORBIDDEN_DECIDER_TYPES = {"AGENT_IDENTITY", "RUNTIME_SYSTEM_IDENTITY", "UNKNOWN_IDENTITY"}
SIM_WORDS = ["agent", "self", "auto", "simulated", "generated", "synthetic"]

REQUIRED_FIELDS = [
    "schema_version", "gate_id", "task_id", "agent_id", "required_for", "requested_action",
    "reason", "decision", "requested_at", "decided_at", "expires_at", "human_decider_id",
    "human_decider_type", "decision_source", "scope", "non_authorization_warning"
]


def emit(result, reason, as_json=False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def parse_iso(value):
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


def now_utc(override):
    if override is None:
        return datetime.now(timezone.utc), None
    dt = parse_iso(override)
    if dt is None:
        return None, "invalid --now value"
    return dt, None


def load_record(path):
    p = Path(path)
    if not p.exists():
        return None, "HUMAN_GATE_INVALID", "record file missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None, "HUMAN_GATE_INVALID", "record file invalid json"
    if not isinstance(data, dict):
        return None, "HUMAN_GATE_INVALID", "record must be object"
    return data, None, None


def simulated(record):
    decider_type = record.get("human_decider_type")
    agent_id = record.get("agent_id")
    decider_id = record.get("human_decider_id")
    source = str(record.get("decision_source", "")).lower()

    if decider_type in FORBIDDEN_DECIDER_TYPES:
        return True, "forbidden human_decider_type indicates simulation"
    if decider_type == "AGENT_IDENTITY":
        return True, "agent decider type indicates simulation"
    if decider_id and agent_id and str(decider_id) == str(agent_id):
        return True, "agent_id equals human_decider_id"
    if any(w in source for w in SIM_WORDS):
        return True, "decision_source indicates simulated/agent-generated decision"
    return False, None


def validate_record(record, required_for=None, now_override=None):
    for f in REQUIRED_FIELDS:
        if f not in record:
            return "HUMAN_GATE_INVALID", f"missing required field: {f}"

    if record["required_for"] not in REQUIRED_FOR:
        return "HUMAN_GATE_INVALID", "invalid required_for value"

    if required_for and record["required_for"] != required_for:
        return "HUMAN_GATE_INVALID", "required_for mismatch"

    decision = record["decision"]
    if decision not in DECISIONS:
        return "HUMAN_GATE_INVALID", "invalid decision value"

    sim, why = simulated(record)
    if sim:
        return "HUMAN_GATE_SIMULATED", why

    decider_type = record["human_decider_type"]
    if decider_type not in ALLOWED_DECIDER_TYPES:
        return "HUMAN_GATE_INVALID", "invalid human_decider_type"

    if decision == "APPROVED":
        if not record.get("human_decider_id"):
            return "HUMAN_GATE_INVALID", "approved decision requires human_decider_id"
        if not record.get("decided_at"):
            return "HUMAN_GATE_INVALID", "approved decision requires decided_at"
        expires_at = record.get("expires_at")
        if expires_at in (None, ""):
            return "HUMAN_GATE_INVALID", "approved decision requires expires_at"
        if expires_at == "never":
            if decider_type != "OWNER_ADMIN_IDENTITY":
                return "HUMAN_GATE_INVALID", "expires_at=never allowed only for OWNER_ADMIN_IDENTITY"
        else:
            exp = parse_iso(expires_at)
            if exp is None:
                return "HUMAN_GATE_INVALID", "invalid expires_at"
            nowv, now_err = now_utc(now_override)
            if now_err:
                return "HUMAN_GATE_INVALID", now_err
            if exp <= nowv:
                return "HUMAN_GATE_EXPIRED", "human gate decision expired"

    # scope consistency check
    if str(record.get("scope", "")).strip() == "":
        return "HUMAN_GATE_INVALID", "scope must not be empty"

    # Result mapping by decision
    if decision == "APPROVED":
        return "HUMAN_GATE_APPROVED", "human gate approved within scope"
    if decision == "REJECTED":
        return "HUMAN_GATE_REJECTED", "human gate rejected"
    if decision == "NEEDS_CLARIFICATION":
        return "HUMAN_GATE_NEEDS_CLARIFICATION", "human gate needs clarification"
    if decision == "UNKNOWN":
        return "HUMAN_GATE_REQUIRED", "human gate decision required"
    if decision == "EXPIRED":
        return "HUMAN_GATE_EXPIRED", "decision marked expired"
    if decision == "INVALID":
        return "HUMAN_GATE_INVALID", "decision marked invalid"
    if decision == "SIMULATED":
        return "HUMAN_GATE_SIMULATED", "decision marked simulated"

    return "HUMAN_GATE_NEEDS_REVIEW", "unhandled decision"


def cmd_request(args):
    record = {
        "schema_version": "1.0",
        "gate_id": "gate-request-000001",
        "task_id": args.task_id,
        "agent_id": args.agent_id,
        "required_for": args.required_for,
        "requested_action": args.required_for,
        "reason": args.reason,
        "decision": "UNKNOWN",
        "requested_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "decided_at": "",
        "expires_at": "",
        "human_decider_id": "",
        "human_decider_type": "HUMAN_REVIEWER_IDENTITY",
        "decision_source": "human_pending",
        "scope": args.required_for,
        "non_authorization_warning": "request is not approval",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    return "HUMAN_GATE_REQUIRED", "checkpoint request created; decision pending"


def main():
    parser = argparse.ArgumentParser(description="Human Gate Checkpoint tool")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--now")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("record_file")
    p_validate.add_argument("--now")

    p_check = sub.add_parser("check")
    p_check.add_argument("--required-for", required=True)
    p_check.add_argument("--record", required=True)
    p_check.add_argument("--now")

    p_request = sub.add_parser("request")
    p_request.add_argument("--required-for", required=True)
    p_request.add_argument("--task-id", required=True)
    p_request.add_argument("--agent-id", required=True)
    p_request.add_argument("--reason", required=True)
    p_request.add_argument("--output", required=True)

    args = parser.parse_args()

    if args.cmd == "request":
        if args.required_for not in REQUIRED_FOR:
            emit("HUMAN_GATE_INVALID", "invalid required_for value", args.json)
            return 1
        res, reason = cmd_request(args)
        emit(res, reason, args.json)
        return 1

    if args.cmd == "validate":
        rec, er, rs = load_record(args.record_file)
        if er:
            emit(er, rs, args.json)
            return 1
        res, reason = validate_record(rec, None, args.now)
        emit(res, reason, args.json)
        return 0 if res == "HUMAN_GATE_APPROVED" else 1

    if args.cmd == "check":
        if args.required_for not in REQUIRED_FOR:
            emit("HUMAN_GATE_INVALID", "invalid required_for value", args.json)
            return 1
        rec, er, rs = load_record(args.record)
        if er:
            emit(er, rs, args.json)
            return 1
        res, reason = validate_record(rec, args.required_for, args.now)
        emit(res, reason, args.json)
        return 0 if res == "HUMAN_GATE_APPROVED" else 1

    emit("HUMAN_GATE_NEEDS_REVIEW", "unknown command", args.json)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
