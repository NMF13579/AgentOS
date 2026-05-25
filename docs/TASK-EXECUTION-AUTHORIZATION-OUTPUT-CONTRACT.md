---
type: contract
milestone: M57
task: 57.4
title: Execution Authorization Output Contract
status: draft
source_intake: reports/m57-m56-completion-intake.md
source_architecture: docs/TASK-EXECUTION-AUTHORIZATION-ARCHITECTURE.md
source_input_contract: docs/TASK-EXECUTION-AUTHORIZATION-INPUT-CONTRACT.md
source_preconditions_contract: docs/TASK-EXECUTION-AUTHORIZATION-PRECONDITIONS-CONTRACT.md
schema: schemas/task-execution-authorization-result.schema.json
template: templates/task-execution-authorization-result.md
authority: output-contract-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# Execution Authorization Output Contract

## 1. Purpose

This document defines the M57 execution authorization output contract.

## 2. Contract Summary

Authorization result is not execution.
Authorization result does not authorize execution.
Authorization result does not start execution.
Authorization result does not start M58.
Authorization result does not create approval records.
Authorization result does not authorize lifecycle mutation.
Authorization result does not modify tasks/active-task.md.
Authorization result is not approval.
Authorization result is not M57 policy.
Authorization result is not CLI behavior by itself.
Authorization result is not evidence approval.
Exit code 0 is not execution.
Exit code 0 does not start M58.
Exit code 0 is not lifecycle mutation.
Exit code 0 is not approval.
M56 COMPLETE does not automatically authorize M58.
M56 COMPLETE_WITH_LIMITATIONS does not automatically authorize M58.
M58 planning may be considered only after M57 completion review.
Unknown authorization result status must fail closed.
Malformed authorization result must fail closed.
Unsafe authority claims must fail closed.
Premature M58 artifacts must fail closed.
Already-started execution must fail closed.

## 3. Result Object Shape

The root object for this contract must be `execution_authorization_result`.

## 4. Required Fields

The nested object `execution_authorization_result` requires the following fields:
* `schema_version`
* `result_id`
* `result`
* `exit_code`
* `source_m56_completion_review`
* `source_m56_evidence_report`
* `source_authorization_input`
* `source_authorization_preconditions`
* `source_active_task`
* `authorization_request_status`
* `preconditions_status`
* `m56_final_status`
* `m56_evidence_status`
* `traceability_result`
* `boundary_result`
* `performed_actions`
* `carry_forward_limitations`
* `warnings`
* `blockers`
* `non_authority_markers`

## 5. Result Statuses

Allowed authorization result statuses:
* `EXECUTION_AUTHORIZATION_CONFIRMED`
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_BLOCKED`

## 6. Exit Code Mapping

The exit code mapping is defined as:
* `EXECUTION_AUTHORIZATION_CONFIRMED -> 0`
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS -> 0`
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED -> 1`
* `EXECUTION_AUTHORIZATION_BLOCKED -> 2`

## 7. Result Status Semantics

* `EXECUTION_AUTHORIZATION_CONFIRMED ->` authorization may be recorded as confirmed for later M57 evidence only
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS ->` authorization may be recorded as confirmed with limitations for later M57 evidence only
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED ->` authorization is not confirmed but not necessarily unsafe
* `EXECUTION_AUTHORIZATION_BLOCKED ->` authorization must fail closed due to unsafe, malformed, contradictory, or boundary-violating input

## 8. Source Carry-Forward

Required source reference values:
```yaml
source_m56_completion_review: reports/m56-completion-review.md
source_m56_evidence_report: reports/m56-execution-readiness-evidence-report.md
source_authorization_input: templates/task-execution-authorization-input.md
source_authorization_preconditions: templates/task-execution-authorization-preconditions.md
source_active_task: tasks/active-task.md
```

## 9. Input Status Carry-Forward

Required input statuses:
* `EXECUTION_AUTHORIZATION_INPUT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_INPUT_NOT_READY`
* `EXECUTION_AUTHORIZATION_INPUT_BLOCKED`

## 10. Preconditions Status Carry-Forward

Required preconditions statuses:
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED`

