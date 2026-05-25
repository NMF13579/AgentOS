---
type: policy
milestone: M55
task: 55.5
title: Task Candidate Active-Task Readiness Policy
status: draft
authority: readiness-policy
created_for: M55
source_intake: reports/m55-m54-readiness-intake.md
source_architecture: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md
source_input_contract: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md
source_proposal_contract: docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md
source_output_contract: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# 1. Purpose

This document defines the M55 active-task readiness policy.

The policy defines when active-task readiness may be reported, but it does not replace active-task.md.

Active-task readiness policy validity is not approval, execution permission, lifecycle mutation, or M56 authorization.

# 2. Authority Boundary

The M55 readiness policy is not approval.
The M55 readiness policy does not authorize execution.
The M55 readiness policy does not authorize active-task replacement.
The M55 readiness policy does not write tasks/active-task.md.
The M55 readiness policy does not create approval records.
The M55 readiness policy does not authorize M56.
The M55 readiness policy does not start M56.

# 3. Readiness Decision Model

1. Validate intake status.
2. Validate upstream contracts exist.
3. Validate queue-entry source boundary.
4. Validate active-task readiness input.
5. Validate active-task proposal.
6. Validate readiness result shape.
7. Validate traceability.
8. Validate carry-forward material.
9. Validate non-authority markers.
10. Apply safe default if anything is missing, malformed, unknown, or contradictory.

M55 readiness policy must fail closed on missing, malformed, unknown, or contradictory inputs.

UNKNOWN must not be treated as ACTIVE_TASK_READINESS_CONFIRMED.

# 4. Allowed Result Tokens

ACTIVE_TASK_READINESS_CONFIRMED
ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS
ACTIVE_TASK_READINESS_NOT_CONFIRMED
ACTIVE_TASK_READINESS_BLOCKED

No other M55 readiness result token is allowed.

# 5. Result Token Semantics

```yaml
ACTIVE_TASK_READINESS_CONFIRMED:
  readiness_confirmed: true
  proposal_ready_for_review: true
  blockers: []
ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS:
  readiness_confirmed: true
  proposal_ready_for_review: true
  blockers: []
  limitations_required: true
ACTIVE_TASK_READINESS_NOT_CONFIRMED:
  readiness_confirmed: false
  proposal_ready_for_review: false
  blockers_allowed: true
ACTIVE_TASK_READINESS_BLOCKED:
  readiness_confirmed: false
  proposal_ready_for_review: false
  blockers_required: true
```

Readiness confirmation means eligible for later human review only.

Readiness confirmation does not authorize active-task replacement.

Readiness confirmation does not authorize execution.

# 6. Exit Code Semantics

```yaml
ACTIVE_TASK_READINESS_CONFIRMED: 0
ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS: 0
ACTIVE_TASK_READINESS_NOT_CONFIRMED: 1
ACTIVE_TASK_READINESS_BLOCKED: 2
```

Exit code 0 is not approval and is not lifecycle mutation.

Exit code 0 does not authorize active-task replacement, execution, or M56.

# 7. Required Upstream Inputs

reports/m55-m54-readiness-intake.md
docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md
docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md
schemas/task-candidate-active-task-readiness-input.schema.json
templates/task-candidate-active-task-readiness-input.md
docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md
schemas/active-task-proposal.schema.json
templates/active-task-proposal.md
docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md
schemas/task-candidate-active-task-readiness-result.schema.json
templates/task-candidate-active-task-readiness-result.md

M55 readiness policy must not invent missing upstream contracts or evidence.

# 8. Queue Entry Conditions

source_queue_entry must point under tasks/queue/.
source_queue_entry must not point to tasks/active-task.md.
Queue entry is not active task.
Queue entry does not authorize active-task replacement.
Queue entry does not authorize execution.

A valid queue entry reference is not permission to write active-task.md.

# 9. Active-Task Proposal Conditions

active_task_proposal must be embedded evidence, not a file in tasks/.
active_task_proposal must preserve required_human_review: true.
active_task_proposal must not authorize active-task replacement.
active_task_proposal must not authorize execution.
active_task_proposal must not authorize M56.

proposal_ready_for_review means reviewable later, not executable now.

# 10. Output Result Conditions

