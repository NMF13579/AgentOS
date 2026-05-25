# Execution Session Preconditions Contract

## Purpose

This document defines the M58 Execution Session Preconditions Contract.

The preconditions contract specifies the required checks, fields, and semantics for an execution session preconditions result artifact. It classifies readiness for boundary evaluation. It does not open an execution session. It does not authorize execution. It does not approve task completion. It does not verify execution result. It does not mutate lifecycle state.

## Preconditions

This contract applies only when:

- `reports/m58-m57-completion-intake.md` exists with `MAY_PROCEED_TO_M58_PLANNING: true`
- `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md` exists with `FINAL_STATUS: M58_ARCHITECTURE_DEFINED`
- `docs/EXECUTION-SESSION-REQUEST-CONTRACT.md` exists with `FINAL_STATUS: M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED`
- `schemas/execution-session-request.schema.json` exists and is valid JSON
- `templates/execution-session-request.md` exists

## Position in M58

This is task 58.3. It follows 58.2 (Request Contract) and precedes 58.4 (Boundary Contract).

A well-formed preconditions result artifact (using this contract) is the gating artifact consumed by 58.4 boundary evaluation. A request with status `EXECUTION_SESSION_PRECONDITIONS_READY` or `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS` may proceed to 58.4. All other statuses must block progression.

## Preconditions Artifact Role

A preconditions result artifact:

- Checks required source artifacts
- Validates the execution session request against the 58.2 contract
- Checks authorization consistency
- Checks boundary input availability
- Checks for forbidden actions
- Checks for premature downstream artifacts
- Checks performed actions
- Classifies the outcome as READY, READY_WITH_WARNINGS, NOT_READY, or BLOCKED
- Declares `handoff_to_boundary_contract: true` only when READY or READY_WITH_WARNINGS

A preconditions result artifact is not:

- An open execution session
- An authorization record
- An approval record
- A result verification
- A lifecycle mutation

## Required Fields

All preconditions result artifacts must include these fields:

- `preconditions_id`
- `task_id`
- `request_id`
- `preconditions_status`
- `checked_at`
- `checked_by`
- `source_references`
- `m57_completion_status`
- `m58_intake_status`
- `m58_architecture_status`
- `request_contract_status`
- `request_status`
- `request_validity`
- `authorization_consistency`
- `source_artifact_checks`
- `request_field_checks`
- `boundary_input_checks`
- `forbidden_action_checks`
- `premature_downstream_artifact_checks`
- `performed_actions`
- `warnings`
- `blockers`
- `handoff_to_boundary_contract`
- `non_authority_acknowledgement`

## Field Semantics

**preconditions_id**: Unique string identifier. Recommended: `exec-session-preconditions-<task_id>-<YYYYMMDDHHMMSS>`. Must not be empty.

**task_id**: The task being checked. Must match `task_id` in the execution session request.

**request_id**: Must reference an execution session request artifact conforming to 58.2.

**preconditions_status**: One of the four allowed statuses. See Allowed Preconditions Statuses.

**checked_at**: Timestamp or date when checks were performed. Must not be empty.

**checked_by**: Metadata only. Must not be treated as approval.

**source_references**: Object with paths to all required source artifacts. See Source Artifact Checks.

**m57_completion_status**: Detected M57 completion status. Allowed proceeding values: `M57_EXECUTION_AUTHORIZATION_COMPLETE`, `M57_EXECUTION_AUTHORIZATION_COMPLETE_WITH_WARNINGS`. Blocking values: `M57_EXECUTION_AUTHORIZATION_INCOMPLETE`, `M57_EXECUTION_AUTHORIZATION_BLOCKED`, `UNKNOWN`, `MISSING`, `MALFORMED`.

**m58_intake_status**: Detected M58 intake status. Allowed proceeding values: `M58_INTAKE_READY`, `M58_INTAKE_READY_WITH_WARNINGS`. Blocking values: `M58_INTAKE_BLOCKED`, `UNKNOWN`, `MISSING`, `MALFORMED`.

**m58_architecture_status**: Must be `M58_ARCHITECTURE_DEFINED`. Missing, unknown, or malformed architecture status must block.

**request_contract_status**: Must be `M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED`. Missing, unknown, or malformed status must block.

**request_status**: One of the 58.2 request statuses. `EXECUTION_SESSION_REQUEST_DRAFT` → NOT_READY. `EXECUTION_SESSION_REQUEST_BLOCKED` → BLOCKED. `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS` → may proceed to classification.

**request_validity**: Describes whether the request conforms to the 58.2 contract. Allowed values: `REQUEST_VALID`, `REQUEST_INVALID`, `REQUEST_MALFORMED`, `REQUEST_MISSING`, `REQUEST_NEEDS_REVIEW`. Only `REQUEST_VALID` may proceed without blocker.

