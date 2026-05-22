---
type: ux-screen-state-model
status: canonical
authority: ux-structure
version: 1.0.0
created: 2026-05-21
owner: human
---

# M47 UX Screen & State Model

## Purpose
Определить каноническую модель экранов и состояний для UX Contract в M47.

## Role in M47
Модель задаёт, как описывать пользовательские экраны и состояния, включая не только позитивные сценарии, но и блокировки, ошибки, необходимость уточнений, точки одобрения и состояние запрета исполнения.

## Relationship to Product Spec
Product Spec остаётся источником продуктовых требований. Эта модель описывает только пользовательскую структуру экранов/состояний и не заменяет Product Spec.

## Relationship to UX Contract
UX Contract должен описывать экраны и состояния по правилам этого документа.

## Relationship to UX Element Vocabulary
Поле `allowed_ux_elements` должно использовать элементы из `docs/UX-ELEMENT-VOCABULARY.md`.

## Screen Model
Каждый экран в UX Contract должен быть описан структурно и однозначно, чтобы человек видел границы и условия показа.

## Screen Definition Format
```yaml
screen_id:
screen_title:
screen_purpose:
source_sections:
allowed_ux_elements:
available_states:
default_state:
entry_conditions:
exit_conditions:
blocked_conditions:
risk_approval_points:
non_authority_notice:
```

## Required Screen Fields
- `screen_id` must be stable and unique inside the UX Contract.
- `screen_title` must be user-facing.
- `screen_purpose` must describe why the screen exists.
- `source_sections` must link the screen to Product Spec sections.
- `allowed_ux_elements` must use elements from docs/UX-ELEMENT-VOCABULARY.md.
- `available_states` must list all states the screen may show.
- `default_state` must be one of the available states.
- `entry_conditions` describe when the screen is shown.
- `exit_conditions` describe how the user leaves the screen.
- `blocked_conditions` describe why the screen may block progress.
- `risk_approval_points` describe visible decision/risk points.
- `non_authority_notice` must preserve the M47 boundary.

## State Model
Состояние описывает, что пользователь видит в конкретный момент и почему.

## Required UX States
- normal
- loading
- empty
- error
- blocked
- needs_clarification
- approval_required
- execution_not_authorized

## State Definition Format
Для каждого состояния нужно указать смысл, ограничения и запреты на ложную трактовку как разрешение на исполнение.

## State Semantics

## State: normal
- The screen has enough information to show its primary UX structure.
- normal does not mean the task is approved.
- normal does not mean execution is authorized.

## State: loading
- The screen is waiting for user-facing data or derived UX structure.
- loading must not hide blocked or error states.
- loading must not imply execution is running.

## State: empty
- The screen has no user-facing items to show.
- empty must explain why no data is available.
- empty must show the next safe action where applicable.

## State: error
- The screen cannot show the expected UX structure because something failed.
- error must include a user-facing explanation.
- error must not be converted into success.
- error must not hide validation failure.

## State: blocked
- The screen cannot proceed because a required condition is not satisfied.
- blocked must include the blocking reason.
- blocked must include required resolution.
- blocked must not be treated as optional warning.

## State: needs_clarification
- The screen or flow requires more information from a human or Product Spec.
- needs_clarification must describe the missing information.
- needs_clarification must not authorize assumptions.

## State: approval_required
- The screen displays that a human approval point exists.
- approval_required must not create approval.
- approval_required must not simulate human approval.
- approval_required must not authorize execution.

## State: execution_not_authorized
- The screen explicitly shows that execution is not authorized.
- execution_not_authorized must be available wherever the user may confuse UX structure with execution permission.
- execution_not_authorized must not provide bypass instructions.

## Blocked and Non-Authorized States
Execution planning is blocked because approval owner is undefined.

```yaml
screen_id: agent_action_review
screen_title: Agent Action Review
available_states:
  - normal
  - loading
  - error
  - blocked
  - needs_clarification
  - approval_required
  - execution_not_authorized
default_state: normal
blocked_conditions:
  - approval owner is undefined
  - affected scope is missing
  - risk level is unknown
```

## Screen-State Mapping Rules
- Every screen must define available_states.
- Every screen must define default_state.
- default_state must be listed in available_states.
- Screens that display approval points must include approval_required.
- Screens that may be confused with execution permission must include execution_not_authorized.
- Screens that depend on incomplete Product Spec information must include needs_clarification.
- Screens that depend on risk or approval data must include blocked.
- Screens must not show only happy path states.
- Blocked states must be visible to the user.
- Error states must be distinguishable from blocked states.
- Loading states must not mask blocked or error states.

## Traceability Requirements
Каждая ссылка на экран и состояние в UX Contract должна сохранять трассировку (привязку к источнику) к:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- source_sections

- Traceability is not approval.
- Traceability is not execution authorization.
- If Product Spec changes, screen/state references may become stale.
- Stale screen/state references must not be treated as current UX authority.

## Risk and Approval State Rules
- UX states may display risk and approval information.
- UX states must not create approval records.
- UX states must not simulate human approval.
- UX states must not authorize execution.
- UX states must not authorize task generation.
- UX states must not authorize implementation.
- UX states must not authorize commit, push, merge, deploy, or release.
- approval_required is a visible state, not approval.
- execution_not_authorized is a required safety state where confusion is possible.

## HTML Preview Boundary
- Screen and state definitions may be rendered in optional Static HTML Preview.
- HTML Preview rendering is visual explanation only.
- HTML Preview is not source of truth.
- HTML Preview is not implementation.
- HTML Preview must preserve visible state boundaries.
- HTML Preview must not contain enabled controls.
- HTML Preview must not contain JavaScript.
- HTML Preview must not contain forms.
- HTML Preview must display non-authority boundaries.

HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.

## Forbidden Uses
Запрещено использовать модель экранов и состояний как разрешение на выполнение, изменение, публикацию или выпуск.
Запрещено выдавать UX-состояния за решение человека.

## Non-Authority Boundary
Screen state model describes UX states.
It does not implement runtime state transitions.
UX Screen & State Model does not define Product Spec requirements.
UX Screen & State Model does not authorize task generation.
UX Screen & State Model does not authorize execution planning.
UX Screen & State Model does not authorize implementation.
UX Screen & State Model does not authorize commit, push, merge, deploy, or release.
UX states may explain blocked or approval-required conditions.
UX states must not approve, execute, or mutate anything.
HTML Preview is optional visual explanation only.

## Future Validator Notes
- Future validate-ux-contract.py should check that required states are present.
- Future validate-ux-contract.py should check that default_state is in available_states.
- Future validate-ux-contract.py should check that approval-related screens include approval_required.
- Future validate-ux-contract.py should check that execution-sensitive screens include execution_not_authorized.
- Future validate-ux-contract.py should check that screens do not contain only happy path states.
- M47.4 does not implement the validator.

## Summary
Документ задаёт обязательную модель экранов и состояний UX для M47, включая защитные состояния `blocked` и `execution_not_authorized`, без внедрения runtime-логики и без полномочий на исполнение.
