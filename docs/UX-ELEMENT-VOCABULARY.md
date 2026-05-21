---
type: ux-element-vocabulary
status: canonical
authority: ux-structure
vocabulary_version: 1.0.0
created: 2026-05-21
owner: human
---

# M47 UX Element Vocabulary

## Purpose
Определить канонический (официальный для структуры UX) начальный набор UX-элементов для M47.
This vocabulary version is 1.0.0.
Future validators that hardcode this allowlist must explicitly state which vocabulary_version they implement.

## Role in M47
Этот документ задаёт разрешённые UX-примитивы (базовые элементы интерфейса) для UX Contract.
For M47, validate-ux-contract.py may use a hardcoded allowlist derived from this initial vocabulary.
M47 does not require vocabulary-file parsing.

## Relationship to UX Contract
UX Contract использует элементы из этого словаря как допустимую структуру UX.
Словарь не заменяет Product Spec и не создаёт разрешение на выполнение действий.

## Initial Allowed UX Elements
Разрешённые начальные типы элементов:
- summary_card
- risk_banner
- approval_card
- decision_card
- status_badge
- review_panel
- task_card
- checklist
- timeline
- empty_state
- error_state
- blocked_state
- confirmation_notice
- audit_note
- non_authority_notice

## Machine-Readable Allowlist
```yaml
allowed_ux_elements:
  - summary_card
  - risk_banner
  - approval_card
  - decision_card
  - status_badge
  - review_panel
  - task_card
  - checklist
  - timeline
  - empty_state
  - error_state
  - blocked_state
  - confirmation_notice
  - audit_note
  - non_authority_notice
```

## Element Definition Format
Каждый элемент описывается одинаково:
- Purpose
- Required Data
- Allowed Usage
- Forbidden Usage
- Required States
- Risk / Approval Notes
- HTML Preview Rendering Rules
- Traceability Requirements

## Element Definitions

## Element: summary_card
### Purpose
Summarize a user-facing object, action, task, spec, or review item.
### Required Data
- title
- summary
- source_reference
- status
### Allowed Usage
- Краткий обзор объекта перед чтением деталей.
### Forbidden Usage
- hidden_decision
- implied_approval
- execution_trigger
### Required States
- normal
- loading
- empty
- error
- blocked
### Risk / Approval Notes
Может показывать риск, но не создаёт одобрение.
### HTML Preview Rendering Rules
Только визуальное отображение без активных контролов.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: risk_banner
### Purpose
Show risk level and risk reason before a user decision or risky action.
### Required Data
- risk_level
- risk_reason
- affected_scope
- mitigation_hint
### Allowed Usage
- Показ риска перед решением пользователя.
### Forbidden Usage
- risk_downgrade
- approval_substitute
- hidden_high_risk
### Required States
- normal
- warning
- high_risk
- blocked
### Risk / Approval Notes
Показывает риск, но не подтверждает действие.
### HTML Preview Rendering Rules
Только визуально, без JavaScript и форм.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: approval_card
### Purpose
Show a human decision point before agent action.
### Required Data
required_data:
  - action_summary
  - risk_level
  - human_owner
  - consequences
  - approve_label
  - decline_label
  - non_authority_notice
### Allowed Usage
- Показ точки принятия решения человеком.
### Forbidden Usage
forbidden:
  - auto_execute
  - hidden_approval
  - enabled_preview_button
  - approval_without_owner
