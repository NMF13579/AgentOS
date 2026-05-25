---
type: contract
milestone: M57
task: 57.3
title: Execution Authorization Preconditions Contract
status: draft
source_intake: reports/m57-m56-completion-intake.md
source_architecture: docs/TASK-EXECUTION-AUTHORIZATION-ARCHITECTURE.md
source_input_contract: docs/TASK-EXECUTION-AUTHORIZATION-INPUT-CONTRACT.md
schema: schemas/task-execution-authorization-preconditions.schema.json
template: templates/task-execution-authorization-preconditions.md
authority: preconditions-contract-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# Execution Authorization Preconditions Contract

## 1. Purpose

This document defines the M57 execution authorization preconditions contract.

## 2. Contract Summary

Authorization preconditions are not authorization.
Authorization preconditions do not authorize execution.
Authorization preconditions do not start execution.
Authorization preconditions do not start M58.
Authorization preconditions do not create approval records.
Authorization preconditions do not authorize lifecycle mutation.
Authorization preconditions do not modify tasks/active-task.md.
Authorization preconditions are not approval.
Authorization preconditions are not M57 policy.
Authorization preconditions are not CLI behavior.
Authorization preconditions are not evidence approval.
M56 COMPLETE does not automatically authorize M58.
M56 COMPLETE_WITH_LIMITATIONS does not automatically authorize M58.
M58 planning may be considered only after M57 completion review.

## 3. Preconditions Object Shape

The root object for this contract is `execution_authorization_preconditions`.

## 4. Required Fields

The nested object `execution_authorization_preconditions` requires the following fields:
* `schema_version`
* `preconditions_id`
* `source_m56_completion_review`
* `source_m56_evidence_report`
* `source_authorization_input`
* `source_active_task`
* `preconditions_status`
* `required_sources`
* `required_traceability`
* `required_boundaries`
* `boundary_flags`
* `performed_actions`
* `carry_forward_limitations`
* `warnings`
* `blockers`
* `non_authority_markers`

## 5. Preconditions Statuses

Allowed status values for `preconditions_status`:
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED`

Preconditions status semantics:
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS` -> preconditions are structurally and semantically ready for later authorization policy evaluation
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS` -> preconditions are ready but carry warnings or limitations forward
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY` -> preconditions are incomplete but not unsafe
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED` -> preconditions are unsafe, malformed, contradictory, or boundary-violating

Important boundary:
* Authorization preconditions are not authorization.
* Authorization preconditions do not start M58.
* Authorization preconditions do not authorize execution.
* Authorization preconditions do not create approval records.
* Authorization preconditions do not mutate lifecycle state.

## 6. Required Sources

Required source reference values must be defined exactly as follows:
* `source_m56_completion_review: reports/m56-completion-review.md`
* `source_m56_evidence_report: reports/m56-execution-readiness-evidence-report.md`
* `source_authorization_input: templates/task-execution-authorization-input.md`
* `source_active_task: tasks/active-task.md`

## 7. M56 Completion Preconditions

The preconditions check must verify that M56 completion review status is one of the allowed readiness statuses:
* `M56_EXECUTION_READINESS_COMPLETE`
* `M56_EXECUTION_READINESS_COMPLETE_WITH_LIMITATIONS`
* `M56_EXECUTION_READINESS_INCOMPLETE`
* `M56_EXECUTION_READINESS_BLOCKED`

Policy distinctions for completion status:
* M56_EXECUTION_READINESS_INCOMPLETE must be classified as EXECUTION_AUTHORIZATION_NOT_CONFIRMED by later policy, not as a successful authorization.
* M56_EXECUTION_READINESS_BLOCKED must be classified as EXECUTION_AUTHORIZATION_BLOCKED by later policy.

## 8. M56 Evidence Preconditions

The preconditions check must verify the status of M56 evidence:
* `M56_EXECUTION_READINESS_EVIDENCE_READY`
* `M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING`
* `M56_EXECUTION_READINESS_EVIDENCE_BLOCKED`

## 9. Authorization Input Preconditions

The preconditions check must verify the status of the authorization input contract:
* `EXECUTION_AUTHORIZATION_INPUT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_INPUT_NOT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_BLOCKED`

## 10. Traceability Preconditions

Preconditions must link back to specific source milestone artifacts and verify the traceability chain.

## 11. Boundary Preconditions

Boundary preconditions check must verify that all non-authority constraints are respected.

Required boundary flags:
* `authorization_preconditions_only: true`
* `execution_authorized: false`
* `execution_started: false`
* `approval_created: false`
* `lifecycle_mutation_authorized: false`
* `m58_authorized: false`
* `m58_started: false`

## 12. No Premature M58 Preconditions

No M58 artifacts must exist prior to authorization. Premature M58 artifacts must fail closed.

## 13. No Execution Started Preconditions

No execution must have started prior to authorization. Already-started execution must fail closed.

## 14. No Approval Records Preconditions

No approval records must have been created.

## 15. No Lifecycle Mutation Preconditions

No lifecycle mutations must have occurred.

## 16. Performed Actions

Required performed actions fields:
* `active_task_modified: false`
* `approval_record_created: false`
* `lifecycle_mutation_performed: false`
* `execution_started: false`
* `m58_artifact_created: false`
* `m58_started: false`

## 17. Carry-Forward Limitations

The carry-forward limitations model tracks limitations inherited from M56 or M57 intake reports.

## 18. Warnings and Blockers

Warnings and blockers must be parsed from source artifacts and recorded in the preconditions payload.

## 19. Non-Authority Markers

The following non-authority markers must be included in the preconditions object:
* `M57 authorization preconditions are not authorization.`
* `M57 authorization preconditions do not authorize execution.`
* `M57 authorization preconditions do not start execution.`
* `M57 authorization preconditions do not create approval records.`
* `M57 authorization preconditions do not authorize lifecycle mutation.`
* `M57 authorization preconditions do not authorize M58.`
* `M57 authorization preconditions do not start M58.`
* `M57 authorization preconditions do not modify tasks/active-task.md.`
* `M58 must independently validate M57 completion before any M58 planning work.`

## 20. Malformed Preconditions Handling

Malformed authorization preconditions must fail closed.

## 21. Unknown Status Handling

Unknown authorization preconditions status must fail closed.

## 22. Unsafe Authority Claims

Unsafe authority claims must fail closed.
This list represents unsafe authority claims that later M57 layers must block:
* `execution is approved`
* `execution is authorized`
* `M58 is authorized`
* `M58 may start`
* `M58 started`
* `approval has been created`
* `lifecycle mutation has been authorized`
* `tasks/active-task.md was modified by M57`

## 23. Relationship to M56

The preconditions contract directly checks the completion review and evidence status of M56 execution readiness.

## 24. Relationship to M57 Input Contract

The preconditions contract checks the input contract status defined in Task 57.2.

## 25. Relationship to M57 Policy

The preconditions contract structures the validated input fields for downstream policy checks.

## 26. Relationship to M57 CLI

The contract defines the schema checked by the CLI when verifying preconditions.

## 27. Relationship to M58

The preconditions contract prevents any M58 session planning until preconditions pass.

## 28. Summary

This document establishes the M57 execution authorization preconditions contract.
Task 57.3 is complete.
