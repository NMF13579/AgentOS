---
type: task-draft-model
milestone: M49
status: canonical
authority: draft-model
version: 1.0.0
created: 2026-05-21
owner: human
---

# M49 Task Draft Model

## Purpose
Task Draft Model defines the required structure for non-executable task drafts derived from UX structure and readiness evidence.

Task Draft Model does not create executable tasks.
Task Draft Model does not create task contracts.
Task Draft Model does not create task contract proposals.
Task Draft Model does not authorize implementation.
Task Draft Model does not authorize execution.

## Role in M49
M49 Task Draft Model defines the first non-executable output shape of UX-to-task decomposition.

Task draft is a planning artifact.
Task draft is not a task contract.
Task draft is not task generation permission.
Task draft is not implementation permission.
Task draft is not execution permission.

## Relationship to M49 Architecture
Task Draft Model depends on docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md.
Task Draft Model must preserve the M49 non-executable output model.
Task Draft Model must preserve execution_authorized: false.
Task Draft Model must preserve draft_status: DRAFT_ONLY unless explicitly blocked or invalid.

Task Draft Model must not weaken M49 architecture boundaries.
Task Draft Model must not convert readiness into execution authorization.

## Relationship to UX-to-Task Input Contract
Task Draft Model depends on docs/UX-TO-TASK-INPUT-CONTRACT.md.
Task drafts may be created only from input packages that satisfy UX-to-task input readiness.
Input readiness is not task generation.
Input readiness is not execution authorization.

UX_TO_TASK_INPUT_READY may inform task draft creation only under a separate authorized task.
UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS may inform task draft creation only if limitations are carried forward.
UX_TO_TASK_INPUT_BLOCKED must not produce task drafts.
UX_TO_TASK_INPUT_INVALID must not produce task drafts.

## Task Draft Definition
Task draft is a non-executable planning artifact that describes a possible future task derived from UX structure, readiness evidence, and carry-forward constraints.

Task draft is earlier than task contract proposal.
Task draft is earlier than authorized task contract.
Task draft is earlier than execution.

## Task Draft Lifecycle
UX-to-task input package
↓
input readiness review
↓
task draft candidate
↓
task draft validation
↓
task contract proposal candidate
↓
separate human authorization
↓
authorized executable task contract

Task draft lifecycle stops before execution.
Task draft lifecycle stops before implementation.
Task draft lifecycle stops before active task state.

## Task Draft Statuses
DRAFT_ONLY means the draft is non-executable and not yet ready for proposal conversion.
DRAFT_READY_FOR_PROPOSAL means the draft may inform a future task contract proposal.
DRAFT_BLOCKED means required source, readiness, carry-forward, or authorization input is missing.
DRAFT_INVALID means the draft violates required structure or authority boundaries.

DRAFT_ONLY does not authorize execution.
DRAFT_READY_FOR_PROPOSAL does not authorize execution.
DRAFT_BLOCKED does not authorize execution.
DRAFT_INVALID does not authorize execution.

## Required Task Draft Model
```yaml
task_draft:
  draft_id:
  draft_status: DRAFT_ONLY
  source_type:
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
  proposed_task:
    proposed_task_type:
    proposed_task_name:
    proposed_goal:
    proposed_scope_summary:
    proposed_non_goals:
    proposed_dependencies:
    proposed_risks:
  carry_forward:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
  authorization:
    human_authorization_for_decomposition:
    authorization_reference:
    authorized_by:
    authorized_at:
  boundaries:
    execution_authorized: false
    human_authorization_required: true
    implementation_authorized: false
    active_task_allowed: false
    task_queue_allowed: false
  review:
    reviewed_by:
    reviewed_at:
```

execution_authorized: false is mandatory.
implementation_authorized: false is mandatory.
human_authorization_required: true is mandatory.
active_task_allowed: false is mandatory.
task_queue_allowed: false is mandatory.

## Required Source Fields
Required source fields:
- draft_id
- draft_status
- source_type
- source_product_spec
- source_ux_contract
- source_readiness_report
- source_boundary_policy
- source_sections

Missing source_product_spec blocks task draft readiness.
Missing source_ux_contract blocks task draft readiness.
Missing source_readiness_report blocks task draft readiness.
Missing source_boundary_policy blocks task draft readiness.
Missing source_sections blocks task draft readiness.

## Required Proposed Task Fields
Required proposed task fields:
- proposed_task_type
- proposed_task_name
- proposed_goal
- proposed_scope_summary
- proposed_non_goals
- proposed_dependencies
- proposed_risks

Proposed task fields are planning fields only.
Proposed task fields do not create an executable task.
Proposed task fields do not create an authorized task contract.

## Required Carry-Forward Fields
Required carry-forward fields:
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary

Accepted limitations must be carried forward into every task draft.
Open questions must be carried forward into every task draft.
Downstream limits must be carried forward into every task draft.
Non-authority boundary must be carried forward into every task draft.

Task drafts must not hide accepted limitations.
Task drafts must not drop open questions.
Task drafts must not drop downstream limits.
Task drafts must not drop non-authority boundaries.

## Required Boundary Fields
Required boundary fields:
- execution_authorized: false
- human_authorization_required: true
- implementation_authorized: false
- active_task_allowed: false
- task_queue_allowed: false

