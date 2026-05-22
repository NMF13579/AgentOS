---
type: task-contract-proposal-template
milestone: M49
status: canonical
authority: template
version: 1.0.0
created: 2026-05-21
owner: human
---

# M49 Task Contract Proposal Template

## Purpose
Task Contract Proposal Template defines the required structure for non-executable task contract proposals derived from task drafts.

Task Contract Proposal Template does not create executable tasks.
Task Contract Proposal Template does not create authorized task contracts.
Task Contract Proposal Template does not authorize implementation.
Task Contract Proposal Template does not authorize execution.

## Role in M49
M49 Task Contract Proposal Template defines the second non-executable output shape of UX-to-task decomposition.

Task contract proposal is a proposal artifact.
Task contract proposal is not an executable task contract.
Task contract proposal is not implementation permission.
Task contract proposal is not execution permission.
Task contract proposal requires separate human authorization before execution.

## Relationship to Task Draft Model
Task Contract Proposal Template depends on docs/TASK-DRAFT-MODEL.md.
Task contract proposals may be derived from task drafts only through a separate authorized task.
Task draft conversion is not execution.
Task draft conversion does not authorize implementation.

Task draft may inform a task contract proposal.
Task draft does not automatically become a task contract proposal.
Task draft conversion requires separate authorization.

## Relationship to UX-to-Task Input Contract
Task Contract Proposal Template depends on docs/UX-TO-TASK-INPUT-CONTRACT.md.
Task contract proposals must preserve UX-to-task input readiness constraints.
Input readiness is not task generation.
Input readiness is not execution authorization.

UX_TO_TASK_INPUT_READY may inform proposal creation only under a separate authorized task.
UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS may inform proposal creation only if limitations are carried forward.
UX_TO_TASK_INPUT_BLOCKED must not produce task contract proposals.
UX_TO_TASK_INPUT_INVALID must not produce task contract proposals.

## Template Usage Rules
This template may be used to draft a non-executable task contract proposal.
This template must not be copied directly into tasks/active-task.md.
This template must not be copied directly into tasks/queue/.
This template must not be treated as an executable task contract.

Template use is not authorization.
Template completion is not authorization.
Template validation is not authorization.

## Required Proposal Frontmatter
```yaml
---
type: task-contract-proposal
proposal_id: PROPOSAL-UX-<source-slug>-<number>
proposal_status: PROPOSED_ONLY
source_draft_id: DRAFT-UX-<source-slug>-<number>
source_task_draft_path: <path-to-task-draft>
source_ux_contract: <path-to-ux-contract>
source_readiness_report: <path-to-readiness-report>
source_boundary_policy: <path-to-boundary-policy>
execution_authorized: false
implementation_authorized: false
human_authorization_required: true
created: YYYY-MM-DD
owner: human
---
```

proposal_status: PROPOSED_ONLY is required.
execution_authorized: false is required.
implementation_authorized: false is required.
human_authorization_required: true is required.

## Required Proposal Body Sections
Required future proposal body sections:
- Purpose
- Source Traceability
- Proposed Task Contract Summary
- Proposed Goal
- Proposed Scope
- Proposed Allowed Changes
- Proposed Forbidden Changes
- Proposed Validation
- Proposed Risk Notes
- Carry-Forward Requirements
- Human Authorization Requirement
- Non-Executable Boundary
- Summary

Proposal body sections are planning sections only.
Proposal body sections do not create an executable task.
Proposal body sections do not create an authorized task contract.

## Required Proposal Model
```yaml
task_contract_proposal:
  proposal_id:
  proposal_status: PROPOSED_ONLY
  source_draft:
    source_draft_id:
    source_task_draft_path:
    draft_status:
  source_product_spec:
    spec_id:
    spec_version:
    product_spec_path:
  source_ux_contract:
    ux_contract_id:
    ux_contract_version:
    ux_contract_path:
    ux_contract_validation_result:
  source_readiness_report:
    readiness_report_path:
    readiness_validation_result:
    readiness_decision:
  source_boundary_policy:
    boundary_policy_path:
  source_sections:
    - section.reference
  proposed_contract:
    proposed_task_id:
    proposed_task_name:
    proposed_mode:
    proposed_goal:
    proposed_scope:
    proposed_allowed_changes:
    proposed_forbidden_changes:
    proposed_validation:
    proposed_expected_final_report:
  carry_forward:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
  authorization:
    human_authorization_required: true
    authorization_reference:
    authorized_by:
    authorized_at:
  boundaries:
    execution_authorized: false
    implementation_authorized: false
    active_task_allowed: false
    task_queue_allowed: false
  review:
    reviewed_by:
    reviewed_at:
```

