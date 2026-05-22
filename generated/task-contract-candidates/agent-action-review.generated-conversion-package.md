# Example Proposal-to-Task Conversion — Agent Action Review

## Example Boundary

Example conversion is not active execution.
Example conversion is not queue placement.
Example task contract candidate must not be copied into tasks/active-task.md.
Example task contract candidate must not be placed into tasks/queue/.
Example task contract candidate is not implementation approval.
Example task contract candidate is not approval evidence for execution.
M50 uses EXECUTION_SHAPE, not EXECUTION.
EXECUTION_SHAPE does not mean execution is authorized.
execution_authorized must remain false.
execution_permission_granted must remain false.
active_task_allowed must remain false.
task_queue_allowed must remain false.

## Source Scenario

Scenario: `agent-action-review`.
The scenario is a bounded review task-contract-proposal path focused on review artifact production only.
No implementation execution is authorized by this example.

## Source Proposal Reference

`source_task_contract_proposal: m49-agent-action-review-proposal-v1`

## Proposal Validation Reference

`proposal_validation_result: TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS`

## Source UX Contract Reference

`source_ux_contract: docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md#agent-action-review`

## Source Readiness Report Reference

`source_readiness_report: reports/m49-readiness-agent-action-review-reference-only.md`

## Source Boundary Policy Reference

`source_boundary_policy: docs/UX-TO-TASK-BOUNDARY-POLICY.md#m50-boundary`

## Conversion Package

```yaml
conversion_package:
  conversion_id: m50-example-conv-agent-action-review-001
  conversion_input_status: CONVERSION_INPUT_READY_WITH_LIMITATIONS
  source_task_contract_proposal: m49-agent-action-review-proposal-v1
  proposal_validation_result: TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS
  source_ux_contract: docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md#agent-action-review
  source_readiness_report: reports/m49-readiness-agent-action-review-reference-only.md
  source_boundary_policy: docs/UX-TO-TASK-BOUNDARY-POLICY.md#m50-boundary
  source_sections:
    - proposal.goal
    - proposal.scope
    - proposal.allowed_changes
    - proposal.forbidden_changes
    - proposal.validation
    - proposal.expected_final_report
    - proposal.risk_notes
  accepted_limitations:
    - review scope excludes runtime implementation and code execution
    - output remains review-artifact-only during M50
  open_questions:
    - should reviewer severity buckets be fixed or configurable in M51
    - should review artifact include mandatory trace IDs for every decision item
  downstream_limits:
    - placement review required before any queue or active-task lifecycle operation
    - no implementation authority is granted by M50 conversion
  non_authority_boundary:
    - conversion does not authorize execution
    - conversion does not authorize queue placement
    - conversion does not authorize active-task replacement
    - conversion does not authorize implementation
  human_authorization_record: example-human-auth-ref-agent-action-review-001
  conversion_scope: convert validated proposal into candidate ready for placement review only
  candidate_output: examples/task-contract-candidate-agent-action-review.md
  boundaries:
    conversion_input_ready_is_execution_permission: false
    conversion_input_ready_is_queue_permission: false
    conversion_input_ready_is_active_task_permission: false
    approval_record_creation_allowed: false
    execution_authorization_granted: false
```

## Example Human Authorization Reference

`human_authorization_record: example-human-auth-ref-agent-action-review-001`

## Embedded Example Authorization Summary

```yaml
human_authorization:
  authorization_id: example-human-auth-ref-agent-action-review-001
  authorization_type: proposal_to_task_contract_candidate_conversion
  source_proposal: m49-agent-action-review-proposal-v1
  authorized_scope: conversion of the validated proposal into task contract candidate ready for placement review only
  not_authorized:
    - execution
    - queue placement
    - active-task replacement
    - implementation
    - commit
    - push
    - merge
    - deploy
    - release
    - approval record creation by agent, validator, script, or system
  authorized_by: human-operator
  authorized_at: 2026-05-22T00:00:00Z
  authorization_status: AUTHORIZATION_VALID
  expires_at: 2099-12-31T23:59:59Z
  evidence_reference: example-only-human-authorization-reference-not-approval-record
  boundaries:
    conversion_only: true
    execution_approval_granted: false
    queue_placement_approval_granted: false
    active_task_replacement_approval_granted: false
    implementation_approval_granted: false
    approval_record_creation_allowed: false
```

