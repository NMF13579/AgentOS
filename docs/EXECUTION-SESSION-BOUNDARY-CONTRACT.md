# Execution Session Boundary Contract

## Purpose

This document defines the M58 Execution Session Boundary Contract.

The boundary contract specifies the required boundary checks, fields, and semantics for an execution session boundary result artifact. It defines limits for controlled execution: scope, command, write path, protected path, session state, and session close boundaries. It does not open an execution session. It does not authorize execution. It does not approve task completion. It does not verify execution result. It does not mutate lifecycle state.

Boundary satisfaction is not execution authorization.

## Preconditions

This contract applies only when:

- `reports/m58-m57-completion-intake.md` exists with `MAY_PROCEED_TO_M58_PLANNING: true`
- `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md` exists with `FINAL_STATUS: M58_ARCHITECTURE_DEFINED`
- `docs/EXECUTION-SESSION-REQUEST-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED`
- `schemas/execution-session-request.schema.json` exists and is valid JSON
- `templates/execution-session-request.md` exists
- `docs/EXECUTION-SESSION-PRECONDITIONS-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_PRECONDITIONS_CONTRACT_DEFINED`
- `schemas/execution-session-preconditions.schema.json` exists and is valid JSON
- `templates/execution-session-preconditions.md` exists

## Position in M58

This is task 58.4. It follows 58.3 (Preconditions Contract) and precedes 58.5 (Session Record / Output Contract).

A boundary result artifact with status `EXECUTION_SESSION_BOUNDARY_SATISFIED` or `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS` may proceed to 58.5 record/output modeling. All other statuses must block progression.

## Boundary Artifact Role

A boundary result artifact:

- Evaluates scope limits declared in the execution session request
- Evaluates command limits declared in the execution session request
- Evaluates write path limits declared in the execution session request
- Evaluates protected path acknowledgements
- Evaluates session state assumptions
- Evaluates session close conditions
- Classifies any detected violations
- Declares `handoff_to_record_output_contract: true` only when SATISFIED or SATISFIED_WITH_WARNINGS

A boundary result artifact is not:

- An open execution session
- An execution authorization
- An approval record
- A result verification
- A lifecycle mutation

## Required Fields

All boundary result artifacts must include these fields:

- `boundary_id`
- `task_id`
- `request_id`
- `preconditions_id`
- `boundary_status`
- `checked_at`
- `checked_by`
- `source_references`
- `scope_boundary`
- `command_boundary`
- `write_boundary`
- `protected_path_boundary`
- `session_state_boundary`
- `session_close_boundary`
- `violation_classification`
- `warnings`
- `blockers`
- `handoff_to_record_output_contract`
- `non_authority_acknowledgement`

## Field Semantics

**boundary_id**: Unique string identifier. Recommended: `exec-session-boundary-<task_id>-<YYYYMMDDHHMMSS>`. Must not be empty.

**task_id**: The task being checked. Must match `task_id` in request and preconditions result.

**request_id**: Must reference an execution session request conforming to 58.2.

**preconditions_id**: Must reference a preconditions result conforming to 58.3 with READY or READY_WITH_WARNINGS status.

**boundary_status**: One of the four allowed statuses. See Allowed Boundary Statuses.

**checked_at**: Timestamp or date. Must not be empty.

**checked_by**: Metadata only. Must not be treated as approval.

**source_references**: Object with paths to all required source artifacts.

**scope_boundary**: Object evaluating scope limits. See Scope Boundary Rules.

**command_boundary**: Object evaluating command limits. See Command Boundary Rules.

**write_boundary**: Object evaluating write path limits. See Write Boundary Rules.

**protected_path_boundary**: Object evaluating protected path constraints. See Protected Path Boundary Rules.

**session_state_boundary**: Object evaluating session state assumptions. See Session State Boundary Rules.

**session_close_boundary**: Object evaluating session close conditions. See Session Close Boundary Rules.

**violation_classification**: Classifies detected boundary violations. See Violation Classification.

