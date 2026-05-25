---
type: contract
milestone: M54
task: 54.3
title: Task Queue Placement Artifact Contract
status: draft
authority: artifact-contract
created_for: M54
depends_on:
  - reports/m54-m53-readiness-intake.md
  - reports/m53-completion-review.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-INPUT-CONTRACT.md
queue_artifact_created: false
queue_materialization_authorized: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

## 1. Purpose

This document defines the canonical M54 queue placement artifact contract.

The queue placement artifact represents queued status only; it does not approve, activate, or execute a candidate.

## 2. Non-Authority Boundary

M54 queue artifact contract is not approval.
M54 queue artifact contract does not authorize execution.
M54 queue artifact contract does not authorize queue placement by itself.
M54 queue artifact contract does not authorize active-task replacement.
M54 queue artifact contract does not authorize lifecycle mutation.
M54 queue artifact contract does not authorize M54 materialization.
M54 queue artifact contract does not authorize M55.

## 3. Artifact Root Object

queue_placement_artifact:

All M54 queue placement artifacts must use queue_placement_artifact as the root object.

## 4. Required Top-Level Fields

task_id:
queue_status:
source_candidate_id:
source_m53_completion_review:
source_m53_placement_result:
source_m52_validation_result:
source_generated_candidate:
placement_created_by:
placement_created_at:
placement_authority:
approval_status:
execution_status:
active_task_status:
required_traceability:
carry_forward:
boundaries:

## 5. Queue Status Fields

queue_status: QUEUED_CANDIDATE
placement_created_by: M54
placement_created_at: ISO 8601 date-time string
placement_authority: QUEUE_PLACEMENT_ONLY
approval_status: NOT_APPROVED
execution_status: NOT_STARTED
active_task_status: NOT_ACTIVE

QUEUED_CANDIDATE means queued only, not approved, not active, and not executable.

## 6. Canonical Source Fields

source_m53_completion_review:
source_m53_placement_result:
source_m52_validation_result:
source_generated_candidate:

A queue artifact must preserve its M52 validation source and M53 placement review source.

A queue artifact must not invent missing upstream evidence.

## 7. Required Traceability

required_traceability:
  source_proposal:
  source_authorization:
  source_conversion_package:
  source_generated_artifact:
  m50_traceability:
  m51_generator_evidence:
  m52_validation_evidence:
  m53_placement_review_evidence:
  m54_materialization_evidence:

A queue artifact must not silently break upstream traceability.

## 8. Carry-Forward Requirements

carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

A queue artifact must not silently drop M53 or M54 carry-forward material.

## 9. Boundary Fields

boundaries:
  queue_entry_created: true
  active_task_replacement_performed: false
  execution_authorized: false
  approval_created: false
  lifecycle_active_transition_performed: false
  m55_start_authorized: false

A queue artifact records queue entry creation only; it must not record active-task replacement, approval, execution, or M55 start.

## 10. Target Location Rule

`tasks/queue/<safe-target-file>.md`

A queue artifact must be created only under `tasks/queue/`.

A queue artifact must never replace `tasks/active-task.md`.

## 11. Invalid Artifact Conditions

Artifact is invalid if:
1. `queue_status` is not `QUEUED_CANDIDATE`
2. `placement_created_by` is not `M54`
3. `placement_created_at` is missing or not an ISO 8601 date-time string
4. `placement_authority` is not `QUEUE_PLACEMENT_ONLY`
5. `approval_status` is not `NOT_APPROVED`
6. `execution_status` is not `NOT_STARTED`
7. `active_task_status` is not `NOT_ACTIVE`
8. `required_traceability` is incomplete
9. `carry_forward` is incomplete
10. `active_task_replacement_performed` is true
11. `execution_authorized` is true
12. `approval_created` is true
13. `lifecycle_active_transition_performed` is true
14. `m55_start_authorized` is true
15. artifact claims approval
16. artifact claims execution permission
17. artifact claims active-task replacement
18. artifact claims M55 authorization

## 12. Relationship to Future M54 CLI

Only the future M54 materialization CLI may create a queue artifact.
This contract defines the artifact shape only.
This contract does not create a queue artifact.
This contract does not authorize a write operation.

## 13. Relationship to M55

A queued candidate is not an active task.
A queued candidate is not approved.
A queued candidate is not executable.
A queued candidate is not M55-authorized.
M55 must independently validate any active-task or execution readiness transition.

## 14. Summary

M54 queue artifact contract defines queued-candidate structure only.

It does not place a candidate.
It does not approve a candidate.
It does not execute a candidate.
It does not replace active-task.md.
It does not authorize M55.
