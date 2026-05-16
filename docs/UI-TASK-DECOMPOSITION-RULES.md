## Purpose
Этот документ задаёт правила декомпозиции UI-задач в M44.

## Position in M44
M44 подготавливает контракты задач, но не запускает выполнение.

## Relationship to M43.5 UI Contract
UI-задачи должны опираться на UI Contract dependency (зависимость от UI-контракта).

## Relationship to Task Contract v2
Правила применяются к Task Contract v2 как слой UI-ограничений.

## Relationship to UX-to-Task Generator
Генератор UX-to-task формирует кандидатов, а этот документ задаёт UI-границы для таких кандидатов.

## UI Task Categories
- app_feature_ui
- agentos_control_ui
- ui_state_handling
- ui_error_handling
- ui_accessibility
- ui_responsive_behavior
- ui_copy
- ui_contract_alignment

## Source Reference Requirements
UI-контракт задачи должен ссылаться на `source_ux` и `source_ui_contract`.

## UI Contract Dependency Rules
Missing UI Contract blocks UI task readiness.

## Semantic Intent Rules
UX prose describes user experience intent, not direct implementation authority.
Agent must describe semantic intent, not visual taste.

## App Feature UI Boundary
`app_feature_ui` описывает UI функциональности приложения через семантические компоненты и допустимые абстракции UI Contract.

## AgentOS Control UI Boundary
`agentos_control_ui` касается только управляющего UI AgentOS через одобренные семантические абстракции.

## State and Error Handling Rules
Состояния задаются семантически: empty/loading/error/success/disabled/blocked.

## Accessibility Rules
Задача должна содержать требования доступности (клавиатура, метки, читаемость, озвучивание и т.д.).

## Responsive Behavior Rules
Адаптивность описывается как поведение и ограничения, а не как жёсткий пиксельный макет.

## UX Copy Rules
Копирайтинг (тексты UI) задаётся как intent + критерии приёмки.

## Allowed UI Task Patterns
- Reference source_ux.
- Reference source_ui_contract.
- Describe UI behavior semantically.
- Define states using task contract acceptance criteria.
- Use approved semantic component abstractions.
- Use approved design tokens only through the UI Contract.
- Keep visual implementation replaceable.
- Put raw styling questions into Known Gaps or owner review.
- Mark missing UI Contract as blocked.
- Mark unknown component boundary as needs_review.
- Use validation plan placeholders for future UI contract checks.

Примеры допустимых формулировок:
- Implement semantic empty/loading/error/success states.
- Add accessible label requirement.
- Add responsive behavior acceptance criteria.
- Add UX copy acceptance criteria.
- Add UI Contract compliance placeholder to validation_plan.

## Forbidden UI Task Patterns
- Directly import components/ui/* from generated feature code.
- Directly import @radix-ui/* from generated feature code.
- Hardcode colors from UX prose.
- Hardcode spacing from UX prose.
- Hardcode typography from UX prose.
- Hardcode animation from UX prose.
- Create new design tokens silently.
- Treat UX screenshot or prose as design system authority.
- Treat source_ui_contract: TODO as UI readiness.
- Treat ui_contract_present: true as proof that referenced file exists on disk.
- Treat UI task contract as execution approval.
- Treat queue placement as execution approval.

## Design Token Boundary
No hardcoded colors from UX prose.
No silent token expansion.
New design tokens require review.

## Raw UI Import Boundary
Feature code must not import components/ui/* directly from generated UI tasks.

## Direct Library Import Boundary
Feature code must not import @radix-ui/* directly from generated UI tasks.

## task_category Schema Gap
task_category is UI-task-specific and is not currently defined in schemas/task-contract-v2.schema.json.
Schema extension or linter behavior for task_category is deferred to future task linting / schema alignment work.

## source_ui_contract TODO Boundary
source_ui_contract: TODO linting behavior is deferred to 44.9.

## Validation Plan Requirements
План проверки должен содержать минимум:
- проверку соответствия UI Contract (placeholder)
- проверку семантических состояний
- проверку accessibility / responsive / copy критериев

## Future Linting Expectations
Негативные фикстуры в этой задаче созданы как примеры будущих нарушений.
Hardcoded-style negative fixture validation checks presence of forbidden example patterns only; final lint classification is deferred to 44.9.

## Non-Approval Boundary
UI task readiness is not execution approval.
UI task contract validity does not replace HumanApprovalGate.
Queue placement does not authorize execution.

## Known Gaps
- This task does not implement a UI task validator.
- This task does not modify Task Contract v2 schema.
- task_category is UI-task-specific and is not currently defined in schemas/task-contract-v2.schema.json.
- Schema extension or linter behavior for task_category is deferred to future task linting / schema alignment work.
- source_ui_contract: TODO linting behavior is deferred to 44.9.
- This task does not verify referenced UI Contract files on disk.
- This task does not define final 44.9 lint outcomes.
- Hardcoded-style negative fixture validation checks presence of forbidden example patterns only; final lint classification is deferred to 44.9.
- This task does not implement UI components.
- This task depends on M43.5 UI Contract artifacts if present.
- KNOWN_GAP: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md is missing.
- KNOWN_GAP: docs/DESIGN-TOKENS-POLICY.md is missing.
- KNOWN_GAP: docs/UI-REPLACEABILITY-POLICY.md is missing.
