# Task Contract Candidate Model

## Purpose

Define the M50 task contract candidate model for placement review readiness.
This model is a controlled candidate shape only and does not grant lifecycle execution permissions.

## Candidate Boundary

Task contract candidate is not active task state.
Task contract candidate is not queue entry.
Task contract candidate must not be copied into tasks/active-task.md by M50.
Task contract candidate must not be placed into tasks/queue/ by M50.

## Required Candidate Shape

```yaml
task_contract_candidate:
  task_id:
  source_proposal:
  source_authorization:
  mode: EXECUTION_SHAPE
  goal:
  scope:
  allowed_changes:
  forbidden_changes:
  validation:
  expected_final_report:
  carry_forward:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
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

## Required Fields

- task_id
- source_proposal
- source_authorization
- mode
- goal
- scope
- allowed_changes
- forbidden_changes
- validation
- expected_final_report
- carry_forward
- carry_forward.accepted_limitations
- carry_forward.open_questions
- carry_forward.downstream_limits
- carry_forward.non_authority_boundary
- boundaries
- boundaries.conversion_validated
- boundaries.executable_contract_shape
- boundaries.candidate_ready_for_placement_review
- boundaries.placement_review_required
- boundaries.execution_authorized
- boundaries.execution_permission_granted
- boundaries.active_task_allowed
- boundaries.task_queue_allowed

## Field Semantics

- task_id: candidate task identifier placeholder.
- source_proposal: required source proposal reference.
- source_authorization: required source authorization reference.
- mode: candidate mode; must be EXECUTION_SHAPE.
- goal: candidate goal derived from source proposal.
- scope: candidate scope derived from source proposal.
- allowed_changes: bounded allowed change set.
- forbidden_changes: bounded forbidden change set.
- validation: required validation requirements block.
- expected_final_report: required expected final report block.
- carry_forward: required carry-forward group.
- carry_forward.accepted_limitations: limitations preserved from source chain.
- carry_forward.open_questions: open questions preserved from source chain.
- carry_forward.downstream_limits: downstream limits preserved from source chain.
- carry_forward.non_authority_boundary: non-authority boundary preserved from source chain.
- boundaries: fixed lifecycle boundary flags.
- boundaries.conversion_validated: conversion validity indicator.
- boundaries.executable_contract_shape: executable-structure indicator.
- boundaries.candidate_ready_for_placement_review: placement review readiness indicator.
- boundaries.placement_review_required: mandatory later placement review indicator.
- boundaries.execution_authorized: execution authorization flag.
- boundaries.execution_permission_granted: lifecycle execution permission flag.
- boundaries.active_task_allowed: active-task replacement permission flag.
- boundaries.task_queue_allowed: queue placement permission flag.

## Mode Semantics

EXECUTION_SHAPE means the candidate has the structure of an executable task contract.
EXECUTION_SHAPE does not mean execution is authorized.
EXECUTION_SHAPE does not allow queue placement.
EXECUTION_SHAPE does not allow active-task replacement.
EXECUTION_SHAPE does not allow implementation.
M50 uses EXECUTION_SHAPE, not EXECUTION.
mode must be EXECUTION_SHAPE.
mode must not be EXECUTION.

## Source Traceability Requirements

source_proposal is required.
source_authorization is required as a reference.
Source traceability must be preserved.

## Source Authorization Reference Boundary

source_authorization is not created by Task 50.4.
source_authorization does not authorize execution.
source_authorization does not authorize queue placement.
source_authorization does not authorize active-task replacement.

## Scope Requirements

Candidate scope must be derived from the source proposal.
Candidate scope must not silently expand proposal scope.
Candidate scope must preserve accepted limitations.
Candidate scope must preserve open questions.
Candidate scope must preserve downstream limits.
Candidate scope must preserve the non-authority boundary.

## Allowed Changes Requirements

allowed_changes must not be expanded beyond the source proposal and conversion scope.
A candidate that expands allowed changes is invalid.

## Forbidden Changes Requirements

forbidden_changes must not be weakened.
forbidden_changes must be preserved if present in the source proposal.
A candidate that weakens forbidden changes is invalid.

## Validation Requirements

Candidate validation must confirm source traceability, scope preservation, carry-forward preservation, and fixed boundary flag values.
Validation must reject any candidate that claims execution, queue placement, active-task replacement, or implementation approval.

## Carry-Forward Requirements

Accepted limitations must be carried forward.
Open questions must be carried forward.
Downstream limits must be carried forward.
Non-authority boundary must be carried forward.
Source traceability must be preserved.

## Boundary Flags

conversion_validated: true means the candidate was produced by a valid conversion process.
executable_contract_shape: true means the candidate has task-contract-like structure.
candidate_ready_for_placement_review: true means the candidate can be reviewed by a later placement gate.
placement_review_required: true means M50 cannot place this candidate into queue or active state.
execution_authorized: false means this candidate cannot be executed by M50.
execution_permission_granted: false means this candidate does not carry lifecycle execution permission.
active_task_allowed: false means this candidate cannot replace tasks/active-task.md in M50.
task_queue_allowed: false means this candidate cannot be placed into tasks/queue/ in M50.

execution_authorized must always be false in M50.
execution_permission_granted must always be false in M50.
active_task_allowed must always be false in M50.
task_queue_allowed must always be false in M50.

## Schema Contract

Schema file: `schemas/task-contract-candidate.schema.json`.
The schema must enforce:
- top-level `task_contract_candidate`;
- required fields;
- `mode` restricted to `EXECUTION_SHAPE`;
- required `carry_forward` set;
- required `boundaries` set;
- `const: true` for conversion/shape/review flags;
- `const: false` for execution/permission/placement flags;
- `additionalProperties: false` in all modeled objects.

## Non-Authority Rules

- This model does not authorize execution.
- This model does not authorize queue placement.
- This model does not authorize active-task replacement.
- This model does not authorize implementation.
- This model does not create approval records.

## Blocking Conditions

- source_proposal missing
- source_authorization missing
- mode is EXECUTION
- mode is not EXECUTION_SHAPE
- goal missing
- scope missing
- allowed_changes missing
- forbidden_changes missing
- validation missing
- expected_final_report missing
- accepted limitations dropped
- open questions dropped
- downstream limits dropped
- non-authority boundary missing
- source traceability missing
- allowed changes expanded
- forbidden changes weakened
- candidate claims execution authorization
- candidate grants execution permission
- candidate allows active task placement
- candidate allows queue placement
- candidate claims implementation approval
- candidate template treated as active task
- candidate template copied into tasks/active-task.md
- candidate template placed into tasks/queue/

## Explicit Non-Goals

Task 50.4 does not do:

- create real task contract candidate instances
- create active tasks
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create real approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create conversion packages
- modify conversion packages
- validate conversion packages
- validate candidates
- create validators
- create fixtures
- create examples
- create evidence reports
- create completion reviews
- commit
- push
- merge
- deploy
- release