**authorization_consistency**: Confirms request does not invent or contradict M57 authorization. Allowed values: `AUTHORIZATION_CONSISTENT`, `AUTHORIZATION_LIMITED_BUT_CONSISTENT`, `AUTHORIZATION_MISSING`, `AUTHORIZATION_CONTRADICTORY`, `AUTHORIZATION_UNKNOWN`. `CONSISTENT` may proceed. `LIMITED_BUT_CONSISTENT` may proceed with warning. `MISSING`, `CONTRADICTORY`, `UNKNOWN` must block or require review.

**source_artifact_checks**: Object with boolean check results for each required source artifact. See Source Artifact Checks.

**request_field_checks**: Object with boolean check results for each required 58.2 request field. See Request Validity Checks.

**boundary_input_checks**: Object with boolean check results for boundary input availability. See Boundary Input Checks.

**forbidden_action_checks**: Object with boolean check results for forbidden premature actions. All must be `false` to proceed. See Forbidden Action Checks.

**premature_downstream_artifact_checks**: Object with boolean check results for premature downstream artifacts. See Premature Downstream Artifact Checks.

**performed_actions**: Object declaring what actions were taken during preconditions checking. All values must be `false` for READY or READY_WITH_WARNINGS. See Performed Actions Checks.

**warnings**: List of non-blocking issues. May be empty. Must not hide blockers.

**blockers**: List of blocking issues. If non-empty, status must be BLOCKED.

**handoff_to_boundary_contract**: Boolean. `true` only when status is READY or READY_WITH_WARNINGS. `false` when NOT_READY or BLOCKED.

**non_authority_acknowledgement**: Must include required non-authority text.

## Allowed Preconditions Statuses

- `EXECUTION_SESSION_PRECONDITIONS_READY` — All checks pass. Request may proceed to 58.4 boundary evaluation.
- `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS` — Checks pass with non-blocking warnings. Request may proceed to 58.4 with warnings preserved.
- `EXECUTION_SESSION_PRECONDITIONS_NOT_READY` — Required information is incomplete but not unsafe. Request must not proceed.
- `EXECUTION_SESSION_PRECONDITIONS_BLOCKED` — Unsafe, contradictory, premature, unauthorized, or malformed conditions detected. Request must not proceed.

## Source Artifact Checks

The `source_artifact_checks` object must include:

```yaml
source_artifact_checks:
  m57_completion_review_exists: <true|false>
  m58_intake_report_exists: <true|false>
  m58_architecture_exists: <true|false>
  request_contract_exists: <true|false>
  request_schema_exists: <true|false>
  request_template_exists: <true|false>
  execution_session_request_exists: <true|false>
  source_paths_consistent: <true|false>
```

Any `false` value must contribute to blockers or warnings depending on criticality. Missing M57 or M58 intake artifacts must always block.

## Request Validity Checks

The `request_field_checks` object must include:

```yaml
request_field_checks:
  required_fields_present: <true|false>
  request_status_allowed: <true|false>
  requested_execution_mode_allowed: <true|false>
  requested_scope_present: <true|false>
  requested_write_paths_present: <true|false>
  requested_commands_present: <true|false>
  forbidden_commands_acknowledged: <true|false>
  protected_paths_acknowledged: <true|false>
  handoff_to_m59_required: <true|false>
  non_authority_acknowledgement_present: <true|false>
```

Any `false` value in a required check must produce a blocker or NOT_READY.

## Authorization Consistency Checks

The `authorization_consistency` field must reflect the result of comparing the request's authorization claim against the actual M57 completion review status.

Rules:
- `AUTHORIZATION_CONSISTENT` — request references and matches M57 COMPLETE status
- `AUTHORIZATION_LIMITED_BUT_CONSISTENT` — request references M57 COMPLETE_WITH_WARNINGS, limitation is preserved
- `AUTHORIZATION_MISSING` — request does not reference M57 completion
- `AUTHORIZATION_CONTRADICTORY` — request claims authorization that contradicts M57 status
- `AUTHORIZATION_UNKNOWN` — cannot determine consistency

Missing, contradictory, and unknown values must block or require review before 58.4.

## Boundary Input Checks

The `boundary_input_checks` object must include:

```yaml
boundary_input_checks:
  scope_input_available: <true|false>
  write_path_input_available: <true|false>
  command_input_available: <true|false>
  protected_path_input_available: <true|false>
  session_state_input_available: <true|false>
  boundary_evaluation_possible: <true|false>
```

Missing boundary input must prevent progression to 58.4. Boundary input availability is not boundary approval.

## Forbidden Action Checks

The `forbidden_action_checks` object must include:

```yaml
forbidden_action_checks:
  execution_already_started: <true|false>
  execution_session_already_open: <true|false>
  task_marked_complete: <true|false>
  approval_created: <true|false>
  lifecycle_mutation_performed: <true|false>
  commit_created: <true|false>
  push_performed: <true|false>
  merge_performed: <true|false>
  result_verification_claimed: <true|false>
```

All values must be `false` to proceed. Any `true` value must produce BLOCKED.

