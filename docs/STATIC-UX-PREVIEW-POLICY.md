---
type: static-ux-preview-policy
status: canonical
authority: ux-structure
version: 1.0.0
created: 2026-05-21
owner: human
---

# Static UX Preview Policy

## Purpose
Определить безопасные правила для опционального статического HTML preview UX-контракта.

## Role in M47
Политика фиксирует, как использовать статический preview только как визуальное объяснение без авторизации действий.

## Relationship to UX Contract
UX Contract = required artifact.
HTML Preview = optional derived artifact.
Preview generation = opt-in only.
M47 completion must not depend on generator.
UX Contract is the required artifact.
HTML Preview is an optional derived artifact.
HTML Preview is visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.
Preview generation is opt-in only.
M47 completion must not depend on generator implementation.
Generator implementation is deferred.

## Relationship to UX Contract Validation
Preview может использоваться только рядом с валидным UX Contract; preview не заменяет валидацию.

## Relationship to UX Element Vocabulary
`data-ux-element` должен использовать только allowlist из `docs/UX-ELEMENT-VOCABULARY.md`.

## Relationship to UX Visual Approval Snapshot
UX Visual Approval Snapshot may reference Static HTML Preview as supporting visual evidence.
UX Visual Approval Snapshot approves visual direction only.
UX Visual Approval Snapshot does not approve production HTML.
UX Visual Approval Snapshot does not authorize implementation.
UX Visual Approval Snapshot does not authorize task generation or execution.

## Required Preview Artifacts
Priority order:
1. docs/STATIC-UX-PREVIEW-POLICY.md — required
2. templates/static-ux-preview.html — required in 47.9.2
3. examples/ux-preview/agent-action-review-preview.html — required in 47.9.3, static authored artifact
4. scripts/generate-static-ux-preview.py — optional, deferred
5. tests/fixtures/static-ux-preview/ — required only if generator is implemented

## Optional Generator Boundary
- scripts/generate-static-ux-preview.py is optional.
- The generator is not implemented in this task.
- The generator may be added in a later task only after UX Contract validation is stable.
- If generator is implemented later, it must be opt-in only.
- If generator is implemented later, it must require a validated UX Contract as input.
- If generator is implemented later, it must not use JavaScript, forms, network calls, or enabled controls.
- If generator is implemented later, fixture tests must be created.
Static HTML Preview generator is optional and deferred.

## Preview Generation Modes
Allowed generation modes:
1. User-requested
2. Agent-suggested + human-confirmed

- User-requested means the user explicitly asks to generate preview.
- Agent-suggested + human-confirmed means the agent suggests preview and a human confirms.
- Silent preview generation is forbidden.
- Automatic preview generation after UX Contract creation is forbidden.
- Preview generation without UX Contract is forbidden.

## Static HTML Safety Rules
- HTML Preview must be static.
- HTML Preview must not contain JavaScript.
- HTML Preview must not contain forms.
- HTML Preview must not contain enabled controls.
- HTML Preview must not call APIs.
- HTML Preview must not make network calls.
- HTML Preview must not claim production UI.
- HTML Preview must not claim implementation.
- HTML Preview must not create approval.
- HTML Preview must not authorize execution.

## Required Preview Header
Every preview must visibly include:
- Static UX Preview
- Source spec_id
- Source ux_contract_id
- Status: Preview only
- This preview is not implementation.

## Required Traceability Attributes
Every rendered UX element block must use this structure:
```html
<section
  data-ux-element="approval_card"
  data-source-spec="SPEC-agent-action-review"
  data-source-ux-contract="UX-agent-action-review"
  data-preview-only="true"
>
```

- data-ux-element must use allowed UX elements from docs/UX-ELEMENT-VOCABULARY.md.
- data-source-spec must reference the Product Spec ID.
- data-source-ux-contract must reference the UX Contract ID.
- data-preview-only must be "true".
- Traceability attributes are not approval.
- Traceability attributes are not implementation permission.

## Allowed UX Elements
summary_card
risk_banner
approval_card
decision_card
status_badge
review_panel
task_card
checklist
timeline
empty_state
error_state
blocked_state
confirmation_notice
audit_note
non_authority_notice

HTML preview may render only allowlisted UX elements.

## Disabled Controls Rule
Examples:
```html
<button disabled>Approve — preview only</button>
<textarea disabled placeholder="Preview only"></textarea>
```

- All controls must be disabled.
- Disabled controls are visual explanation only.
- Disabled controls must not submit, mutate, approve, or execute anything.

## Forbidden HTML Patterns
Forbidden patterns:
- <script>
- onclick=
- onchange=
- onsubmit=
- javascript:
- <form>

enabled buttons are forbidden
API calls are forbidden
network calls are forbidden

## CSP Requirement
```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'none'; style-src 'unsafe-inline'; img-src 'self'">
```

## Template Requirements
Template in 47.9.2 must include required header, CSP, traceability attributes, disabled controls, and no forbidden patterns.

## Example Preview Requirements
Example in 47.9.3 must be static authored artifact, not generated, and must keep preview-only boundary visible.

## Validation Rules
Проверка должна подтверждать: наличие header, CSP, allowlisted elements, required data attributes, disabled controls, и отсутствие forbidden patterns.

## Non-Authority Boundary
HTML Preview is visual explanation only.
HTML Preview is not source of truth.
HTML Preview is not implementation.
HTML Preview does not create approval.
HTML Preview does not authorize task generation.
HTML Preview does not authorize execution planning.
HTML Preview does not authorize implementation.
HTML Preview does not authorize commit, push, merge, deploy, or release.
Preview generation is opt-in only.
Static HTML Preview generator is optional and deferred.
UX Contract remains the source of truth for UX structure.

## Future Generator Notes
Генератор может быть добавлен позже как отдельный шаг после стабилизации валидации UX Contract, без JavaScript/форм/сетевых вызовов, с обязательными фикстурами.

## Summary
Политика закрепляет, что static UX preview опционален, безопасен и не имеет полномочий на утверждение, генерацию задач или исполнение.