Task contract proposal must preserve source_draft_id.
Task contract proposal must preserve source_sections.
Task contract proposal must preserve carry-forward constraints.
Task contract proposal must preserve non-authority boundary.

## Required Source Fields
Required source fields:
- proposal_id
- proposal_status
- source_draft_id
- source_task_draft_path
- source_product_spec
- source_ux_contract
- source_readiness_report
- source_boundary_policy
- source_sections

Missing source_draft_id blocks proposal readiness.
Missing source_task_draft_path blocks proposal readiness.
Missing source_ux_contract blocks proposal readiness.
Missing source_readiness_report blocks proposal readiness.
Missing source_boundary_policy blocks proposal readiness.
Missing source_sections blocks proposal readiness.

## Required Proposed Contract Fields
Required proposed contract fields:
- proposed_task_id
- proposed_task_name
- proposed_mode
- proposed_goal
- proposed_scope
- proposed_allowed_changes
- proposed_forbidden_changes
- proposed_validation
- proposed_expected_final_report

Proposed contract fields are proposal fields only.
Proposed contract fields do not create an executable task.
Proposed contract fields do not create an authorized task contract.

## Required Carry-Forward Fields
Required carry-forward fields:
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary

Accepted limitations must be carried forward into every task contract proposal.
Open questions must be carried forward into every task contract proposal.
Downstream limits must be carried forward into every task contract proposal.
Non-authority boundary must be carried forward into every task contract proposal.

Task contract proposals must not hide accepted limitations.
Task contract proposals must not drop open questions.
Task contract proposals must not drop downstream limits.
Task contract proposals must not drop non-authority boundaries.

## Required Boundary Fields
Required boundary fields:
- proposal_status: PROPOSED_ONLY
- execution_authorized: false
- implementation_authorized: false
- human_authorization_required: true
- active_task_allowed: false
- task_queue_allowed: false

Task contract proposal with execution_authorized: true is invalid.
Task contract proposal with implementation_authorized: true is invalid.
Task contract proposal with human_authorization_required: false is invalid.
Task contract proposal with active_task_allowed: true is invalid.
Task contract proposal with task_queue_allowed: true is invalid.

## Required Human Authorization Fields
Required human authorization fields:
- human_authorization_required
- authorization_reference
- authorized_by
- authorized_at

Human authorization is required before any task contract proposal becomes an executable task contract.
Human authorization must be attached to a specific proposal conversion action.
Human authorization cannot be inferred from proposal_status.
Human authorization cannot be inferred from validator PASS.
Human authorization cannot be inferred from readiness.

Missing human authorization blocks executable task contract creation.
Generic approval is not sufficient for proposal execution.

## Proposal Statuses
PROPOSED_ONLY means the proposal is non-executable and not yet ready for review.
PROPOSAL_READY_FOR_REVIEW means the proposal may be reviewed for future authorization.
PROPOSAL_BLOCKED means required source, readiness, carry-forward, or authorization input is missing.
PROPOSAL_INVALID means the proposal violates required structure or authority boundaries.

PROPOSED_ONLY does not authorize execution.
PROPOSAL_READY_FOR_REVIEW does not authorize execution.
PROPOSAL_BLOCKED does not authorize execution.
PROPOSAL_INVALID does not authorize execution.

