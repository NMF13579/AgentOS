# Guardrails

## Purpose
Этот документ объясняет, как защитные правила AgentOS ограничивают рискованные действия.

## Guardrail Philosophy
No lower gate can override a higher safety gate.

## Gate Contract Summary
Ворота выполняются по фиксированному порядку и не могут обходить более ранние блокировки.

## Gate Result Semantics
Используются результаты:
- PASS
- BLOCKED
- WARN
- ERROR
- NOT_APPLICABLE
- NOT_RUN

## Single-Role Execution Guard
Enforces that each agent execution operates under exactly one declared role (planner, implementor, auditor, etc.) with deterministic boundaries. It prevents role-mixing (e.g., an auditor fixing its own findings) and ensures that each run stays within its authorized write-scope.

## Output Marker Requirements
Ключевые маркеры:
- GATE_NAME
- GATE_REQUIRED
- GATE_RESULT
- GATE_REASON

## Policy and Approval Boundary
- Approval cannot override policy blocks.

## Preconditions and Controlled Apply Boundary
- Preconditions cannot downgrade policy blocks.
- Controlled apply cannot start when required policy is missing.

## Validation Boundary
- Validation NOT_RUN is not PASS.
- Validation ERROR is not PASS.

## Audit and Evidence Boundary
- Evidence cannot convert a prior BLOCKED gate into PASS.
- Audit cannot legalize an unsafe operation.

## Non-Bypass Rules
- Поздний этап не может повысить заблокированный результат предыдущего этапа.
- Отсутствующий обязательный маркер не считается успешным прохождением.

## Common Failure Modes
- Пропущен обязательный gate-marker.
- Результат NOT_RUN ошибочно трактован как PASS.
- ERROR ошибочно трактован как PASS.
- usage/traceback ошибочно трактованы как валидное прохождение.

## Non-Goals
- Не описывать маркетинговые обещания качества вывода AI.
- Не заменять evidence/completion review этапы итоговым решением.