**warnings**: List of non-blocking boundary issues. Must not hide blockers.

**blockers**: List of blocking issues. If non-empty, `boundary_status` must be `EXECUTION_SESSION_BOUNDARY_BLOCKED`.

**handoff_to_record_output_contract**: Boolean. `true` only when status is SATISFIED or SATISFIED_WITH_WARNINGS.

**non_authority_acknowledgement**: Must include required non-authority text.

## Allowed Boundary Statuses

- `EXECUTION_SESSION_BOUNDARY_SATISFIED` — All boundary checks pass. Request may proceed to 58.5 record/output modeling.
- `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS` — Checks pass with non-blocking warnings. Request may proceed with warnings preserved.
- `EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED` — Required boundary information is incomplete or insufficient but not unsafe.
- `EXECUTION_SESSION_BOUNDARY_BLOCKED` — Unsafe, contradictory, forbidden, protected, or premature conditions detected.

Boundary satisfaction is not execution authorization.

## Scope Boundary Rules

The `scope_boundary` object must include:

```yaml
scope_boundary:
  scope_summary_present: <true|false>
  allowed_files_declared: <true|false>
  allowed_dirs_declared: <true|false>
  out_of_scope_declared: <true|false>
  max_file_count_declared: <true|false>
  scope_expansion_allowed: <false>
  scope_expansion_policy: <string>
  scope_boundary_result: <SCOPE_BOUNDARY_SATISFIED|SCOPE_BOUNDARY_SATISFIED_WITH_WARNINGS|SCOPE_BOUNDARY_NOT_SATISFIED|SCOPE_BOUNDARY_BLOCKED>
```

Rules:

- `scope_expansion_allowed` must be `false` unless a future human checkpoint explicitly permits expansion.
- Missing `out_of_scope` declaration makes the boundary not satisfied.
- Scope expansion claims without human checkpoint must block.
- Broad or ambiguous scope must produce a warning or blocker depending on severity.
- This contract defines scope boundaries only; it does not execute within any scope.

## Command Boundary Rules

The `command_boundary` object must include:

```yaml
command_boundary:
  allowed_commands_declared: <true|false>
  forbidden_commands_declared: <true|false>
  unknown_commands_policy: <string>
  dangerous_commands_absent_from_allowed: <true|false>
  human_checkpoint_commands_declared: <true|false>
  command_boundary_result: <COMMAND_BOUNDARY_SATISFIED|COMMAND_BOUNDARY_SATISFIED_WITH_WARNINGS|COMMAND_BOUNDARY_NOT_SATISFIED|COMMAND_BOUNDARY_BLOCKED>
```

Rules:

- Unknown commands must not be treated as allowed.
- `git push` must not appear in allowed commands.
- `git merge` must not appear in allowed commands.
- `git reset --hard` must not appear in allowed commands.
- `rm -rf` must not appear in allowed commands.
- `curl | sh` must not appear in allowed commands.
- `wget | sh` must not appear in allowed commands.
- Dangerous commands must block unless explicitly classified as forbidden or human-checkpoint-only.
- This contract defines command boundaries only; it does not execute commands.

## Write Boundary Rules

The `write_boundary` object must include:

```yaml
write_boundary:
  requested_write_paths_declared: <true|false>
  write_paths_within_scope: <true|false>
  write_paths_exclude_m59_artifacts: <true|false>
  write_paths_exclude_approval_records: <true|false>
  write_paths_exclude_lifecycle_state: <true|false>
  write_paths_exclude_unscoped_protected_reports: <true|false>
  write_boundary_result: <WRITE_BOUNDARY_SATISFIED|WRITE_BOUNDARY_SATISFIED_WITH_WARNINGS|WRITE_BOUNDARY_NOT_SATISFIED|WRITE_BOUNDARY_BLOCKED>
```

Rules:

