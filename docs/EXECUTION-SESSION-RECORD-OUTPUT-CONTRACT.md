# Execution Session Record / Output Contract

## Purpose

This document defines the M58 Execution Session Record / Output Contract.

The record/output contract specifies the required structure, fields, and semantics for an execution session record/output artifact. It defines how controlled execution session evidence must be recorded and what output fields are required for M59 verification input. It does not open an execution session. It does not authorize execution. It does not approve task completion. It does not verify execution result. It does not mutate lifecycle state.

M58 record/output is input for M59 verification.

## Preconditions

This contract applies only when:

- `reports/m58-m57-completion-intake.md` exists with `MAY_PROCEED_TO_M58_PLANNING: true`
- `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md` exists with `FINAL_STATUS: M58_ARCHITECTURE_DEFINED`
- `docs/EXECUTION-SESSION-REQUEST-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED`
- `schemas/execution-session-request.schema.json` exists and is valid JSON
- `docs/EXECUTION-SESSION-PRECONDITIONS-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_PRECONDITIONS_CONTRACT_DEFINED`
- `schemas/execution-session-preconditions.schema.json` exists and is valid JSON
- `docs/EXECUTION-SESSION-BOUNDARY-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_BOUNDARY_CONTRACT_DEFINED`
- `schemas/execution-session-boundary.schema.json` exists and is valid JSON

## Position in M58

This is task 58.5. It follows 58.4 (Boundary Contract) and precedes 58.6 (Policy).

The record/output artifact captures what happened (or would happen) during a controlled execution session and provides structured data for 58.6 policy evaluation and ultimately for M59 verification input.

## Record / Output Artifact Role

A record/output artifact:

- Links the execution session to its request, preconditions result, and boundary result
- Summarizes session state without approving result completion
- Preserves a snapshot of boundary results that governed the session
- Records commands requested, allowed, and blocked
- Records write paths requested, allowed, and blocked
- Records blocked actions
- Records session close state
- Provides M59 handoff fields

A record/output artifact is not:

- An open execution session
- An execution authorization
- An approval record
- A result verification
- A lifecycle mutation
- A task completion record

## Required Fields

All record/output artifacts must include these fields:

- `record_id`
- `task_id`
- `session_id`
- `request_id`
- `preconditions_id`
- `boundary_id`
- `record_status`
- `created_at`
- `created_by`
- `source_references`
- `session_state_summary`
- `boundary_snapshot`
- `command_records`
- `write_records`
- `blocked_action_records`
- `session_close`
- `m59_handoff`
- `warnings`
- `blockers`
- `non_authority_acknowledgement`

## Field Semantics

**record_id**: Unique string identifier. Recommended: `exec-session-record-<task_id>-<YYYYMMDDHHMMSS>`. Must not be empty.

**task_id**: The task associated with the session. Must match across request, preconditions, and boundary artifacts.

**session_id**: Identifies the controlled execution session being recorded. Must not be treated as proof that execution is approved or result is verified.

**request_id**: Must reference an execution session request conforming to 58.2.

**preconditions_id**: Must reference a preconditions result conforming to 58.3.

**boundary_id**: Must reference a boundary result conforming to 58.4.

**record_status**: One of the five allowed statuses. See Allowed Record Statuses.

**created_at**: Timestamp or date. Must not be empty.

**created_by**: Metadata only. Must not be treated as approval.

**source_references**: Object with paths to all required source artifacts.

**session_state_summary**: Describes session state without approving result completion. See Session State Summary Rules.

**boundary_snapshot**: Preserves evaluated boundary results. See Boundary Snapshot Rules.

**command_records**: Records command-related information. See Command Record Rules.

**write_records**: Records write-related information. See Write Record Rules.

**blocked_action_records**: Records forbidden or blocked actions. See Blocked Action Record Rules.

**session_close**: Defines how the session record closes. See Session Close Rules.

**m59_handoff**: Describes what M59 receives. See M59 Handoff Rules.

**warnings**: List of non-blocking issues. Must not hide blockers.

**blockers**: List of blocking issues. If non-empty, status must not be `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`.

**non_authority_acknowledgement**: Must include required non-authority text.

## Allowed Record Statuses