## 11. M56 Completion Status Carry-Forward

Required M56 completion statuses:
* `M56_EXECUTION_READINESS_COMPLETE`
* `M56_EXECUTION_READINESS_COMPLETE_WITH_LIMITATIONS`
* `M56_EXECUTION_READINESS_INCOMPLETE`
* `M56_EXECUTION_READINESS_BLOCKED`

## 12. M56 Evidence Status Carry-Forward

Required M56 evidence statuses:
* `M56_EXECUTION_READINESS_EVIDENCE_READY`
* `M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING`
* `M56_EXECUTION_READINESS_EVIDENCE_BLOCKED`

## 13. Traceability Result

The output object tracks links back to specific source milestone artifacts and verifies the traceability chain.

## 14. Boundary Result

`boundary_result` required fields:
```yaml
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
```

## 15. Performed Actions Result

`performed_actions` required fields:
```yaml
active_task_modified: false
approval_record_created: false
lifecycle_mutation_performed: false
execution_started: false
m58_artifact_created: false
m58_started: false
```

## 16. Warnings, Blockers, and Limitations

Warnings, blockers, and limitations must be collected from previous steps and carried forward to the result object.

## 17. Non-Authority Markers

Required non-authority markers:
* `M57 authorization result is not execution.`
* `M57 authorization result does not authorize execution.`
* `M57 authorization result does not start execution.`
* `M57 authorization result does not create approval records.`
* `M57 authorization result does not authorize lifecycle mutation.`
* `M57 authorization result does not authorize M58.`
* `M57 authorization result does not start M58.`
* `M57 authorization result does not modify tasks/active-task.md.`
* `M58 must independently validate M57 completion before any M58 planning work.`

## 18. Malformed Source Handling

Malformed authorization result must fail closed.

## 19. Unknown Status Handling

Unknown authorization result status must fail closed.

## 20. Unsafe Authority Claims

Unsafe authority claims must fail closed.
The later M57 layers must block unsafe authority claims equivalent to:
* `execution is approved`
* `execution is authorized`
* `M58 is authorized`
* `M58 may start`
* `M58 started`
* `approval has been created`
* `lifecycle mutation has been authorized`
* `tasks/active-task.md was modified by M57`

## 21. Fail-Closed Semantics

Any error, unknown status, malformed source, unsafe claim, premature M58 artifact, or already-started execution must fail closed.

## 22. Relationship to M56

The output contract carry forward verification checks the final status and evidence of M56 execution readiness.
* M56_EXECUTION_READINESS_INCOMPLETE must be classified as EXECUTION_AUTHORIZATION_NOT_CONFIRMED by later policy, not as a successful authorization.
* M56_EXECUTION_READINESS_BLOCKED must be classified as EXECUTION_AUTHORIZATION_BLOCKED by later policy.

## 23. Relationship to M57 Policy

The output contract defines the schema of the results generated by policy evaluation.

## 24. Relationship to M57 CLI

The M57 CLI validates output data structures against this contract.

## 25. Relationship to M58

The output contract ensures that no M58 session planning can occur without a confirmed authorization result structure.

## 26. Summary

This section provides a summary of the relationship and structure defined above.

## 27. Known Accepted Risks

Timeout handling in M56 readiness layer was not directly exercised in fixture-matrix validation during the M56 stage. This limitation is accepted. It does not block M57 authorization output contract definition.

This closes the carry-forward limitation that has been tracked since task 57.0.

## 28. Summary

This document establishes the M57 execution authorization output contract.
Task 57.4 is complete.

## Final Status

FINAL_STATUS: M57_OUTPUT_CONTRACT_DEFINED
may_proceed_to_57_5: true

This means only that the output contract document,
JSON schema, and template exist and are valid.
It does not mean execution is authorized.
It does not mean M57 is complete.
It does not mean M58 may start.
