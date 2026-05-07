# M27 Retry Enforcement Runtime

## Purpose

Bound and enforce retry decisions before execution after failure/warning/violation/blocked states.

## Relationship to M26 Bounded Retry Policy

Implements bounded retry limits from M26 as runtime enforcement.

## Relationship to M27 Runtime Boundary

Retry enforcement is a mandatory runtime boundary, not optional helper logic.

## Relationship to 27.2.1 Permission State

Permission state may be provided and is validated through subprocess to `scripts/agentos-permission-state.py`.

## Relationship to 27.7.1 Audit Log

If `--audit-log` is provided, decision is appended using `scripts/agentos-audit-log.py`.

## Relationship to 27.8.1 Human Gate

If `--human-gate-record` is provided, it is validated through `scripts/agentos-human-gate.py`.

## Relationship to 27.9.1 Violation Enforcement

Retry decisions depend on prior violation flags and blocked states produced by violation enforcement.

## Retry Limits

- max attempts per task: `3`
- same failure max: `2`
- after warning without human review: `1`
- after violation without human review: `0`
- after critical violation: `0`
- after blocked state without owner/admin review: `0`

## Retry Reasons

- `TASK_FAILURE`
- `VALIDATION_FAILURE`
- `SAME_FAILURE`
- `WARNING`
- `VIOLATION`
- `CRITICAL_VIOLATION`
- `BLOCKED_STATE`
- `HUMAN_REVIEW_RETRY`
- `OWNER_RESTORATION_RETRY`
- `UNKNOWN_REASON`

## Result Value Exit Semantics

- `RETRY_ALLOWED` => exit 0
- `RETRY_BLOCKED` => exit 1
- `RETRY_EXHAUSTED` => exit 1
- `RETRY_NEEDS_HUMAN_REVIEW` => exit 1
- `RETRY_NEEDS_OWNER_REVIEW` => exit 1
- `RETRY_POLICY_VIOLATION` => exit 1
- `RETRY_INVALID` => exit 1
- `PERMISSION_BLOCKED` => exit 1
- `PERMISSION_INVALID` => exit 1
- `PERMISSION_DENIED` => exit 1

## Required Retry Record Fields

- `schema_version`
- `retry_id`
- `task_id`
- `agent_id`
- `retry_reason`
- `failure_type`
- `failure_signature`
- `attempt_number`
- `retry_count`
- `same_failure_count`
- `prior_warning`
- `prior_violation`
- `prior_critical_violation`
- `blocked_state`
- `requested_permission`
- `current_permission`
- `previous_task_id`
- `created_at`
- `last_attempt_at`
- `non_authorization_warning`

## Evaluation Order

1. Parse arguments.
2. Load retry record.
3. Validate required fields.
4. Validate retry_reason.
5. Validate numeric counters.
6. Detect retry count reset attempt.
7. Detect same-failure exhaustion.
8. Detect new-task reset attempt.
9. Load permission state if provided.
10. Validate permission state via 27.2.1.
11. Apply critical/block hard blocks.
12. Apply retry limits.
13. Validate human gate when required.
14. Compute next counters.
15. On apply, write only to `--state-out`.
16. Append audit only when `--audit-log` provided.
17. Return final result.

## Validation Behavior

Fail closed for missing/invalid retry records, unknown reason, invalid counters, inconsistent `attempt_number`, missing `failure_signature` for `SAME_FAILURE`, and ambiguous failure type.

## Retry Limit Behavior

- `retry_count >= 3` => `RETRY_EXHAUSTED`
- `same_failure_count >= 2` => `RETRY_EXHAUSTED`
- warning retry without human review after one retry => `RETRY_NEEDS_HUMAN_REVIEW`
- violation retry without gate => blocked/review
- critical violation => owner review required
- blocked state => owner review required

## Reset Detection Behavior

- lower retry_count than prior baseline => `RETRY_POLICY_VIOLATION`
- lower same_failure_count than prior baseline => `RETRY_POLICY_VIOLATION`
- new-task retry reset pattern for same failure signature => `RETRY_POLICY_VIOLATION`

## Permission State Behavior

- validate permission via subprocess when provided
- blocked permission => fail closed
- invalid permission => fail closed
- retry never increases permission
- retry never clears open violations
- retry never resets retry_count

## Human Gate Behavior

- human gate is validated through 27.8.1 when provided
- agent-created gate records are invalid
- gate approval does not clear violations
- gate approval does not reset retry counters
- owner/admin gate required for blocked/critical retry continuation

## Apply Behavior

- `check` is read-only
- `apply` writes only to `--state-out`
- `apply` does not overwrite input permission state
- `apply` does not modify retry record
- `apply` fails without `--state-out`
- `apply` increments counters only

## Audit Behavior

- if `--audit-log` provided, append decision via 27.7.1
- if audit append fails, fail closed as `RETRY_NEEDS_HUMAN_REVIEW`
- audit does not authorize retry and does not clear violations

## `--now` Behavior

- `--now` may be used as test-time timestamp override.
- if provided, current-time comparisons use `--now`.
- if missing, use current UTC time.
- invalid `--now` => `RETRY_INVALID`.
- `--now` does not modify records.

## Known Gap

Known gap: time-based retry window validation is not implemented; `--now` is reserved for future time-based checks.

## Non-Authorization Clauses

- This runtime is not approval.
- It does not authorize commit.
- It does not authorize push.
- It does not authorize merge.
- It does not authorize release.
- It does not authorize violation clearance.

## CLI Output Examples

```text
RESULT: RETRY_ALLOWED
REASON: retry permitted within bounds
```

```text
RESULT: RETRY_EXHAUSTED
REASON: max attempts per task reached
```

```text
RESULT: RETRY_POLICY_VIOLATION
REASON: retry_count reset attempt detected
```

## Continuation Boundary

Retry enforcement does not approve continuation by itself.
