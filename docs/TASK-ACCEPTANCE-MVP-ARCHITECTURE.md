# Task Acceptance MVP Architecture

## 1. Purpose
Определить минимальную архитектуру M62 для тонкой (минимальной) проверяемой цепочки проверки пакета результата задачи агента.

## 2. M62 Position in the Roadmap
M62 — это первый контролируемый сквозной MVP-этап перед формализацией полной модели в M63–M67.
M62 строит только минимальный путь проверки и передачи результата на ручной обзор.

## 3. Dependency on M61 Completion
Источник зависимости: `reports/m62-m61-completion-intake.md`.
Наблюдаемый intake-статус: `M62_INTAKE_READY_WITH_WARNINGS`.
Зависимость на M61 считается достаточной для архитектурного шага M62.1, при обязательном переносе предупреждений в следующие задачи M62.

## 4. MVP Scope
M62 создаёт тонкий контролируемый MVP для проверки пакета результата задачи.
M62 проверяет только минимальные структурные и граничные условия.
M62 доказывает сквозной путь на контролируемых примерах.
M62 не является production-уровнем приёмки задач.

В MVP-область входят только такие проверки:
- файл задачи существует;
- файл evidence (доказательства) существует;
- JSON changed-files существует и корректно читается;
- ожидаемые артефакты существуют, если они были заявлены;
- среди изменённых файлов нет явно запрещённых путей;
- `human_review_required` равно `true`;
- отсутствуют заявления об approval/merge/push/release;
- отсутствуют заявления о completion/изменении lifecycle-состояния;
- MVP-результат попадает в разрешённые значения решения.

## 5. End-to-End MVP Flow
task brief
→ declared scope
→ expected artifacts
→ actual changed files / diff summary
→ agent-provided evidence
→ MVP validation runner
→ task validation result
→ human review handoff

Это контролируемый MVP flow, а не production acceptance.

## 6. MVP Inputs
Архитектурные категории входов для будущего MVP:
- `task_id`
- `task_brief_path`
- `declared_allowed_scope`
- `declared_forbidden_changes`
- `expected_artifacts`
- `actual_changed_files`
- `diff_reference`
- `agent_evidence_path`
- `validation_commands_claimed`
- `human_review_required`

Граница: в 62.1 задаются только категории.
Детальный input contract определяется в 62.2.

## 7. MVP Outputs
Архитектурные категории выходов для будущего MVP:
- `TASK_VALIDATION_PASS`
- `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `TASK_VALIDATION_BLOCKED`
- `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`
- `human_review_required: true`
- `warnings`
- `blockers`

Граница: в 62.1 перечисляются только категории.
Детальная семантика решений определяется в 62.3.

## 8. MVP Runner Role
Будущий MVP runner:
- read-only;
- ориентирован на controlled examples;
- MVP-level only;
- не production gate;
- не completion gate;
- не approval;
- не lifecycle mutation;
- не merge/push/release authorization.

Будущий путь runner (только ссылка на план): `scripts/check-task-acceptance-mvp.py`.
Runner в 62.1 не создаётся.

## 9. Human Review Handoff
Любой результат MVP передаётся человеку на финальный разбор.
Даже при PASS ручной обзор обязателен.

## 10. Relation to M63-M67
- M63 определяет full task validation contract.
- M64 определяет full task output evidence model.
- M65 определяет acceptance criteria checker.
- M66 определяет unified agent task validation runner.
- M67 определяет false PASS resistance и completion gate integration.

M62 не должен поглощать ответственность M63-M67.

## 11. What M62 Can Decide
M62 может решать:
- достаточно ли минимальной структуры пакета для MVP-проверки;
- выявлены ли MVP-уровневые запрещённые условия;
- сохраняется ли обязательность human review;
- дают ли контролируемые примеры ожидаемые MVP-значения результата;
- готов ли тонкий путь к формализации контракта в M63.

## 12. What M62 Must Not Decide
M62 не может решать:
- final task approval;
- production task acceptance;
- полное выполнение acceptance criteria;
- полную достаточность evidence;
- полную корректность diff;
- readiness completion gate;
- merge readiness;
- release readiness;
- можно ли пропустить human review.

## 13. Non-Authority Boundary
M62 task acceptance MVP is not approval.
M62 task acceptance MVP does not replace human review.
M62 task acceptance MVP does not complete the task.
M62 task acceptance MVP does not validate completed agent tasks as a production gate.
M62 task acceptance MVP does not authorize merge, push, or release.
M62 task acceptance MVP does not start M63.
Human review remains required.

## 14. Required Outputs of M62
M62 должен выдать архитектурно связанный набор артефактов по шагам 62.1–62.10, где каждый следующий шаг остаётся в MVP-границе и не подменяет M63–M67.
На шаге 62.1 создаётся только архитектурный документ.

## 15. Completion Conditions for M62
M62 считается завершённым только после выполнения всех задач M62-цепочки, подтверждения границ и обязательного human review.
Отдельный PASS любого MVP-подшага сам по себе не означает итоговое завершение.

## 16. Final Status
FINAL_STATUS: M62_TASK_ACCEPTANCE_MVP_ARCHITECTURE_DEFINED