Task draft with execution_authorized: true is invalid.
Task draft with implementation_authorized: true is invalid.
Task draft with active_task_allowed: true is invalid.
Task draft with task_queue_allowed: true is invalid.

## Allowed Source Types
Allowed source types:
- screen
- state
- flow
- user_action
- approval_point
- risk_point
- blocked_state
- open_question
- accepted_limitation
- downstream_limit
- traceability_gap

Source type identifies the UX or readiness source that motivated the draft.
Source type does not authorize implementation.
Source type does not authorize execution.

## Allowed Proposed Task Types
Allowed proposed task types:
- ui_structure
- state_handling
- flow_definition
- interaction_behavior
- approval_boundary
- risk_communication
- blocked_behavior
- clarification
- limitation_carry_forward
- traceability_repair

Proposed task type is classification only.
Proposed task type is not permission to implement.
Proposed task type is not permission to execute.

## Draft ID Rules
Draft ID format:
- DRAFT-UX-<source-slug>-<number>

Examples:
- DRAFT-UX-agent-action-review-001
- DRAFT-UX-agent-action-review-002
- DRAFT-UX-agent-action-review-003

Rules:
- Draft IDs must be deterministic.
- Draft IDs must be stable for the same source input.
- Draft IDs must not imply execution order.
- Draft IDs must not imply priority.
- Draft IDs must not imply authorization.

Draft ID is not execution order.

## Traceability Requirements
Every task draft must preserve:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- ux_contract_version
- ux_contract_path
- readiness_report_path
- boundary_policy_path
- source_sections

source_sections must be plural.
source_sections must be a list.
source_section must not be used.
Traceability is not approval.
Traceability is not execution authorization.

## Blocking Conditions
Task draft creation is blocked if:
- UX-to-task input is missing
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
- human authorization for decomposition is missing
- authority claim exists

Blocked input must not produce task drafts.
Invalid input must not produce task drafts.
Missing carry-forward fields block task draft readiness.
Authority claims block task draft readiness.

## Invalid Draft Conditions
A task draft is invalid if:
- execution_authorized is true
- implementation_authorized is true
- human_authorization_required is false
- active_task_allowed is true
- task_queue_allowed is true
- source_section is used instead of source_sections
- required source fields are missing
- required proposed task fields are missing
- required carry-forward fields are missing
- forbidden authority claim exists

Executable task draft is invalid.
Implementation-authorizing task draft is invalid.
Task draft without carry-forward limits is invalid.
Task draft with forbidden authority claim is invalid.

## Non-Executable Boundary
Task draft is non-executable by definition.
Task draft must not be copied into tasks/active-task.md.
Task draft must not be copied into tasks/queue/.
Task draft must not be used as an active task.
Task draft must not be used as an executable task contract.

No executable task may be created from a task draft alone.
No active task may be created from a task draft alone.
No task queue entry may be created from a task draft alone.

## Human Authorization Boundary
Human authorization for decomposition permits draft review only.
Human authorization for decomposition does not authorize implementation.
Human authorization for decomposition does not authorize execution.
Human authorization for decomposition does not convert a task draft into a task contract.

Task draft requires separate human authorization before becoming a task contract proposal.
Task contract proposal requires separate human authorization before becoming executable.

## Relationship to Future Task Contract Proposal
Task draft may inform a future task contract proposal.
Task draft must be converted into a task contract proposal by a separate authorized task.
Task draft must preserve carry-forward constraints when converted into a proposal.
Task draft must preserve non-authority boundary when converted into a proposal.

Task draft is not task contract proposal.
Task draft conversion is not execution.
Task draft conversion requires separate authorization.

## Future Validator Notes
Future M49 validator may check task draft required fields.
Future M49 validator may check allowed source types.
Future M49 validator may check allowed proposed task types.
Future M49 validator may check execution_authorized: false.
Future M49 validator may check implementation_authorized: false.
Future M49 validator may check human_authorization_required: true.
Future M49 validator may check active_task_allowed: false.
Future M49 validator may check task_queue_allowed: false.
Future M49 validator may check carry-forward fields.
Future M49 validator may check forbidden authority claims.

Future M49 validator must not create task drafts.
Future M49 validator must not create task contract proposals.
Future M49 validator must not authorize implementation.
Future M49 validator must not authorize execution.

## What This Model Does Not Do
Task Draft Model does not:
- create task drafts automatically
- create task contract proposals
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

Task Draft Model does not perform UX-to-task decomposition.

## Non-Authority Boundary
Task Draft Model is not task generation.
Task Draft Model is not implementation approval.
Task Draft Model does not create task drafts automatically.
Task Draft Model does not create task contract proposals.
Task Draft Model does not create executable tasks.
Task Draft Model does not create authorized task contracts.
Task Draft Model does not authorize task generation.
Task Draft Model does not authorize implementation.
Task Draft Model does not authorize execution planning.
Task Draft Model does not authorize commit, push, merge, deploy, or release.
Task Draft Model may define non-executable draft structure only.
Future task contract proposals require separate authorized tasks.
Future executable task contracts require separate human authorization.

## Summary
Task Draft Model fixes a strict, non-executable structure for task draft artifacts in M49.
It allows planning structure only.
It preserves carry-forward constraints and authority boundaries.
It blocks execution authority at draft level.
It keeps conversion to proposal and conversion to executable contract under separate human authorization.
