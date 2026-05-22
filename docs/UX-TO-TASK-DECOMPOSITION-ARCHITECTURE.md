---
type: ux-to-task-decomposition-architecture
milestone: M49
status: canonical
authority: architecture
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX-to-Task Decomposition Architecture

## Purpose
UX-to-Task Decomposition Architecture defines how readiness-approved UX inputs may be transformed into non-executable task drafts and task contract proposals.
UX-to-Task Decomposition Architecture does not create executable tasks.
UX-to-Task Decomposition Architecture does not create authorized task contracts.
UX-to-Task Decomposition Architecture does not authorize implementation.
UX-to-Task Decomposition Architecture does not authorize execution.

## Role in M49
M49 defines the proposal layer between UX Planning Readiness and future authorized task contracts.
M49 may define how task drafts are derived.
M49 may define how task contract proposals are structured.
M49 must preserve M48 non-authority boundaries.
M49 must preserve human authorization requirements.

M49 is a decomposition architecture layer.
M49 is not an execution layer.
M49 is not an implementation layer.
M49 is not an authorization layer.

## Relationship to M47
M47 created the UX Contract layer.
M47 defines UX structure, screens, states, flows, UX elements, traceability, preview, and visual approval-like supporting evidence.
M49 may use validated M47 UX Contract artifacts as source inputs only.

M47 UX Contract is a source input, not execution permission.
M47 Static HTML Preview is supporting visual evidence only.
M47 UX Visual Approval Snapshot is supporting visual evidence only.

## Relationship to M48
M48 created the UX Planning Readiness Layer.
M48 determines whether a validated UX Contract may inform future planning.
M48 does not generate tasks.
M48 does not create task contracts.
M48 does not authorize implementation.
M48 does not authorize execution.

M48 completion does not authorize UX-to-task decomposition.
M48 readiness may inform M49 only under a separate authorized task contract.
M49 must carry forward M48 downstream limits.

## Architecture Chain
Validated UX Contract
↓
UX Planning Readiness Report
↓
UX-to-Task Boundary Policy
↓
UX-to-Task Decomposition Architecture
↓
Task Drafts
↓
Task Contract Proposals
↓
Separate human authorization
↓
Executable task contracts

The architecture chain is sequential.
No lower layer may skip human authorization.
No proposal may become executable without separate authorization.

## Decomposition Scope
UX-to-task decomposition is the process of deriving non-executable task drafts and task contract proposals from validated UX structure and readiness evidence.

Decomposition may consider:
- screens
- states
- flows
- user actions
- risk points
- approval points
- blocked states
- open questions
- accepted limitations
- downstream limits
- traceability

## Inputs
Required M49 inputs:
- source_product_spec
- source_ux_contract
- ux_contract_validation_result
- ux_planning_readiness_report
- readiness_validation_result
- readiness_decision
- ux_to_task_boundary_policy
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- human_authorization_for_decomposition

Missing readiness report blocks UX-to-task decomposition.
Missing readiness validation result blocks UX-to-task decomposition.
Missing downstream limits blocks UX-to-task decomposition.
Missing human authorization for decomposition blocks UX-to-task decomposition.

## Outputs
Allowed outputs:
- task drafts
- task contract proposals
- decomposition traceability records
- carry-forward records
- open question records
- limitation carry-forward records

M49 outputs are non-executable.
M49 outputs are proposal artifacts.
M49 outputs require separate human authorization before execution.

## Non-Executable Output Model
Every M49 output must preserve execution_authorized: false.
Every M49 output must preserve human_authorization_required: true.
Every M49 output must preserve proposal_status: PROPOSED_ONLY or draft_status: DRAFT_ONLY.

execution_authorized: false is required for M49 outputs.
human_authorization_required: true is required for task contract proposals.

## Task Draft Boundary
Task draft is a non-executable planning artifact derived from UX structure and readiness evidence.

Task draft is not a task contract.
Task draft is not authorization.
Task draft must not be executed.
Task draft must not be placed into active execution.

## Task Contract Proposal Boundary
Task contract proposal is a structured candidate for a future executable task contract, pending separate human authorization.

Task Contract Proposal is not executable.
Task Contract Proposal does not authorize execution.
Task Contract Proposal does not authorize implementation.
Task Contract Proposal requires separate human authorization before becoming an executable task contract.

## Human Authorization Boundary
Human authorization is required before UX-to-task decomposition begins.
Human authorization is required before any task proposal becomes executable.
Human authorization must be attached to a specific downstream action.
Generic readiness approval is not sufficient for task execution.

Human authorization cannot be inferred from readiness.
Human authorization cannot be inferred from visual approval.
Human authorization cannot be inferred from validator PASS.

## Carry-Forward Requirements
M49 outputs must carry forward:
- source_product_spec
- source_ux_contract
- ux_contract_validation_result
- ux_planning_readiness_report
- readiness_validation_result
- readiness_decision
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- source_sections

