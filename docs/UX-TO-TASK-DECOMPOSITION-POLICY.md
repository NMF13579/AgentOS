---
type: ux-to-task-decomposition-policy
milestone: M49
status: canonical
authority: policy
version: 1.0.0
created: 2026-05-21
owner: human
---

# M49 UX-to-Task Decomposition Policy

## Purpose
UX-to-Task Decomposition Policy defines how validated UX sources may be mapped into non-executable task drafts and task contract proposal candidates.

UX-to-Task Decomposition Policy does not create task drafts.
UX-to-Task Decomposition Policy does not create task contract proposals.
UX-to-Task Decomposition Policy does not create executable tasks.
UX-to-Task Decomposition Policy does not authorize implementation.
UX-to-Task Decomposition Policy does not authorize execution.

## Role in M49
M49 Decomposition Policy defines mapping rules between UX evidence and future non-executable planning artifacts.

Decomposition policy is a mapping policy.
Decomposition policy is not a generator.
Decomposition policy is not an execution policy.
Decomposition policy is not an implementation policy.
Decomposition policy is not an authorization policy.

## Relationship to M49 Architecture
UX-to-Task Decomposition Policy depends on docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md.
UX-to-Task Decomposition Policy must preserve the non-executable output model.
UX-to-Task Decomposition Policy must preserve human authorization requirements.

Policy mapping must not weaken M49 architecture boundaries.
Policy mapping must not convert readiness into execution authorization.
Policy mapping must not convert proposal artifacts into executable tasks.

## Relationship to UX-to-Task Input Contract
UX-to-Task Decomposition Policy depends on docs/UX-TO-TASK-INPUT-CONTRACT.md.
UX-to-task decomposition may be considered only when input readiness is not blocked or invalid.
Input readiness is not task generation.
Input readiness is not implementation approval.
Input readiness is not execution authorization.

UX_TO_TASK_INPUT_READY may inform decomposition mapping only under a separate authorized task.
UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS may inform decomposition mapping only if limitations are carried forward.
UX_TO_TASK_INPUT_BLOCKED must not produce decomposition outputs.
UX_TO_TASK_INPUT_INVALID must not produce decomposition outputs.

## Relationship to Task Draft Model
UX-to-Task Decomposition Policy depends on docs/TASK-DRAFT-MODEL.md.
Policy mappings may describe potential task drafts only.
Policy mappings must preserve draft_status semantics.
Policy mappings must preserve execution_authorized: false.

Policy mapping does not create task drafts automatically.
Policy mapping does not create active tasks.
Policy mapping does not create task queue entries.

## Relationship to Task Contract Proposal Template
UX-to-Task Decomposition Policy depends on templates/task-contract-proposal.md.
Policy mappings may describe future task contract proposal candidates only.
Policy mappings must preserve proposal_status: PROPOSED_ONLY.
Policy mappings must preserve human_authorization_required: true.

Policy mapping does not create task contract proposals automatically.
Policy mapping does not create authorized task contracts.
Policy mapping does not create executable task contracts.

## Policy Scope
The policy covers these UX source types:
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

The policy may map sources only to these non-executable planning categories:
- task draft candidate
- task contract proposal candidate
- carry-forward record
- clarification record
- traceability repair record

Policy scope ends before execution.
Policy scope ends before implementation.
Policy scope ends before active task state.
Policy scope ends before task queue state.

## Decomposition Eligibility
Before mapping may be reviewed, all of the following must exist:
- UX-to-task input package exists
- input_status is UX_TO_TASK_INPUT_READY or UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS
- UX Contract validation result is UX_CONTRACT_VALIDATION_OK
- readiness validation result is UX_PLANNING_READINESS_VALIDATION_OK
- readiness_decision is UX_PLANNING_READY or UX_PLANNING_READY_WITH_LIMITATIONS
- accepted limitations are carried forward
- open questions are carried forward
- downstream limits are carried forward
- non-authority boundary is carried forward
- human authorization for decomposition exists

