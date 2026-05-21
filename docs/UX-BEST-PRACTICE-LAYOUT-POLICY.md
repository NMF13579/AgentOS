---
type: ux-best-practice-layout-policy
status: canonical
authority: ux-structure
version: 1.0.0
created: 2026-05-21
owner: human
---

# M47 UX Best Practice Layout Policy

## Purpose
Определить канонические рекомендации по расположению UX-элементов в UX Contract для M47.

## Role in M47
Политика задаёт рекомендуемый порядок отображения информации, чтобы пользователь видел риск, границы, решения и безопасные следующие шаги.

## Relationship to Product Spec
Product Spec остаётся источником продуктовых требований. Эта политика не заменяет и не изменяет Product Spec.

## Relationship to UX Contract
Политика помогает авторам UX Contract выбирать понятный и безопасный порядок блоков, но не заменяет UX Contract.

## Relationship to UX Element Vocabulary
`required_ux_elements` и `optional_ux_elements` должны использовать элементы из `docs/UX-ELEMENT-VOCABULARY.md`.

## Relationship to UX Screen & State Model
Рекомендации учитывают состояния и должны явно поддерживать blocked/error/approval/execution_not_authorized контексты.

## Relationship to UX Flow Policy
Рекомендации по layout поддерживают UX Flow и помогают визуально показывать решения, риск и блокировки в нужной последовательности.

## Best-Practice Layout Definition
- Best-practice layout is a recommended ordering of UX elements.
- Best-practice layout helps users understand risk, scope, decisions, and next safe actions.
- Best-practice layout may guide UX Contract authors.
- Best-practice layout may guide optional Static HTML Preview.
- Best-practice layout is not source of truth for Product Spec requirements.
- Best-practice layout is not approval.
- Best-practice layout does not override Product Spec.
- Best-practice layout does not override UX Contract.
- Best-practice layout does not authorize task generation.
- Best-practice layout does not authorize execution planning.
- Best-practice layout does not authorize implementation.
- Best-practice layout does not implement UI.

Best-practice layout is recommendation.
Best-practice layout is not approval.
Best-practice layout does not override Product Spec or UX Contract.

## Layout Recommendation Format
```yaml
layout_id:
layout_title:
layout_purpose:
applies_to_screens:
applies_to_states:
recommended_order:
required_ux_elements:
optional_ux_elements:
risk_visibility:
approval_visibility:
blocked_state_handling:
non_authority_notice_placement:
not_authorized:
traceability:
```

## Required Layout Fields
- layout_id must be stable and unique inside the policy.
- layout_title must be human-readable.
- layout_purpose must explain why the layout exists.
- applies_to_screens must describe which screen types may use the layout.
- applies_to_states must describe which UX states the layout supports.
- recommended_order must describe the preferred order of visible blocks.
- required_ux_elements must use elements from docs/UX-ELEMENT-VOCABULARY.md.
- optional_ux_elements must use elements from docs/UX-ELEMENT-VOCABULARY.md.
- risk_visibility must describe where risk is shown.
- approval_visibility must describe where approval points are shown.
- blocked_state_handling must describe how blocked states remain visible.
- non_authority_notice_placement must describe where the boundary is shown.
- not_authorized must explicitly list what the layout does not authorize.
- traceability must preserve source references.

## Recommended Layout Patterns
Ниже определены 5 канонических шаблонов-рекомендаций.

## Approval Workflow Layout
Approval workflow layout may show an approval point.
Approval workflow layout must show risk before approval card.
Approval workflow layout must show affected scope before approval card.
Approval workflow layout must show non-authority boundary.
Approval workflow layout must not create approval.
Approval workflow layout must not simulate human approval.
Approval workflow layout must not authorize execution.

## Risk Review Layout
Risk review layout must show risk reason.
Risk review layout must show affected scope where known.
Unknown risk must be represented as blocked or needs clarification.
Risk review layout must not downgrade risk.
Risk review layout must not hide high-risk conditions.
Risk review layout must not replace approval.

## Blocked State Layout
Blocked state layout must make the blocker visible.
Blocked state layout must explain why progress is blocked.
Blocked state layout must show required resolution.
Blocked state layout must not provide bypass instructions.
Blocked state layout must not present blocked state as optional warning.
Blocked state layout must not authorize execution.

