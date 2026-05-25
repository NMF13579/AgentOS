---
type: policy
milestone: M54
task: 54.5
title: Task Candidate Queue Placement Materialization Policy
status: draft
authority: policy
created_for: M54
depends_on:
  - reports/m54-m53-readiness-intake.md
  - reports/m53-completion-review.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-INPUT-CONTRACT.md
  - docs/TASK-QUEUE-PLACEMENT-ARTIFACT-CONTRACT.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-OUTPUT-CONTRACT.md
queue_materialization_authorized_by_this_document: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

# Task Candidate Queue Placement Materialization Policy

## 1. Purpose

This policy defines the pre-materialization rules for future M54 queue placement materialization.

This policy does not itself create a queue artifact, approve a candidate, execute a candidate, or authorize M55.

M54 policy can define when future materialization is allowed.
M54 policy does not itself materialize anything.

## 2. Non-Authority Boundary

M54 policy is not approval.
M54 policy does not authorize execution.
M54 policy does not authorize active-task replacement.
M54 policy does not authorize lifecycle mutation.
M54 policy does not authorize M55.
M54 policy does not itself create queue entries.
M54 policy does not itself materialize candidates.

## 3. Policy Decision Tokens

```yaml
M54_QUEUE_PLACEMENT_POLICY_ALLOWED:
  meaning: all pre-materialization checks pass and no limitations are present

M54_QUEUE_PLACEMENT_POLICY_ALLOWED_WITH_LIMITATIONS:
  meaning: all blocking checks pass, but carry-forward limitations, warnings, downstream limits, open questions, or known gaps are present

M54_QUEUE_PLACEMENT_POLICY_NOT_ALLOWED:
  meaning: policy can evaluate the candidate safely, but the candidate is not suitable for queue materialization

M54_QUEUE_PLACEMENT_POLICY_BLOCKED:
  meaning: policy cannot safely evaluate or must stop due to missing evidence, unsafe authority claims, unsafe paths, or failed preconditions
```

A policy decision is not a materialization result.

## 4. Required Inputs for Future Materialization

```yaml
required_inputs:
  m54_intake_report: reports/m54-m53-readiness-intake.md
  m53_completion_review: reports/m53-completion-review.md
  m53_placement_result: reports/m53-placement-review-result-agent-action-review.json
  queue_placement_input:
  generated_candidate:
  target_queue_path:
```

Future materialization must not proceed without the canonical M53 completion review and canonical M53 placement result.

## 5. M53 Completion Review Preconditions

Future materialization must require `reports/m53-completion-review.md`.

```yaml
allowed_m53_completion_status:
  - M53_PLACEMENT_REVIEW_LAYER_COMPLETE
  - M53_PLACEMENT_REVIEW_LAYER_COMPLETE_WITH_LIMITATIONS
```

```yaml
blocking_m53_completion_status:
  - M53_INCOMPLETE
  - M53_BLOCKED
```

If M53 completion review is missing, incomplete, blocked, or unreadable, M54 queue materialization must be blocked.

## 6. M53 Placement Result Preconditions

Future materialization must require:

```yaml
placement_review_result.result:
  - PLACEMENT_REVIEW_ELIGIBLE
  - PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS
```

Future materialization must block if M53 placement result is:

```yaml
placement_review_result.result:
  - PLACEMENT_REVIEW_NOT_ELIGIBLE
  - PLACEMENT_REVIEW_BLOCKED
```

Future materialization must require:

```yaml
eligible_for_downstream_placement: true
eligible_as_m54_queue_materialization_input: true
eligible_as_m54_active_task_proposal_input: false
m54_independent_validation_required: true
m54_may_not_start_without_own_gate: true
m54_materialization_authorized: false
queue_placement_performed: false
active_task_replacement_performed: false
approval_created: false
```

M53 eligibility is required input for M54; it is not M54 materialization approval.

## 7. M54 Input Preconditions

Future materialization must require valid `task-candidate-queue-placement-input` with:

```yaml
placement_kind: queue_materialization
queue_materialization_requested: true
active_task_replacement_requested: false
approval_requested: false
execution_requested: false
m55_requested: false
```

Future materialization must require safe boundary flags:

```yaml
queue_materialization_authorized_by_input: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
```

Input may request review for queue materialization, but it must not claim that materialization is already authorized.

## 8. Target Queue Path Policy

Future materialization may only target:

`tasks/queue/<safe-target-file>.md`

Target queue path must satisfy:

1. path is under `tasks/queue/`
2. path has `.md` suffix
3. path is relative to repository root
4. path does not contain `..`
5. path does not resolve outside repository root
6. path does not equal `tasks/active-task.md`
7. path does not point into `approvals/`
8. path does not point into `reports/`
9. path does not point into `generated/`
10. target file does not already exist

Queue target path safety is a blocking pre-materialization check.

## 9. Repository State Conflict Checks for Future CLI

The following read boundary defines policy for future M54 CLI implementation, not for this task 54.5.

