# risky-deploy-change

## Purpose
Показать, как обрабатывать рискованный запрос, связанный с deploy-изменениями.

## User Request
Пользователь просит быстро внести изменение, влияющее на deploy-путь.

## Task Contract Summary
- scope: изменение с повышенным риском
- required gates: POLICY_GATE, APPROVAL_GATE, CONTROLLED_APPLY
- condition: deploy change не разрешается автоматически

## Relevant Guardrails
- No lower gate can override a higher safety gate.
- POLICY_GATE обязателен до запуска controlled path.
- approval cannot override policy blocks.

## Expected Checks
- Явная policy-оценка перед любым controlled apply.
- Проверка, нужен ли approval и есть ли он.
- Проверка, что без policy CONTROLLED_APPLY не стартует.

## Possible Failure
Policy отсутствует или даёт BLOCKED, но команда всё равно пытается продолжить.

## Correct Safe Result
Если policy отсутствует или BLOCKED, выполнение должно остановиться; безопасный следующий шаг — NEEDS_REVIEW или явная policy evaluation.

## What Not To Do
- Не стартовать CONTROLLED_APPLY при missing policy.
- Не считать approval достаточным для обхода policy.

## MVP Boundary
This scenario is documentation only and does not mark AgentOS as MVP-ready.
