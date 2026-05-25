---
type: contract
milestone: M53
task: 53.3
title: Task Candidate Placement Review Output Contract
status: draft
authority: canonical
created_for: M53
depends_on:
  - reports/m52-completion-review.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-INPUT-CONTRACT.md
schema:
  - schemas/task-candidate-placement-review-result.schema.json
template:
  - templates/task-candidate-placement-review-result.md
---

## 1. Metadata

This contract defines the canonical output boundary for M53 task 53.3.

## 2. Purpose

The placement review output contract defines the review-only result package for M53 placement eligibility review.

- the result package records the placement review decision
- the result package records whether the review was completed, not eligible, blocked, or completed with limitations
- the result package preserves M50/M51/M52 traceability
- the result package preserves carry-forward limitations, warnings, open questions, downstream limits, and known gaps
- the result package declares non-authority boundary flags
- the result package may identify an input candidate for M54
- the result package does not authorize placement or materialization
- authorization flags live only in boundary_flags

## 3. Non-Authority Boundary

M53 placement review result is not approval.
M53 placement review result does not authorize execution.
M53 placement review result does not authorize queue placement.
M53 placement review result does not authorize active-task replacement.
M53 placement review result does not authorize lifecycle mutation.
M53 placement review result does not authorize M54 materialization.

## 4. Result Tokens

```yaml
result:
  - PLACEMENT_REVIEW_ELIGIBLE
  - PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS
  - PLACEMENT_REVIEW_NOT_ELIGIBLE
  - PLACEMENT_REVIEW_BLOCKED
```

- PLACEMENT_REVIEW_ELIGIBLE means the candidate is eligible as a future M54 input candidate, with no carried-forward limitations that block eligibility.
- PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS means the candidate is eligible as a future M54 input candidate only if limitations, warnings, open questions, downstream limits, and known gaps are preserved.
- PLACEMENT_REVIEW_NOT_ELIGIBLE means the candidate was reviewed and is not eligible for downstream placement consideration.
- PLACEMENT_REVIEW_BLOCKED means placement review could not be completed because required dependencies, evidence, traceability, or boundaries were missing or unsafe.

PLACEMENT_REVIEW_ELIGIBLE does not mean queue placement was performed.

## 5. Exit Semantics

```yaml
exit_code:
  PLACEMENT_REVIEW_ELIGIBLE: 0
  PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS: 0
  PLACEMENT_REVIEW_NOT_ELIGIBLE: 1
  PLACEMENT_REVIEW_BLOCKED: 2
```

- exit 0 does not authorize placement
- exit 0 does not authorize execution
- exit 0 does not authorize M54 materialization
- exit 1 means review completed but candidate is not eligible
- exit 2 means review was blocked and no eligibility claim may be made

## 6. Eligibility Fields

```yaml
eligible_for_downstream_placement: true | false
eligible_as_m54_queue_materialization_input: true | false
eligible_as_m54_active_task_proposal_input: true | false
```

- these fields are eligibility classifications only
- they do not authorize queue placement
- they do not authorize active-task replacement
- they do not authorize M54 materialization
- they do not create queue entries
- they do not modify tasks/active-task.md

Rules:
- If result is PLACEMENT_REVIEW_ELIGIBLE or PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS:
  - eligible_for_downstream_placement may be true
- If result is PLACEMENT_REVIEW_NOT_ELIGIBLE or PLACEMENT_REVIEW_BLOCKED:
  - eligible_for_downstream_placement must be false
  - eligible_as_m54_queue_materialization_input must be false
  - eligible_as_m54_active_task_proposal_input must be false

## 7. Required Source Fields

Required source fields:
- checked_candidate_id
- source_m52_completion_review
- source_m52_validation_result
- source_generated_artifact

source_m52_completion_review must equal reports/m52-completion-review.md.

- non-canonical M52 completion review paths are invalid
- missing source_m52_validation_result blocks the review result
- missing source_generated_artifact blocks the review result
- source artifacts must be reported, not inferred