active_task_readiness_result.result must be one of the allowed result tokens.
active_task_readiness_result.exit_code must match the result token.
active_task_readiness_result.readiness_confirmed must match the result token.
active_task_readiness_result.proposal_ready_for_review must match the result token.
active_task_readiness_result.active_task_replacement_authorized must be false.
active_task_readiness_result.active_task_file_created must be false.

Any mismatch between result, exit_code, readiness_confirmed, and proposal_ready_for_review must block readiness confirmation.

# 11. Traceability Policy

source_proposal
source_authorization
source_conversion_package
source_generated_artifact
m50_traceability
m51_generator_evidence
m52_validation_evidence
m53_placement_review_evidence
m54_materialization_evidence
queue_entry_evidence
m55_readiness_input_evidence
m55_active_task_proposal_evidence

M55 readiness policy must not silently break upstream traceability.

# 12. Carry-Forward Policy

accepted_limitations
warnings
open_questions
downstream_limits
known_gaps
non_authority_boundary

M55 readiness policy must carry forward limitations instead of converting them into approval.

Limitations do not authorize active-task replacement.

# 13. Non-Authority Policy

M55 readiness policy is not approval.
M55 readiness policy does not authorize execution.
M55 readiness policy does not authorize active-task replacement.
M55 readiness policy does not write tasks/active-task.md.
M55 readiness policy does not create approval records.
M55 readiness policy does not authorize M56.
M55 readiness policy does not start M56.

# 14. Blocking Conditions

Readiness must be blocked if:

1. intake file is missing
2. intake status is M55_INTAKE_BLOCKED
3. intake status is missing
4. intake status is malformed
5. upstream architecture is missing
6. input contract is missing
7. proposal contract is missing
8. output contract is missing
9. any upstream schema is missing
10. any upstream template is missing
11. queue entry source is missing
12. queue entry source does not point under tasks/queue/
13. queue entry source points to tasks/active-task.md
14. target active-task path is not tasks/active-task.md
15. target active-task path is treated as write authorization
16. active-task proposal is missing
17. active-task proposal is written as a file in tasks/
18. active-task proposal lacks required_human_review: true
19. readiness result root object is missing
20. readiness result token is unknown
21. readiness result exit code does not match token
22. readiness result confirmation fields do not match token
23. proposal_ready_for_review is true while readiness_confirmed is false
24. active_task_replacement_authorized is true
25. active_task_file_created is true
26. active_task_write_allowed is true
27. execution_authorized is true
28. approval_created is true
29. lifecycle_mutation_authorized is true
30. m56_authorized is true
31. m56_started is true
32. performed actions claim active-task replacement
33. performed actions claim approval creation
34. performed actions claim execution start
35. performed actions claim lifecycle mutation
36. performed actions claim M56 start
37. traceability is incomplete
38. carry-forward fields are incomplete
39. non-authority markers are missing
40. result claims approval
41. result claims execution permission
42. result claims active-task replacement
43. result claims M56 authorization
44. any required input is unknown
45. any required input is contradictory

Any blocking condition must produce ACTIVE_TASK_READINESS_BLOCKED or ACTIVE_TASK_READINESS_NOT_CONFIRMED, never ACTIVE_TASK_READINESS_CONFIRMED.

# 15. Safe Default

The safe default is ACTIVE_TASK_READINESS_BLOCKED.
Missing input must block.
Malformed input must block.
Unknown status must block.
Contradictory evidence must block.
Unsafe authority claim must block.

Safe default must never authorize active-task replacement.

# 16. Future CLI Obligations

The future M55 CLI must be read-only.
The future M55 CLI must not write to tasks/active-task.md.
The future M55 CLI must not write to tasks/queue/.
The future M55 CLI must not write to approvals/.
The future M55 CLI must not create M56 artifacts.
The future M55 CLI must not include a fixture mode; fixture integration belongs to 55.8.
The future M55 CLI must fail closed on missing, malformed, unknown, or contradictory inputs.

The future M55 CLI may report readiness but must not perform lifecycle mutation.

# 17. Relationship to M56

M56 must independently validate execution readiness.
M55 readiness policy does not authorize M56 execution.
M55 readiness policy does not start M56.
M55 readiness policy does not create M56 artifacts.

# 18. Summary

M55 active-task readiness policy defines readiness decision rules only.
It does not replace active-task.md.
It does not create a file in tasks/.
It does not approve a task.
It does not execute a task.
It does not create approval records.
It does not authorize M56.
