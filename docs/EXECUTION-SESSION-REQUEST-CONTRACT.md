# Execution Session Request Contract

## Purpose

This document defines the M58 Execution Session Request Contract.

The request contract specifies the required structure, fields, and semantics for an execution session request artifact. It does not open an execution session. It does not approve execution. It does not verify execution result.

## Preconditions

This contract applies only when:

- `reports/m58-m57-completion-intake.md` exists and contains `MAY_PROCEED_TO_M58_PLANNING: true`
- `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md` exists and contains `FINAL_STATUS: M58_ARCHITECTURE_DEFINED`

## Position in M58

This is task 58.2. It follows 58.1 (Architecture) and precedes 58.3 (Preconditions Contract).

A well-formed request artifact (using this contract) is the input consumed by 58.3 precondition checks. The request contract does not perform those checks.

## Request Artifact Role

A request artifact:

- Declares the intent to open an execution session for a specific task
- Declares the intended scope, write paths, and command categories
- Acknowledges protected paths and forbidden commands
- Declares that M59 handoff is required
- Provides structured input for M58 precondition checks (58.3)

A request artifact is not:

- An open execution session
- An authorization record
- An approval record
- A result verification
- A lifecycle mutation

## Required Fields

All request artifacts must include these fields:

- `request_id`
- `task_id`
- `request_status`
- `created_at`
- `created_by`
- `source_task_path`
- `m57_completion_review_path`
- `m58_intake_report_path`
- `m58_architecture_path`
- `authorization_status`
- `requested_execution_mode`
- `requested_scope`
- `requested_write_paths`
- `requested_commands`
- `forbidden_commands_acknowledged`
- `protected_paths_acknowledged`
- `expected_outputs`
- `expected_validation_evidence`
- `handoff_to_m59_required`
- `non_authority_acknowledgement`

## Field Semantics

**request_id**: Unique string identifier for this request. Recommended format: `exec-session-request-<task_id>-<YYYYMMDDHHMMSS>`. Must not be empty.

**task_id**: The task this request refers to. Must not be empty.

**request_status**: One of `EXECUTION_SESSION_REQUEST_DRAFT`, `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS`, `EXECUTION_SESSION_REQUEST_BLOCKED`. See Allowed Request Statuses.

**created_at**: Timestamp or date when the request was created. Must not be empty.

**created_by**: Identifies the creator as metadata only. Must not be treated as approval. Must not grant authority.

**source_task_path**: Path to the task artifact being requested for controlled execution. Must not be empty.

**m57_completion_review_path**: Must reference `reports/m57-completion-review.md`. Must not be empty.

**m58_intake_report_path**: Must reference `reports/m58-m57-completion-intake.md`. Must not be empty.

**m58_architecture_path**: Must reference `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md`. Must not be empty.

**authorization_status**: Must reflect the M57 authorization result or limitation state. Must not invent authorization.

**requested_execution_mode**: One of the allowed modes. See Requested Execution Modes.

**requested_scope**: Object with `summary`, `allowed_files`, `allowed_dirs`, `out_of_scope`, `max_file_count`, `scope_expansion_allowed`. `summary` must not be empty. `scope_expansion_allowed` must be `false` unless a future human checkpoint explicitly allows expansion.

**requested_write_paths**: List of requested write paths. May be empty only for `READ_ONLY_VALIDATION`. Must not include approval records. Must not include M59 artifacts. Must not include `tasks/active-task.md` unless a later transition task explicitly allows it.

**requested_commands**: Object with `allowed`, `forbidden`, `requires_human_checkpoint`. `allowed` must be explicit. Unknown commands must not be treated as allowed. `git push`, `git merge`, `git reset --hard`, `rm -rf`, `curl | sh`, `wget | sh` must not appear in `allowed`.

**forbidden_commands_acknowledged**: Must be `true`.

**protected_paths_acknowledged**: Must be `true`.

**expected_outputs**: Describes expected M58 session outputs or records. Must not claim task completion.

**expected_validation_evidence**: Describes what evidence is expected to be passed to M59. Must not claim that validation has already passed.

**handoff_to_m59_required**: Must be `true`.

**non_authority_acknowledgement**: Must include the required non-authority text. See Non-Authority Rules.

## Allowed Request Statuses

- `EXECUTION_SESSION_REQUEST_DRAFT` — Request is not ready for 58.3. Must not be checked by preconditions logic.
- `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS` — Request may be checked by 58.3 preconditions.
- `EXECUTION_SESSION_REQUEST_BLOCKED` — Request must not proceed.

## Requested Execution Modes

Allowed values for `requested_execution_mode`:

- `READ_ONLY_VALIDATION` — No writes permitted. Scope inspection only.
- `CONTROLLED_WRITE` — Targeted writes within declared scope.
- `CONTROLLED_REPAIR` — Targeted repair writes within declared scope.
- `CONTROLLED_DOCUMENTATION_UPDATE` — Documentation files only within declared scope.
- `CONTROLLED_CODE_CHANGE` — Source code files within declared scope.

The request contract defines allowed values only. It does not grant permission to execute any mode.

## Requested Scope Rules

The `requested_scope` object must include:

- `summary`: non-empty string describing the scope
- `allowed_files`: list of allowed file paths (may be empty if `allowed_dirs` is non-empty)
- `allowed_dirs`: list of allowed directory paths (may be empty if `allowed_files` is non-empty)
- `out_of_scope`: list of explicitly excluded paths or patterns
- `max_file_count`: integer or null
- `scope_expansion_allowed`: must be `false` unless a future human checkpoint explicitly allows expansion

For `READ_ONLY_VALIDATION`, `allowed_files` and `allowed_dirs` may both be empty.

For all other modes, at least one of `allowed_files` or `allowed_dirs` must contain at least one item.

## Requested Write Path Rules

- `requested_write_paths` may be empty only for `READ_ONLY_VALIDATION`
- Must not include approval records (`approvals/`)
- Must not include protected reports unless explicitly scoped for a future controlled report task
- Must not include M59 artifacts
- Must not include `tasks/active-task.md` unless a later transition task explicitly allows it
- Must not include `generated/` unless explicitly scoped

## Requested Command Rules

The `requested_commands` object must include:

- `allowed`: explicit list of allowed command categories or commands
- `forbidden`: list of forbidden commands
- `requires_human_checkpoint`: list of commands requiring explicit human checkpoint

Rules:

- Unknown commands must not be treated as allowed
- The following must never appear in `allowed`: `git push`, `git merge`, `git reset --hard`, `rm -rf`, `curl | sh`, `wget | sh`
- All forbidden commands must be acknowledged via `forbidden_commands_acknowledged: true`

## Protected Path Acknowledgement

`protected_paths_acknowledged: true` must be present in every request.

This acknowledges that the following paths are protected and must not be modified by the execution session without explicit boundary authorization from 58.4:

- `tasks/active-task.md`
- `tasks/queue/`
- `approvals/`
- `generated/`
- M57 report artifacts
- M56 report artifacts
- Any path not in `requested_write_paths`

## Handoff to M59

`handoff_to_m59_required: true` must be present in every request.

This declares that the result of the execution session must be handed off to M59 for independent verification. No request may set this to `false`.

The request itself does not produce M59 input. That is the responsibility of the session record (58.5). The field here is a structural declaration only.

## Non-Authority Rules

Every request artifact must include this exact non-authority acknowledgement:

> This execution session request does not open an execution session.
> This execution session request does not authorize execution.
> This execution session request does not approve task completion.
> This execution session request does not verify execution result.
> This execution session request does not mutate lifecycle state.
> This execution session request only provides structured input for M58 precondition checks.

## Malformed Request Conditions

A request is malformed if any of the following are true:

- `request_id` is missing or empty
- `task_id` is missing or empty
- `request_status` is missing
- `request_status` is an unknown value (not one of the three allowed statuses)
- Any of the three source reference fields are missing or empty
- `requested_scope` is missing or does not contain required subfields
- `requested_commands` is missing or does not contain `allowed`, `forbidden`, and `requires_human_checkpoint`
- `handoff_to_m59_required` is missing
- `non_authority_acknowledgement` is missing or does not contain required text
- Schema has invalid JSON structure
- Schema has extra top-level fields not allowed by `additionalProperties: false`

## Unsafe Request Conditions

A request is unsafe if any of the following are true:

- Request claims execution is already open
- Request claims task is complete
- Request claims result is verified
- Request claims approval exists without an approval artifact
- Request allows raw `git push` or `git merge`
- Request allows lifecycle mutation
- Request allows protected path write without future boundary validation (58.4)
- Request bypasses M57 completion (missing `m57_completion_review_path`)
- Request bypasses M58 intake (missing `m58_intake_report_path`)
- Request states M59 is optional
- Request sets `handoff_to_m59_required: false`

## Relationship to 58.3 Preconditions

A request with status `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS` is consumed by 58.3 (Execution Session Preconditions Contract). 58.3 will independently verify:

- That M57 completion is confirmed
- That M58 intake is READY
- That declared scope is safe
- That declared write paths do not violate boundaries
- That declared commands do not violate policy
- That required acknowledgements are present

This contract (58.2) defines the structure only. 58.3 defines the validation logic.

## Forbidden Claims

The request contract, schema, and template must not claim:

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

FINAL_STATUS: M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED

This status means only that the request contract exists.
It does not mean a request has passed preconditions.