Future CLI may perform read-only checks for:

```yaml
allowed_read_only_paths:
  - tasks/queue/
  - tasks/active-task.md
  - approvals/
```

Future CLI must block if:

1. candidate is already queued
2. candidate is already active
3. approval record already exists for the same placement attempt
4. target queue file already exists
5. repository state cannot be safely read
6. path resolution is unsafe

Repository state checks must be read-only and must not create, modify, approve, execute, or materialize anything.

## 10. Source Traceability Policy

Future materialization must preserve:

```yaml
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
```

M54 materialization must not silently break upstream traceability.

## 11. Carry-Forward Policy

Future materialization must preserve:

```yaml
carry_forward:
  accepted_limitations:
  warnings:
  open_questions:
  downstream_limits:
  known_gaps:
  non_authority_boundary:
```

If any carry-forward field is non-empty, policy decision must be:

```yaml
M54_QUEUE_PLACEMENT_POLICY_ALLOWED_WITH_LIMITATIONS
```

unless a blocking or not-allowed condition applies first.

M54 materialization must not silently drop M53 or M54 carry-forward material.

## 12. Allowed Decision Conditions

Policy decision may be `M54_QUEUE_PLACEMENT_POLICY_ALLOWED` only if:

1. M54 intake is ready
2. M53 completion review is complete
3. M53 placement result is eligible
4. M53 placement result has queue materialization eligibility
5. M54 input is structurally valid
6. queue target path is safe
7. target queue file does not exist
8. candidate is not already queued
9. candidate is not already active
10. no approval record already exists for this placement
11. required source traceability is complete
12. required carry-forward fields are present
13. all authority flags are safe
14. no carry-forward limitation fields are non-empty

## 13. Allowed With Limitations Conditions

Policy decision must be `M54_QUEUE_PLACEMENT_POLICY_ALLOWED_WITH_LIMITATIONS` if:

1. all blocking checks pass
2. all not-allowed checks pass
3. candidate is eligible for queue materialization
4. one or more carry-forward fields are non-empty

Carry-forward fields include:

```yaml
accepted_limitations
warnings
open_questions
downstream_limits
known_gaps
```

Allowed with limitations is still not approval, not execution, not active-task replacement, and not M55 authorization.

## 14. Not Allowed Conditions

Policy decision must be `M54_QUEUE_PLACEMENT_POLICY_NOT_ALLOWED` if:

1. review can complete safely
2. candidate is not suitable for queue materialization
3. candidate is only suitable for active-task proposal
4. requested target is incompatible with candidate shape
5. candidate requires expanding allowed changes
6. candidate requires weakening forbidden changes
7. candidate cannot preserve downstream limits
8. candidate cannot preserve known gaps

## 15. Blocking Conditions

Policy decision must be `M54_QUEUE_PLACEMENT_POLICY_BLOCKED` if:

1. M54 intake is missing
2. M54 intake is blocked
3. M53 completion review is missing
4. M53 completion review is incomplete
5. M53 completion review is blocked
6. M53 placement result is missing
7. M53 placement result is malformed
8. M53 placement result is blocked
9. M53 placement result is not eligible
10. M54 input is missing
11. M54 input is malformed
12. source traceability is missing
13. carry-forward fields are missing
14. target queue path is unsafe
15. target queue file already exists
16. candidate is already queued
17. candidate is already active
18. approval already exists for this placement
19. any authority flag claims execution authorization
20. any authority flag claims active-task replacement authorization
21. any authority flag claims approval creation
22. any authority flag claims M55 authorization
23. any input or result claims queue placement already happened
24. repository state cannot be safely read
25. path traversal is detected

## 16. Authority Flag Policy

Future materialization policy must require these safe values before any write may occur:

```yaml
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
queue_placement_performed_before_materialization: false
```

Any claim that execution, approval, active-task replacement, or M55 has already been authorized must block M54 materialization.

## 17. Future CLI Obligations

Future M54 CLI must:

1. validate M54 intake
2. validate M53 completion review
3. validate M53 placement result
4. validate M54 input
5. validate target queue path
6. validate target file absence
7. validate repository conflict state read-only
8. validate source traceability
9. validate carry-forward preservation
10. validate authority flags
11. produce a result using the M54 output contract
12. write to `tasks/queue/` only if all pre-materialization checks allow it
13. never write `tasks/active-task.md`
14. never write `approvals/`
15. never write reports directly
16. never authorize execution
17. never authorize M55

The future M54 CLI must verify all pre-materialization checks from this policy before executing any queue write.

## 18. Relationship to Output Contract

Policy decision precedes materialization result; it is not itself the materialization result.

Future materialization result must follow schemas/task-candidate-queue-placement-result.schema.json.

## 19. Summary

M54 policy defines pre-materialization conditions only.

It does not create a queue artifact.
It does not approve a candidate.
It does not execute a candidate.
It does not replace active-task.md.
It does not authorize M55.