### Required States
- normal
- approval_required
- blocked
### Risk / Approval Notes
approval_card may display a decision point.
approval_card must not create approval by itself.
approval_card must not authorize execution by itself.
### HTML Preview Rendering Rules
Только визуально; кнопки в превью неактивны.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: decision_card
### Purpose
Present available conceptual choices to the user.
### Required Data
- decision_title
- options
- consequences
- recommended_next_step
- non_authority_notice
### Allowed Usage
- Показ возможных вариантов выбора.
### Forbidden Usage
- automatic_decision
- hidden_default_choice
- decision_as_approval_record
### Required States
- normal
- needs_clarification
- blocked
### Risk / Approval Notes
Может объяснять выборы, но не принимает решение.
### HTML Preview Rendering Rules
Только визуальная демонстрация вариантов.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: status_badge
### Purpose
Display current status in compact form.
### Required Data
- status
- status_label
- status_meaning
### Allowed Usage
- Компактная индикация состояния.
### Forbidden Usage
- hiding_blocked_status
- converting_warning_to_pass
- status_without_source
### Required States
- normal
- warning
- blocked
- deprecated
### Risk / Approval Notes
Статус информирует, но не авторизует действия.
### HTML Preview Rendering Rules
Допускается только текст/метка состояния.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: review_panel
### Purpose
Show reviewable details before a human decision.
### Required Data
- review_subject
- review_items
- affected_scope
- source_references
### Allowed Usage
- Показ деталей для проверки человеком.
### Forbidden Usage
- silent_approval
- hidden_risk
- execution_button
### Required States
- normal
- loading
- blocked
### Risk / Approval Notes
Поддерживает проверку, но не даёт разрешение на исполнение.
### HTML Preview Rendering Rules
Без активных контролов и без форм.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: task_card
### Purpose
Summarize a task or candidate task for review.
### Required Data
- task_id
- task_title
- task_status
- scope_summary
- source_reference
### Allowed Usage
- Краткое описание задачи для ревью.
### Forbidden Usage
- task_generation_permission
- execution_permission
- lifecycle_mutation
### Required States
- normal
- review
- blocked
### Risk / Approval Notes
Показывает сведения о задаче, не запускает задачу.
### HTML Preview Rendering Rules
Только визуальная карточка, без кнопок выполнения.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: checklist
### Purpose
Show required review or verification items.
### Required Data
- checklist_title
- items
- completion_status
### Allowed Usage
- Контроль обязательных пунктов проверки.
### Forbidden Usage
- checklist_as_approval
- unchecked_items_as_passed
- hidden_failed_items
### Required States
- normal
- in_progress
- blocked
### Risk / Approval Notes
Чеклист не является одобрением.
### HTML Preview Rendering Rules
Статический список без интерактивного изменения состояния.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: timeline
### Purpose
Show ordered steps or history.
### Required Data
- timeline_title
- events
- event_statuses
### Allowed Usage
- Показ последовательности событий.
### Forbidden Usage
- fake_history
- missing_source_events
- timeline_as_authorization
### Required States
- normal
- loading
- blocked
### Risk / Approval Notes
История только объясняет, не разрешает действия.
### HTML Preview Rendering Rules
Статический порядок событий, без запуска шагов.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: empty_state
### Purpose
Explain that no user-facing data or actions are currently available.
### Required Data
- title
- reason
- next_safe_action
### Allowed Usage
- Объяснение отсутствия данных или действий.
### Forbidden Usage
- hiding_error
- hiding_blocked_state
- fake_completion
### Required States
- empty
- blocked
### Risk / Approval Notes
Не может трактоваться как успешное выполнение.
### HTML Preview Rendering Rules
Только текстовое объяснение безопасного следующего шага.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: error_state
### Purpose
Explain an error in a user-facing way.
### Required Data
- error_summary
- error_reason
- recovery_hint
- source_reference
### Allowed Usage
- Прозрачное отображение ошибок.
### Forbidden Usage
- masking_blocked_state
- treating_error_as_success
- hiding_validation_failure
### Required States
- error
- blocked
### Risk / Approval Notes
Ошибка не может быть показана как успех.
### HTML Preview Rendering Rules
Статическая ошибка с пояснением, без интерактивного обхода.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: blocked_state
### Purpose
Explain why a user or agent flow is blocked.
### Required Data
- blocked_reason
- blocking_rule
- required_resolution
- owner
### Allowed Usage
- Явно показать блокировку и как её снять.
### Forbidden Usage
- bypass_instruction
- hidden_blocker
- blocked_as_optional_warning
### Required States
- blocked
### Risk / Approval Notes
Блокировка обязательна к соблюдению.
### HTML Preview Rendering Rules
Показывать правило блокировки и владельца решения.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: confirmation_notice
### Purpose
Show that a user-facing non-execution event was acknowledged.
### Required Data
- confirmation_summary
- confirmed_scope
- timestamp_or_reference
### Allowed Usage
- Подтверждение факта ознакомления/подтверждения без выполнения.
### Forbidden Usage
- confirmation_as_approval
- confirmation_as_execution_permission
- fake_completion
### Required States
- normal
- acknowledged
### Risk / Approval Notes
Подтверждение не равно одобрению выполнения.
### HTML Preview Rendering Rules
Только уведомление без активных действий.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: audit_note
### Purpose
Surface audit-relevant context in a user-facing way.
### Required Data
- audit_subject
- audit_reference
- audit_summary
### Allowed Usage
- Показ контекста для аудита.
### Forbidden Usage
- audit_as_approval
- hidden_audit_failure
- audit_note_as_source_of_truth
### Required States
- normal
- warning
- blocked
### Risk / Approval Notes
Аудитная заметка не даёт разрешение на действия.
### HTML Preview Rendering Rules
Только отображение контекста и ссылок аудита.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## Element: non_authority_notice
### Purpose
Explicitly show that the current UX structure, preview, or card is not approval and not execution permission.
### Required Data
- notice_text
- applies_to
- boundary_reference
### Allowed Usage
- Явное предупреждение о границах полномочий.
### Forbidden Usage
- omitted_boundary
- weakened_boundary
- authority_claim
### Required States
- normal
- required
### Risk / Approval Notes
Критично для защиты от ложной трактовки как разрешения.
### HTML Preview Rendering Rules
Должно быть видимо в превью рядом с релевантным элементом.
### Traceability Requirements
Связь с spec_id, spec_version, product_spec_path, ux_contract_id, source_sections.

