# STATE.md — Текущее состояние проекта
<!-- Обновляется агентом при каждом переходе. Не редактировать вручную. -->
<!-- Агент обязан прочитать этот файл ПЕРВЫМ при старте каждой сессии. -->

---

## Project
state: MAINTENANCE
sub_state: iteration-1-state-machine
last_event: ITERATION_3_COMPLETED
last_updated: 2026-04-19

## Session
state: HANDOFF
last_event: ""
mode: ""

## Task
active_task: TASK-001 State Layer Migration
state: PLANNED
risk: ""

## Guards
forbidden:
  - execute_without_explicit_approval
  - write_code_before_planning
  - release_without_audit
  - skip_self_verification
next_allowed_actions:
  - continue TASK-001 (State Layer Migration)

## Transition Log
- 2026-04-18: ITERATION_3_COMPLETED → MAINTENANCE
- 2026-04-19: HANDOFF reset → TASK-001 PLANNED (State Layer Migration)
