# Agent Evidence Integrity Rules

## 1. Purpose
Определить правила целостности evidence (доказательных данных) и правила принятия результата проверки на уровне M64.

integrity_scope: agent_task_output_evidence_integrity
schema_path: schemas/agent-task-output-evidence.schema.json
contract_path: docs/AGENT-TASK-OUTPUT-EVIDENCE-CONTRACT.md
defines_evidence_integrity_mapping: true
defines_evidence_decision_semantics: true
defines_exit_code_minus_one_semantics: true
validation_results_without_commands_run_blocks: false
validation_results_without_commands_run_warns: true
defines_exact_claim_boundary: false
defines_evidence_checker: false
defines_evidence_fixtures: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. M64 Position in the Roadmap
M64 integrity rules оценивают структуру и внутреннюю согласованность evidence.
M65 проверяет критерии приёмки.
M66 объединяет M63+M64+M65+scope/diff проверки.
M67 усиливает устойчивость к ложному PASS и completion gate.

## 3. Inputs and Dependencies
Использованы:
- reports/m64-m63-completion-intake.md
- docs/TASK-OUTPUT-EVIDENCE-MODEL-ARCHITECTURE.md
- schemas/agent-task-output-evidence.schema.json
- docs/AGENT-TASK-OUTPUT-EVIDENCE-CONTRACT.md
- reports/m63-completion-review.md
- docs/TASK-VALIDATION-HUMAN-REVIEW-BOUNDARY.md

Состояние зависимостей: intake и архитектура со статусом `WITH_WARNINGS`, схема и контракт присутствуют.

## 4. Evidence Integrity Categories
Каждая категория: смысл, почему важно, ожидаемое отображение (mapping) и блокирует ли clean PASS.

- missing evidence: файл evidence отсутствует. Важно, потому что проверять нечего. Mapping: BLOCKED. Блокирует PASS: да.
- malformed evidence: JSON сломан. Важно, потому что структура не читается. Mapping: BLOCKED. Блокирует PASS: да.
- unsupported evidence version: неизвестная версия контракта. Важно, потому что правила могут не совпасть. Mapping: BLOCKED. Блокирует PASS: да.
- wrong evidence type: неверный тип evidence. Важно, потому что проверяется не тот контракт. Mapping: BLOCKED. Блокирует PASS: да.
- missing identity: нет `agent_identity`. Важно для трассируемости источника. Mapping: BLOCKED. Блокирует PASS: да.
- empty identity: пустые `agent_name` или `agent_role`. Важно для идентификации. Mapping: BLOCKED. Блокирует PASS: да.
- task mismatch: `task_id` не совпадает с ожидаемым. Важно, потому что данные могут быть от другой задачи. Mapping: BLOCKED. Блокирует PASS: да.
- missing required fields: отсутствуют обязательные поля. Mapping: BLOCKED. Блокирует PASS: да.
- wrong field types: неверные типы полей. Mapping: BLOCKED. Блокирует PASS: да.
- empty evidence: все evidence-bearing массивы пустые. Mapping: NOT_ENOUGH_EVIDENCE. Блокирует clean PASS: да.
- not enough evidence: данных недостаточно для проверяемого вывода. Mapping: NOT_ENOUGH_EVIDENCE. Блокирует clean PASS: да.
- contradictory evidence: взаимные противоречия полей/заметок. Mapping: BLOCKED или PASS_WITH_WARNINGS. Блокирует clean PASS: да.
- stale evidence: признаки устаревших данных. Mapping: BLOCKED / PASS_WITH_WARNINGS / NOT_ENOUGH_EVIDENCE. Блокирует clean PASS: да.
- hidden blocker: блокер замаскирован как warning/note. Mapping: BLOCKED или PASS_WITH_WARNINGS. Блокирует clean PASS: да.
- forbidden action: `forbidden_actions_performed=true` или эквивалентный сигнал. Mapping: BLOCKED. Блокирует clean PASS: да.
- human review bypass: попытка отключить ручную проверку. Mapping: BLOCKED. Блокирует clean PASS: да.
- unsafe claim: утверждение с риском ложного завершения/одобрения. Mapping: BLOCKED или PASS_WITH_WARNINGS. Блокирует clean PASS: да.
- downstream scope absorption: claims о старте/выполнении M65-M67 на уровне M64 evidence. Mapping: BLOCKED. Блокирует clean PASS: да.

