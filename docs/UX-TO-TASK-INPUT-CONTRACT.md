---
type: ux-to-task-input-contract
milestone: M49
status: canonical
authority: input-contract
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX-to-Task Input Contract

## Purpose
UX-to-Task Input Contract defines the required inputs that must exist before future UX-to-task decomposition may be reviewed.
UX-to-Task Input Contract does not create task drafts.
UX-to-Task Input Contract does not create task contract proposals.
UX-to-Task Input Contract does not create executable tasks.
UX-to-Task Input Contract does not authorize implementation.
UX-to-Task Input Contract does not authorize execution.

## Role in M49
M49 Input Contract defines the input gate for the UX-to-Task Decomposition Layer.
Input readiness is not task generation.
Input readiness is not implementation approval.
Input readiness is not execution authorization.
Input readiness only determines whether decomposition input may be reviewed.

## Relationship to M49 Architecture
M49 Architecture defines the decomposition layer.
M49 Input Contract defines the required inputs for that layer.
M49 Input Contract must preserve the non-executable output model from the architecture.
UX-to-Task Input Contract depends on docs/UX-TO-TASK-DECOMPOSITION-ARCHITECTURE.md.
UX-to-Task Input Contract must not weaken M49 architecture boundaries.

## Relationship to M48 Readiness
M48 readiness may inform M49 only under a separate authorized task contract.
M48 completion does not authorize UX-to-task decomposition.
M48 readiness result is an input, not authorization.
M48 evidence is supporting evidence only.
M48 readiness does not authorize task generation.
M48 readiness does not authorize implementation.
M48 readiness does not authorize execution.

## Input Contract Model
M47 UX Contract
+
M48 Readiness Report
+
M48 Readiness Validation Result
+
M48 UX-to-Task Boundary Policy
+
Human Authorization for Decomposition
↓
M49 Input Contract Review
↓
UX_TO_TASK_INPUT_READY or UX_TO_TASK_INPUT_BLOCKED

UX_TO_TASK_INPUT_READY does not authorize task generation.
UX_TO_TASK_INPUT_READY does not authorize implementation.
UX_TO_TASK_INPUT_READY does not authorize execution.

## Required Input Package
Canonical input package format:

```yaml
ux_to_task_input:
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
  carry_forward:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
  traceability:
    source_sections:
  authorization:
    human_authorization_for_decomposition:
    authorization_reference:
    authorized_by:
    authorized_at:
  input_status:
    status:
    reviewed_by:
    reviewed_at:
```

source_sections must be plural.
source_sections must be a list.
source_section must not be used.

## Required Source References
Required source references:
- source_product_spec
- source_ux_contract
- source_readiness_report
- source_boundary_policy

Missing source Product Spec blocks UX-to-task input readiness.
Missing source UX Contract blocks UX-to-task input readiness.
Missing readiness report blocks UX-to-task input readiness.
Missing boundary policy blocks UX-to-task input readiness.

## Required Validation Inputs
Required validation inputs:
- ux_contract_validation_result
- readiness_validation_result

Allowed UX Contract validation result:
- UX_CONTRACT_VALIDATION_OK

Allowed readiness validation result:
- UX_PLANNING_READINESS_VALIDATION_OK

UX_CONTRACT_VALIDATION_OK is required for UX-to-task input readiness.
UX_PLANNING_READINESS_VALIDATION_OK is required for UX-to-task input readiness.
Skipped validation is not passed validation.
Missing validation is not passed validation.

## Required Readiness Inputs
Required readiness input:
- readiness_decision

Allowed readiness decisions for input readiness:
- UX_PLANNING_READY
- UX_PLANNING_READY_WITH_LIMITATIONS

Blocking readiness decisions:
- UX_PLANNING_NOT_READY
- UX_PLANNING_BLOCKED

UX_PLANNING_READY may inform future decomposition review.
UX_PLANNING_READY_WITH_LIMITATIONS may inform future decomposition review only if limitations are carried forward.
UX_PLANNING_NOT_READY blocks UX-to-task input readiness.
UX_PLANNING_BLOCKED blocks UX-to-task input readiness.

## Required Boundary Inputs
Required boundary inputs:
- ux_to_task_boundary_policy
- non_authority_boundary
- downstream_limits

Missing UX-to-Task Boundary Policy blocks UX-to-task input readiness.
Missing non-authority boundary blocks UX-to-task input readiness.
Missing downstream limits blocks UX-to-task input readiness.

## Required Carry-Forward Inputs
Required carry-forward inputs:
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- source_sections

Accepted limitations must be carried forward.
Open questions must be carried forward.
Downstream limits must be carried forward.
Non-authority boundary must be carried forward.
Traceability source_sections must be carried forward.

Accepted limitations must not be dropped during input review.
Open questions must not be dropped during input review.
Downstream limits must not be dropped during input review.

## Required Human Authorization Input
Required authorization inputs:
- human_authorization_for_decomposition
- authorization_reference
- authorized_by
- authorized_at