- `EXECUTION_SESSION_RECORD_DRAFT` — Record is incomplete.
- `EXECUTION_SESSION_RECORD_READY_FOR_POLICY` — Record/output structure may be evaluated by 58.6 policy.
- `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION` — Session record is closed only for handoff to M59. Not task completion.
- `EXECUTION_SESSION_RECORD_BLOCKED` — Record contains blockers.
- `EXECUTION_SESSION_RECORD_ABORTED` — Session was or would be aborted. Must not be treated as complete.

No record status may claim task completion or result verification.

## Session State Summary Rules

The `session_state_summary` object must include:

```yaml
session_state_summary:
  initial_state: <SESSION_NOT_STARTED|SESSION_READY_FOR_CONTROLLED_OPEN>
  final_state: <SESSION_NOT_STARTED|SESSION_BLOCKED|SESSION_ABORTED|SESSION_CLOSED_PENDING_M59_VERIFICATION>
  session_opened: <true|false>
  session_paused: <true|false>
  session_blocked: <true|false>
  session_aborted: <true|false>
  session_closed_pending_m59: <true|false>
```

Rules:

- `session_closed_pending_m59` may be `true` only if `final_state` is `SESSION_CLOSED_PENDING_M59_VERIFICATION`.
- `SESSION_CLOSED_PENDING_M59_VERIFICATION` is not task completion.
- No field may claim `SESSION_VERIFIED` or `TASK_DONE`.

## Boundary Snapshot Rules

The `boundary_snapshot` object must include:

```yaml
boundary_snapshot:
  scope_boundary_result: <...>
  command_boundary_result: <...>
  write_boundary_result: <...>
  protected_path_boundary_result: <...>
  session_state_boundary_result: <...>
  session_close_boundary_result: <...>
  violation_classification: <...>
```

Rules:

- Boundary snapshot records boundary state only.
- Boundary snapshot does not authorize execution by itself.
- Any blocked boundary result must prevent `record_status: EXECUTION_SESSION_RECORD_READY_FOR_POLICY`.

## Command Record Rules

The `command_records` object must include:

```yaml
command_records:
  commands_requested: [...]
  commands_allowed: [...]
  commands_blocked: [...]
  unknown_commands_detected: <true|false>
  dangerous_commands_detected: <true|false>
```

Rules:

- `commands_allowed` must not include `git push`, `git merge`, `git reset --hard`, `rm -rf`, `curl | sh`, or `wget | sh`.
- `commands_blocked` must preserve blocked commands.
- Unknown commands must not be silently treated as allowed.
- Command records do not prove validation success.

## Write Record Rules

The `write_records` object must include:

```yaml
write_records:
  write_paths_requested: [...]
  write_paths_allowed: [...]
  write_paths_blocked: [...]
  protected_write_attempts: <integer>
  m59_artifact_write_attempts: <integer>
  approval_record_write_attempts: <integer>
  lifecycle_state_write_attempts: <integer>
```

Rules:

- M59 artifact writes must not be allowed.
- Approval record writes must not be allowed.
- Lifecycle state writes must not be allowed.
- Protected writes must require future explicit human checkpoint.
- Write records do not prove task completion.

## Blocked Action Record Rules

The `blocked_action_records` object must include:

```yaml
blocked_action_records:
  execution_start_blocked: <true|false>
  command_blocked: <true|false>
  write_blocked: <true|false>
  protected_path_blocked: <true|false>
  approval_creation_blocked: <true|false>
  lifecycle_mutation_blocked: <true|false>
  commit_blocked: <true|false>
  push_blocked: <true|false>
  merge_blocked: <true|false>
  m59_artifact_blocked: <true|false>
```

Rules:

- Blocked action records must not be removed from output.
- Blocked action records must be available to M59 and human review.
- Presence of blockers must prevent clean closure.

## Session Close Rules

The `session_close` object must include:

```yaml
session_close:
  close_status: <SESSION_CLOSE_NOT_CLOSED|SESSION_CLOSE_PENDING_M59_VERIFICATION|SESSION_CLOSE_ABORTED|SESSION_CLOSE_BLOCKED>
  closed_at: <timestamp or null>
  close_reason: <string>
  closed_pending_m59_verification: <true|false>
  task_completion_claimed: false
  result_verification_claimed: false
  lifecycle_mutation_claimed: false
```