## 5. Evidence Integrity Result Values
- EVIDENCE_INTEGRITY_PASS
- EVIDENCE_INTEGRITY_PASS_WITH_WARNINGS
- EVIDENCE_INTEGRITY_BLOCKED
- EVIDENCE_INTEGRITY_NOT_ENOUGH_EVIDENCE

## 6. Evidence Checker Result Values
- M64_EVIDENCE_CHECK_PASS
- M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
- M64_EVIDENCE_CHECK_BLOCKED
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE

Mapping:
- EVIDENCE_INTEGRITY_PASS -> M64_EVIDENCE_CHECK_PASS
- EVIDENCE_INTEGRITY_PASS_WITH_WARNINGS -> M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
- EVIDENCE_INTEGRITY_BLOCKED -> M64_EVIDENCE_CHECK_BLOCKED
- EVIDENCE_INTEGRITY_NOT_ENOUGH_EVIDENCE -> M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE

Запрещено вводить результаты вида APPROVED/COMPLETED/MERGED/RELEASED.

## 7. Decision Priority Order
Порядок приоритета решения:
1. M64_EVIDENCE_CHECK_BLOCKED
2. M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE
3. M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
4. M64_EVIDENCE_CHECK_PASS

Правила:
- BLOCKED выше NOT_ENOUGH_EVIDENCE.
- NOT_ENOUGH_EVIDENCE выше PASS_WITH_WARNINGS.
- PASS_WITH_WARNINGS выше clean PASS.
- Warnings нельзя тихо превращать в clean PASS.
- Blockers нельзя понижать до warning.
- NOT_ENOUGH_EVIDENCE нельзя считать PASS.

## 8. BLOCKED Conditions
Возвращать `M64_EVIDENCE_CHECK_BLOCKED`, если есть хотя бы одно условие:
- missing/malformed evidence;
- missing required field или wrong type;
- unsupported `contract_version`;
- wrong `evidence_type`;
- `task_id` отсутствует или не совпадает с ожидаемым;
- `agent_identity` отсутствует;
- пустой `agent_identity.agent_name` или `agent_identity.agent_role`;
- `human_review_required=false` или поле отсутствует;
- `forbidden_actions_performed=true`;
- `non_authority_boundary` отсутствует или пуст;
- отсутствуют required non-authority statements;
- claim-категории: approval/merge/push/release/lifecycle mutation/автостарт M65-M67/completion gate passed;
- `blockers` непустой;
- `validation_results` содержит FAIL для required check;
- `commands_run` содержит FAIL для required command;
- hidden blocker high-confidence;
- claim task completion without human review.

Точный список фраз forbidden claims определяется в 64.4.

## 9. NOT_ENOUGH_EVIDENCE Conditions
Возвращать `M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE` только если нет BLOCKED.

Случаи:
- все evidence-bearing массивы пустые:
  - files_changed
  - created_artifacts
  - modified_artifacts
  - deleted_artifacts
  - commands_run
  - validation_results
- evidence слишком расплывчатый для структурной проверки;
- есть claims, но они не интерпретируются на уровне evidence;
- commands/validation results состоят только из `UNKNOWN`.

Обязательные утверждения:
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE is not approval.
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE must not be treated as PASS.
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE means human review lacks enough structured evidence.
- Human review remains required.

## 10. PASS_WITH_WARNINGS Conditions
Возвращать `M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS`, только если:
- нет BLOCKED;
- нет NOT_ENOUGH_EVIDENCE;
- остаются неблокирующие предупреждения.

