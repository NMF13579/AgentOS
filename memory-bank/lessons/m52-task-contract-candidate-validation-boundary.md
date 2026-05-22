# M52 Task Contract Candidate Validation Boundary Lesson

lesson_metadata:
  lesson_id: m52-task-contract-candidate-validation-boundary
  source_milestone: M52
  source_evidence: reports/m52-task-contract-candidate-validation-evidence-report.md
  source_integration_report: reports/m52-task-contract-candidate-validation-integration.md
  source_validation_result: reports/m52-candidate-validation-result-agent-action-review.json
  lesson_status: DRAFT
  lesson_confirmed_by: null
  confirmation_expected_from: reports/m52-completion-review.md
  downstream_reuse:
    - M53

## Purpose

Capture reusable M52 boundary lesson for downstream M53 use.

## Source Evidence

- reports/m52-task-contract-candidate-validation-evidence-report.md
- reports/m52-task-contract-candidate-validation-integration.md
- reports/m52-candidate-validation-result-agent-action-review.json

## Core Lesson

Validated candidate is not placed.
Validated candidate is not active.
Validated candidate is not approved.
Validated candidate is not executable.
Validated candidate remains waiting for M53 placement review.

Validation OK is not approval.
Validation OK is not execution permission.
Validation OK is not queue placement.
Validation OK is not active-task replacement.
Validation OK is not M53 placement authorization.

## Boundary Lesson

Candidate validation must preserve M50/M51 traceability.
Candidate validation must preserve carry-forward fields.
Candidate validation must reject boundary weakening.
Candidate validation must reject candidate without conversion package wrapper when wrapper is expected.
Validator stdout JSON is not report side effect.
M53 must independently decide placement.

## Traceability Lesson

M52 candidate validation depends on explicit source traceability.

Preserve:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- source_candidate_origin
- m50_traceability
- m51_generator_evidence

source_authorization is provenance authorization only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.

## Carry-Forward Lesson

accepted_limitations, open_questions, downstream_limits, and non_authority_boundary must be preserved for M53 review.
Carry-forward fields must not be deleted.
Carry-forward fields must not be softened.
Carry-forward fields must not be converted into approval.
Carry-forward fields must not be hidden from M53 review.

## Wrapper Requirement Lesson

M52 validates generated conversion package wrapper with embedded task_contract_candidate.
A standalone candidate-only artifact is not the primary valid artifact when expected_candidate_shape is generated_conversion_package_with_embedded_candidate.
Candidate without conversion package wrapper must be rejected when wrapper is expected.
candidate-without-conversion-package-wrapper.md proves this boundary.

Reference fixture:
- tests/fixtures/task-contract-candidate-validation/negative/candidate-without-conversion-package-wrapper.md

## Stdout JSON Lesson

Validator JSON output goes to stdout only.
Reports JSON is created by caller shell redirection.
Validator must not open, create, or modify reports/*.json directly.
stdout JSON is not approval.
stdout JSON is not placement.
stdout JSON is not execution permission.

## M53 Handoff Lesson

m53_review_input_candidate: true means only that the artifact may be used as input for M53 review.
m53_review_input_candidate: true is not placement approval.
M53 must independently decide placement eligibility.
M52 must not decide queue placement.
M52 must not create queue entries.
M52 must not modify tasks/active-task.md.
M52 must not create approval records.
M52 must not authorize execution.

## Non-Authority Boundary

M52 lesson is not approval.
M52 lesson does not authorize execution.
M52 lesson does not authorize queue placement.
M52 lesson does not authorize active-task replacement.
M52 lesson does not create lifecycle state.
M52 lesson does not authorize M53 placement.

Lesson entry is not completion review.
Lesson entry does not confirm M52 completion.
Lesson entry does not start M53.

## Reuse Guidance for M53

M53 may use the validated candidate as review input only if M52 completion review confirms M52 completion.
M53 must independently check placement eligibility.
M53 must not treat M52 validation OK as queue placement approval.
M53 must not copy candidate into tasks/queue/ without its own placement decision.
M53 must not copy candidate into tasks/active-task.md as part of M52.
M53 must preserve M50/M51/M52 traceability.
M53 must preserve carry-forward fields and downstream limits.
M53 must continue to treat approval, execution, queue placement, and active-task replacement as separate lifecycle gates.

## Lesson Status

lesson_status: DRAFT means the lesson is captured but not confirmed.
lesson_confirmed_by: null means no completion review has confirmed this lesson yet.
confirmation_expected_from: reports/m52-completion-review.md means confirmation can only occur during M52 completion review.

The lesson must not claim M52 completion.
The lesson must not claim M53 readiness.
The lesson must not claim placement authorization.
The lesson must not claim approval.
