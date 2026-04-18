# STATE.md — Текущее состояние проекта
<!-- Обновляется агентом при каждом переходе. Не редактировать вручную. -->
<!-- Агент обязан прочитать этот файл ПЕРВЫМ при старте каждой сессии. -->

---

## Project
state: INIT
sub_state: ""
last_event: PROJECT_CREATED
last_updated: ""

## Session
state: BOOTSTRAP
last_event: ""
mode: ""

## Task
active_task: ""
state: ""
risk: ""

## Guards
forbidden:
  - execute_without_explicit_approval
  - write_code_before_planning
  - release_without_audit
  - skip_self_verification
next_allowed_actions:
  - read_START.md
  - launch_interview

## Transition Log
- YYYY-MM-DD: PROJECT_CREATED → INIT
