# Proposal-to-Task Conversion Policy

## Purpose

Define the controlled policy for transforming a validated task contract proposal into a task contract candidate ready for placement review in M50.

## Policy Boundary

Proposal-to-task conversion is a controlled transformation policy only.
Proposal-to-task conversion does not authorize execution.
Proposal-to-task conversion does not authorize queue placement.
Proposal-to-task conversion does not authorize active-task replacement.
Proposal-to-task conversion does not create approval records.
Proposal-to-task conversion does not start implementation.

## Conversion Eligibility

Conversion is allowed only when all of the following are true:

- source proposal is present
- source proposal status is eligible
- proposal validation result is valid
- conversion input package is present
- human authorization reference is present
- human authorization is scoped to conversion only
- human authorization is valid at validator runtime
- accepted limitations are preserved
- open questions are preserved
- downstream limits are preserved
- non-authority boundary is preserved
- source traceability is preserved
- conversion scope does not expand proposal scope

Proposal status alone is not sufficient for conversion.
Proposal validation result is required.
M49_COMPLETE is not sufficient for conversion.

## Allowed Proposal Statuses

Allowed normalized statuses:

- TASK_CONTRACT_PROPOSAL_VALIDATED
- TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS

Not eligible statuses:

- TASK_CONTRACT_PROPOSAL_DRAFT
- TASK_CONTRACT_PROPOSAL_NEEDS_CLARIFICATION
- TASK_CONTRACT_PROPOSAL_BLOCKED
- TASK_CONTRACT_PROPOSAL_INVALID
- TASK_CONTRACT_PROPOSAL_REJECTED

## Required Proposal Validation Results

- proposal_validation_result must exist
- proposal_validation_result must reference the source proposal
- proposal_validation_result must indicate validated or validated_with_limitations
- proposal_validation_result must not indicate invalid, blocked, missing, failed, or unknown

Validator PASS is not human authorization.
Validated proposal is not execution permission.

## Required Human Authorization Conditions

Human authorization for conversion is required.
Human authorization for conversion must be explicit.
Human authorization for conversion must be scoped.
Human authorization for conversion must reference a specific proposal.
Human authorization for conversion must be valid when the conversion validator runs.
Human authorization for conversion is not execution approval.
Human authorization for conversion is not queue placement approval.
Human authorization for conversion is not active-task replacement approval.
Human authorization for conversion is not implementation approval.
Generic approval is not sufficient.
Agent-simulated approval is not sufficient.
Validator-created approval records are invalid.

## Required Conversion Input Conditions

Required conversion input fields:

- source_task_contract_proposal
- proposal_validation_result
- source_ux_contract
- source_readiness_report
- source_boundary_policy
- source_sections
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- human_authorization_record
- conversion_scope
- candidate_output

Missing accepted_limitations must block conversion.
Missing open_questions must block conversion.
Missing downstream_limits must block conversion.
Missing non_authority_boundary must block conversion.
Missing human_authorization_record must block conversion or require human authorization review.

## Field Transfer Policy

Fields are divided into:

- exact transfer fields
- transformable fields
- non-expandable fields

## Exact Transfer Fields

These fields must be preserved without weakening, omission, or reinterpretation:

- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- source_traceability
- risk_notes
- validation_requirements
- forbidden_changes

Exact transfer fields must not be silently normalized.
Exact transfer fields must not be summarized in a way that removes constraints.
Exact transfer fields must not be dropped because they are inconvenient.

## Transformable Fields

Transformation is allowed only for formatting and candidate-structure alignment.

Transformations are allowed only when they preserve source meaning.
Transformations must not expand scope.
Transformations must not weaken restrictions.
Transformations must not create implied acceptance criteria.
Transformations must not create implied approval.
Transformations must not create implied queue eligibility.
Transformations must not create implied active-task eligibility.

Allowed transformation examples:

- renaming proposal goal into candidate goal when meaning is preserved
- formatting validation items into a candidate validation section
- formatting source references into traceability fields
- copying limitations into carry_forward.accepted_limitations
- copying open questions into carry_forward.open_questions
- copying downstream limits into carry_forward.downstream_limits

Forbidden transformation examples:

- turning open questions into accepted requirements
- turning downstream limits into permission
- turning limitations into optional notes
- turning forbidden changes into warnings
- turning allowed changes into broader implementation scope
- turning human authorization for conversion into execution approval

## Non-Expandable Fields

