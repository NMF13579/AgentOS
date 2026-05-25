# Task Contract Candidate Validation Output Contract (M52)

## Purpose

This document defines the machine-readable output contract emitted by future M52 candidate validation.

## What candidate_validation_result Is

`candidate_validation_result` is the validation output object describing result token, status fields, traceability, carry-forward state, boundaries, and review-input eligibility for M53 review.

## What candidate_validation_result Is Not

Candidate validation result is not approval.
Candidate validation result is not execution permission.
Candidate validation result is not queue placement.
Candidate validation result is not active-task replacement.
Candidate validation result does not create lifecycle state.
Candidate validation result does not authorize M53 placement.

TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not approval.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not queue placement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not active-task replacement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not execution permission.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not M53 placement authorization.

## Result Tokens

- TASK_CONTRACT_CANDIDATE_VALIDATION_OK
- TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS
- TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED
- TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED

## Exit Code and Status Semantics

- OK: `exit_code: 0`, `validated: true`, `m53_review_input_candidate: true`, no blockers.
- OK_WITH_LIMITATIONS: `exit_code: 0`, `validated: true`, `m53_review_input_candidate: true`, warnings may exist, limitations/open questions may remain, no blockers.
- FAILED: `exit_code: 1`, `validated: false`, `m53_review_input_candidate: false`.
- BLOCKED: `exit_code: 2`, `validated: false`, `m53_review_input_candidate: false`.

## m53_review_input_candidate Semantics

m53_review_input_candidate: true means only that the artifact may be used as input for M53 review.
m53_review_input_candidate: true does not authorize M53 placement.
m53_review_input_candidate: true does not authorize queue placement.
m53_review_input_candidate: true does not authorize active-task replacement.
m53_review_input_candidate: true does not authorize execution.
m53_review_input_candidate: true does not create approval.
m53_review_input_candidate: true does not create lifecycle state.

FAILED and BLOCKED results cannot be M53 review input.

## Source Traceability Semantics

source_traceability must be an object, not a free-form string.
source_generated_artifact appears both at top level for quick reference and inside source_traceability for full provenance tracing.

source_authorization means provenance authorization for source conversion / candidate generation only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.

## required_sections Semantics

required_sections must be an object, not a free-form string.
required_sections fields indicate candidate section presence for classification and do not authorize approval, execution, or placement.
required_sections fields indicate candidate section presence for classification and do not authorize approval, execution, or placement.
Each required_sections field is boolean.
required_sections may contain false in FAILED or BLOCKED.
required_sections does not create approval.
required_sections does not authorize execution.
required_sections does not authorize placement.

## carry_forward Semantics

carry_forward must be an object, not a free-form string.
accepted_limitations, open_questions, downstream_limits, and non_authority_boundary must be preserved from source conversion package without deletion.
OK_WITH_LIMITATIONS must preserve limitations and open questions.

## boundary_flags and Final Authority Semantics

boundary_flags must be an object, not a free-form string.

boundary_flags must enforce:
- validation_only: true
- placement_authorized: false
- execution_authorized: false
- queue_write_allowed: false
- active_task_write_allowed: false
- approval_record_creation_allowed: false

Final authority fields must remain false:
- placement_authorized
- execution_authorized
- active_task_write_allowed
- queue_write_allowed
- approval_record_creation_allowed

Candidate validation result is valid only if all non-authority boundary fields remain false.
Any result that sets placement_authorized, execution_authorized, queue_write_allowed, active_task_write_allowed, or approval_record_creation_allowed to true is invalid.

## non_authority_markers Semantics

non_authority_markers must include all required M52 non-authority markers.
Required markers:
- CANDIDATE_VALIDATION_IS_NOT_APPROVAL
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_EXECUTION
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_QUEUE_PLACEMENT
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_ACTIVE_TASK_REPLACEMENT
- CANDIDATE_VALIDATION_DOES_NOT_CREATE_LIFECYCLE_STATE
- CANDIDATE_VALIDATION_REQUIRES_M53_PLACEMENT_REVIEW

## findings / warnings / blockers Semantics

- findings explain observed validation outcomes.
- warnings capture non-blocking limitations.
- blockers explain why validation failed or could not safely proceed.

## Schema Layout Constraints For Task 52.3

candidate_validation_result.properties and candidate_validation_result.allOf must be declared on the same schema object.
All fields referenced by result conditional logic must be declared in candidate_validation_result.properties.

Task 52.3 defines output contract only.
Task 52.3 does not implement validator CLI.
Task 52.3 does not create a real validation result JSON in reports/.

## Why Output Does Not Grant Authority

OK does not authorize M53 placement.
OK does not authorize queue placement.
OK does not authorize active-task replacement.
OK does not authorize execution.
The output contract does not create lifecycle state.
