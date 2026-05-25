# Controlled Execution Session Policy

## Purpose

This document defines the M58 Controlled Execution Session Policy.

The policy classifies whether the controlled execution session chain is ready, not ready, ready with warnings, or blocked. It does not open an execution session. It does not authorize task completion. It does not verify execution result. It does not approve merge, push, or release. It does not mutate lifecycle state.

Policy readiness is not execution approval.
Policy readiness is not task completion approval.
Policy readiness is not result verification.

## Preconditions

This policy applies only when all of the following are present and valid:

- `reports/m58-m57-completion-intake.md` with `MAY_PROCEED_TO_M58_PLANNING: true`
- `docs/CONTROLLED-EXECUTION-SESSION-ARCHITECTURE.md` with `FINAL_STATUS: M58_ARCHITECTURE_DEFINED`
- `docs/EXECUTION-SESSION-REQUEST-CONTRACT.md` with `FINAL_STATUS: M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED`
- `schemas/execution-session-request.schema.json` (valid JSON)
- `docs/EXECUTION-SESSION-PRECONDITIONS-CONTRACT.md` with `FINAL_STATUS: M58_EXECUTION_SESSION_PRECONDITIONS_CONTRACT_DEFINED`
- `schemas/execution-session-preconditions.schema.json` (valid JSON)
- `docs/EXECUTION-SESSION-BOUNDARY-CONTRACT.md` with `FINAL_STATUS: M58_EXECUTION_SESSION_BOUNDARY_CONTRACT_DEFINED`
- `schemas/execution-session-boundary.schema.json` (valid JSON)
- `docs/EXECUTION-SESSION-RECORD-OUTPUT-CONTRACT.md` with `FINAL_STATUS: M58_EXECUTION_SESSION_RECORD_OUTPUT_CONTRACT_DEFINED`
- `schemas/execution-session-record-output.schema.json` (valid JSON)

## Position in M58

This is task 58.6. It follows 58.5 (Record / Output Contract) and precedes 58.7 (CLI).

The policy document is consumed by 58.7 (CLI) as the authoritative rule set for classifying execution session readiness. It does not implement the CLI itself.

## Policy Inputs

The policy evaluates these inputs:

```yaml
policy_input:
  request_status:           # from 58.2 request artifact
  preconditions_status:     # from 58.3 preconditions result artifact
  boundary_status:          # from 58.4 boundary result artifact
  record_status:            # from 58.5 record/output artifact
  m57_completion_status:    # from M57 completion review
  m58_intake_status:        # from M58 intake report
  architecture_status:      # from M58 architecture doc
  request_contract_status:  # from M58 request contract
  preconditions_contract_status:  # from M58 preconditions contract
  boundary_contract_status: # from M58 boundary contract
  record_output_contract_status:  # from M58 record/output contract
  warnings:                 # accumulated warnings from all layers
  blockers:                 # accumulated blockers from all layers
  performed_actions:        # from 58.3 preconditions result
  forbidden_action_checks:  # from 58.3 preconditions result
  premature_downstream_artifact_checks:  # from 58.3 preconditions result
  m59_handoff:              # from 58.5 record/output artifact
```

All inputs are read-only. The policy does not mutate any artifact. Missing or malformed inputs fail closed.

## Allowed Policy Decisions

The policy produces exactly one of these decisions:

- `M58_SESSION_POLICY_READY` — The controlled execution session chain is structurally ready for future CLI handling.
- `M58_SESSION_POLICY_READY_WITH_WARNINGS` — The chain is structurally ready for future CLI handling with warnings preserved.
- `M58_SESSION_POLICY_NOT_READY` — Required information is incomplete but not unsafe.
- `M58_SESSION_POLICY_BLOCKED` — Unsafe, contradictory, unauthorized, premature, or forbidden conditions were detected.

Policy readiness is not execution approval.
Policy readiness is not task completion approval.
Policy readiness is not result verification.

## Decision Priority Order

`BLOCKED > NOT_READY > READY_WITH_WARNINGS > READY`

Rules:

- Any blocker must produce `M58_SESSION_POLICY_BLOCKED`.
- Any unsafe condition must produce `M58_SESSION_POLICY_BLOCKED`.
- Any forbidden action must produce `M58_SESSION_POLICY_BLOCKED`.
- Any premature M59 artifact must produce `M58_SESSION_POLICY_BLOCKED`.
- Missing required input must produce `M58_SESSION_POLICY_NOT_READY` or `M58_SESSION_POLICY_BLOCKED` depending on severity.
- Warnings must not hide blockers.
- Unknown values must fail closed.