`expires_at: 2099-12-31T23:59:59Z is used here as an example-only far-future value for deterministic validation.`
`It is not a recommended real authorization expiration value.`
`It does not create open-ended authorization.`

## Candidate Output Reference

`candidate_output: examples/task-contract-candidate-agent-action-review.md`

## Embedded Task Contract Candidate Summary

```yaml
task_contract_candidate:
  task_id: m50-example-task-agent-action-review-001
  source_proposal: m49-agent-action-review-proposal-v1
  source_authorization: example-human-auth-ref-agent-action-review-001
  mode: EXECUTION_SHAPE
  goal:
    - produce bounded review artifact for agent-action-review proposal scope
    - preserve source constraints, limits, and validation requirements
  scope:
    - analyze agent actions defined in the source proposal only
    - produce structured review artifact only
  allowed_changes:
    - create review artifact at approved target path from proposal scope
    - format reviewer findings according to source validation requirements
  forbidden_changes:
    - no queue placement
    - no active-task replacement
    - no implementation execution
    - no approval record creation
  validation:
    - verify source traceability links are preserved
    - verify carry-forward fields are preserved and non-empty
    - verify boundary flags remain fixed and non-authorizing
  expected_final_report:
    - summary of reviewed actions
    - bounded risk notes aligned with source proposal
    - unresolved open questions preserved
  carry_forward:
    accepted_limitations:
      - review scope excludes runtime implementation and code execution
      - output remains review-artifact-only during M50
    open_questions:
      - should reviewer severity buckets be fixed or configurable in M51
      - should review artifact include mandatory trace IDs for every decision item
    downstream_limits:
      - placement review required before any queue or active-task lifecycle operation
      - no implementation authority is granted by M50 conversion
    non_authority_boundary:
      - conversion does not authorize execution
      - conversion does not authorize queue placement
      - conversion does not authorize active-task replacement
      - conversion does not authorize implementation
  boundaries:
    conversion_validated: true
    executable_contract_shape: true
    candidate_ready_for_placement_review: true
    placement_review_required: true
    execution_authorized: false
    execution_permission_granted: false
    active_task_allowed: false
    task_queue_allowed: false
```

## Carry-Forward Preservation

- accepted_limitations preserved
- open_questions preserved
- downstream_limits preserved
- non_authority_boundary preserved
- source traceability preserved
- forbidden_changes preserved
- validation requirements preserved

## Non-Authority Boundary

- no execution authorization
- no queue placement authorization
- no active-task replacement authorization
- no implementation authorization

## Validator Compatibility Notes

Boundary values set to false are required and must not be treated as forbidden patterns.
Only corresponding true values are forbidden.
Validator 50.6 rejects forbidden actor names only when they appear in authorization provenance/source fields such as authorized_by, decision_source, or equivalent provenance fields.
The not_authorized field may mention forbidden actors as actors that are not allowed to authorize conversion, execution, queue placement, active-task replacement, or implementation.

## Validator Expected Result

`python3 scripts/validate-proposal-to-task-conversion.py --conversion examples/proposal-to-task-conversion-agent-action-review.md`

Expected result token:
`PROPOSAL_TO_TASK_CONVERSION_VALIDATION_OK`

## Explicit Non-Goals

Task 50.7 does not do:

- create real approval records
- create files under approvals/
- create active tasks
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create validators
- create schemas
- create templates
- create fixtures
- create reports
- create completion reviews
- commit
- push
- merge
- deploy
- release