Decomposition eligibility is not task generation.
Decomposition eligibility is not implementation approval.
Decomposition eligibility is not execution authorization.

## Source-to-Draft Mapping Rules
Mapping table:
- screen -> ui_structure task draft candidate
- state -> state_handling task draft candidate
- flow -> flow_definition task draft candidate
- user_action -> interaction_behavior task draft candidate
- approval_point -> approval_boundary task draft candidate
- risk_point -> risk_communication task draft candidate
- blocked_state -> blocked_behavior task draft candidate
- open_question -> clarification task draft candidate
- accepted_limitation -> limitation_carry_forward task draft candidate
- downstream_limit -> limitation_carry_forward task draft candidate
- traceability_gap -> traceability_repair task draft candidate

Source-to-draft mapping creates candidate mappings only.
Source-to-draft mapping does not create task drafts automatically.
Source-to-draft mapping does not authorize implementation.
Source-to-draft mapping does not authorize execution.

## Source-to-Proposal Mapping Rules
Mapping table:
- ui_structure task draft candidate -> task contract proposal candidate
- state_handling task draft candidate -> task contract proposal candidate
- flow_definition task draft candidate -> task contract proposal candidate
- interaction_behavior task draft candidate -> task contract proposal candidate
- approval_boundary task draft candidate -> task contract proposal candidate
- risk_communication task draft candidate -> task contract proposal candidate
- blocked_behavior task draft candidate -> task contract proposal candidate
- clarification task draft candidate -> task contract proposal candidate
- limitation_carry_forward task draft candidate -> task contract proposal candidate
- traceability_repair task draft candidate -> task contract proposal candidate

Source-to-proposal mapping creates candidate mappings only.
Source-to-proposal mapping does not create task contract proposals automatically.
Source-to-proposal mapping does not authorize implementation.
Source-to-proposal mapping does not authorize execution.

## Screen Mapping Rules
A screen may map to a ui_structure task draft candidate.
A screen mapping must preserve source_sections.
A screen mapping must preserve screen states.
A screen mapping must preserve downstream limits.

Screen mapping must not imply frontend implementation.
Screen mapping must not choose a frontend framework.
Screen mapping must not create component architecture.

## State Mapping Rules
A state may map to a state_handling task draft candidate.
A state mapping must preserve normal state coverage.
A state mapping must preserve loading state coverage.
A state mapping must preserve empty state coverage.
A state mapping must preserve error state coverage.
A state mapping must preserve blocked state coverage.

Happy-path-only state mapping is incomplete.
State mapping does not authorize implementation.
State mapping does not authorize execution.

## Flow Mapping Rules
A flow may map to a flow_definition task draft candidate.
A flow mapping must preserve entry state.
A flow mapping must preserve exit state.
A flow mapping must preserve blocked or error exit paths.
A flow mapping must preserve user-visible risk communication where applicable.

Flow without exit state must not produce ready draft candidates.
Flow without blocked or error path must be carried forward as a limitation or gap.
Flow mapping does not authorize workflow implementation.

## User Action Mapping Rules
A user action may map to an interaction_behavior task draft candidate.
A user action mapping must preserve action owner.
A user action mapping must preserve allowed action.
A user action mapping must preserve forbidden action.
A user action mapping must preserve expected feedback.

User action without owner must not produce ready draft candidates.
User action mapping does not authorize UI implementation.
User action mapping does not authorize backend behavior.

## Approval Point Mapping Rules
An approval point may map to an approval_boundary task draft candidate.
An approval point mapping must preserve human owner.
An approval point mapping must preserve approval scope.
An approval point mapping must preserve not-approved scope.
An approval point mapping must preserve non-authority boundary.

Approval point without human owner blocks ready draft candidates.
Approval point mapping does not create approval.
Approval point mapping does not authorize implementation.
Approval point mapping does not authorize execution.