## Blocking Conditions
Proposal creation is blocked if:
- task draft is missing
- task draft status is DRAFT_BLOCKED
- task draft status is DRAFT_INVALID
- UX-to-task input status is UX_TO_TASK_INPUT_BLOCKED
- UX-to-task input status is UX_TO_TASK_INPUT_INVALID
- source UX Contract is missing
- UX Contract validation result is not UX_CONTRACT_VALIDATION_OK
- readiness validation result is not UX_PLANNING_READINESS_VALIDATION_OK
- readiness_decision is UX_PLANNING_NOT_READY
- readiness_decision is UX_PLANNING_BLOCKED
- accepted limitations are not carried forward
- open questions are not carried forward
- downstream limits are missing
- non-authority boundary is missing
- source_sections are missing
- authority claim exists

Blocked task draft must not produce task contract proposals.
Invalid task draft must not produce task contract proposals.
Missing carry-forward fields block proposal readiness.
Authority claims block proposal readiness.

## Invalid Proposal Conditions
A proposal is invalid if:
- execution_authorized is true
- implementation_authorized is true
- human_authorization_required is false
- active_task_allowed is true
- task_queue_allowed is true
- proposal_status implies execution
- source_section is used instead of source_sections
- required source fields are missing
- required proposed contract fields are missing
- required carry-forward fields are missing
- forbidden authority claim exists

Executable task contract proposal is invalid.
Implementation-authorizing task contract proposal is invalid.
Task contract proposal without carry-forward limits is invalid.
Task contract proposal with forbidden authority claim is invalid.

## Non-Executable Boundary
Task contract proposal is non-executable by definition.
Task contract proposal must not be copied into tasks/active-task.md.
Task contract proposal must not be copied into tasks/queue/.
Task contract proposal must not be used as an active task.
Task contract proposal must not be used as an executable task contract.

No executable task may be created from a task contract proposal alone.
No active task may be created from a task contract proposal alone.
No task queue entry may be created from a task contract proposal alone.

## Conversion Boundary
Task contract proposal may inform a future executable task contract.
Task contract proposal must be converted into an executable task contract by a separate authorized task.
Task contract proposal conversion must preserve carry-forward constraints.
Task contract proposal conversion must preserve non-authority boundary.

Task contract proposal conversion is not execution.
Task contract proposal conversion requires separate authorization.
Task contract proposal conversion must not bypass human gate.

## Future Validator Notes
Future M49 validator may check task contract proposal required fields.
Future M49 validator may check proposal_status values.
Future M49 validator may check execution_authorized: false.
Future M49 validator may check implementation_authorized: false.
Future M49 validator may check human_authorization_required: true.
Future M49 validator may check active_task_allowed: false.
Future M49 validator may check task_queue_allowed: false.
Future M49 validator may check carry-forward fields.
Future M49 validator may check forbidden authority claims.

Future M49 validator must not create task contract proposals.
Future M49 validator must not create executable task contracts.
Future M49 validator must not authorize implementation.
Future M49 validator must not authorize execution.

## What This Template Does Not Do
This template does not:
- create task contract proposals automatically
- create executable tasks
- create task contracts
- write to tasks/active-task.md
- write to tasks/queue/
- generate task graph
- perform decomposition
- approve implementation
- approve execution
- choose frontend framework
- define production component architecture
- write frontend code
- write backend code
- commit
- push
- merge
- deploy
- release

Task Contract Proposal Template does not perform UX-to-task decomposition.

## Non-Authority Boundary
Task Contract Proposal Template is not task generation.
Task Contract Proposal Template is not implementation approval.
Task Contract Proposal Template does not create task contract proposals automatically.
Task Contract Proposal Template does not create executable tasks.
Task Contract Proposal Template does not create authorized task contracts.
Task Contract Proposal Template does not authorize task generation.
Task Contract Proposal Template does not authorize implementation.
Task Contract Proposal Template does not authorize execution planning.
Task Contract Proposal Template does not authorize commit, push, merge, deploy, or release.
Task Contract Proposal Template may define non-executable proposal structure only.
Future executable task contracts require separate authorized tasks.
Future executable task contracts require separate human authorization.

## Summary
This template defines a strict non-executable format for task contract proposals.
It preserves source traceability and carry-forward constraints.
It preserves boundary restrictions and human gate requirements.
It does not authorize implementation or execution at any step.