Примеры:
- non-empty `known_limitations`;
- non-empty `warnings`, но без hidden blocker;
- `validation_results` есть, `commands_run` пуст (warning, не auto-block);
- `NOT_RUN` есть только для не-required command/check;
- неполная корреляция artifacts c `files_changed`, но есть объяснение;
- suspected stale evidence;
- ambiguous hidden blocker/ambiguous forbidden claim без подтверждения.

PASS_WITH_WARNINGS не является clean PASS и не является approval.

## 11. PASS Conditions
Возвращать `M64_EVIDENCE_CHECK_PASS` только если одновременно:
- evidence есть и парсится;
- required fields и field types валидны;
- `contract_version` поддерживается;
- `evidence_type` корректен;
- `task_id` есть и совпадает (если ожидаемое значение передано);
- `agent_identity` заполнен;
- структуры `commands_run` и `validation_results` валидны;
- `human_review_required=true`;
- `forbidden_actions_performed=false`;
- `non_authority_boundary` присутствует и включает required statements;
- нет claim-категорий approval/lifecycle/merge/push/release/M65-M67 absorption;
- нет blockers;
- нет conditions NOT_ENOUGH_EVIDENCE;
- нет warnings.

Clean PASS не равен одобрению задачи, а только означает структурную пригодность evidence на уровне M64.

## 12. Cross-Field Rules
- Если `validation_results` не пуст и `commands_run` пуст: результат `PASS_WITH_WARNINGS`, не BLOCKED, если нет других блокеров.
- Если `created_artifacts` не пуст, они должны быть в `files_changed` или должно быть объяснение в notes/limitations/warnings.
- Если `modified_artifacts` не пуст, они должны быть в `files_changed` или должно быть объяснение.
- Если `deleted_artifacts` не пуст, они должны быть в `files_changed` или должно быть объяснение.
- Если `blockers` не пуст, clean PASS запрещён.
- Если `warnings` не пуст, clean PASS запрещён.
- Если `forbidden_actions_performed=true`, результат BLOCKED.
- Если `human_review_required=false` или отсутствует, результат BLOCKED.
- Если все evidence-bearing массивы пусты, результат NOT_ENOUGH_EVIDENCE, если нет BLOCKED.

## 13. Command and Validation Result Semantics
Допустимые значения `commands_run.result` и `validation_results.result`:
- PASS
- FAIL
- NOT_RUN
- UNKNOWN

Смысл:
- PASS: агент заявляет, что команда/проверка прошла.
- FAIL: агент заявляет, что команда/проверка провалилась.
- NOT_RUN: агент заявляет, что команда/проверка не запускалась.
- UNKNOWN: агент не может дать надёжный результат.

Правила:
- FAIL для required command/check -> BLOCKED.
- NOT_RUN для required command/check -> BLOCKED или WARN по статусу обязательности.
- UNKNOWN-only evidence -> не может дать clean PASS.
- PASS остаётся claim до независимой проверки следующими слоями.

exit_code semantics:
exit_code: -1 means the command exit code is unknown or the command was not run.
- `exit_code=-1` + `NOT_RUN` не блокирует сам по себе.
- `exit_code=-1` + `UNKNOWN` не блокирует сам по себе, если команда не required.
- `exit_code=-1` + `PASS` это противоречие и не может дать clean PASS.
- `exit_code=-1` + `FAIL` для required команды может блокировать, иначе минимум warning.

M64 не подтверждает подлинность выполнения команд.
M65/M66 позже усиливают корреляцию команд и результатов.

## 14. Hidden Blocker Rule
Hidden blocker: блокирующее условие скрыто в warning/known_limitations/notes.

Если `blockers` пуст, но в `warnings`, `known_limitations`, `commands_run.notes` или `validation_results.notes` есть сигналы типа:
- blocked
- cannot proceed
- critical
- blocker
- unsafe
- failed required
- required check failed
- must fix
- not safe

то это candidate hidden blocker.

Mapping:
- high-confidence hidden blocker -> M64_EVIDENCE_CHECK_BLOCKED
- ambiguous hidden blocker -> M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
- no signal -> обычная логика

При нерешённых сигналах hidden blocker clean PASS запрещён.
Точная реализация детектора относится к 64.5.

