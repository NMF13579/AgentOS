## Purpose
Определяет канонический формат Task Contract v2 для M44.

## Position in M44
Task Contract v2 используется после readiness входов и до постановки в очередь.

## Relationship to Decomposition Input Contract
Task Contract v2 опирается на `docs/DECOMPOSITION-INPUT-CONTRACT.md` и его readiness_result.

## Relationship to Task Queue
Queue placement does not authorize execution.

## Relationship to M45 Controlled Autopilot
M45 может использовать Task Contract v2 позже, но M44.3 не запускает автопилот.

## Required Fields
- contract_version
- task_id
- source_spec
- source_ux
- source_ui_contract
- goal
- expected_result
- in_scope
- out_of_scope
- affected_paths
- forbidden_paths
- dependencies
- blocked_by
- priority
- risk_level
- risk_reason
- acceptance_criteria
- validation_plan
- rollback_plan
- human_approval_required
- owner_review_required
- context_required
- created_at

## Source References
Каждый контракт должен ссылаться на source Spec, source UX и source UI Contract dependency.

## Scope Rules
No scope → no task.

## Affected Paths Rules
Затрагиваемые пути должны быть перечислены явно.

## Forbidden Paths Rules
Запрещённые пути должны быть перечислены явно. Их перечисление не даёт разрешения на изменение.

## Dependency Rules
- Зависимости указываются явно в `dependencies`.
- Блокеры указываются в `blocked_by`.
- Blocked dependency -> задача не ready.

## Priority Rules
Допустимые значения priority:
- high
- normal
- low

## Risk Level Rules
Допустимые значения risk_level:
- LOW
- MEDIUM
- HIGH
- CRITICAL

Правила:
- LOW risk may not require human approval by default.
- MEDIUM risk requires rollback plan metadata.
- HIGH risk requires human_approval_required: true.
- CRITICAL risk requires human_approval_required: true and owner_review_required: true.

## Acceptance Criteria Rules
No acceptance criteria → no task.

## Validation Plan Rules
No validation plan → no task.

## Rollback Plan Rules
`rollback_plan` обязателен для всех контрактов.

## Human Approval Metadata Rules
- `human_approval_required` обязателен.
- Для HIGH/CRITICAL должен быть `true`.

## Owner Review Metadata Rules
- `owner_review_required` обязателен.
- Для CRITICAL должен быть `true`.

## Context Required Rules
- `context_required` currently records whether context is required.
- `context_required` does not yet describe which context must be selected.

## UI Task Contract Boundary
- UI tasks must reference UI Contract dependency when UI work is involved.
- Missing UI Contract blocks UI task readiness.

## Non-Approval Boundary
Task Contract readiness does not approve execution.
Task Contract validity does not replace HumanApprovalGate.
Queue placement does not authorize execution.
Task Contract validity is not task queue approval.
Task Contract validity is not commit approval.
Task Contract validity is not push approval.
Context readiness does not authorize execution.

## Known Gaps
- KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
- KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
- KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
- UI dependency is recorded generically until upstream artifacts exist.

context_required currently records whether context is required.
It does not yet describe which context must be selected.
Future M44 tasks or M45 integration should define context details such as required_context_sources, context_pack_id, selected_context_files, relevance reasons, and must_follow rules.
