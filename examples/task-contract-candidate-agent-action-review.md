# Example Task Contract Candidate — Agent Action Review

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

## Source References

- source_proposal: `m49-agent-action-review-proposal-v1`
- source_authorization: `example-human-auth-ref-agent-action-review-001`
- scenario: `agent-action-review`

## Candidate Shape

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

## Goal

- produce review artifact only
- keep conversion and candidate boundaries intact

## Scope

- source-proposal bounded review scope only
- no implementation or lifecycle transitions

## Allowed Changes

- review-artifact generation within proposal scope
- formatting outputs required by validation rules

## Forbidden Changes

- queue placement
- active-task replacement
- implementation execution
- approval record creation

## Validation

- source traceability must be preserved
- carry-forward fields must remain present and non-empty
- forbidden_changes must remain preserved
- allowed_changes must not be expanded
- boundary flags must remain fixed

## Expected Final Report

- review summary
- preserved risk notes
- preserved open questions
- preserved downstream limits

## Carry-Forward

- accepted_limitations preserved
- open_questions preserved
- downstream_limits preserved
- non_authority_boundary preserved
- source traceability preserved

## Boundary Flags

- conversion_validated: true
- executable_contract_shape: true
- candidate_ready_for_placement_review: true
- placement_review_required: true
- execution_authorized: false
- execution_permission_granted: false
- active_task_allowed: false
- task_queue_allowed: false

## Non-Authority Boundary

- no execution authorization
- no queue placement authorization
- no active-task replacement authorization
- no implementation authorization

## Placement Review Boundary

Candidate is ready for placement review only.
This example is not an active task and not a queue entry.

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