## Request Status Interpretation

| Request Status | Policy Interpretation |
|---|---|
| `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS` | May proceed if other layers are clean |
| `EXECUTION_SESSION_REQUEST_DRAFT` | NOT_READY |
| `EXECUTION_SESSION_REQUEST_BLOCKED` | BLOCKED |
| missing | BLOCKED |
| unknown | BLOCKED |
| malformed | BLOCKED |

## Preconditions Status Interpretation

| Preconditions Status | Policy Interpretation |
|---|---|
| `EXECUTION_SESSION_PRECONDITIONS_READY` | May proceed if other layers are clean |
| `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS` | READY_WITH_WARNINGS candidate |
| `EXECUTION_SESSION_PRECONDITIONS_NOT_READY` | NOT_READY |
| `EXECUTION_SESSION_PRECONDITIONS_BLOCKED` | BLOCKED |
| missing | BLOCKED |
| unknown | BLOCKED |
| malformed | BLOCKED |

## Boundary Status Interpretation

| Boundary Status | Policy Interpretation |
|---|---|
| `EXECUTION_SESSION_BOUNDARY_SATISFIED` | May proceed if other layers are clean |
| `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS` | READY_WITH_WARNINGS candidate |
| `EXECUTION_SESSION_BOUNDARY_NOT_SATISFIED` | NOT_READY |
| `EXECUTION_SESSION_BOUNDARY_BLOCKED` | BLOCKED |
| missing | BLOCKED |
| unknown | BLOCKED |
| malformed | BLOCKED |

## Record / Output Status Interpretation

| Record/Output Status | Policy Interpretation |
|---|---|
| `EXECUTION_SESSION_RECORD_READY_FOR_POLICY` | May proceed if other layers are clean |
| `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION` | May proceed only as M59 handoff candidate |
| `EXECUTION_SESSION_RECORD_DRAFT` | NOT_READY |
| `EXECUTION_SESSION_RECORD_BLOCKED` | BLOCKED |
| `EXECUTION_SESSION_RECORD_ABORTED` | BLOCKED |
| missing | BLOCKED |
| unknown | BLOCKED |
| malformed | BLOCKED |

**Important:** `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION` does not mean the task is complete. It means only that a controlled execution session record is ready to be passed to M59 verification.

## M57 and M58 Source Status Interpretation

| Status | Policy Interpretation |
|---|---|
| `M57_EXECUTION_AUTHORIZATION_COMPLETE` | May proceed if other layers are clean |
| `M57_EXECUTION_AUTHORIZATION_COMPLETE_WITH_WARNINGS` | READY_WITH_WARNINGS candidate |
| `M57_EXECUTION_AUTHORIZATION_INCOMPLETE` | NOT_READY |
| `M57_EXECUTION_AUTHORIZATION_BLOCKED` | BLOCKED |
| `M58_INTAKE_READY` | May proceed if other layers are clean |
| `M58_INTAKE_READY_WITH_WARNINGS` | READY_WITH_WARNINGS candidate |
| `M58_INTAKE_BLOCKED` | BLOCKED |
| `M58_ARCHITECTURE_DEFINED` | May proceed if other layers are clean |
| `M58_EXECUTION_SESSION_REQUEST_CONTRACT_DEFINED` | May proceed if other layers are clean |
| `M58_EXECUTION_SESSION_PRECONDITIONS_CONTRACT_DEFINED` | May proceed if other layers are clean |
| `M58_EXECUTION_SESSION_BOUNDARY_CONTRACT_DEFINED` | May proceed if other layers are clean |
| `M58_EXECUTION_SESSION_RECORD_OUTPUT_CONTRACT_DEFINED` | May proceed if other layers are clean |
| missing, malformed, or unknown | Fail closed → BLOCKED |

## Blocker Rules

The policy must produce `M58_SESSION_POLICY_BLOCKED` if any of the following are detected:

- Blocker list is non-empty
- M57 completion is blocked or missing
- M58 intake is blocked or missing
- Request is blocked, missing, or malformed
- Preconditions are blocked, missing, or malformed
- Boundary is blocked, missing, or malformed
- Record/output is blocked, aborted, missing, or malformed
- Authorization is missing, contradictory, or invented
- `performed_actions.execution_session_started: true`
- `performed_actions.execution_session_opened: true`
- `performed_actions.execution_performed: true`
- `performed_actions.task_marked_done: true`
- `performed_actions.result_verified` is true
- `performed_actions.approval_record_created: true`
- `performed_actions.lifecycle_mutation_performed: true`
- `performed_actions.commit_created: true`
- `performed_actions.push_performed: true`
- `performed_actions.merge_performed: true`
- `performed_actions.m59_artifact_created: true`
- Task marked complete
- Result verification claimed
- Approval record created
- Lifecycle mutation performed
- Commit created unexpectedly
- Push performed unexpectedly
- Merge performed unexpectedly
- Release performed unexpectedly
- M59 artifact created prematurely
- Protected path violation detected
- Forbidden command allowed (git push, git merge, git reset --hard, rm -rf, curl \| sh, wget \| sh)
- Dangerous command detected in `commands_allowed`
- M59 handoff disabled or claimed optional
- Human review replaced or bypassed
- Unapproved downstream task IDs beyond 58.13 introduced

## Not Ready Rules

The policy must produce `M58_SESSION_POLICY_NOT_READY` if all of the following hold:

- No unsafe condition is present
- No blocker is detected
- AND at least one of:
  - Request is draft
  - Preconditions are not ready
  - Boundary is not satisfied due to incomplete (not unsafe) information
  - Record/output is draft
  - Required source artifact is missing but no unsafe claim is present
  - Required field is incomplete but no unsafe claim is present
  - Boundary input is incomplete but not unsafe
  - M59 handoff is incomplete but not falsely disabled

If a missing artifact or field creates ambiguity around safety, classify as BLOCKED, not NOT_READY.

## Ready With Warnings Rules

The policy must produce `M58_SESSION_POLICY_READY_WITH_WARNINGS` if all of the following hold:

- All required layers are present
- No blockers exist
- No unsafe condition exists
- Request is `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS`
- Preconditions are `EXECUTION_SESSION_PRECONDITIONS_READY` or `EXECUTION_SESSION_PRECONDITIONS_READY_WITH_WARNINGS`
- Boundary is `EXECUTION_SESSION_BOUNDARY_SATISFIED` or `EXECUTION_SESSION_BOUNDARY_SATISFIED_WITH_WARNINGS`
- Record/output is `EXECUTION_SESSION_RECORD_READY_FOR_POLICY` or `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`
- At least one warning is present
- M59 handoff remains required

Warnings must be preserved for 58.7 CLI, 58.10 integration summary, 58.11 action review, and 58.12 evidence report.

## Ready Rules

The policy must produce `M58_SESSION_POLICY_READY` only if all of the following hold:

- All required layers are present
- All source statuses are valid
- Request status is `EXECUTION_SESSION_REQUEST_READY_FOR_PRECONDITIONS`
- Preconditions status is `EXECUTION_SESSION_PRECONDITIONS_READY`
- Boundary status is `EXECUTION_SESSION_BOUNDARY_SATISFIED`
- Record/output status is `EXECUTION_SESSION_RECORD_READY_FOR_POLICY` or `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`
- Warning list is empty
- Blocker list is empty
- All performed actions are safe (all `false`)
- No forbidden actions detected
- No premature downstream artifacts detected
- M59 handoff is required

## Performed Actions Policy

The policy must classify these as blockers if `true`:

```yaml
performed_actions:
  execution_session_started: true   -> BLOCKER
  execution_session_opened: true    -> BLOCKER
  execution_performed: true         -> BLOCKER
  task_marked_done: true            -> BLOCKER
  result_verified:  true             -> BLOCKER
  approval_record_created: true     -> BLOCKER
  lifecycle_mutation_performed: true -> BLOCKER
  commit_created: true              -> BLOCKER
  push_performed: true              -> BLOCKER
  merge_performed: true             -> BLOCKER
  m59_artifact_created: true        -> BLOCKER
```

For policy readiness before actual CLI/session handling, all these values must be `false` unless a later explicitly approved task changes the contract.

## Forbidden Action Policy

The policy must classify these as blockers if detected:

```yaml
forbidden_actions:
  approval_creation:             -> BLOCKER
  lifecycle_mutation:            -> BLOCKER
  task_completion_claim:         -> BLOCKER
  result_verification_claim:     -> BLOCKER
  commit:                        -> BLOCKER
  push:                          -> BLOCKER
  merge:                         -> BLOCKER
  release:                       -> BLOCKER
  m59_artifact_creation:         -> BLOCKER
  protected_path_violation:      -> BLOCKER
  raw_dangerous_command:         -> BLOCKER
```

## Premature Downstream Artifact Policy