Rules:

- `closed_pending_m59_verification` must be `true` only for `SESSION_CLOSE_PENDING_M59_VERIFICATION`.
- `task_completion_claimed` must be `false`.
- `result_verification_claimed` must be `false`.
- `lifecycle_mutation_claimed` must be `false`.
- M58 close does not mean M59 verification passed.

## M59 Handoff Rules

The `m59_handoff` object must include:

```yaml
m59_handoff:
  handoff_required: true
  handoff_ready: <true|false>
  expected_m59_inputs: [...]
  known_warnings: [...]
  known_blockers: [...]
  unresolved_questions: [...]
```

Rules:

- `handoff_required` must be `true`.
- `handoff_ready` may be `true` only if the record is closed pending M59 verification without blockers.
- M59 handoff is not M59 start.
- M59 handoff is not result verification.
- M59 handoff is not approval.

## Warning and Blocker Semantics

**Warnings** are non-blocking record issues that must be recorded and preserved in the M59 handoff. Warnings do not prevent record closure.

**Blockers** are issues that prevent clean closure. If `blockers` is non-empty, `record_status` must not be `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`. Blockers must be visible to M59 and human review.

Warnings must not hide blockers.

## Non-Authority Rules

Every record/output artifact must include this exact non-authority acknowledgement:

> This execution session record does not approve task completion.
> This execution session record does not verify execution result.
> This execution session record does not authorize merge, push, or release.
> This execution session record does not mutate lifecycle state.
> This execution session record only records controlled execution session output for M59 verification.

## Malformed Record Conditions

A record/output artifact is malformed if any of the following are true:

- `record_id` is missing or empty
- `task_id` is missing or empty
- `session_id` is missing or empty
- `request_id` is missing or empty
- `preconditions_id` is missing or empty
- `boundary_id` is missing or empty
- `record_status` is missing
- `record_status` is an unknown value
- `source_references` is missing
- `session_state_summary` is missing or incomplete
- `boundary_snapshot` is missing or incomplete
- `command_records` is missing or incomplete
- `write_records` is missing or incomplete
- `blocked_action_records` is missing or incomplete
- `session_close` is missing or incomplete
- `m59_handoff` is missing or incomplete
- `non_authority_acknowledgement` is missing or does not contain required text
- Schema has invalid JSON structure
- Schema has extra top-level fields not allowed by `additionalProperties: false`

## Unsafe Record Conditions

A record/output artifact is unsafe if any of the following are true:

- Record claims task completion
- Record claims result verification
- Record claims approval
- Record claims merge is allowed
- Record claims push is allowed
- Record claims release is allowed
- Record claims lifecycle mutation is allowed
- Record says M59 verification is optional
- `commands_allowed` includes `git push`, `git merge`, `git reset --hard`, `rm -rf`, `curl | sh`, or `wget | sh`
- Write records allow M59 artifact writes
- Write records allow approval record writes
- Write records allow lifecycle state writes
- `session_close.task_completion_claimed` is `true`
- `session_close.result_verification_claimed` is `true`
- `m59_handoff` is missing
- Blockers are present but `record_status` is `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`

## Relationship to 58.6 Policy

58.6 (Controlled Execution Session Policy) will consume a record/output artifact with status `EXECUTION_SESSION_RECORD_READY_FOR_POLICY`. Policy will define the rules for how boundary snapshots, command records, write records, and blocked action records translate into policy decisions. This contract defines the data structure only.

## Relationship to 58.7 CLI

58.7 (Controlled Execution Session CLI) will produce or validate record/output artifacts against this schema. The CLI must populate all required fields and must not claim task completion or result verification.

## Forbidden Claims

The contract, schema, and template must not claim:

- task is complete
- result is verified
- task is approved
- human review is replaced
- M59 verification is optional
- commit is allowed
- push is allowed
- merge is allowed
- release is allowed
- lifecycle state may be mutated

## Final Contract Status

FINAL_STATUS: M58_EXECUTION_SESSION_RECORD_OUTPUT_CONTRACT_DEFINED

This status means only that the record/output contract exists.
It does not mean an execution session was opened.
It does not mean the result was verified.
