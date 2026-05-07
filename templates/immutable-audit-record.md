# Immutable Audit Record Template

## JSON Record Example

```json
{
  "schema_version": "1.0",
  "record_id": "rec-000001",
  "previous_hash": "GENESIS",
  "payload_hash": "<sha256(payload)>",
  "current_hash": "<sha256(record-without-current_hash)>",
  "timestamp": "2026-05-07T10:00:00Z",
  "actor_id": "runtime-system",
  "actor_type": "RUNTIME_SYSTEM_IDENTITY",
  "action_type": "AUDIT_VALIDATION",
  "task_id": "27.7.1",
  "decision": "AUDIT_OK",
  "reason": "validation passed",
  "payload": {"checked_records": 1}
}
```

## Field Descriptions

- `schema_version`: schema version.
- `record_id`: monotonically increasing logical record id.
- `previous_hash`: `GENESIS`/`null` for first record, else previous `current_hash`.
- `payload_hash`: hash of canonicalized `payload`.
- `current_hash`: hash of canonicalized record except `current_hash`.
- `timestamp`: UTC timestamp when appended.
- `actor_id`: actor identifier.
- `actor_type`: identity category.
- `action_type`: audited action category.
- `task_id`: task context id.
- `decision`: decision result.
- `reason`: human-readable reason.
- `payload`: structured details.

## Hash Field Explanations

- `payload_hash` protects payload integrity.
- `current_hash` binds all record fields.
- `previous_hash` links records into a tamper-evident chain.

## Actor Identity Warning

Actor identity must be truthful and traceable.
Agent identity must not be written as human reviewer or owner/admin identity.

## Non-Authorization Warning

This record is evidence only.
It is not approval and does not authorize commit, push, merge, release, or human approval.