## Premature Downstream Artifact Checks

The `premature_downstream_artifact_checks` object must include:

```yaml
premature_downstream_artifact_checks:
  m58_boundary_contract_created: <true|false>
  m58_policy_created: <true|false>
  m58_cli_created: <true|false>
  m58_fixtures_created: <true|false>
  m58_evidence_report_created: <true|false>
  m58_completion_review_created: <true|false>
  m59_artifact_created: <true|false>
```

Any premature downstream artifact must be classified as blocker unless explicitly expected from previously completed tasks.

## Performed Actions Checks

The `performed_actions` object must include:

```yaml
performed_actions:
  execution_session_started: false
  execution_session_opened: false
  execution_performed: false
  task_marked_done: false
  result_verified: false
  approval_record_created: false
  lifecycle_mutation_performed: false
  commit_created: false
  push_performed: false
  merge_performed: false
  m59_artifact_created: false
```

All values must be `false` for READY or READY_WITH_WARNINGS. Any `true` value must produce BLOCKED.

## Warning and Blocker Semantics

**Warnings** are non-blocking issues that must be recorded but do not prevent progression to 58.4. Warnings must be preserved in the 58.4 boundary contract.

**Blockers** are issues that prevent any progression. If `blockers` is non-empty, `preconditions_status` must be `EXECUTION_SESSION_PRECONDITIONS_BLOCKED` and `handoff_to_boundary_contract` must be `false`.

Warnings must not hide blockers. A warning about a condition that is actually unsafe must be reclassified as a blocker.

## Handoff to 58.4 Boundary Contract

`handoff_to_boundary_contract` governs whether the preconditions result artifact may be consumed by 58.4.

Rules:
- `true` allowed only when `preconditions_status` is `EXECUTION_SESSION_PRECONDITIONS_READY` or `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS`
- `false` required when `preconditions_status` is `EXECUTION_SESSION_PRECONDITIONS_NOT_READY` or `EXECUTION_SESSION_PRECONDITIONS_BLOCKED`

The handoff is a structural flag only. It does not open a session. It does not authorize execution.

## Non-Authority Rules

Every preconditions result artifact must include this exact non-authority acknowledgement:

> This execution session preconditions result does not open an execution session.
> This execution session preconditions result does not authorize execution.
> This execution session preconditions result does not approve task completion.
> This execution session preconditions result does not verify execution result.
> This execution session preconditions result does not mutate lifecycle state.
> This execution session preconditions result only determines whether the request may proceed to M58 boundary evaluation.

## Malformed Preconditions Conditions

A preconditions result is malformed if any of the following are true:

- `preconditions_id` is missing or empty
- `task_id` is missing or empty
- `request_id` is missing or empty
- `preconditions_status` is missing
- `preconditions_status` is an unknown value
- `source_references` is missing
- `request_validity` is missing
- `authorization_consistency` is missing
- `boundary_input_checks` is missing or incomplete
- `forbidden_action_checks` is missing or incomplete
- `performed_actions` is missing or incomplete
- `handoff_to_boundary_contract` is missing
- `non_authority_acknowledgement` is missing or does not contain required text
- Schema has invalid JSON structure
- Schema has extra top-level fields not allowed by `additionalProperties: false`

## Unsafe Preconditions Conditions

A preconditions result is unsafe if any of the following are true:

- M57 completion review is missing or blocked
- M58 intake is missing or blocked
- M58 architecture is missing or malformed
- Request contract is missing or malformed
- Execution session request is missing
- Request invents authorization not supported by M57
- Request contradicts M57 authorization status
- Request bypasses M58 intake check
- Request states M59 is optional
- Request claims execution session already open
- Request claims result already verified
- Request claims task already complete
- `performed_actions.execution_session_started` is `true`
- `performed_actions.lifecycle_mutation_performed` is `true`
- `performed_actions.approval_record_created` is `true`
- `performed_actions.commit_created` is `true`
- `performed_actions.push_performed` is `true`
- `performed_actions.merge_performed` is `true`
- Premature M59 artifact exists

## Relationship to 58.4 Boundary Contract

58.4 (Execution Session Boundary Contract) consumes a preconditions result artifact with status `EXECUTION_SESSION_PRECONDITIONS_READY` or `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS`. 58.4 will independently define:

- Scope boundary enforcement
- Command boundary enforcement
- Write path boundary enforcement
- Protected path boundary enforcement
- Session state boundary enforcement
- Session close boundary enforcement

This contract (58.3) defines the precondition checks only. 58.4 defines the boundary enforcement logic.

## Relationship to 58.6 Policy

58.6 (Controlled Execution Session Policy) will define the policy rules that govern how preconditions interact with boundary enforcement. This contract defines the data structures. Policy defines the decision rules.

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

FINAL_STATUS: M58_EXECUTION_SESSION_PRECONDITIONS_CONTRACT_DEFINED

This status means only that the preconditions contract exists.
It does not mean preconditions passed.
