---
type: contract
milestone: M57
task: 57.2
title: Execution Authorization Input Contract
status: draft
source_intake: reports/m57-m56-completion-intake.md
source_architecture: docs/TASK-EXECUTION-AUTHORIZATION-ARCHITECTURE.md
schema: schemas/task-execution-authorization-input.schema.json
template: templates/task-execution-authorization-input.md
authority: input-contract-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# Execution Authorization Input Contract

## 1. Purpose

This document defines the M57 execution authorization input contract.

## 2. Contract Summary

Authorization input is not authorization.
Authorization input does not authorize execution.
Authorization input does not start execution.
Authorization input does not start M58.
Authorization input does not create approval records.
Authorization input does not authorize lifecycle mutation.
Authorization input does not modify tasks/active-task.md.
Authorization input is not approval.
Authorization input is not M57 policy.
Authorization input is not CLI behavior.
Authorization input is not evidence approval.
M56 COMPLETE does not automatically authorize M58.
M56 COMPLETE_WITH_LIMITATIONS does not automatically authorize M58.
M58 planning may be considered only after M57 completion review.

## 3. Input Object Shape

The root object for the contract must be `execution_authorization_input`.

## 4. Required Fields

The nested object `execution_authorization_input` requires the following fields:
* `schema_version`
* `input_id`
* `source_m56_completion_review`
* `source_m56_evidence_report`
* `source_active_task`
* `authorization_request_status`
* `requested_execution_mode`
* `expected_execution_session_type`
* `required_traceability`
* `required_boundaries`
* `boundary_flags`
* `carry_forward_limitations`
* `warnings`
* `blockers`
* `non_authority_markers`

## 5. Authorization Request Statuses

Allowed status values for `authorization_request_status`:
* `EXECUTION_AUTHORIZATION_INPUT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_INPUT_NOT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_BLOCKED`

## 6. Requested Execution Modes

Allowed requested execution modes:
* `M58_PLANNING_ONLY`
* `CONTROLLED_EXECUTION_SESSION_PLANNING`
* `DRY_RUN_SESSION_PLANNING`

## 7. Expected Execution Session Types

Allowed expected execution session types:
* `CONTROLLED_EXECUTION_SESSION`
* `DRY_RUN_CONTROLLED_EXECUTION_SESSION`

## 8. Source References

Required source references must be defined exactly as follows:
* `source_m56_completion_review: reports/m56-completion-review.md`
* `source_m56_evidence_report: reports/m56-execution-readiness-evidence-report.md`
* `source_active_task: tasks/active-task.md`

## 9. Required Traceability

Inputs must link back to specific source milestone artifacts and verify the traceability chain.

## 10. Required Boundaries

Boundary verification logic must confirm that all non-authority constraints are respected.

## 11. Boundary Flags

Required boundary flags configuration:
* `authorization_input_only: true`
* `execution_authorized: false`
* `execution_started: false`
* `approval_created: false`
* `lifecycle_mutation_authorized: false`
* `m58_authorized: false`
* `m58_started: false`

## 12. Carry-Forward Limitations

The carry-forward limitations model tracks limitations inherited from M56 or M57 intake reports.

## 13. Warnings and Blockers

Warnings and blockers must be parsed from source artifacts and recorded in the input payload.

## 14. Non-Authority Markers

The following non-authority markers must be included in the submission:
* `M57 authorization input is not authorization.`
* `M57 authorization input does not authorize execution.`
* `M57 authorization input does not start execution.`
* `M57 authorization input does not create approval records.`
* `M57 authorization input does not authorize lifecycle mutation.`
* `M57 authorization input does not authorize M58.`
* `M57 authorization input does not start M58.`
* `M57 authorization input does not modify tasks/active-task.md.`
* `M58 must independently validate M57 completion before any M58 planning work.`

## 15. Malformed Input Handling

Malformed authorization input must fail closed.

## 16. Unknown Status Handling

Unknown authorization input status must fail closed.

## 17. Unsafe Authority Claims

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

## 18. Relationship to M56

The input contract maps structural completion indicators from M56 to the input status.

## 19. Relationship to M57 Policy

The contract prepares the input object for consumption by later M57 authorization policy evaluation.

## 20. Relationship to M57 CLI

The contract defines the schema and constraints that the CLI validates when checking execution authorization.

## 21. Relationship to M58

The input contract ensures that M58 cannot plan controlled execution sessions without verified input structure.

## 22. Summary

This document establishes the M57 execution authorization input contract.
Task 57.2 is complete.