## HTML Preview Rendering Boundary
UX elements may be rendered in optional Static HTML Preview.
HTML Preview rendering is visual explanation only.
HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.
HTML Preview must not contain enabled controls.
HTML Preview must not contain JavaScript.
HTML Preview must not contain forms.
HTML Preview must preserve traceability attributes where rendered.
HTML Preview must display non-authority boundaries.

## Traceability Requirements
Every UX element used in a UX Contract must preserve traceability to:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- source_sections
Traceability is not approval.
Traceability is not execution authorization.
If Product Spec changes, UX element references may become stale.
Stale UX element references must not be treated as current UX authority.

## Risk and Approval Rules
UX elements may display risk and approval information.
UX elements must not create approval records.
UX elements must not simulate human approval.
UX elements must not authorize execution.
UX elements must not authorize task generation.
UX elements must not authorize implementation.
UX elements must not authorize commit, push, merge, deploy, or release.

## Forbidden Uses
Запрещено использовать словарь и элементы как источник разрешения на запуск, реализацию или выпуск.
Запрещено трактовать элементы как замену решения человека.

## Non-Authority Boundary
UX Element Vocabulary defines allowed UX primitives.
UX Element Vocabulary does not define Product Spec requirements.
UX Element Vocabulary does not authorize task generation.
UX Element Vocabulary does not authorize execution planning.
UX Element Vocabulary does not authorize implementation.
UX Element Vocabulary does not authorize commit, push, merge, deploy, or release.
UX elements may explain decisions.
UX elements must not make decisions.
UX elements may display approval points.
UX elements must not create approval.
HTML Preview is optional visual explanation only.

## Future Extension Rules
New UX element types require explicit review.
New UX element types must not be silently added.
New UX element types must include the same required element section format.
New UX element types must include forbidden usage.
New UX element types must include traceability requirements.
New UX element types must preserve non-authority boundaries.
Future parser support may be added after the vocabulary format is stable.
M47 does not require vocabulary-file parsing.
Future validators that hardcode this allowlist must explicitly state which vocabulary_version they implement.
For M47, validate-ux-contract.py may use a hardcoded allowlist derived from this initial vocabulary.
This vocabulary version is 1.0.0.
Future validators that hardcode this allowlist must explicitly state which vocabulary_version they implement.

## Summary
Документ фиксирует начальный словарь UX-элементов M47 версии 1.0.0, границы применения и запрет на авторизацию исполнения.