- Write paths must be explicit.
- Empty write paths are allowed only for `READ_ONLY_VALIDATION` mode.
- M59 artifacts must not be writable by M58 execution session.
- Approval records must not be writable by M58 execution session.
- Lifecycle state files must not be writable by M58 execution session.
- `tasks/active-task.md` must not be writable unless a later transition task explicitly allows it.
- Protected reports must not be writable unless explicitly scoped for a future controlled report task.

## Protected Path Boundary Rules

The `protected_path_boundary` object must include:

```yaml
protected_path_boundary:
  protected_paths_declared: <true|false>
  protected_paths_acknowledged: <true|false>
  protected_paths_excluded_from_writes: <true|false>
  protected_path_override_requested: <true|false>
  protected_path_human_checkpoint_required: <true|false>
  protected_path_boundary_result: <PROTECTED_PATH_BOUNDARY_SATISFIED|PROTECTED_PATH_BOUNDARY_SATISFIED_WITH_WARNINGS|PROTECTED_PATH_BOUNDARY_NOT_SATISFIED|PROTECTED_PATH_BOUNDARY_BLOCKED>
```

Rules:

- Protected paths must be acknowledged.
- Protected path override must not be silently allowed.
- Protected path override requires future explicit human checkpoint.
- Protected path override does not mean approval.
- Missing protected path acknowledgement must block.

## Session State Boundary Rules

The `session_state_boundary` object must include:

```yaml
session_state_boundary:
  session_already_open: <true|false>
  conflicting_session_record_exists: <true|false>
  session_state_claimed_by_request: <string>
  allowed_initial_state: <true|false>
  session_state_boundary_result: <SESSION_STATE_BOUNDARY_SATISFIED|SESSION_STATE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_STATE_BOUNDARY_NOT_SATISFIED|SESSION_STATE_BOUNDARY_BLOCKED>
```

Rules:

- Existing open session must block.
- Conflicting session record must block.
- Request claiming session is already open must block.
- Valid initial state is not an execution session start.
- Valid initial state only means boundary evaluation may proceed.

## Session Close Boundary Rules

The `session_close_boundary` object must include:

```yaml
session_close_boundary:
  allowed_close_state: <string>
  m59_handoff_required: <true|false>
  task_completion_claim_absent: <true|false>
  result_verification_claim_absent: <true|false>
  lifecycle_mutation_claim_absent: <true|false>
  session_close_boundary_result: <SESSION_CLOSE_BOUNDARY_SATISFIED|SESSION_CLOSE_BOUNDARY_SATISFIED_WITH_WARNINGS|SESSION_CLOSE_BOUNDARY_NOT_SATISFIED|SESSION_CLOSE_BOUNDARY_BLOCKED>
```

Rules:

- M58 may close only as pending M59 verification.
- M58 close must not claim task completion.
- M58 close must not claim result verification.
- M58 close must not mutate lifecycle state.
- M59 handoff must be required (`m59_handoff_required: true`).

## Violation Classification

The `violation_classification` field must classify the overall boundary result:

- `NO_BOUNDARY_VIOLATION` — No violations detected. All sub-boundary checks satisfied.
- `BOUNDARY_WARNING` — Non-blocking violation detected. Warnings must be recorded.
- `BOUNDARY_NOT_SATISFIED` — Required boundary information incomplete or insufficient.
- `BOUNDARY_BLOCKER` — Blocking condition detected. Must produce BLOCKED status.
- `BOUNDARY_UNSAFE` — Unsafe condition detected (dangerous command, forbidden write, etc.). Must produce BLOCKED status.
- `BOUNDARY_CONTRADICTORY` — Contradictory boundary claims detected. Must produce BLOCKED status.
- `BOUNDARY_PREMATURE_DOWNSTREAM` — Premature M59 artifact or lifecycle mutation detected. Must produce BLOCKED status.

Any unsafe, contradictory, or premature_downstream violation must produce `EXECUTION_SESSION_BOUNDARY_BLOCKED`.
Warnings must not hide blockers.

## Warning and Blocker Semantics

