---
type: ux-flow-policy
status: canonical
authority: ux-structure
version: 1.0.0
created: 2026-05-21
owner: human
---

# M47 UX Flow Policy

## Purpose
Определить канонические правила описания пользовательских UX-потоков в UX Contract для M47.

## Role in M47
Документ задаёт единый способ описания пути пользователя через экраны, состояния, точки решения, риска, одобрения, блокировки и безопасного следующего шага.

## Relationship to Product Spec
Product Spec остаётся источником продуктовых требований. UX Flow Policy описывает только UX-структуру взаимодействия.

## Relationship to UX Contract
Каждый UX Flow в UX Contract должен соответствовать правилам и формату этого документа.

## Relationship to UX Screen & State Model
Состояния в потоке должны ссылаться на разрешённые состояния из `docs/UX-SCREEN-STATE-MODEL.md`.

## Relationship to UX Element Vocabulary
Элементы в шагах потока должны ссылаться на разрешённые элементы из `docs/UX-ELEMENT-VOCABULARY.md`.

## UX Flow Definition
- UX Flow describes a user-facing interaction path.
- UX Flow connects screens, states, elements, decisions, risks, and next actions.
- UX Flow must show happy paths and blocked paths.
- UX Flow must show what is not authorized.
- UX Flow is not runtime workflow.
- UX Flow is not task state transition.
- UX Flow is not execution planning.
- UX Flow is not approval.

## Flow Definition Format
```yaml
flow_id:
flow_title:
actor:
source_sections:
entry_point:
preconditions:
steps:
decision_points:
risk_points:
approval_points:
blocked_states:
exit_states:
next_step:
not_authorized:
traceability:
non_authority_notice:
```

## Required Flow Fields
- flow_id must be stable and unique inside the UX Contract.
- flow_title must be user-facing.
- actor must identify who experiences or initiates the flow.
- source_sections must link the flow to Product Spec sections.
- entry_point must describe how the flow starts.
- preconditions must describe what must be known before the flow is shown.
- steps must describe visible user-facing flow steps.
- decision_points must describe conceptual user choices.
- risk_points must describe where risk is visible.
- approval_points must describe where approval may be required.
- blocked_states must describe where the flow cannot proceed.
- exit_states must describe how the flow ends.
- next_step must describe the next safe user-facing action.
- not_authorized must explicitly list what the flow does not authorize.
- traceability must preserve source references.
- non_authority_notice must preserve the M47 boundary.

## Flow Step Model
```yaml
step_id:
screen_id:
state:
ux_elements:
user_visible_text:
user_action:
system_response:
risk_visibility:
approval_visibility:
blocked_condition:
next_step:
```

- Flow steps describe visible interaction structure.
- Flow steps must reference screen IDs where applicable.
- Flow steps must reference states from docs/UX-SCREEN-STATE-MODEL.md.
- Flow steps must reference UX elements from docs/UX-ELEMENT-VOCABULARY.md.
- Flow steps must not execute commands.
- Flow steps must not mutate files.
- Flow steps must not change task lifecycle status.
- Flow steps must not create approval records.

Every UX Flow must describe:
- actor
- entry point
- steps
- decision points
- risk points
- approval points
- blocked states
- exit states
- next step
- what is not authorized

The required content list:
actor
entry point
steps
decision points
risk points
approval points
blocked states
exit states
next step
what is not authorized

User opens Agent Action Review
↓
System shows action summary
↓
System shows risk banner
↓
User reviews affected files
↓
User sees approval card
↓
User may approve / decline conceptually
↓
Execution is still not authorized by preview or UX Contract

```yaml
flow_id: agent_action_review_flow
flow_title: Agent Action Review Flow
actor: human_user
entry_point: User opens Agent Action Review
decision_points:
  - review proposed agent action
  - choose approve conceptually
  - choose decline conceptually
risk_points:
  - risk banner visible before decision
approval_points:
  - approval card visible
blocked_states:
  - approval owner is undefined
  - affected scope is missing
  - risk level is unknown
exit_states:
  - user requests changes
  - user records conceptual approval direction
  - user declines proposed action
next_step: Create or update downstream task contract only through separate authorized process.
not_authorized:
  - task generation
  - execution planning
  - implementation
  - commit
  - push
  - merge
  - deploy
  - release
```