## Error Recovery Layout
Error recovery layout must distinguish error from blocked state.
Error recovery layout must not convert error into success.
Error recovery layout must not hide validation failure.
Error recovery layout must not imply execution authorization.

## Task Review Layout
Task review layout may summarize a candidate task.
Task review layout must not create task contracts.
Task review layout must not authorize task generation.
Task review layout must not authorize task lifecycle mutation.
Task review layout must not authorize execution.

## Layout Pattern: approval_workflow
layout_id: approval_workflow
layout_title: Approval Workflow Layout
layout_purpose: Показать путь проверки и концептуального одобрения без авторизации исполнения.
applies_to_screens:
  - agent_action_review
applies_to_states:
  - normal
  - approval_required
  - execution_not_authorized
recommended_order:
  - 1. Action summary
  - 2. Risk banner
  - 3. Affected scope panel
  - 4. Human approval card
  - 5. Decline reason preview
  - 6. Audit trail note
  - 7. Non-authority boundary
required_ux_elements:
  - summary_card
  - risk_banner
  - review_panel
  - approval_card
  - audit_note
  - non_authority_notice
optional_ux_elements:
  - status_badge
risk_visibility: Risk banner must be visible before approval_card.
approval_visibility: Approval card must be explicit and human-owned.
blocked_state_handling: If approval owner/scope/risk unknown, show blocked context visibly.
non_authority_notice_placement: Place near approval card and before any execution-sensitive wording.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
traceability:
  - spec_id
  - spec_version
  - product_spec_path
  - ux_contract_id
  - source_sections

## Layout Pattern: risk_review
layout_id: risk_review
layout_title: Risk Review Layout
layout_purpose: Показать риск и охват до любых концептуальных решений.
applies_to_screens:
  - risk_review
  - agent_action_review
applies_to_states:
  - normal
  - needs_clarification
  - blocked
recommended_order:
  - 1. Summary card
  - 2. Status badge
  - 3. Risk banner
  - 4. Review panel
  - 5. Checklist
  - 6. Non-authority boundary
required_ux_elements:
  - summary_card
  - status_badge
  - risk_banner
  - review_panel
  - checklist
  - non_authority_notice
optional_ux_elements:
  - audit_note
risk_visibility: Show risk reason and affected scope where known.
approval_visibility: Approval points are secondary and must not replace risk context.
blocked_state_handling: Unknown risk must appear as blocked or needs_clarification.
non_authority_notice_placement: Place after risk/review content and before actionable-looking phrases.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
traceability:
  - spec_id
  - spec_version
  - product_spec_path
  - ux_contract_id
  - source_sections

## Layout Pattern: blocked_state
layout_id: blocked_state
layout_title: Blocked State Layout
layout_purpose: Явно показать невозможность продолжения и что нужно для разблокировки.
applies_to_screens:
  - any_execution_sensitive_screen
applies_to_states:
  - blocked
  - execution_not_authorized
recommended_order:
  - 1. Blocked state
  - 2. Blocking reason
  - 3. Required resolution
  - 4. Owner or responsible party
  - 5. Next safe action
  - 6. Non-authority boundary
required_ux_elements:
  - blocked_state
  - non_authority_notice
optional_ux_elements:
  - review_panel
  - audit_note
risk_visibility: Show explicit blocker-to-risk relation.
approval_visibility: If approval owner missing, keep blocker visible near notice.
blocked_state_handling: Blocked content must stay visible until resolution is defined.
non_authority_notice_placement: Place adjacent to blocked reason and next safe action.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
traceability:
  - spec_id
  - spec_version
  - product_spec_path
  - ux_contract_id
  - source_sections

## Layout Pattern: error_recovery
layout_id: error_recovery
layout_title: Error Recovery Layout
layout_purpose: Прозрачно показать ошибку, причину и безопасное восстановление.
applies_to_screens:
  - any_screen_with_error
applies_to_states:
  - error
  - blocked
recommended_order:
  - 1. Error state
  - 2. Error summary
  - 3. Error reason
  - 4. Recovery hint
  - 5. Source reference
  - 6. Non-authority boundary
required_ux_elements:
  - error_state
  - audit_note
  - non_authority_notice
optional_ux_elements:
  - review_panel