## Risk Point Mapping Rules
A risk point may map to a risk_communication task draft candidate.
A risk point mapping must preserve risk description.
A risk point mapping must preserve user-visible risk communication.
A risk point mapping must preserve mitigation notes.
A risk point mapping must preserve downstream limits.

Risk point without user-visible risk communication must not produce ready draft candidates.
Risk mapping does not approve risk acceptance.
Risk mapping does not authorize implementation.

## Blocked State Mapping Rules
A blocked state may map to a blocked_behavior task draft candidate.
A blocked state mapping must preserve block reason.
A blocked state mapping must preserve user-visible explanation.
A blocked state mapping must preserve recovery path if available.
A blocked state mapping must preserve non-authority boundary.

Blocked state mapping does not authorize bypass.
Blocked state mapping does not weaken safety gates.
Blocked state mapping does not authorize execution.

## Open Question Mapping Rules
An open question may map to a clarification task draft candidate.
An open question mapping must preserve question text.
An open question mapping must preserve owner.
An open question mapping must preserve carry_forward_required.
An open question mapping must preserve downstream impact.

Open questions must not be dropped.
Open questions must not be silently resolved.
Open question mapping does not authorize implementation.

## Accepted Limitation Mapping Rules
An accepted limitation may map to a limitation_carry_forward task draft candidate.
An accepted limitation mapping must preserve limitation text.
An accepted limitation mapping must preserve rationale.
An accepted limitation mapping must preserve downstream_risk.
An accepted limitation mapping must preserve owner.
An accepted limitation mapping must preserve carry_forward_required: true.

Accepted limitations must not hide blocking gaps.
Accepted limitations must not be dropped.
Accepted limitation mapping does not approve implementation.
Accepted limitation mapping does not authorize execution.

## Downstream Limit Mapping Rules
A downstream limit may map to a limitation_carry_forward task draft candidate.
A downstream limit mapping must preserve no implementation authorization.
A downstream limit mapping must preserve no execution authorization.
A downstream limit mapping must preserve no commit, push, merge, deploy, or release authorization.

Downstream limits must not be weakened.
Downstream limits must not be dropped.
Downstream limit mapping does not authorize future execution.

## Traceability Gap Mapping Rules
A traceability gap may map to a traceability_repair task draft candidate.
A traceability gap mapping must preserve missing source reference.
A traceability gap mapping must preserve affected UX source.
A traceability gap mapping must preserve repair requirement.

Traceability gaps must not be hidden.
Traceability gap mapping does not create traceability automatically.
Traceability gap mapping does not authorize execution.

## Carry-Forward Rules
Every mapping must carry forward:
- source_product_spec
- source_ux_contract
- ux_contract_validation_result
- ux_planning_readiness_report
- readiness_validation_result
- readiness_decision
- source_sections
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- human_authorization_for_decomposition

Every mapping must preserve source_sections.
Every mapping must preserve accepted limitations.
Every mapping must preserve open questions.
Every mapping must preserve downstream limits.
Every mapping must preserve non-authority boundary.
Every mapping must preserve execution_authorized: false.

## Blocking Conditions
Mapping is blocked if:
- UX-to-task input package is missing
- input_status is UX_TO_TASK_INPUT_BLOCKED
- input_status is UX_TO_TASK_INPUT_INVALID
- UX Contract validation result is not UX_CONTRACT_VALIDATION_OK
- readiness validation result is not UX_PLANNING_READINESS_VALIDATION_OK
- readiness_decision is UX_PLANNING_NOT_READY
- readiness_decision is UX_PLANNING_BLOCKED
- blocking gaps exist
- source_sections are missing
- accepted limitations are not carried forward
- open questions are not carried forward
- downstream limits are missing
- non-authority boundary is missing
- human authorization for decomposition is missing
- authority claim exists

Blocked input must not produce decomposition mappings.
Invalid input must not produce decomposition mappings.
Blocking gaps block decomposition mapping.
Authority claims block decomposition mapping.

