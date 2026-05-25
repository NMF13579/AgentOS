---
type: contract
milestone: M55
task: 55.2
title: Task Candidate Active-Task Readiness Input Contract
status: draft
authority: input-contract
created_for: M55
source_intake: reports/m55-m54-readiness-intake.md
source_architecture: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# Task Candidate Active-Task Readiness Input Contract

## 1. Purpose

This document defines the M55 active-task readiness input contract.

The input contract describes what a future M55 readiness checker may read; it does not authorize active-task replacement.

Input contract validity is not approval, execution permission, or M56 authorization.

## 2. Root Object

active_task_readiness_input:

All M55 active-task readiness input packages must use active_task_readiness_input as the root object.

## 3. Required Top-Level Fields

input_id:
source_m54_completion_review:
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:
checked_queue_entry_id:
target_active_task_path:
readiness_mode:
required_traceability:
carry_forward:
boundary_flags:
non_authority_markers:

## 4. Canonical Source Fields

source_m54_completion_review: reports/m54-completion-review.md
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:

M55 input must preserve M54, M53, and M52 source references.

M55 input must not invent missing upstream evidence.

source_queue_entry must point under tasks/queue/ and must not point to tasks/active-task.md.

## 5. Target Active-Task Path

target_active_task_path: tasks/active-task.md

target_active_task_path may reference tasks/active-task.md only as the canonical future target path.

target_active_task_path does not authorize writing to tasks/active-task.md.

The input contract must not perform active-task replacement.

## 6. Readiness Mode

Allowed readiness modes:
- ACTIVE_TASK_READINESS_REVIEW
- ACTIVE_TASK_PROPOSAL_DRY_RUN

Readiness mode selects the future review behavior but does not authorize mutation.

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
  queue_entry_evidence:

M55 input must not silently break upstream traceability.

## 8. Carry-Forward

carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

M55 input must carry forward M54 limitations and non-authority boundaries.

Carry-forward material must not be converted into approval.

Limitations do not authorize active-task replacement.

M55 contracts must carry limitations forward.

## 9. Boundary Flags

boundary_flags:
  active_task_readiness_only: true
  active_task_replacement_authorized: false
  execution_authorized: false
  approval_created: false
  lifecycle_mutation_authorized: false
  m56_authorized: false
  m56_started: false

Boundary flags must preserve that M55 input is readiness-only.

## 10. Non-Authority Markers

Required markers:
- M55 input is not approval.
- M55 input does not authorize execution.
- M55 input does not authorize active-task replacement.
- M55 input does not create approval records.
- M55 input does not authorize M56.
- M55 input does not start M56.

## 11. Invalid Input Conditions

Input is invalid if:
1. root object is missing
2. required top-level field is missing
3. source_m54_completion_review is not reports/m54-completion-review.md
4. source_queue_entry does not point under tasks/queue/
5. source_queue_entry points to tasks/active-task.md
6. target_active_task_path is not tasks/active-task.md
7. target_active_task_path is treated as write authorization
8. readiness mode is unknown
9. required traceability is incomplete
10. carry-forward fields are incomplete
11. non-authority markers are missing
12. active_task_readiness_only is not true
13. active_task_replacement_authorized is true
14. execution_authorized is true
15. approval_created is true
16. lifecycle_mutation_authorized is true
17. m56_authorized is true
18. m56_started is true
19. input claims approval
20. input claims execution permission
21. input claims active-task replacement
22. input claims M56 authorization

## 12. Relationship to Active-Task Proposal

active_task_proposal is not created by this input contract.
active_task_proposal is a future schema/template/result concept only.
active_task_proposal must not exist as a file in tasks/.
active_task_proposal does not authorize active-task replacement.

## 13. Relationship to Future CLI

The future M55 CLI must be read-only.
The future M55 CLI may validate this input contract.
The future M55 CLI must not write to tasks/active-task.md, tasks/queue/, approvals/, or M56 artifacts.
The future M55 CLI must not include a fixture mode; fixture integration belongs to 55.8.

## 14. Relationship to M56

M56 must independently validate execution readiness.
M55 input does not authorize M56 execution.
M55 input does not start M56.
M55 input does not create M56 artifacts.

## 15. Summary

M55 input contract defines readiness input structure only.

It does not replace active-task.md.
It does not approve a task.
It does not execute a task.
It does not create approval records.
It does not authorize M56.
