---
type: contract
milestone: M55
task: 55.3
title: Active-Task Proposal Contract
status: draft
authority: proposal-contract
created_for: M55
source_intake: reports/m55-m54-readiness-intake.md
source_architecture: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md
source_input_contract: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# Active-Task Proposal Contract

## 1. Purpose

This document defines the M55 active-task proposal contract.

An active-task proposal describes a possible future active-task shape; it does not replace active-task.md.

Active-task proposal validity is not approval, execution permission, lifecycle mutation, or M56 authorization.

## 2. Root Object

active_task_proposal:

All M55 active-task proposal packages must use active_task_proposal as the root object.

## 3. Required Top-Level Fields

proposal_id:
proposal_status:
source_active_task_readiness_input:
source_m54_completion_review:
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:
checked_queue_entry_id:
target_active_task_path:
proposed_active_task:
required_traceability:
carry_forward:
proposal_findings:
warnings:
blockers:
boundary_flags:
non_authority_markers:

## 4. Proposal Status

Allowed proposal statuses:
- ACTIVE_TASK_PROPOSAL_DRAFT
- ACTIVE_TASK_PROPOSAL_READY_FOR_REVIEW
- ACTIVE_TASK_PROPOSAL_BLOCKED

ACTIVE_TASK_PROPOSAL_READY_FOR_REVIEW does not authorize active-task replacement.

ACTIVE_TASK_PROPOSAL_BLOCKED must not be converted into approval.

## 5. Canonical Source Fields

source_active_task_readiness_input:
source_m54_completion_review: reports/m54-completion-review.md
source_m54_materialization_result:
source_queue_entry:
source_m53_placement_result:
source_m52_validation_result:

Active-task proposal must preserve M55 input, M54, M53, and M52 source references.

Active-task proposal must not invent missing upstream evidence.

source_queue_entry must point under tasks/queue/ and must not point to tasks/active-task.md.

## 6. Target Active-Task Path

target_active_task_path: tasks/active-task.md

target_active_task_path may reference tasks/active-task.md only as the canonical future target path.

target_active_task_path does not authorize writing to tasks/active-task.md.

The active-task proposal contract must not perform active-task replacement.

## 7. Proposed Active-Task Object

proposed_active_task:
  task_id:
  title:
  mode:
  repository:
  branch:
  source_queue_entry:
  proposed_scope_summary:
  proposed_validation_summary:
  readiness_basis:
  required_human_review: true

proposed_active_task is an embedded proposal object, not a file in tasks/.

proposed_active_task.required_human_review must remain true.

The proposed active-task object must not be written to tasks/active-task.md by Task 55.3.

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
  m54_materialization_evidence:
  queue_entry_evidence:
  m55_readiness_input_evidence:

Active-task proposal must not silently break upstream traceability.

## 9. Carry-Forward

carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:

Active-task proposal must carry forward M54 and M55 limitations and non-authority boundaries.

Carry-forward material must not be converted into approval.

Limitations do not authorize active-task replacement.

## 10. Proposal Findings

proposal_findings:
warnings:
blockers:

Proposal findings may explain readiness concerns but must not authorize mutation.

## 11. Boundary Flags

boundary_flags:
  proposal_only: true
  active_task_file_created: false
  active_task_replacement_authorized: false
  active_task_write_allowed: false
  execution_authorized: false
  approval_created: false
  lifecycle_mutation_authorized: false
  m56_authorized: false
  m56_started: false

Boundary flags must preserve that active-task proposal is proposal-only.

## 12. Non-Authority Markers

Required markers:
- Active-task proposal is not approval.
- Active-task proposal does not authorize execution.
- Active-task proposal does not authorize active-task replacement.
- Active-task proposal does not write tasks/active-task.md.
- Active-task proposal does not create approval records.
- Active-task proposal does not authorize M56.
- Active-task proposal does not start M56.

## 13. Invalid Proposal Conditions

Proposal is invalid if:
1. root object is missing
2. required top-level field is missing
3. proposal_status is unknown
4. source_m54_completion_review is not reports/m54-completion-review.md
5. source_queue_entry does not point under tasks/queue/
6. source_queue_entry points to tasks/active-task.md
7. target_active_task_path is not tasks/active-task.md
8. target_active_task_path is treated as write authorization
9. proposed_active_task is missing
10. proposed_active_task.required_human_review is false
11. proposed active-task object is written as a real file in tasks/
12. required traceability is incomplete
13. carry-forward fields are incomplete
14. non-authority markers are missing
15. proposal_only is not true
16. active_task_file_created is true
17. active_task_replacement_authorized is true
18. active_task_write_allowed is true
19. execution_authorized is true
20. approval_created is true
21. lifecycle_mutation_authorized is true
22. m56_authorized is true
23. m56_started is true
24. proposal claims approval
25. proposal claims execution permission
26. proposal claims active-task replacement
27. proposal claims M56 authorization

## 14. Relationship to Input Contract

Active-task proposal depends on a valid M55 readiness input package.
Active-task proposal must preserve M55 readiness input sources.
Active-task proposal must not broaden the input contract authority.
Active-task proposal must not convert readiness input into active-task replacement.

## 15. Relationship to Future Readiness Result

Task 55.3 does not create the M55 readiness result contract.
A future readiness result may reference active_task_proposal.
A future readiness result must independently validate proposal consistency.
A future readiness result must not treat proposal as approval.

## 16. Relationship to Future CLI

The future M55 CLI must be read-only.
The future M55 CLI may validate active-task proposal packages.
The future M55 CLI must not write to tasks/active-task.md, tasks/queue/, approvals/, or M56 artifacts.
The future M55 CLI must not include a fixture mode; fixture integration belongs to 55.8.

## 17. Relationship to M56

M56 must independently validate execution readiness.
Active-task proposal does not authorize M56 execution.
Active-task proposal does not start M56.
Active-task proposal does not create M56 artifacts.

## 18. Summary

Active-task proposal contract defines proposal structure only.

It does not replace active-task.md.
It does not create a file in tasks/.
It does not approve a task.
It does not execute a task.
It does not create approval records.
It does not authorize M56.
