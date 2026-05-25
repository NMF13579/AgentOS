---
type: contract
milestone: M53
task: 53.2
title: Task Candidate Placement Review Input Contract
status: draft
authority: canonical
created_for: M53
depends_on:
  - reports/m52-completion-review.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-ARCHITECTURE.md
schema:
  - schemas/task-candidate-placement-review-input.schema.json
template:
  - templates/task-candidate-placement-review-input.md
---

## 1. Metadata

This contract defines the canonical input boundary for M53 task 53.2.

## 2. Purpose

The placement review input contract defines the review-only input package for M53 placement eligibility review.

The input package identifies the M52-validated candidate.
The input package identifies canonical M52 dependency artifacts.
The input package preserves M50/M51/M52 traceability.
The input package preserves accepted limitations, warnings, open questions, downstream limits, and known gaps.
The input package declares review-only authority boundaries.
The input package does not authorize placement or materialization.

## 3. Non-Authority Boundary

M53 placement review input is not approval.
M53 placement review input does not authorize execution.
M53 placement review input does not authorize queue placement.
M53 placement review input does not authorize active-task replacement.
M53 placement review input does not authorize lifecycle mutation.
M53 placement review input does not authorize M54 materialization.

## 4. Canonical Dependency

The canonical M52 completion dependency for M53 input is reports/m52-completion-review.md.

```yaml
source_m52_completion_review: reports/m52-completion-review.md
```

- non-canonical M52 completion review paths are invalid
- missing source_m52_completion_review is invalid
- source_m52_completion_review must not be inferred
- source_m52_completion_review must not be replaced by legacy M52 reports

## 5. Field Definitions

Required fields in `placement_review_input`:
- input_id: unique input package identifier
- source_candidate_id: candidate identifier under review
- source_m52_completion_review: canonical M52 completion dependency path
- source_m52_evidence_report: M52 evidence report path
- source_m52_integration_report: M52 integration report path
- source_m52_validation_result: M52 validation result token or summary
- source_generated_artifact: generated candidate artifact path
- source_candidate_origin: origin class of candidate
- placement_review_mode: review mode requested
- expected_candidate_shape: expected candidate data shape
- m52_reports_dir: M52 reports directory path
- required_traceability: mandatory upstream traceability fields
- required_carry_forward: limitations/warnings/gaps to preserve
- placement_target: requested review target classification
- boundaries: fixed authority boundary flags

## 6. Allowed Values

```yaml
source_candidate_origin:
  - M51_GENERATED_STAGING_ARTIFACT
  - M52_VALIDATED_CANDIDATE_RESULT
  - MANUAL_CANONICAL_CANDIDATE_REFERENCE

placement_review_mode:
  - REVIEW_ONLY
  - QUEUE_CANDIDATE_ELIGIBILITY_REVIEW
  - ACTIVE_TASK_PROPOSAL_ELIGIBILITY_REVIEW

expected_candidate_shape:
  - TASK_CONTRACT_CANDIDATE
  - QUEUE_MATERIALIZATION_INPUT_CANDIDATE
  - ACTIVE_TASK_PROPOSAL_INPUT_CANDIDATE
```

- REVIEW_ONLY is the safest default
- QUEUE_CANDIDATE_ELIGIBILITY_REVIEW does not authorize queue placement
- ACTIVE_TASK_PROPOSAL_ELIGIBILITY_REVIEW does not authorize active-task replacement
- any unknown enum value is invalid

## 7. Required Traceability

Traceability is required for:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- m50_traceability
- m51_generator_evidence
- m52_validation_evidence

M53 input must preserve M50/M51/M52 traceability and must not create a candidate with broken provenance.

## 8. Required Carry-Forward

Carry-forward is required for:
- accepted_limitations
- warnings
- open_questions
- downstream_limits
- known_gaps
- non_authority_boundary

M53 input must not silently drop accepted limitations, warnings, open questions, downstream limits, or known gaps from M52.

- empty carry-forward arrays are allowed only when reviewed M52 source artifacts contain no such items
- limitations must not be weakened
- warnings must not be converted into clean completion
- open questions must not be removed without source evidence
- downstream limits must not be expanded silently
- non-authority boundaries must be preserved

## 9. Placement Target

```yaml
placement_target:
  queue_candidate_allowed_for_review: true | false
  active_task_candidate_allowed_for_review: true | false
```

- these fields describe what kind of eligibility review is being requested
- they do not authorize queue placement
- they do not authorize active-task replacement
- both may not be true unless the input explicitly requests dual eligibility review
- dual eligibility review is allowed only as review-only classification, not materialization

## 10. Boundary Flags

```yaml
boundaries:
  review_only: true
  queue_write_allowed: false
  active_task_write_allowed: false
  execution_authorized: false
  approval_record_creation_allowed: false
  lifecycle_mutation_allowed: false
  m54_materialization_authorized: false
```

- any boundary flag that grants authority must block placement review input
- review_only must be true
- all authority-expanding flags must be false
- M53 input cannot authorize M54 materialization

## 11. Invalid Input Conditions

- missing placement_review_input
- missing input_id
- missing source_candidate_id
- missing source_m52_completion_review
- source_m52_completion_review not equal to reports/m52-completion-review.md
- missing source_m52_validation_result
- missing source_generated_artifact
- missing required_traceability
- missing required_carry_forward
- missing placement_target
- missing boundaries
- review_only not true
- queue_write_allowed not false
- active_task_write_allowed not false
- execution_authorized not false
- approval_record_creation_allowed not false
- lifecycle_mutation_allowed not false
- m54_materialization_authorized not false
- unknown source_candidate_origin
- unknown placement_review_mode
- unknown expected_candidate_shape
- limitations dropped
- warnings dropped
- open questions dropped
- downstream limits dropped
- known gaps dropped
- forbidden changes weakened
- allowed changes expanded
- input claims queue placement already occurred
- input claims active-task replacement already occurred
- input claims approval already exists
- input claims M54 materialization is authorized

## 12. Relationship to M54

M53 input may identify a candidate for future M54 consideration.
M53 input does not authorize M54 to run.
M53 input does not authorize queue materialization.
M53 input does not authorize active-task proposal materialization.
M54 must independently validate materialization.

## 13. Summary

The M53 placement review input contract is a review-only input boundary.

It may prepare a candidate for placement eligibility review.
It must not place the candidate.
It must not approve the candidate.
It must not execute the candidate.
It must not materialize the candidate.
