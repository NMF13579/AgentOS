# Thin Task Validation Decision Model

## 1. Purpose
Определить минимальную модель принятия решения для M62 MVP-проверки пакета результата задачи.

## 2. M62 Position in the Roadmap
M62 задаёт тонкий MVP-уровень валидации до полного контракта M63-M67.
M62 описывает минимальные решения по результату проверки и обязательную передачу на ручной обзор.

## 3. Dependency on MVP Input Contract
Зависимость: `docs/MVP-TASK-RESULT-INPUT-CONTRACT.md`.
Наблюдаемый статус входного контракта: `FINAL_STATUS: M62_MVP_TASK_RESULT_INPUT_CONTRACT_DEFINED`.

## 4. Decision Model Scope
Эта модель определяет только MVP-уровень классификации результатов.
Она не реализует runner в коде и не подменяет полную production-модель валидации.

## 5. Allowed Result Values
Допустимы только 4 значения:
- `TASK_VALIDATION_PASS`
- `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `TASK_VALIDATION_BLOCKED`
- `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`

Другие значения в 62.3 не допускаются.

## 6. Result Semantics
`TASK_VALIDATION_PASS`:
- означает, что в контролируемой MVP-области блокирующих нарушений не найдено;
- TASK_VALIDATION_PASS is not approval.
- TASK_VALIDATION_PASS does not complete the task.
- TASK_VALIDATION_PASS does not replace human review.
- TASK_VALIDATION_PASS does not authorize merge, push, or release.

`TASK_VALIDATION_PASS_WITH_WARNINGS`:
- означает, что блокеров нет, но есть предупреждения, отложенные проверки, неподдерживаемые необязательные проверки или некритичная неполнота;
- Warnings must be visible.
- Warnings must not be silently converted into clean PASS.
- PASS_WITH_WARNINGS is not approval.
- Human review remains required.

`TASK_VALIDATION_BLOCKED`:
- означает, что найдено блокирующее условие, которое мешает честной MVP-валидации.

`TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`:
- означает, что обязательные evidence-артефакты есть, но их недостаточно, они неполные, слабо связаны или не поддерживают честное MVP-решение;
- NOT_ENOUGH_EVIDENCE must not be treated as PASS.
- NOT_ENOUGH_EVIDENCE must not be converted into BLOCKED unless a blocking condition is also present.
- NOT_ENOUGH_EVIDENCE requires human review.

Приоритет решений:
1. BLOCKED conditions
2. NOT_ENOUGH_EVIDENCE conditions
3. PASS_WITH_WARNINGS conditions
4. PASS conditions

A blocker overrides all other outcomes.
NOT_ENOUGH_EVIDENCE applies only when no blocker exists.
PASS_WITH_WARNINGS applies only when no blocker and no not-enough-evidence condition exists.
PASS applies only when no blocker, no not-enough-evidence condition, and no warning exists.

## 7. Blocking Conditions
Блокирующие условия MVP (минимум):
- required task file missing;
- required evidence file missing;
- changed-files JSON missing;
- changed-files JSON malformed;
- changed-files JSON has absolute paths;
- changed-files JSON missing `changed_files` field;
- expected artifact missing;
- forbidden path changed;
- human_review_required is false;
- approval claim present;
- task completion approved claim present;
- human review not required claim present;
- merge authorized claim present;
- push authorized claim present;
- release authorized claim present;
- lifecycle mutation claim present;
- M63/M64/M65/M66/M67 artifact created early;
- runner cannot parse required input;
- MVP boundary violation.

Blocking conditions must produce TASK_VALIDATION_BLOCKED.

## 8. Warning Conditions
Предупреждающие условия MVP (минимум):
- optional field missing;
- known limitation declared;
- validation command claimed but not independently verified;
- unsupported optional check;
- `changed_files` is empty for validation-only example;
- deferred M63-M67 check;
- evidence contains minor ambiguity but required MVP fields exist.

Warning conditions may produce TASK_VALIDATION_PASS_WITH_WARNINGS only if no blocking condition exists.
Warnings must be visible in runner output.
Warnings must not be silently converted into TASK_VALIDATION_PASS.

## 9. Not-Enough-Evidence Conditions
Условия `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE` (минимум):
- evidence exists but task_id correlation is missing;
- evidence exists but summary_of_work is absent;
- evidence exists but declared_changed_files do not correlate with changed-files input;
- evidence exists but validation claims are too vague;
- evidence exists but known limitations prevent honest MVP validation;
- task brief exists but expected artifacts cannot be determined.

Not-enough-evidence conditions produce TASK_VALIDATION_NOT_ENOUGH_EVIDENCE when no blocking condition is present.
If a blocking condition is also present, TASK_VALIDATION_BLOCKED takes priority.

## 10. PASS Conditions
`TASK_VALIDATION_PASS` можно использовать только если одновременно:
- task file exists;
- evidence file exists;
- changed-files JSON exists and parses;
- changed-files entries are repository-relative;
- expected artifacts exist when declared;
- no forbidden paths are changed;
- human_review_required is true;
- no approval / lifecycle / merge / push / release claims are present;
- no M63-M67 artifacts are created early;
- no blocking condition exists;
- no warning condition exists.

`TASK_VALIDATION_PASS_WITH_WARNINGS` можно использовать только если:
- all required MVP inputs exist;
- no blocking condition exists;
- human_review_required is true;
- warnings exist and are reported.

## 11. Missing Evidence vs Not Enough Evidence
missing evidence = required evidence artifact absent → TASK_VALIDATION_BLOCKED
not enough evidence = evidence exists but is insufficient/uncorrelated → TASK_VALIDATION_NOT_ENOUGH_EVIDENCE

Примеры:
- `agent_evidence_path` указывает на отсутствующий файл → `TASK_VALIDATION_BLOCKED`
- evidence-файл есть, но не содержит `task_id` → `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`
- evidence-файл есть, но нет `summary_of_work` → `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`
- evidence-файл есть, но `human_review_required` равно `false` → `TASK_VALIDATION_BLOCKED`

## 12. Human Review Requirement
`human_review_required: true` обязательно для безопасной MVP-границы.
Отключение ручной проверки в M62 недопустимо.
Human review remains required.

## 13. Runner Responsibility Boundary
62.3 defines decision semantics only.
62.4 implements the MVP runner.
62.5 creates controlled fixtures.
62.6 verifies fixture outcomes.

The future MVP runner validates a packaged task result, not the entire live repository state.

## 14. Relation to M63-M67
M62 decision model is a thin MVP decision model.
M63 defines the full task validation contract.
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.

M62 decision model must not absorb M63-M67 responsibilities.

## 15. Non-Authority Boundary
M62 thin validation decision model is not approval.
M62 thin validation decision model does not replace human review.
M62 thin validation decision model does not complete the task.
M62 thin validation decision model does not validate completed agent tasks as a production gate.
M62 thin validation decision model does not create the MVP runner.
M62 thin validation decision model does not authorize merge, push, or release.
M62 thin validation decision model does not start M63.
Human review remains required.

## 16. Final Status
FINAL_STATUS: M62_THIN_VALIDATION_DECISION_MODEL_DEFINED
