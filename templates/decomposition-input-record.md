---
contract_version:
record_id:
source_spec:
source_spec_approved:
source_ux:
source_ux_approved:
ui_contract:
ui_contract_required:
ui_contract_present:
screen_map:
user_flows:
state_error_matrix:
ux_acceptance_criteria:
known_constraints:
known_risks:
readiness_result:
human_review_required:
created_at:
---

## Summary
Краткая сводка состояния входов и readiness_result.

## Source Spec
Путь к approved Spec и подтверждение approve.

## Source UX
Путь к approved UX brief и подтверждение approve.

## UI Contract
Путь к UI Contract dependency, required/present, и влияние на декомпозицию.

## Screen Map
Список экранов и покрытие.

## User Flows
Список пользовательских сценариев.

## State and Error Matrix
Состояния/ошибки и покрытие.

## UX Acceptance Criteria
Список UX критериев приёмки.

## Known Constraints
Ограничения, влияющие на разбиение задач.

## Known Risks
Риски, влияющие на готовность входов.

## Readiness Decision
Один из токенов:
- DECOMPOSITION_INPUT_READY
- DECOMPOSITION_INPUT_MISSING_SPEC_APPROVAL
- DECOMPOSITION_INPUT_MISSING_UX_APPROVAL
- DECOMPOSITION_INPUT_MISSING_UI_CONTRACT
- DECOMPOSITION_INPUT_INCOMPLETE
- DECOMPOSITION_INPUT_NEEDS_REVIEW

## Human Review Boundary
This decomposition input record is not approval.
This decomposition input record does not authorize execution.
This decomposition input record does not replace HumanApprovalGate.

Также:
- decomposition input readiness is not task queue approval
- decomposition input readiness is not commit approval
- decomposition input readiness is not push approval

## Known Gaps
Зафиксируйте отсутствующие upstream artifacts без выдумывания содержимого.