## Invalid Decomposition Conditions
A mapping is invalid if:
- mapping that creates executable task
- mapping that creates active task
- mapping that creates task queue entry
- mapping that creates task contract proposal automatically
- mapping that authorizes implementation
- mapping that authorizes execution
- mapping that drops source_sections
- mapping that drops accepted limitations
- mapping that drops open questions
- mapping that drops downstream limits
- mapping that drops non-authority boundary
- mapping that infers human authorization

Executable decomposition mapping is invalid.
Implementation-authorizing decomposition mapping is invalid.
Execution-authorizing decomposition mapping is invalid.
Mapping that drops carry-forward constraints is invalid.

## Non-Executable Boundary
UX-to-task decomposition mappings are non-executable by definition.
UX-to-task decomposition mappings must not be copied into tasks/active-task.md.
UX-to-task decomposition mappings must not be copied into tasks/queue/.
UX-to-task decomposition mappings must not be used as active tasks.
UX-to-task decomposition mappings must not be used as executable task contracts.

No executable task may be created from a decomposition mapping alone.
No active task may be created from a decomposition mapping alone.
No task queue entry may be created from a decomposition mapping alone.

## Human Authorization Boundary
Human authorization for decomposition permits decomposition review only.
Human authorization for decomposition does not authorize implementation.
Human authorization for decomposition does not authorize execution.
Human authorization for decomposition does not convert mappings into task drafts automatically.
Human authorization for decomposition does not convert mappings into task contract proposals automatically.

Human authorization cannot be inferred from readiness.
Human authorization cannot be inferred from validator PASS.
Human authorization cannot be inferred from visual approval.
Human authorization cannot be inferred from decomposition mapping.

## Future Validator Notes
Future M49 validator may check decomposition mapping source types.
Future M49 validator may check decomposition mapping target types.
Future M49 validator may check carry-forward requirements.
Future M49 validator may check source_sections preservation.
Future M49 validator may check execution_authorized: false.
Future M49 validator may check forbidden authority claims.
Future M49 validator may check blocked and invalid mapping conditions.

Future M49 validator must not create decomposition mappings.
Future M49 validator must not create task drafts.
Future M49 validator must not create task contract proposals.
Future M49 validator must not authorize implementation.
Future M49 validator must not authorize execution.

## What This Policy Does Not Do
This policy does not:
- create decomposition mappings automatically
- create task drafts
- create task contract proposals
- create executable tasks
- create task contracts
- write to tasks/active-task.md
- write to tasks/queue/
- generate task graph
- perform implementation planning
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

UX-to-Task Decomposition Policy does not perform UX-to-task decomposition automatically.

## Non-Authority Boundary
UX-to-Task Decomposition Policy is not task generation.
UX-to-Task Decomposition Policy is not implementation approval.
UX-to-Task Decomposition Policy does not create decomposition mappings automatically.
UX-to-Task Decomposition Policy does not create task drafts.
UX-to-Task Decomposition Policy does not create task contract proposals.
UX-to-Task Decomposition Policy does not create executable tasks.
UX-to-Task Decomposition Policy does not create authorized task contracts.
UX-to-Task Decomposition Policy does not authorize task generation.
UX-to-Task Decomposition Policy does not authorize implementation.
UX-to-Task Decomposition Policy does not authorize execution planning.
UX-to-Task Decomposition Policy does not authorize commit, push, merge, deploy, or release.
UX-to-Task Decomposition Policy may define mapping rules only.
Future task drafts require separate authorized tasks.
Future task contract proposals require separate authorized tasks.
Future executable task contracts require separate human authorization.

## Summary
This policy defines mapping rules from validated UX evidence to non-executable planning candidates.
It preserves carry-forward constraints and boundary protections.
It does not generate tasks and does not authorize implementation or execution.
Any move toward executable task contracts remains under separate human authorization.