Human authorization for decomposition is required before UX-to-task input readiness can pass.
Human authorization must be attached to a specific decomposition review action.
Human authorization cannot be inferred from M48 completion.
Human authorization cannot be inferred from readiness validator PASS.
Human authorization cannot be inferred from visual approval.

Missing human authorization for decomposition blocks UX-to-task input readiness.
Generic approval is not sufficient for decomposition input readiness.

## Allowed Input Statuses
Allowed statuses:
- UX_TO_TASK_INPUT_READY
- UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS
- UX_TO_TASK_INPUT_BLOCKED
- UX_TO_TASK_INPUT_INVALID

Status semantics:
- UX_TO_TASK_INPUT_READY means all required inputs exist and no blocking condition is present.
- UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS means required inputs exist and limitations must be carried forward.
- UX_TO_TASK_INPUT_BLOCKED means required inputs are missing or blocked by readiness state.
- UX_TO_TASK_INPUT_INVALID means the input package violates required structure or authority boundaries.

UX_TO_TASK_INPUT_READY may inform future decomposition review.
UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS may inform future decomposition review only if limitations are carried forward.
UX_TO_TASK_INPUT_READY does not authorize task generation.
UX_TO_TASK_INPUT_READY_WITH_LIMITATIONS does not authorize task generation.
UX_TO_TASK_INPUT_BLOCKED does not authorize task generation.
UX_TO_TASK_INPUT_INVALID does not authorize task generation.

## Blocking Conditions
Input readiness is blocked if:
- source_product_spec is missing
- source_ux_contract is missing
- ux_contract_validation_result is missing
- ux_contract_validation_result is not UX_CONTRACT_VALIDATION_OK
- source_readiness_report is missing
- readiness_validation_result is missing
- readiness_validation_result is not UX_PLANNING_READINESS_VALIDATION_OK
- readiness_decision is UX_PLANNING_NOT_READY
- readiness_decision is UX_PLANNING_BLOCKED
- accepted_limitations are not carried forward
- open_questions are not carried forward
- downstream_limits are missing
- non_authority_boundary is missing
- source_sections are missing
- human_authorization_for_decomposition is missing
- authorization_reference is missing
- authority claim exists

Blocking conditions prevent UX_TO_TASK_INPUT_READY.
Input readiness must fail closed.
UNKNOWN input state is not ready.
NOT_RUN validation is not ready.

## Missing Input Rules
Missing required input must produce UX_TO_TASK_INPUT_BLOCKED.
Missing source reference must produce UX_TO_TASK_INPUT_BLOCKED.
Missing validation result must produce UX_TO_TASK_INPUT_BLOCKED.
Missing human authorization must produce UX_TO_TASK_INPUT_BLOCKED.

## Invalid Input Rules
Invalid input structure must produce UX_TO_TASK_INPUT_INVALID.
Invalid readiness decision must produce UX_TO_TASK_INPUT_INVALID.
Invalid validation token must produce UX_TO_TASK_INPUT_INVALID.
Invalid authority claim must produce UX_TO_TASK_INPUT_INVALID.

## Non-Executable Input Boundary
UX-to-task input readiness is not output generation.
UX-to-task input readiness is not task draft creation.
UX-to-task input readiness is not task contract proposal creation.
UX-to-task input readiness is not execution permission.

No executable task may be created from input readiness alone.
No active task may be created from input readiness alone.
No task queue entry may be created from input readiness alone.

## Traceability Requirements
Every input package must preserve:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- ux_contract_version
- ux_contract_path
- readiness_report_path
- boundary_policy_path
- source_sections

Traceability is required for UX-to-task input readiness.
Traceability is not approval.
Traceability is not execution authorization.

## Future Validator Notes
Future M49 input validator may check input package required fields.
Future M49 input validator may check validation result tokens.
Future M49 input validator may check readiness decision values.
Future M49 input validator may check carry-forward fields.
Future M49 input validator may check human authorization fields.
Future M49 input validator may check forbidden authority claims.

Future M49 input validator must not generate task drafts.
Future M49 input validator must not generate task contract proposals.
Future M49 input validator must not authorize implementation.
Future M49 input validator must not authorize execution.

## What This Contract Does Not Do
This contract does not:
- create task drafts
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

UX-to-Task Input Contract does not perform UX-to-task decomposition.

## Non-Authority Boundary
UX-to-Task Input Contract is not task generation.
UX-to-Task Input Contract is not implementation approval.
UX-to-Task Input Contract does not create task drafts.
UX-to-Task Input Contract does not create task contract proposals.
UX-to-Task Input Contract does not create executable tasks.
UX-to-Task Input Contract does not authorize task generation.
UX-to-Task Input Contract does not authorize implementation.
UX-to-Task Input Contract does not authorize execution planning.
UX-to-Task Input Contract does not authorize commit, push, merge, deploy, or release.
UX-to-Task Input Contract may define decomposition input requirements only.
Future task drafts and task contract proposals require separate authorized tasks.

## Summary
M49 input readiness is a strict precondition gate. It ensures required sources, validations, carry-forward boundaries, and human authorization metadata are present before decomposition review may begin, while preserving non-executable and non-authority boundaries.
