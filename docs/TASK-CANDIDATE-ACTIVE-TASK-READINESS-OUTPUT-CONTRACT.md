---
type: contract
milestone: M55
task: 55.4
title: Task Candidate Active-Task Readiness Output Contract
status: draft
authority: output-contract
created_for: M55
source_intake: reports/m55-m54-readiness-intake.md
source_architecture: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md
source_input_contract: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md
source_proposal_contract: docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# Task Candidate Active-Task Readiness Output Contract

## 1. Purpose

This document defines the M55 active-task readiness output contract.

The output contract records readiness results only; it does not replace active-task.md.

Readiness output validity is not approval, execution permission, lifecycle mutation, or M56 authorization.

## 2. Root Object

active_task_readiness_result:

All M55 active-task readiness result packages must use active_task_readiness_result as the root object.

## 3. Required Top-Level Fields

result:
exit_code:
readiness_confirmed:
proposal_ready_for_review:
active_task_replacement_authorized:
active_task_file_created:
checked_queue_entry_id:
target_active_task_path:
source_active_task_readiness_input:
source_active_task_proposal:
source_m54_completion_review:
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:
required_traceability:
carry_forward:
readiness_findings:
warnings:
blockers:
boundary_flags:
performed_actions:
non_authority_markers:

## 4. Result Tokens and Exit Codes

ACTIVE_TASK_READINESS_CONFIRMED:
  exit_code: 0

ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS:
  exit_code: 0

ACTIVE_TASK_READINESS_NOT_CONFIRMED:
  exit_code: 1

ACTIVE_TASK_READINESS_BLOCKED:
  exit_code: 2

The process exit code must match active_task_readiness_result.exit_code.

A successful exit code does not authorize approval, execution, active-task replacement, lifecycle mutation, or M56.

## 5. Result Meaning

ACTIVE_TASK_READINESS_CONFIRMED:
  readiness_confirmed: true
  proposal_ready_for_review: true

ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS:
  readiness_confirmed: true
  proposal_ready_for_review: true

ACTIVE_TASK_READINESS_NOT_CONFIRMED:
  readiness_confirmed: false
  proposal_ready_for_review: false

ACTIVE_TASK_READINESS_BLOCKED:
  readiness_confirmed: false
  proposal_ready_for_review: false

Only ACTIVE_TASK_READINESS_CONFIRMED and ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS may report proposal_ready_for_review: true.

proposal_ready_for_review does not authorize active-task replacement.

## 6. Canonical Source Fields

source_active_task_readiness_input:
source_active_task_proposal:
source_m54_completion_review: reports/m54-completion-review.md
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:

M55 readiness output must preserve M55 input, active-task proposal, M54, M53, and M52 source references.

M55 readiness output must not invent missing upstream evidence.

source_queue_entry must point under tasks/queue/ and must not point to tasks/active-task.md.

## 7. Target Active-Task Path

target_active_task_path: tasks/active-task.md

target_active_task_path may reference tasks/active-task.md only as the canonical future target path.

target_active_task_path does not authorize writing to tasks/active-task.md.

The readiness output contract must not perform active-task replacement.

## 8. Proposal Review Readiness

proposal_ready_for_review means the proposal may be reviewed later; it does not approve or activate the task.

proposal_ready_for_review must not be treated as active-task replacement.

proposal_ready_for_review must not create approval records.

## 9. Required Traceability

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
  m55_readiness_input_evidence:
  m55_active_task_proposal_evidence:

M55 readiness output must not silently break upstream traceability.

## 10. Carry-Forward

carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

M55 readiness output must carry forward M54, M55 input, and proposal limitations.

Carry-forward material must not be converted into approval.

Limitations do not authorize active-task replacement.

## 11. Readiness Findings

readiness_findings:
warnings:
blockers:

Readiness findings may explain readiness concerns but must not authorize mutation.

## 12. Boundary Flags

boundary_flags:
  readiness_result_only: true
  active_task_file_created: false
  active_task_replacement_authorized: false
  active_task_write_allowed: false
  execution_authorized: false
  approval_created: false
  lifecycle_mutation_authorized: false
  m56_authorized: false
  m56_started: false

Boundary flags must preserve that M55 readiness output is result-only.

## 13. Performed Actions

performed_actions:
  active_task_file_created: false
  active_task_replacement_performed: false
  approval_created: false
  execution_started: false
  lifecycle_mutation_performed: false
  m56_started: false

M55 readiness output must record performed actions without claiming approval, execution, active-task replacement, lifecycle mutation, or M56 start.

## 14. Non-Authority Markers

Required markers:
- M55 readiness output is not approval.
- M55 readiness output does not authorize execution.
- M55 readiness output does not authorize active-task replacement.
- M55 readiness output does not write tasks/active-task.md.
- M55 readiness output does not create approval records.
- M55 readiness output does not authorize M56.
- M55 readiness output does not start M56.

## 15. Invalid Result Conditions

Result is invalid if:
1. root object is missing
2. required top-level field is missing
3. result is not one of the allowed result tokens
4. exit_code does not match result token
5. readiness_confirmed does not match result token
6. proposal_ready_for_review does not match result token
7. proposal_ready_for_review is true when readiness is not confirmed
8. active_task_replacement_authorized is true
9. active_task_file_created is true
10. target_active_task_path is not tasks/active-task.md
11. target_active_task_path is treated as write authorization
12. source_m54_completion_review is not reports/m54-completion-review.md
13. source_queue_entry does not point under tasks/queue/
14. source_queue_entry points to tasks/active-task.md
15. required traceability is incomplete
16. carry-forward fields are incomplete
17. non-authority markers are missing
18. readiness_result_only is not true
19. active_task_write_allowed is true
20. execution_authorized is true
21. approval_created is true
22. lifecycle_mutation_authorized is true
23. m56_authorized is true
24. m56_started is true
25. active_task_replacement_performed is true
26. execution_started is true
27. lifecycle_mutation_performed is true
28. result claims approval
29. result claims execution permission
30. result claims active-task replacement
31. result claims M56 authorization

## 16. Relationship to Input Contract

M55 readiness output depends on a valid M55 readiness input package.
M55 readiness output must preserve M55 readiness input sources.
M55 readiness output must not broaden the input contract authority.
M55 readiness output must not convert readiness input into active-task replacement.

## 17. Relationship to Active-Task Proposal

M55 readiness output may reference active_task_proposal.
M55 readiness output must not treat active_task_proposal as approval.
M55 readiness output must not treat proposal_ready_for_review as active-task replacement.
M55 readiness output must preserve required_human_review boundary from active_task_proposal.

## 18. Relationship to Future CLI

The future M55 CLI must be read-only.
The future M55 CLI may produce active_task_readiness_result.
The future M55 CLI must not write to tasks/active-task.md, tasks/queue/, approvals/, or M56 artifacts.
The future M55 CLI must not include a fixture mode; fixture integration belongs to 55.8.

## 19. Relationship to M56

M56 must independently validate execution readiness.
M55 readiness output does not authorize M56 execution.
M55 readiness output does not start M56.
M55 readiness output does not create M56 artifacts.

## 20. Summary

M55 readiness output contract defines readiness result structure only.

It does not replace active-task.md.
It does not create a file in tasks/.
It does not approve a task.
It does not execute a task.
It does not create approval records.
It does not authorize M56.