**Warnings** are non-blocking boundary issues that must be recorded and preserved in 58.5. Warnings do not prevent progression to 58.5.

**Blockers** are boundary issues that prevent any progression. If `blockers` is non-empty, `boundary_status` must be `EXECUTION_SESSION_BOUNDARY_BLOCKED` and `handoff_to_record_output_contract` must be `false`.

## Handoff to 58.5 Record / Output Contract

`handoff_to_record_output_contract` governs whether the boundary result artifact may be consumed by 58.5.

Rules:

- `true` allowed only when `boundary_status` is `EXECUTION_SESSION_BOUNDARY_SATISFIED` or `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS`
- `false` required when `boundary_status` is `EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED` or `EXECUTION_SESSION_BOUNDARY_BLOCKED`

The handoff is a structural flag only. It does not open a session. It does not authorize execution. It does not approve task completion.

## Non-Authority Rules

Every boundary result artifact must include this exact non-authority acknowledgement:

> This execution session boundary result does not open an execution session.
> This execution session boundary result does not authorize execution.
> This execution session boundary result does not approve task completion.
> This execution session boundary result does not verify execution result.
> This execution session boundary result does not mutate lifecycle state.
> This execution session boundary result only determines whether the request may proceed to M58 record/output modeling.

## Malformed Boundary Conditions

A boundary result is malformed if any of the following are true:

- `boundary_id` is missing or empty
- `task_id` is missing or empty
- `request_id` is missing or empty
- `preconditions_id` is missing or empty
- `boundary_status` is missing
- `boundary_status` is an unknown value
- `source_references` is missing
- `scope_boundary` is missing or incomplete
- `command_boundary` is missing or incomplete
- `write_boundary` is missing or incomplete
- `protected_path_boundary` is missing or incomplete
- `session_state_boundary` is missing or incomplete
- `session_close_boundary` is missing or incomplete
- `violation_classification` is missing
- `handoff_to_record_output_contract` is missing
- `non_authority_acknowledgement` is missing or does not contain required text
- Schema has invalid JSON structure
- Schema has extra top-level fields not allowed by `additionalProperties: false`

## Unsafe Boundary Conditions

A boundary result is unsafe if any of the following are true:

- Scope expansion allowed without future human checkpoint
- Allowed command includes `git push`
- Allowed command includes `git merge`
- Allowed command includes `git reset --hard`
- Allowed command includes `rm -rf`
- Allowed command includes `curl | sh`
- Allowed command includes `wget | sh`
- Requested write path includes M59 artifact
- Requested write path includes approval records
- Requested write path includes lifecycle state
- Requested write path includes unscoped protected report
- Protected path override is silently allowed
- Session already open
- Conflicting session record exists
- Request claims execution session is already open
- Request claims task already complete
- Request claims result already verified
- Request claims lifecycle mutation is allowed
- M59 handoff is not required

## Relationship to 58.5 Record / Output Contract

58.5 (Execution Session Record / Output Contract) consumes a boundary result with status `EXECUTION_SESSION_BOUNDARY_SATISFIED` or `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS`. 58.5 will independently define the structure of what must be recorded during a session and what output fields are required for M59 verification input.

This contract (58.4) defines boundary limits only. 58.5 defines record and output structure.

## Relationship to 58.6 Policy

58.6 (Controlled Execution Session Policy) will define the enforcement rules that translate boundary results into policy decisions. This contract defines data structures and boundary rules. Policy defines operational enforcement.

## Forbidden Claims

The contract, schema, and template must not claim:

- execution session is open
- execution is authorized
- task is complete
- result is verified
- task is approved
- human review is replaced
- M59 verification is optional
- commit is allowed
- push is allowed
- merge is allowed
- lifecycle state may be mutated

## Final Contract Status

FINAL_STATUS: M58_EXECUTION_SESSION_BOUNDARY_CONTRACT_DEFINED

This status means only that the boundary contract exists.
It does not mean boundary evaluation passed.
It does not mean execution is authorized.
