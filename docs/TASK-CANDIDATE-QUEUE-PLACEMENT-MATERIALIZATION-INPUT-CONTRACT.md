---
type: contract
milestone: M54
task: 54.2
title: Task Candidate Queue Placement Materialization Input Contract
status: draft
authority: input-contract
created_for: M54
depends_on:
  - reports/m54-m53-readiness-intake.md
  - reports/m53-completion-review.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-ARCHITECTURE.md
queue_materialization_authorized: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

## 1. Purpose

This document defines the M54 queue placement materialization input contract.

The input contract describes what M54 may review for future queue placement materialization; it does not materialize a queue entry.

## 2. Non-Authority Boundary

M54 input contract is not approval.
M54 input contract does not authorize execution.
M54 input contract does not authorize queue placement.
M54 input contract does not authorize active-task replacement.
M54 input contract does not authorize lifecycle mutation.
M54 input contract does not authorize M54 materialization.
M54 input contract does not authorize M55.

## 3. Contract Root Object

queue_placement_input:

All M54 queue placement materialization input packages must use queue_placement_input as the root object.

## 4. Required Top-Level Fields

input_id:
source_candidate_id:
source_m53_completion_review:
source_m53_evidence_report:
source_m53_integration_report:
source_m53_placement_result:
source_m52_completion_review:
source_m52_validation_result:
source_generated_candidate:
source_candidate_origin:
materialization_mode:
target_queue_dir:
target_queue_file:
required_traceability:
required_carry_forward:
pre_materialization_checks:
boundaries:

## 5. Canonical Source Fields

source_m53_completion_review: reports/m53-completion-review.md
source_m53_evidence_report: reports/m53-task-candidate-placement-review-evidence-report.md
source_m53_integration_report: reports/m53-task-candidate-placement-review-integration.md
source_m53_placement_result: reports/m53-placement-review-result-agent-action-review.json
source_m52_completion_review: reports/m52-completion-review.md

M53 completion is required input evidence, but M53 completion does not authorize materialization.

## 6. Candidate Origin and Mode

source_candidate_origin: M53_PLACEMENT_ELIGIBLE_CANDIDATE
materialization_mode: QUEUE_PLACEMENT_ONLY

QUEUE_PLACEMENT_ONLY forbids active-task replacement and execution start.

## 7. Target Queue Fields

target_queue_dir: tasks/queue/
target_queue_file:

target_queue_dir must resolve under `tasks/queue/`.

target_queue_file must be a safe filename, not a path.

The input contract alone cannot create `tasks/queue/<safe-target-file>.md`.

## 8. Required Traceability

required_traceability:
  source_proposal:
  source_authorization:
  source_conversion_package:
  source_generated_artifact:
  m50_traceability:
  m51_generator_evidence:
  m52_validation_evidence:
  m53_placement_review_evidence:

M54 input must not silently break upstream traceability.

## 9. Required Carry-Forward

required_carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

M54 input must not silently drop M53 carry-forward material.

## 10. Pre-Materialization Checks

pre_materialization_checks:
  m53_completion_valid:
  m53_input_review_ready:
  m53_materialization_authorized_false:
  candidate_not_already_queued:
  candidate_not_active:
  target_path_safe:
  target_file_absent:

All pre-materialization checks must pass before any future M54 write-mode operation.

## 11. Boundary Fields

boundaries:
  queue_materialization_requested: true
  queue_write_allowed_only_by_m54_cli: true
  active_task_write_allowed: false
  execution_authorized: false
  approval_record_creation_allowed: false
  lifecycle_active_transition_allowed: false
  m55_start_authorized: false

M54 input may request materialization review, but it does not authorize materialization by itself.

## 12. Invalid Input Conditions

Input is invalid or blocked if:
- `source_m53_completion_review` is missing
- `source_m53_completion_review` is not `reports/m53-completion-review.md`
- `source_candidate_origin` is not `M53_PLACEMENT_ELIGIBLE_CANDIDATE`
- `materialization_mode` is not `QUEUE_PLACEMENT_ONLY`
- `target_queue_dir` does not resolve under `tasks/queue/`
- `target_queue_file` contains a slash
- `target_queue_file` contains path traversal
- `required_traceability` is incomplete
- `required_carry_forward` is incomplete
- `active_task_write_allowed` is true
- `execution_authorized` is true
- `approval_record_creation_allowed` is true
- `lifecycle_active_transition_allowed` is true
- `m55_start_authorized` is true

## 13. Summary

M54 input contract defines review input only.

It does not place a candidate.
It does not approve a candidate.
It does not execute a candidate.
It does not replace active-task.md.
It does not authorize M55.