The policy must produce `M58_SESSION_POLICY_BLOCKED` if any of the following exist prematurely:

- M58 CLI artifact before 58.7
- M58 fixtures before 58.8.1 / 58.8.2
- M58 fixture runner before 58.9
- M58 integration summary before 58.10
- M58 action review before 58.11
- M58 evidence report before 58.12
- M58 completion review before 58.13
- Any M59 verification artifact

Expected previous artifacts from 58.0–58.5 are not premature.

## M59 Handoff Policy

The policy requires M59 handoff.

Rules:

- `handoff_to_m59_required` must be `true`.
- `m59_handoff.handoff_required` must be `true`.
- M59 handoff is not M59 start.
- M59 handoff is not result verification.
- M59 handoff is not approval.
- Missing M59 handoff must produce `M58_SESSION_POLICY_NOT_READY` or `M58_SESSION_POLICY_BLOCKED` depending on severity.
- Claiming M59 is optional must produce `M58_SESSION_POLICY_BLOCKED`.

## Policy-to-Result Mapping

The policy maps decisions to CLI result codes as follows:

| Policy Decision | CLI Result |
|---|---|
| `M58_SESSION_POLICY_READY` | `CONTROLLED_EXECUTION_SESSION_READY` |
| `M58_SESSION_POLICY_READY_WITH_WARNINGS` | `CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS` |
| `M58_SESSION_POLICY_NOT_READY` | `CONTROLLED_EXECUTION_SESSION_NOT_READY` |
| `M58_SESSION_POLICY_BLOCKED` | `CONTROLLED_EXECUTION_SESSION_BLOCKED` |

## Exit Code Mapping for Future CLI

| CLI Result | Exit Code |
|---|---|
| `CONTROLLED_EXECUTION_SESSION_READY` | `exit 0` |
| `CONTROLLED_EXECUTION_SESSION_READY_WITH_WARNINGS` | `exit 0` |
| `CONTROLLED_EXECUTION_SESSION_NOT_READY` | `exit 1` |
| `CONTROLLED_EXECUTION_SESSION_BLOCKED` | `exit 2` |

Exit code 0 does not authorize execution.
Exit code 0 does not approve task completion.
Exit code 0 does not verify result.

## Fail-Closed Rules

The policy must fail closed for:

- Missing required artifact
- Malformed required artifact
- Unknown status value
- Unknown policy decision
- Contradictory statuses across layers
- Unsafe execution claim (session open, session started, result verified)
- Unsafe approval claim
- Unsafe result verification claim
- M59 optional claim
- Protected path ambiguity
- Allowed dangerous command ambiguity
- Lifecycle mutation ambiguity
- Unapproved downstream numbering expansion

**Fail closed means:**

- `M58_SESSION_POLICY_BLOCKED` when safety is ambiguous
- `M58_SESSION_POLICY_NOT_READY` only when incompleteness is clearly non-unsafe

## Non-Authority Rules

M58 policy does not open an execution session.
M58 policy does not authorize task completion.
M58 policy does not verify execution result.
M58 policy does not create approval.
M58 policy does not authorize merge, push, or release.
M58 policy does not mutate lifecycle state.
M58 policy only classifies controlled execution session readiness for future M58 CLI handling.

## Forbidden Claims

The policy document must not claim:

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
- release is allowed
- lifecycle state may be mutated

## Relationship to 58.7 CLI

58.7 (Controlled Execution Session CLI) must implement this policy document exactly. The CLI reads policy inputs from artifact files, applies the rules in this document in the defined priority order, and outputs one of the four policy decisions and its corresponding exit code. The CLI must not modify inputs or add new policy rules.

## Relationship to 58.10 Integration Summary

58.10 (Integration Summary) will reference this policy as the authority for readiness classification during the M58 chain. The integration summary must preserve all warnings recorded during policy evaluation.

## Relationship to 58.11 Action Review

58.11 (Action Review) will verify that the policy was applied correctly and that no forbidden actions were performed during M58. Action review consumes the policy decision and warnings as evidence.

## Relationship to 58.12 Evidence Report

58.12 (Evidence Report) will record the policy decision and its supporting evidence — all layer statuses, warnings, blockers, and handoff state — as structured M59 input. The evidence report must preserve the non-authority boundaries defined here.

## Final Policy Status

FINAL_STATUS: M58_CONTROLLED_EXECUTION_SESSION_POLICY_DEFINED

This status means only that the policy document exists.
It does not mean policy was executed by CLI.
It does not mean execution was authorized.
It does not mean result was verified.