Accepted limitations must be carried forward into task drafts.
Open questions must be carried forward into task drafts.
Downstream limits must be carried forward into task drafts.
Non-authority boundary must be carried forward into task drafts.

## Blocking Conditions
M49 decomposition is blocked if:
- source UX Contract is missing
- UX Contract validation result is missing
- UX Contract validation result is not UX_CONTRACT_VALIDATION_OK
- readiness report is missing
- readiness validation result is missing
- readiness validation result is not UX_PLANNING_READINESS_VALIDATION_OK
- readiness_decision is UX_PLANNING_NOT_READY
- readiness_decision is UX_PLANNING_BLOCKED
- blocking_gaps exist
- accepted limitations are not carried forward
- open questions are not carried forward
- downstream limits are missing
- human authorization for decomposition is missing
- authority claim exists

Blocking gaps block UX-to-task decomposition.
Readiness blocked status blocks UX-to-task decomposition.
Readiness not-ready status blocks UX-to-task decomposition.
Authority claims block UX-to-task decomposition.

## Forbidden Authority Claims
The architecture forbids claims that convert M49 proposal artifacts into execution permission.
Any claim that decomposition architecture grants implementation permission is invalid.
Any claim that decomposition architecture grants execution permission is invalid.
Any claim that task drafts become executable directly is invalid.
Any claim that task contract proposals become executable without separate authorization is invalid.

## What M49 May Do
M49 may:
- define decomposition architecture
- define required decomposition inputs
- define task draft model in later task
- define task contract proposal template in later task
- define decomposition policy in later task
- define proposal validator in later task
- create non-executable example proposals in later task
- collect evidence in later task
- complete M49 in later task

## What M49 Must Not Do
M49 must not:
- create executable tasks
- modify active task state
- write to tasks/active-task.md
- write to tasks/queue/
- authorize task execution
- authorize implementation
- choose frontend framework
- define production component architecture
- write frontend code
- write backend code
- commit
- push
- merge
- deploy
- release

M49 must not create executable task contracts.

## Future M49 Artifacts
Planned M49 artifacts:
- docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md
- docs/UX-TO-TASK-INPUT-CONTRACT.md
- docs/TASK-DRAFT-MODEL.md
- templates/task-contract-proposal.md
- docs/UX-TO-TASK-DECOMPOSITION-POLICY.md
- scripts/validate-ux-to-task-proposal.py
- tests/fixtures/ux-to-task-proposal/
- examples/ux-to-task-proposals-agent-action-review.md
- reports/m49-ux-to-task-decomposition-evidence-report.md
- reports/m49-completion-review.md

## Future Validator Notes
Future M49 validator may check required inputs.
Future M49 validator may check task draft required fields.
Future M49 validator may check task contract proposal required fields.
Future M49 validator may check execution_authorized: false.
Future M49 validator may check human_authorization_required: true.
Future M49 validator may check carry-forward requirements.
Future M49 validator may check forbidden authority claims.

Future M49 validator must not generate task contracts.
Future M49 validator must not authorize implementation.
Future M49 validator must not authorize execution.

## Non-Authority Boundary
UX-to-Task Decomposition Architecture is not task generation.
UX-to-Task Decomposition Architecture is not implementation approval.
UX-to-Task Decomposition Architecture does not create executable tasks.
UX-to-Task Decomposition Architecture does not create authorized task contracts.
UX-to-Task Decomposition Architecture does not authorize implementation.
UX-to-Task Decomposition Architecture does not authorize execution planning.
UX-to-Task Decomposition Architecture does not authorize commit, push, merge, deploy, or release.
UX-to-Task Decomposition Architecture may define proposal architecture only.
Future executable task contracts require separate human authorization.

## Summary
M49 formalizes the transition from readiness outputs to non-executable proposal artifacts. It preserves M48 boundaries, enforces human authorization gates, and prevents direct execution authority from decomposition artifacts.

Additional boundary reminders for downstream work:
- M49 proposal artifacts are planning artifacts only.
- Proposal artifacts require explicit transition rules before authorization.
- Authorization remains a separate governance action.
- Queue placement alone is not authorization.
- Validation success alone is not authorization.
- Readiness evidence alone is not authorization.
- Visual direction evidence alone is not authorization.
- Preview artifacts alone are not authorization.
- Decomposition records are traceability assets, not execution signals.
- Any downstream execution still requires a separately authorized task contract.

Additional carry-forward reminders:
- Preserve source_sections when deriving draft work units.
- Preserve limitation ownership on every draft.
- Preserve open question ownership on every draft.
- Preserve downstream limits verbatim where possible.
- Preserve non-authority boundary statements in downstream proposal outputs.

Additional blocking reminders:
- Do not proceed when readiness_decision is blocked or not-ready.
- Do not proceed when required upstream references are missing.
- Do not proceed when authorization metadata is missing.
- Do not proceed when blocking gaps are present.
- Do not proceed when carry-forward fields are incomplete.
