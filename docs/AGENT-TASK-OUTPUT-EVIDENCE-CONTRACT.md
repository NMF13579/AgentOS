# Agent Task Output Evidence Contract

## 1. Purpose
Определить контракт (правила формата) для evidence, который агент предоставляет после выполнения задачи.

contract_scope: agent_task_output_evidence_schema
schema_path: schemas/agent-task-output-evidence.schema.json
contract_version: m64.agent_task_output_evidence.v1
evidence_type: agent_task_output_evidence
task_id_min_length_required: true
task_brief_path_min_length_required: true
non_authority_boundary_min_items_required: true
command_exit_code_minimum: -1
command_items_additional_properties_false: true
validation_result_items_additional_properties_false: true
defines_evidence_integrity_mapping: false
defines_evidence_claim_boundary: false
defines_evidence_checker: false
defines_evidence_fixtures: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. M64 Position in the Roadmap
M64 задаёт структуру evidence.
M65 проверяет критерии приёмки (acceptance criteria).
M66 объединяет проверки в единый запуск (unified runner).
M67 усиливает устойчивость против ложного PASS и связывает это с completion gate.

## 3. Evidence Object Role
Agent evidence is required for validation.
Agent evidence is not approval.
Agent evidence must be checked, not trusted.
Human review remains required.

Evidence — это структурированный набор заявлений агента, а не автоматическое подтверждение завершения.

## 4. Required Top-Level Fields
Обязательные поля верхнего уровня:
- contract_version
- evidence_type
- task_id
- task_brief_path
- agent_identity
- files_changed
- created_artifacts
- modified_artifacts
- deleted_artifacts
- commands_run
- validation_results
- known_limitations
- warnings
- blockers
- forbidden_actions_performed
- human_review_required
- non_authority_boundary

## 5. Required Const Values
Жёстко фиксированные значения (`const`):
- contract_version = `m64.agent_task_output_evidence.v1`
- evidence_type = `agent_task_output_evidence`
- forbidden_actions_performed = `false`
- human_review_required = `true`

## 6. Field Type Requirements
- task_id: строка, `minLength: 1`
- task_brief_path: строка, `minLength: 1`
- non_authority_boundary: массив строк, `minItems: 1`
- files/artifacts массивы: элементы-строки (`minLength: 1`)
- commands_run: массив объектов команд
- validation_results: массив объектов результатов
- known_limitations/warnings/blockers: массивы строк

## 7. Agent Identity
`agent_identity` — объект с полями:
- agent_name: строка, `minLength: 1`
- agent_role: строка, `minLength: 1`

`agent_identity` identifies author, but gives no approval authority.

## 8. File and Artifact Evidence
Поля:
- files_changed
- created_artifacts
- modified_artifacts
- deleted_artifacts

Это заявления агента о файлах/артефактах. Они не доказывают фактическую корректность diff (списка изменений).

## 9. Command Evidence
`commands_run` — массив объектов с обязательными полями:
- command
- purpose
- exit_code
- result
- notes

Ограничения:
- `command`: непустая строка
- `exit_code`: целое число, минимум `-1`
- `result`: enum `PASS|FAIL|NOT_RUN|UNKNOWN`
- объект команды: `additionalProperties: false`

## 10. Validation Result Evidence
`validation_results` — массив объектов с обязательными полями:
- check_name
- result
- notes

Ограничения:
- `check_name`: непустая строка
- `result`: enum `PASS|FAIL|NOT_RUN|UNKNOWN`
- объект результата: `additionalProperties: false`

## 11. Limitations, Warnings, and Blockers
Поля:
- known_limitations
- warnings
- blockers

Схема проверяет только форму данных. Смысл (когда warning должен стать blocker и т.д.) не определяется этим документом.

## 12. Human Review Invariant
`human_review_required` закреплён как `const: true`.
Evidence не может отключить ручную проверку.
Human review remains required.

## 13. Forbidden Actions Invariant
`forbidden_actions_performed` закреплён как `const: false`.
Evidence не может быть структурно валидным, если в нём заявлено выполнение запрещённых действий.

## 14. Non-Authority Boundary Structure
`non_authority_boundary` обязателен как непустой массив строк (`minItems: 1`).
Схема требует наличие структуры, но не фиксирует точные обязательные фразы (это позже, в 64.4/64.5).

Рекомендуемые фразы:
- Agent evidence is not approval.
- Agent evidence does not complete the task.
- Agent evidence does not replace human review.
- Agent evidence does not authorize merge, push, or release.
- Human review remains required.

## 15. Schema Boundary
Схема проверяет:
- обязательные поля
- типы полей
- enum/const ограничения
- базовую форму объектов и массивов

Схема не проверяет:
- реальную корректность diff
- подлинность выполнения команд
- подлинность результатов проверок
- выполнение acceptance criteria
- approval/completion/merge/release readiness

## 16. Relationship to 64.3 Integrity Rules
64.3 defines evidence integrity and decision semantics.
Этот документ не задаёт mapping-логику решений PASS/BLOCKED/NOT_ENOUGH_EVIDENCE.

## 17. Relationship to 64.4 Claim Boundary
64.4 defines exact evidence claim boundary.
Этот документ не задаёт полный список и детектирование всех запрещённых утверждений.

## 18. Relationship to 64.5 Evidence Checker
64.5 implements evidence checker.
Этот документ не реализует скрипт проверки evidence.

## 19. Relationship to M65-M67
M65 will define acceptance criteria checking.
M66 will define unified agent task validation runner.
M67 will define false PASS resistance and completion gate integration.

M64 evidence schema defines what evidence looks like.
M65 checks whether task requirements were satisfied.
M66 combines validation layers into one runner.
M67 hardens the full pipeline against false PASS.

## 20. Non-Authority Boundary
Agent task output evidence schema is not approval.
Agent task output evidence schema does not replace human review.
Agent task output evidence schema does not complete M64.
Agent task output evidence schema does not start M65.
Agent task output evidence schema does not validate completed agent tasks as a production gate.
Agent task output evidence schema does not prove task completion.
Agent task output evidence schema does not prove command execution authenticity.
Agent task output evidence schema does not prove acceptance criteria satisfaction.
Agent task output evidence schema does not create the evidence checker.
Agent task output evidence schema does not define acceptance criteria checking.
Agent task output evidence schema does not create the unified agent task validation runner.
Agent task output evidence schema does not create the false PASS resistance suite.
Agent task output evidence schema does not integrate the completion gate.
Agent task output evidence schema does not approve any agent task result.
Agent task output evidence schema does not authorize merge, push, or release.
Human review remains required.

## 21. Final Status
FINAL_STATUS: M64_AGENT_EVIDENCE_SCHEMA_DEFINED_WITH_WARNINGS
