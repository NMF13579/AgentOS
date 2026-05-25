---
type: contract
milestone: M54
task: 54.4
title: Task Candidate Queue Placement Materialization Output Contract
status: draft
authority: output-contract
created_for: M54
depends_on:
  - reports/m54-m53-readiness-intake.md
  - reports/m53-completion-review.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-INPUT-CONTRACT.md
  - docs/TASK-QUEUE-PLACEMENT-ARTIFACT-CONTRACT.md
queue_materialization_authorized: false
queue_placement_authorized_as_approval: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

## 1. Purpose

This document defines the M54 queue placement materialization output contract.

The output contract records materialization results only; it does not approve, activate, or execute a candidate.

## 2. Non-Authority Boundary

M54 output contract is not approval.
M54 output contract does not authorize execution.
M54 output contract does not authorize queue placement by itself.
M54 output contract does not authorize active-task replacement.
M54 output contract does not authorize lifecycle mutation.
M54 output contract does not authorize M54 materialization.
M54 output contract does not authorize M55.

## 3. Result Root Object

queue_placement_result:

All M54 queue placement materialization result packages must use queue_placement_result as the root object.

## 4. Required Top-Level Fields

result:
exit_code:
materialized:
queue_entry_created:
queue_entry_path:
checked_candidate_id:
source_m53_completion_review:
source_m53_placement_result:
source_m52_validation_result:
source_generated_candidate:
source_traceability:
carry_forward:
materialization_findings:
warnings:
blockers:
boundary_flags:
performed_actions:
non_authority_markers:

## 5. Result Tokens and Exit Codes

QUEUE_PLACEMENT_MATERIALIZED:
  exit_code: 0

QUEUE_PLACEMENT_MATERIALIZED_WITH_LIMITATIONS:
  exit_code: 0

QUEUE_PLACEMENT_NOT_MATERIALIZED:
  exit_code: 1

QUEUE_PLACEMENT_BLOCKED:
  exit_code: 2

The process exit code must match queue_placement_result.exit_code.

A successful exit code does not authorize approval, execution, active-task replacement, or M55.

## 6. Result Meaning

QUEUE_PLACEMENT_MATERIALIZED:
  materialized: true
  queue_entry_created: true

QUEUE_PLACEMENT_MATERIALIZED_WITH_LIMITATIONS:
  materialized: true
  queue_entry_created: true

QUEUE_PLACEMENT_NOT_MATERIALIZED:
  materialized: false
  queue_entry_created: false

QUEUE_PLACEMENT_BLOCKED:
  materialized: false
  queue_entry_created: false

Only QUEUE_PLACEMENT_MATERIALIZED and QUEUE_PLACEMENT_MATERIALIZED_WITH_LIMITATIONS may report queue_entry_created: true.

## 7. Queue Entry Path

queue_entry_path:

queue_entry_path must be under `tasks/queue/` when queue_entry_created is true.

queue_entry_path must be null when queue_entry_created is false.

queue_entry_path is not an active-task path.

## 8. Canonical Source Fields

source_m53_completion_review: reports/m53-completion-review.md
source_m53_placement_result: reports/m53-placement-review-result-agent-action-review.json
source_m52_validation_result:
source_generated_candidate:

The output result must preserve M52 validation and M53 placement review sources.

The output result must not invent missing upstream evidence.

## 9. Source Traceability

source_traceability:
  source_proposal:
  source_authorization:
  source_conversion_package:
  source_generated_artifact:
  m50_traceability:
  m51_generator_evidence:
  m52_validation_evidence:
  m53_placement_review_evidence:
  m54_materialization_evidence:

M54 output must not silently break upstream traceability.

## 10. Carry-Forward

carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

M54 output must not silently drop M53 or M54 carry-forward material.

## 11. Boundary Flags

boundary_flags:
  queue_materialization_only: true
  active_task_write_allowed: false
  execution_authorized: false
  approval_record_creation_allowed: false
  lifecycle_active_transition_allowed: false
  m55_start_authorized: false

M54 output may record queue materialization only; it must not authorize active-task writes, approval, execution, lifecycle activation, or M55.

## 12. Performed Actions

performed_actions:
  queue_entry_created:
  active_task_replacement_performed: false
  approval_created: false
  execution_started: false
  m55_started: false

M54 output must record performed actions without claiming approval, execution, active-task replacement, or M55 start.

performed_actions.queue_entry_created must match top-level queue_entry_created.

## 13. Non-Authority Markers

Queue placement is not approval.
Queue placement is not execution.
Queue placement is not active-task replacement.
Queue placement is not M55 authorization.

M54 output must include non-authority markers in every result.

## 14. Invalid Output Conditions

Output is invalid if:
1. `result` is not one of the allowed result tokens
2. `exit_code` does not match result token
3. `materialized` does not match result token
4. `queue_entry_created` does not match result token
5. `queue_entry_created` is true while `queue_entry_path` is null
6. `queue_entry_created` is false while `queue_entry_path` is not null
7. `queue_entry_path` is outside `tasks/queue/`
8. `queue_entry_path` points to `tasks/active-task.md`
9. `checked_candidate_id` is missing
10. source fields are missing
11. source traceability is incomplete
12. carry-forward fields are incomplete
13. `active_task_write_allowed` is true
14. `execution_authorized` is true
15. `approval_record_creation_allowed` is true
16. `lifecycle_active_transition_allowed` is true
17. `m55_start_authorized` is true
18. `active_task_replacement_performed` is true
19. `approval_created` is true
20. `execution_started` is true
21. `m55_started` is true
22. non-authority markers are missing
23. output claims approval
24. output claims execution permission
25. output claims active-task replacement
26. output claims M55 authorization
27. `performed_actions.queue_entry_created` does not match top-level `queue_entry_created`

## 15. Relationship to Future M54 CLI

Only the future M54 materialization CLI may produce a materialization result.
This contract defines the result shape only.
This contract does not create a queue artifact.
This contract does not authorize a write operation.

Task 54.4 validation must verify cross-field consistency on the template JSON instance.

## 16. Relationship to M55

A materialized queue result is not an active task.
A materialized queue result is not approval.
A materialized queue result is not execution permission.
A materialized queue result is not M55 authorization.
M55 must independently validate any active-task or execution readiness transition.

## 17. Summary

M54 output contract defines materialization result structure only.

It does not place a candidate.
It does not approve a candidate.
It does not execute a candidate.
It does not replace active-task.md.
It does not authorize M55.