## 15. Stale Evidence Rule
Stale evidence: данные могут не соответствовать текущему состоянию задачи.

Примеры:
- old task_id;
- obsolete artifact path;
- validation от прошлого запуска;
- ссылки на файлы вне текущего контекста;
- несогласованные timestamps/run identifiers (если есть).

Классификация:
- confirmed stale + влияет на required evidence -> BLOCKED
- suspected stale -> PASS_WITH_WARNINGS
- слишком расплывчато для вывода -> NOT_ENOUGH_EVIDENCE

Stale evidence не может дать clean PASS.

## 16. Contradictory Evidence Rule
Contradictory evidence: конфликт полей и заявлений.

Примеры:
- `blockers=[]`, но warnings описывают blocker;
- `forbidden_actions_performed=false`, но в тексте есть forbidden action;
- validation result PASS, но notes говорят failed;
- command result PASS при `exit_code=-1`;
- created_artifacts не коррелируют с files_changed без объяснения;
- `human_review_required=true`, но notes говорят review not required.

Mapping:
- confirmed contradiction в required evidence -> BLOCKED
- ambiguous contradiction -> PASS_WITH_WARNINGS
- minor optional contradiction -> PASS_WITH_WARNINGS

Contradictory evidence не может дать clean PASS.

## 17. Human Review Boundary
Agent evidence is claim.
Evidence integrity checks evaluate the claim structure and internal consistency.
Evidence integrity checks do not prove task completion.
Evidence integrity checks do not approve the task.
Human review remains required.

M64 evidence integrity is not acceptance criteria checking.
M64 evidence integrity is not git diff verification.
M64 evidence integrity is not command output authentication.
M64 evidence integrity is not completion gate integration.

Evidence integrity PASS is not approval.
Evidence integrity PASS does not complete the task.
Evidence integrity PASS does not replace human review.
Evidence integrity PASS does not authorize merge, push, or release.
Human review remains required.

## 18. Relationship to 64.4 Claim Boundary
64.3 задаёт категории claims и mapping результата целостности.
64.4 задаёт точную границу запрещённых claims и обязательные non-authority statements.
Этот документ не задаёт финальный phrase inventory.

## 19. Relationship to 64.5 Evidence Checker
64.3 задаёт decision semantics.
64.5 реализует checker (`scripts/check-agent-task-evidence.py`) и документ `docs/AGENT-TASK-EVIDENCE-CHECKER.md`.
Этот документ описывает поведение, но не содержит реализацию кода.

## 20. Relationship to M65-M67
M65 will define acceptance criteria checking.
M66 will define unified agent task validation runner.
M67 will define false PASS resistance and completion gate integration.

Разделение:
- M64: структура и внутренняя согласованность evidence.
- M65: выполнены ли требования задачи.
- M66: объединение M63+M64+M65+scope/diff.
- M67: усиление против false PASS на уровне полного пайплайна.

## 21. Non-Authority Boundary
M64 evidence integrity rules are not approval.
M64 evidence integrity rules do not replace human review.
M64 evidence integrity rules do not complete M64.
M64 evidence integrity rules do not start M65.
M64 evidence integrity rules do not validate completed agent tasks as a production gate.
M64 evidence integrity rules do not prove task completion.
M64 evidence integrity rules do not prove command execution authenticity.
M64 evidence integrity rules do not prove acceptance criteria satisfaction.
M64 evidence integrity rules do not create the evidence checker.
M64 evidence integrity rules do not create evidence fixtures.
M64 evidence integrity rules do not define acceptance criteria checking.
M64 evidence integrity rules do not create the unified agent task validation runner.
M64 evidence integrity rules do not create the false PASS resistance suite.
M64 evidence integrity rules do not integrate the completion gate.
M64 evidence integrity rules do not approve any agent task result.
M64 evidence integrity rules do not authorize merge, push, or release.
Human review remains required.

## 22. Final Status
FINAL_STATUS: M64_EVIDENCE_INTEGRITY_AND_DECISION_SEMANTICS_DEFINED_WITH_WARNINGS
