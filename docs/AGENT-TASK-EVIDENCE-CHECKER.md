# Agent Task Evidence Checker

## 1. Purpose
Документ описывает read-only checker, который проверяет один JSON evidence-файл по правилам M64.

checker_scope: agent_task_output_evidence_checker
checker_path: scripts/check-agent-task-evidence.py
schema_path: schemas/agent-task-output-evidence.schema.json
contract_path: docs/AGENT-TASK-OUTPUT-EVIDENCE-CONTRACT.md
integrity_rules_path: docs/AGENT-EVIDENCE-INTEGRITY-RULES.md
claim_boundary_path: docs/AGENT-EVIDENCE-CLAIM-BOUNDARY.md
implements_evidence_checker: true
creates_evidence_fixtures: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. M64 Position in the Roadmap
M64 checker проверяет структуру, базовую целостность и границы claims в evidence.
M65/M66/M67 остаются отдельными этапами.

## 3. CLI Usage
```bash
python3 scripts/check-agent-task-evidence.py --evidence <path> --json
python3 scripts/check-agent-task-evidence.py --evidence <path> --task-id <expected-task-id> --json
python3 scripts/check-agent-task-evidence.py --evidence <path> --strict --json
```

## 4. Input Contract
Вход: один JSON-файл evidence.
Обязательны все top-level поля M64 контракта, константы, типы и required non-authority statements.

## 5. Result Values
- `M64_EVIDENCE_CHECK_PASS`
- `M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS`
- `M64_EVIDENCE_CHECK_BLOCKED`
- `M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE`

## 6. Exit Codes
- `0`: PASS или PASS_WITH_WARNINGS
- `1`: BLOCKED или NOT_ENOUGH_EVIDENCE
- `2`: ошибка CLI/внутренняя ошибка checker

## 7. JSON Output Contract
При `--json` выводится JSON со стабильными полями:
- `result`
- `evidence_checked`
- `evidence_json_valid`
- `required_fields_present`
- `required_field_types_valid`
- `contract_version_supported`
- `evidence_type_supported`
- `task_id_check_performed`
- `task_id_match`
- `agent_identity_valid`
- `commands_run_valid`
- `validation_results_valid`
- `human_review_required`
- `forbidden_actions_performed`
- `non_authority_boundary_present`
- `required_non_authority_statements_present`
- `forbidden_claims_found`
- `hidden_blocker_candidate_found`
- `not_enough_evidence`
- `m65_m67_scope_absorption_found`
- `strict`
- `warnings`
- `blockers`

`task_id_check_performed`: true только если передан `--task-id`.
`task_id_match`: `null`, если `--task-id` не передан.

## 8. Field Validation Behavior
Checker валидирует:
- required fields
- required const values
- базовые типы полей
- bool-строгость (`true/false`, не `1/0`)

Нарушения -> `M64_EVIDENCE_CHECK_BLOCKED`.

## 9. Agent Identity Checks
Проверяется `agent_identity`:
- объект
- `agent_name` непустая строка
- `agent_role` непустая строка
- нет лишних ключей

## 10. Command Evidence Checks
Проверяются элементы `commands_run`:
- объект с полями `command`, `purpose`, `exit_code`, `result`, `notes`
- `result` из `PASS|FAIL|NOT_RUN|UNKNOWN`
- `exit_code >= -1`
- `exit_code = -1` трактуется как unknown/not-run контекст
- `exit_code=-1` + `PASS` не даёт clean PASS

## 11. Validation Result Checks
Проверяются элементы `validation_results`:
- объект с полями `check_name`, `result`, `notes`
- `result` из `PASS|FAIL|NOT_RUN|UNKNOWN`
- `FAIL`/`NOT_RUN` для явно required check может блокировать

## 12. Cross-Field Rules
Реализованы правила:
- `validation_results` не пуст и `commands_run` пуст -> warning (не авто-block)
- неполная корреляция artifact-массивов с `files_changed` -> warning
- `blockers`/`warnings` не позволяют clean PASS
- `human_review_required=false` или `forbidden_actions_performed=true` -> BLOCKED
- пустые evidence-bearing массивы -> NOT_ENOUGH_EVIDENCE (если нет block)

## 13. Forbidden Claim Detection
Checker рекурсивно сканирует строковые значения.
Безопасные контексты (safe-context), например `non_authority_boundary` и policy-фразы с `must not/does not/is not`, не считаются affirmative claims сами по себе.
Явные запрещённые claims вне safe-context -> BLOCKED.
Неоднозначные -> warnings.

## 14. Hidden Blocker Detection
Checker ищет скрытые блокеры в `known_limitations`, `warnings`, `blockers`, `commands_run.notes`, `validation_results.notes`, `non_authority_boundary`.
High-confidence сигналы -> BLOCKED.
Неоднозначные сигналы -> PASS_WITH_WARNINGS.

## 15. NOT_ENOUGH_EVIDENCE Behavior
`M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE` возвращается, когда нет блокеров и evidence-данных недостаточно (например, все evidence-bearing массивы пустые или UNKNOWN-only).

## 16. Strict Mode
`--strict` не добавляет approval-смыслов.
`--strict` не понижает BLOCKED и не превращает NOT_ENOUGH_EVIDENCE в PASS.
Используется для более заметной маркировки неоднозначных рисков.

## 17. Human Review Boundary
Checker требует `human_review_required=true`.
Checker не утверждает, что задача одобрена или завершена.
Human review remains required.

## 18. Relationship to 64.2 Schema
64.2 определяет структуру schema/contract.
64.5 реализует практическую проверку этой структуры в runtime.

## 19. Relationship to 64.3 Integrity Rules
64.3 задаёт семантику целостности и приоритеты решения.
64.5 реализует эту семантику в коде checker.

## 20. Relationship to 64.4 Claim Boundary
64.4 задаёт границу запрещённых claims и safe-context правила.
64.5 применяет эти правила для детектирования claim-рисков.

## 21. Relationship to 64.6 Fixtures
64.6 создаёт fixture-наборы.
64.5 не создаёт fixtures.

## 22. Relationship to M65-M67
M65: acceptance criteria checking.
M66: unified runner.
M67: false PASS resistance + completion gate integration.
M64 checker не поглощает эти ответственности.

## 23. Non-Authority Boundary
M64 evidence checker is not approval.
M64 evidence checker does not replace human review.
M64 evidence checker does not complete M64.
M64 evidence checker does not start M65.
M64 evidence checker does not validate completed agent tasks as a production gate.
M64 evidence checker does not prove task completion.
M64 evidence checker does not prove command execution authenticity.
M64 evidence checker does not prove acceptance criteria satisfaction.
M64 evidence checker does not create evidence fixtures.
M64 evidence checker does not define acceptance criteria checking.
M64 evidence checker does not create the unified agent task validation runner.
M64 evidence checker does not create the false PASS resistance suite.
M64 evidence checker does not integrate the completion gate.
M64 evidence checker does not approve any agent task result.
M64 evidence checker does not authorize merge, push, or release.
Human review remains required.

## 24. Final Status
FINAL_STATUS: M64_EVIDENCE_CHECKER_DEFINED_WITH_WARNINGS