## 8. Traceability Output

Required source_traceability fields:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- m50_traceability
- m51_generator_evidence
- m52_validation_evidence

M53 output must preserve M50/M51/M52 traceability and must not claim eligibility with broken provenance.

## 9. Carry-Forward Output

Required carry_forward fields:
- accepted_limitations
- warnings
- open_questions
- downstream_limits
- known_gaps
- non_authority_boundary

M53 output must not silently drop accepted limitations, warnings, open questions, downstream limits, or known gaps from M52.

- limitations must not be weakened
- warnings must not be converted into clean eligibility
- open questions must not be removed without source evidence
- downstream limits must not be expanded silently
- known gaps must remain visible
- non-authority boundaries must be preserved

## 10. Findings, Warnings, and Blockers

```yaml
placement_findings: []
warnings: []
blockers: []
```

- placement_findings record review observations
- warnings record non-blocking limitations or caution conditions
- blockers record conditions that prevent eligibility
- blockers must force result to PLACEMENT_REVIEW_BLOCKED or PLACEMENT_REVIEW_NOT_ELIGIBLE depending on severity
- warnings must not be silently dropped when result is eligible with limitations

## 11. Boundary Flags

```yaml
boundary_flags:
  review_only: true
  queue_write_allowed: false
  active_task_write_allowed: false
  execution_authorized: false
  approval_record_creation_allowed: false
  lifecycle_mutation_allowed: false
  m54_materialization_authorized: false
```

- boundary_flags is the only place where authorization flags are represented
- any result that sets authority-expanding flags to true is invalid
- review_only must be true
- all authority-expanding flags must be false
- M53 result cannot authorize M54 materialization
- there must be no top-level execution_authorized field

## 12. M54 Handoff Boundary

```yaml
m54_independent_validation_required: true
m54_may_not_start_without_own_gate: true
m54_materialization_authorized: false
```

M53 result may identify a candidate for future M54 consideration.
M53 result does not authorize M54 to run.
M53 result does not authorize queue materialization.
M53 result does not authorize active-task proposal materialization.
M54 must independently validate materialization.

## 13. Performed Action Flags

```yaml
queue_placement_performed: false
active_task_replacement_performed: false
approval_created: false
```

- if any performed action flag is true, the result is invalid
- M53 output must never claim that queue placement was performed
- M53 output must never claim that active-task replacement was performed
- M53 output must never claim that approval was created
- execution authorization is represented only by `boundary_flags.execution_authorized`
- `boundary_flags.execution_authorized` must always be false

## 14. Invalid Output Conditions

- missing placement_review_result
- missing result
- unknown result token
- exit_code does not match result token
- missing checked_candidate_id
- missing source_m52_completion_review
- source_m52_completion_review not equal to reports/m52-completion-review.md
- missing source_m52_validation_result
- missing source_generated_artifact
- missing source_traceability
- missing carry_forward
- missing boundary_flags
- review_only not true
- queue_write_allowed not false
- active_task_write_allowed not false
- boundary_flags.execution_authorized not false
- approval_record_creation_allowed not false
- lifecycle_mutation_allowed not false
- m54_materialization_authorized not false
- m54_independent_validation_required not true
- m54_may_not_start_without_own_gate not true
- queue_placement_performed not false
- active_task_replacement_performed not false
- approval_created not false
- top-level execution_authorized field exists
- limitations dropped
- warnings dropped
- open questions dropped
- downstream limits dropped
- known gaps dropped
- result claims M54 authorization
- result claims queue placement was performed
- result claims active-task replacement was performed
- result claims approval was created
- PLACEMENT_REVIEW_BLOCKED with eligible_for_downstream_placement true
- PLACEMENT_REVIEW_NOT_ELIGIBLE with eligible_for_downstream_placement true

## 15. Summary

The M53 placement review result is a review-only eligibility result.

It may mark a candidate as eligible for future M54 consideration.
It must not place the candidate.
It must not approve the candidate.
It must not execute the candidate.
It must not materialize the candidate.