These fields must not be expanded beyond the source proposal and conversion scope:

- scope
- allowed_changes
- implementation surface
- affected paths
- risk acceptance
- authorization scope
- candidate permissions

No scope expansion is allowed during M50 conversion.
No allowed_changes expansion is allowed during M50 conversion.
No authorization scope expansion is allowed during M50 conversion.

## Allowed Changes Policy

allowed_changes must be derived from the source proposal and conversion scope.
allowed_changes must not be expanded.
allowed_changes must not include paths or operations absent from the proposal or authorization scope.
allowed_changes must not include queue placement.
allowed_changes must not include active-task replacement.
allowed_changes must not include implementation unless later lifecycle gates authorize it.

## Forbidden Changes Policy

forbidden_changes must be preserved.
forbidden_changes must not be weakened.
forbidden_changes must not be converted into optional guidance.
forbidden_changes must not be dropped during conversion.
A candidate that weakens forbidden_changes is invalid.
A candidate that omits source forbidden_changes is invalid unless the source explicitly has none.

## Validation Preservation Policy

validation requirements must be preserved.
validation requirements may be reformatted but not weakened.
validation requirements must not be replaced by generic validation.
validation requirements must not imply execution approval.
validation requirements must not imply completion approval.

## Risk Notes Preservation Policy

risk_notes must be preserved when present.
risk_notes must not be downgraded.
risk_notes must not be hidden in summary text.
risk_notes must not be converted into non-blocking notes if the source marks them as blocking.

## Downstream Limits Preservation Policy

downstream_limits must be preserved.
downstream_limits must not be dropped.
downstream_limits must not be converted into permission.
downstream_limits must not be treated as resolved by conversion.
downstream_limits must remain visible for M51+.

## Carry-Forward Policy

Accepted limitations must be carried forward.
Open questions must be carried forward.
Downstream limits must be carried forward.
Non-authority boundary must be carried forward.
Source traceability must be preserved.

## Scope Expansion Prohibition

Conversion scope must not expand proposal scope.
Conversion scope must not expand human authorization scope.
Conversion scope must not create new implementation authority.
Conversion scope must not create queue placement authority.
Conversion scope must not create active-task authority.

## Silent Transformation Prohibition

No silent normalization.
No silent scope rewriting.
No inferred authorization.
No implied acceptance criteria.
No implied queue eligibility.
No implied active-task eligibility.
No expansion of allowed changes.
No weakening of forbidden changes.
No removal of limitations.
No removal of open questions.
No removal of downstream limits.
No conversion from candidate to active task.
No conversion from candidate to queue entry.
No conversion from human authorization into execution approval.

## Candidate Boundary Policy

Task contract candidate is not active task state.
Task contract candidate is not queue entry.
Task contract candidate must not be copied into tasks/active-task.md by M50.
Task contract candidate must not be placed into tasks/queue/ by M50.
M50 uses EXECUTION_SHAPE, not EXECUTION.
EXECUTION_SHAPE does not mean execution is authorized.
execution_authorized must always be false in M50.
execution_permission_granted must always be false in M50.
active_task_allowed must always be false in M50.
task_queue_allowed must always be false in M50.

## Blocking Conditions

- proposal invalid
- proposal validation missing
- proposal validation unknown
- proposal validation failed
- proposal status not eligible
- human authorization missing
- human authorization expired
- human authorization invalid at validator runtime
- authorization scope mismatch
- conversion input missing
- accepted limitations dropped
- open questions dropped
- downstream limits dropped
- forbidden changes weakened
- allowed changes expanded
- source traceability missing
- non-authority boundary missing
- risk notes downgraded
- validation requirements weakened
- conversion scope expands proposal scope
- conversion scope expands authorization scope
- candidate mode is EXECUTION
- candidate mode is not EXECUTION_SHAPE
- candidate claims execution authorization
- candidate grants execution permission
- candidate allows active task placement
- candidate allows queue placement
- validator creates approval side effect

## Non-Authority Rules

Policy compliance is not execution approval.
Policy compliance is not queue placement approval.
Policy compliance is not active-task replacement approval.
Policy compliance is not implementation approval.
Policy document existence is not approval.

## Explicit Non-Goals

Task 50.5 does not do:

- create conversion packages
- create task contract candidates
- create active tasks
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create real approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create templates
- create schemas
- create validators
- create fixtures
- create examples
- create evidence reports
- create completion reviews
- commit
- push
- merge
- deploy
- release
