# Immutable / Tamper-Evident Audit Log Policy

## Purpose

Define append-only JSONL audit records with hash-chain validation for M27 traceability.

## Relationship to M27 Runtime Boundary

Audit records capture runtime guard decisions and support evidence checks.
Audit record is not approval and does not authorize actions.

## Relationship to 27.6.1 Identity Boundary

Audit records must preserve actor identity separation and traceability (`actor_id`, `actor_type`).

## Relationship to 27.6.2 Token Scope Policy

Audit records provide evidence that token/credential boundary decisions are tracked and reviewable.

## Relationship to 27.2.1 through 27.5.1 Runtime Guards

Applies to decisions produced by:
- `27.2.1` Permission State Store
- `27.3.1` Command Enforcement Runtime
- `27.4.1` Write Enforcement Runtime
- `27.5.1` Commit / Push Runtime Guard

## Append-Only Model

- Records are JSON objects, one per line (JSONL).
- New records are appended only.
- Previous records must not be modified, deleted, rewritten, reordered, or backdated.

## Limitation

Tamper-evident, not tamper-proof.
Hash checks detect modifications but do not provide cryptographic signing authority.

## Required Record Fields

- `schema_version`
- `record_id`
- `previous_hash`
- `payload_hash`
- `current_hash`
- `timestamp`
- `actor_id`
- `actor_type`
- `action_type`
- `task_id`
- `decision`
- `reason`
- `payload`

## Hash-Chain Model

- `payload_hash` = hash of canonicalized `payload`.
- `current_hash` = hash of canonicalized record excluding `current_hash`.
- `previous_hash` = previous record `current_hash`.
- Genesis `previous_hash` is `null` or `GENESIS`.

## actor_type Values

- `AGENT_IDENTITY`
- `HUMAN_REVIEWER_IDENTITY`
- `OWNER_ADMIN_IDENTITY`
- `RUNTIME_SYSTEM_IDENTITY`
- `UNKNOWN_IDENTITY`

## action_type Values

- `COMMAND_DECISION`
- `WRITE_DECISION`
- `GIT_DECISION`
- `PERMISSION_DECISION`
- `VIOLATION_DECISION`
- `RETRY_DECISION`
- `HUMAN_GATE_DECISION`
- `TOKEN_SCOPE_REVIEW`
- `AUDIT_VALIDATION`
- `UNKNOWN_ACTION`

## Append Rules

- Append must not rewrite existing records.
- Append must read last `current_hash` and set next `previous_hash`.
- Missing log file may start a genesis append.
- Append to invalid chain must fail closed.
- Caller must not provide `current_hash`.
- Script computes hashes.
- Append must not create approval records.
- Append must not authorize audited action.

## Validation Rules

- Valid chain => `AUDIT_OK`, exit 0.
- Missing log => `AUDIT_NEEDS_REVIEW` or `AUDIT_EMPTY`, fail closed by command policy.
- Empty log => `AUDIT_EMPTY`, exit 0.
- Malformed JSONL => `AUDIT_INVALID`, exit 1.
- Missing required field => `AUDIT_INVALID`, exit 1.
- Broken previous hash => `AUDIT_CHAIN_BROKEN`, exit 1.
- Tampered payload/hash => `AUDIT_TAMPERED`, exit 1.

## Empty Log Behavior

An empty log is a valid starting state before first append.

## Tampering Examples

- Change payload text without recomputing hash.
- Edit `previous_hash` in any non-genesis record.
- Edit `timestamp` in historical record.
- Delete or reorder middle records.

## CLI Output Examples

```text
RESULT: AUDIT_OK
REASON: validated 2 record(s)
```

```text
RESULT: AUDIT_APPENDED
REASON: appended record rec-000003
```

```text
RESULT: AUDIT_TAMPERED
REASON: current hash mismatch at record 2
```

## Non-Authorization Clauses

- This policy is not approval.
- This policy does not authorize commit.
- This policy does not authorize push.
- This policy does not authorize merge.
- This policy does not authorize release.
- This policy does not authorize human approval.
- This policy does not create production enforcement authority by itself.

## Action Approval Boundary

Audit records do not approve actions.