risk_visibility: Keep failure severity explicit; do not reframe as success.
approval_visibility: Approval-related wording must not appear as remediation shortcut.
blocked_state_handling: Distinguish error root cause from blocked preconditions.
non_authority_notice_placement: Place immediately after recovery hint.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
traceability:
  - spec_id
  - spec_version
  - product_spec_path
  - ux_contract_id
  - source_sections

## Layout Pattern: task_review
layout_id: task_review
layout_title: Task Review Layout
layout_purpose: Структурировать обзор кандидатной задачи без мутации жизненного цикла задачи.
applies_to_screens:
  - task_review
  - agent_action_review
applies_to_states:
  - normal
  - blocked
  - needs_clarification
recommended_order:
  - 1. Task card
  - 2. Scope summary
  - 3. Risk banner
  - 4. Checklist
  - 5. Review panel
  - 6. Audit note
  - 7. Non-authority boundary
required_ux_elements:
  - task_card
  - risk_banner
  - checklist
  - review_panel
  - audit_note
  - non_authority_notice
optional_ux_elements:
  - status_badge
risk_visibility: Show risk before any conceptual approval wording.
approval_visibility: Approval point, if shown, remains conceptual only.
blocked_state_handling: Missing owner/scope/risk must render blocked context.
non_authority_notice_placement: Place near task decision area and before next-step text.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
traceability:
  - spec_id
  - spec_version
  - product_spec_path
  - ux_contract_id
  - source_sections

## Non-Authority Notice Placement
- Non-authority notice must be visible in layouts that show approval, risk, blocked, or task review content.
- Non-authority notice should appear near decision or approval points.
- Non-authority notice should appear before any user might confuse UX structure with execution permission.
- Non-authority notice must not be hidden in footer-only placement when the layout contains approval or execution-sensitive language.
- Non-authority notice must preserve the M47 boundary.

## Traceability Requirements
Каждая layout-рекомендация, используемая в UX Contract, должна сохранять связь с источником:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- source_sections

- Traceability is not approval.
- Traceability is not execution authorization.
- If Product Spec changes, layout recommendations may become stale.
- Stale layout recommendations must not be treated as current UX authority.

## HTML Preview Boundary
- Best-practice layouts may be rendered in optional Static HTML Preview.
- HTML Preview rendering is visual explanation only.
- HTML Preview is not source of truth.
- HTML Preview is not implementation.
- HTML Preview may show recommended layout order.
- HTML Preview must not contain enabled controls.
- HTML Preview must not contain JavaScript.
- HTML Preview must not contain forms.
- HTML Preview must display non-authority boundaries.
- HTML Preview must not convert recommended layout into implementation.

HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.

## Forbidden Uses
Best-practice layouts must not be used to:
- override Product Spec;
- override UX Contract;
- create approval;
- simulate human approval;
- authorize task generation;
- authorize execution planning;
- authorize implementation;
- authorize commit, push, merge, deploy, or release;
- define production UI;
- define frontend components;
- define CSS or design tokens;
- replace validation;
- hide blocked states;
- hide error states;
- downgrade risk.

## Non-Authority Boundary
Best-practice layout is recommendation.
Best-practice layout is not approval.
Best-practice layout does not override Product Spec or UX Contract.
Best-practice layout does not authorize task generation.
Best-practice layout does not authorize execution planning.
Best-practice layout does not authorize implementation.
Best-practice layout does not authorize commit, push, merge, deploy, or release.
Best-practice layout may guide UX structure.
Best-practice layout must not implement UI.
HTML Preview is optional visual explanation only.

## Future Validator Notes
- Future validate-ux-contract.py may check that layouts reference allowed UX elements.
- Future validate-ux-contract.py may check that approval layouts include risk_banner.
- Future validate-ux-contract.py may check that approval layouts include approval_card.
- Future validate-ux-contract.py may check that approval layouts include non_authority_notice.
- Future validate-ux-contract.py may check that blocked layouts include visible blocked reason.
- Future validate-ux-contract.py may check that error layouts do not hide validation failures.
- Future validate-ux-contract.py may check that layouts do not claim implementation authority.
- M47.6 does not implement the validator.

## Summary
Документ фиксирует канонические рекомендации по layout для M47, сохраняя границы неавторизации и запрет на реализацию UI.
