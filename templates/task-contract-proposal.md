---
proposal_version: 1.0
proposal_id:
source_readiness_report:
source_readiness_decision:
source_spec:
source_ux_contract:
source_validation_result:
goal:
expected_result:
in_scope:
out_of_scope:
affected_paths:
forbidden_paths:
dependencies:
blocked_by:
priority:
risk_level:
risk_reason:
acceptance_criteria:
validation_plan:
rollback_plan:
human_authorization_required:
owner_review_required:
created_at:
---

## Purpose
Шаблон для `Task Contract Proposal`.
Это черновик предложения задачи, а не исполняемый Task Contract.

## Source References
Укажите источники:
- `source_readiness_report`
- `source_readiness_decision`
- `source_spec`
- `source_ux_contract`
- `source_validation_result`

## Goal
Кратко: какую проблему решает предложение.

## Expected Result
Что должно измениться после выполнения задачи.

## In Scope
Что разрешено делать в рамках предложения.

## Out of Scope
Что явно запрещено добавлять в задачу.

## Affected Paths
Список путей, которые потенциально могут быть изменены.

## Forbidden Paths
Пути, которые менять нельзя.

## Dependencies
Нужные зависимости для старта.

## Blocked By
Блокеры, из-за которых задача не может перейти к авторизации.

## Priority
Допустимые значения: `high`, `normal`, `low`.

## Risk
Допустимые значения `risk_level`: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.
Добавьте `risk_reason`.

## Acceptance Criteria
Проверяемые критерии приёмки.

## Validation Plan
Конкретный план проверки результата.

## Rollback Plan
План отката обязателен.

## Human Authorization Boundary
Опишите, какое отдельное человеческое подтверждение нужно для перехода от proposal к авторизованному контракту.

## Owner Review Boundary
Опишите требования проверки владельцем/ответственным.

## Decomposition Carry-Forward
Если proposal строится из readiness-артефактов, перенесите:
- blocking_gaps
- major_gaps
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary

## Status Rules
- Proposal можно обсуждать и править.
- Proposal нельзя исполнять.
- Proposal нельзя считать разрешением на запуск задач.

## Non-Authority Boundary
Task Contract Proposal is not task generation.
Task Contract Proposal is not implementation approval.
Task Contract Proposal does not create executable tasks.
Task Contract Proposal does not authorize task generation.
Task Contract Proposal does not authorize implementation.
Task Contract Proposal does not authorize execution planning.
Task Contract Proposal does not authorize commit, push, merge, deploy, or release.
Separate human authorization is required before execution.

## Notes
Если данных недостаточно, помечайте поля как `TODO:` и не считайте proposal готовым к авторизации.
