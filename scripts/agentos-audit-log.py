#!/usr/bin/env python3
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

RESULT_OK = "AUDIT_OK"
RESULT_APPENDED = "AUDIT_APPENDED"
RESULT_EMPTY = "AUDIT_EMPTY"
RESULT_INVALID = "AUDIT_INVALID"
RESULT_CHAIN_BROKEN = "AUDIT_CHAIN_BROKEN"
RESULT_TAMPERED = "AUDIT_TAMPERED"
RESULT_NEEDS_REVIEW = "AUDIT_NEEDS_REVIEW"

REQUIRED_FIELDS = [
    "schema_version",
    "record_id",
    "previous_hash",
    "payload_hash",
    "current_hash",
    "timestamp",
    "actor_id",
    "actor_type",
    "action_type",
    "task_id",
    "decision",
    "reason",
    "payload",
]

ALLOWED_ACTOR_TYPES = {
    "AGENT_IDENTITY",
    "HUMAN_REVIEWER_IDENTITY",
    "OWNER_ADMIN_IDENTITY",
    "RUNTIME_SYSTEM_IDENTITY",
    "UNKNOWN_IDENTITY",
}

ALLOWED_ACTION_TYPES = {
    "COMMAND_DECISION",
    "WRITE_DECISION",
    "GIT_DECISION",
    "PERMISSION_DECISION",
    "VIOLATION_DECISION",
    "RETRY_DECISION",
    "HUMAN_GATE_DECISION",
    "TOKEN_SCOPE_REVIEW",
    "AUDIT_VALIDATION",
    "UNKNOWN_ACTION",
}


def emit(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def canonical_json(value) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def payload_hash(payload) -> str:
    return sha256_text(canonical_json(payload))


def compute_current_hash(record: dict) -> str:
    base = {k: v for k, v in record.items() if k != "current_hash"}
    return sha256_text(canonical_json(base))


def parse_jsonl(path: Path):
    if not path.exists():
        return None, RESULT_EMPTY, "log file does not exist"
    text = path.read_text(encoding="utf-8")
    if text.strip() == "":
        return [], None, None

    records = []
    for idx, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "":
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            return None, RESULT_INVALID, f"malformed jsonl at line {idx}"
        if not isinstance(obj, dict):
            return None, RESULT_INVALID, f"record at line {idx} is not object"
        records.append(obj)
    return records, None, None


def validate_records(records):
    if len(records) == 0:
        return RESULT_EMPTY, "log is empty"

    prev_current = None
    for i, rec in enumerate(records):
        idx = i + 1
        for field in REQUIRED_FIELDS:
            if field not in rec:
                return RESULT_INVALID, f"missing required field {field} at record {idx}"

        if rec["actor_type"] not in ALLOWED_ACTOR_TYPES:
            return RESULT_INVALID, f"invalid actor_type at record {idx}"
        if rec["action_type"] not in ALLOWED_ACTION_TYPES:
            return RESULT_INVALID, f"invalid action_type at record {idx}"

        expected_payload_hash = payload_hash(rec["payload"])
        if rec["payload_hash"] != expected_payload_hash:
            return RESULT_TAMPERED, f"payload hash mismatch at record {idx}"

        expected_current_hash = compute_current_hash(rec)
        if rec["current_hash"] != expected_current_hash:
            return RESULT_TAMPERED, f"current hash mismatch at record {idx}"

        if i == 0:
            if rec["previous_hash"] not in (None, "GENESIS"):
                return RESULT_CHAIN_BROKEN, "genesis previous_hash must be null or GENESIS"
        else:
            if rec["previous_hash"] != prev_current:
                return RESULT_CHAIN_BROKEN, f"previous_hash mismatch at record {idx}"

        prev_current = rec["current_hash"]

    return RESULT_OK, f"validated {len(records)} record(s)"


def next_record_id(records):
    return f"rec-{len(records)+1:06d}"


def append_record(path: Path, args):
    records, err_result, err_reason = parse_jsonl(path)
    if err_result == RESULT_EMPTY and not path.exists():
        records = []
    elif err_result:
        return err_result, err_reason

    if records:
        status, reason = validate_records(records)
        if status != RESULT_OK:
            if status == RESULT_EMPTY:
                pass
            else:
                return status, f"append blocked: {reason}"

    try:
        payload = json.loads(args.payload_json)
    except json.JSONDecodeError:
        return RESULT_INVALID, "payload-json must be valid json"

    if args.actor_type not in ALLOWED_ACTOR_TYPES:
        return RESULT_INVALID, "invalid actor_type"
    if args.action_type not in ALLOWED_ACTION_TYPES:
        return RESULT_INVALID, "invalid action_type"

    prev = "GENESIS" if len(records) == 0 else records[-1]["current_hash"]
    record = {
        "schema_version": "1.0",
        "record_id": next_record_id(records),
        "previous_hash": prev,
        "payload_hash": payload_hash(payload),
        "current_hash": "",
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "actor_id": args.actor_id,
        "actor_type": args.actor_type,
        "action_type": args.action_type,
        "task_id": args.task_id,
        "decision": args.decision,
        "reason": args.reason,
        "payload": payload,
    }
    record["current_hash"] = compute_current_hash(record)

    line = canonical_json(record)
    if path.exists() and path.read_text(encoding="utf-8") != "" and not path.read_text(encoding="utf-8").endswith("\n"):
        path.write_text(path.read_text(encoding="utf-8") + "\n" + line + "\n", encoding="utf-8")
    else:
        with path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    return RESULT_APPENDED, f"appended record {record['record_id']}"


def show_records(path: Path):
    records, err_result, err_reason = parse_jsonl(path)
    if err_result:
        return err_result, err_reason
    if len(records) == 0:
        return RESULT_EMPTY, "log is empty"

    print(f"records: {len(records)}")
    print(f"last_record_id: {records[-1].get('record_id')}")
    print(f"last_current_hash: {records[-1].get('current_hash')}")
    return RESULT_OK, "show complete"


def main():
    parser = argparse.ArgumentParser(description="Immutable/tamper-evident audit log tool")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("log_file")

    p_append = sub.add_parser("append")
    p_append.add_argument("log_file")
    p_append.add_argument("--actor-id", required=True)
    p_append.add_argument("--actor-type", required=True)
    p_append.add_argument("--action-type", required=True)
    p_append.add_argument("--task-id", required=True)
    p_append.add_argument("--decision", required=True)
    p_append.add_argument("--reason", required=True)
    p_append.add_argument("--payload-json", required=True)

    p_show = sub.add_parser("show")
    p_show.add_argument("log_file")

    args = parser.parse_args()
    log_path = Path(getattr(args, "log_file"))

    if args.cmd == "validate":
        records, err_result, err_reason = parse_jsonl(log_path)
        if err_result == RESULT_EMPTY and not log_path.exists():
            emit(RESULT_NEEDS_REVIEW, err_reason, args.json)
            return 1
        if err_result:
            emit(err_result, err_reason, args.json)
            return 1

        status, reason = validate_records(records)
        if status == RESULT_EMPTY:
            emit(status, reason, args.json)
            return 0
        emit(status, reason, args.json)
        return 0 if status == RESULT_OK else 1

    if args.cmd == "append":
        status, reason = append_record(log_path, args)
        emit(status, reason, args.json)
        return 0 if status == RESULT_APPENDED else 1

    if args.cmd == "show":
        status, reason = show_records(log_path)
        emit(status, reason, args.json)
        return 0 if status in (RESULT_OK, RESULT_EMPTY) else 1

    emit(RESULT_NEEDS_REVIEW, "unknown command", args.json)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