## Decision Point Rules
- Decision points show conceptual user choices.
- Decision points must show consequences.
- Decision points must show safer alternatives where applicable.
- Decision points must not silently choose defaults.
- Decision points must not create approval records.
- Decision points must not authorize execution.
- Decision points must not authorize implementation.

## Risk Point Rules
- Risk points must be visible before risky decisions.
- Risk points must include risk reason.
- Risk points must include affected scope where known.
- Unknown risk must be represented as blocked or needs clarification.
- Risk points must not downgrade risk.
- Risk points must not hide high-risk conditions.
- Risk points must not replace approval.

## Approval Point Rules
- Approval points may be displayed in UX Flow.
- Approval points must identify the human owner where known.
- Approval points must show consequences.
- Approval points must preserve non-authority notice.
- Approval points must not create approval.
- Approval points must not simulate human approval.
- Approval points must not authorize execution.
- Approval points must not authorize task generation.
- Approval points must not authorize implementation.

## Blocked State Rules
- UX Flows must include blocked states where required information is missing.
- UX Flows must include blocked states where risk is unknown.
- UX Flows must include blocked states where approval owner is undefined.
- UX Flows must include blocked states where affected scope is missing.
- Blocked states must be visible to the user.
- Blocked states must include required resolution.
- Blocked states must not be treated as optional warnings.
- Blocked states must not provide bypass instructions.

## Exit State Rules
- Exit states must describe user-facing end points.
- Exit states must distinguish conceptual review from implementation readiness.
- Exit states must not imply execution authorization.
- Exit states must not imply task lifecycle mutation.
- Exit states must not imply deployment or release readiness.

## Next Step Rules
- Next step must describe the next safe user-facing action.
- Next step may refer to future task planning only as a separate downstream process.
- Next step must not directly create task contracts.
- Next step must not directly authorize implementation.
- Next step must not directly trigger execution.

## What Is Not Authorized
UX Flow does not execute workflow.
UX Flow does not mutate task state.
UX Flow does not create approval.
UX Flow does not authorize task generation.
UX Flow does not authorize execution planning.
UX Flow does not authorize implementation.
UX Flow does not authorize commit, push, merge, deploy, or release.

## Traceability Requirements
Каждый UX Flow в UX Contract должен сохранять трассируемость к:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- source_sections

- Traceability is not approval.
- Traceability is not execution authorization.
- If Product Spec changes, UX Flow references may become stale.
- Stale UX Flow references must not be treated as current UX authority.

## HTML Preview Boundary
- UX Flows may be rendered in optional Static HTML Preview.
- HTML Preview rendering is visual explanation only.
- HTML Preview is not source of truth.
- HTML Preview is not implementation.
- HTML Preview must preserve flow boundaries.
- HTML Preview must show blocked and non-authorized states where relevant.
- HTML Preview must not contain enabled controls.
- HTML Preview must not contain JavaScript.
- HTML Preview must not contain forms.
- HTML Preview must display non-authority boundaries.

HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.

## Forbidden Uses
Запрещено трактовать UX Flow как исполняемый процесс, разрешение на реализацию или изменение жизненного цикла задачи.
Запрещено использовать UX Flow как замену человеческого решения или официального одобрения.

## Non-Authority Boundary
UX Flow describes user-facing interaction structure.
UX Flow does not execute workflow.
UX Flow does not mutate task state.
UX Flow does not create approval.
UX Flow does not authorize task generation.
UX Flow does not authorize execution planning.
UX Flow does not authorize implementation.
UX Flow does not authorize commit, push, merge, deploy, or release.
UX Flow may show decision, risk, approval, blocked, and exit points.
UX Flow must not make decisions, approve actions, or execute actions.
HTML Preview is optional visual explanation only.

## Future Validator Notes
- Future validate-ux-contract.py should check that every flow has required fields.
- Future validate-ux-contract.py should check that every flow has at least one step.
- Future validate-ux-contract.py should check that flow states reference allowed UX states.
- Future validate-ux-contract.py should check that flow elements reference allowed UX elements.
- Future validate-ux-contract.py should check that approval-related flows include approval points.
- Future validate-ux-contract.py should check that risk-related flows include risk points.
- Future validate-ux-contract.py should check that blocked flows include blocked states.
- Future validate-ux-contract.py should check that not_authorized is present.
- M47.5 does not implement the validator.

## Summary
Документ фиксирует каноническую политику UX-потоков M47: как описывать путь пользователя, риски, решения, блокировки и границы неавторизации без выполнения действий.
