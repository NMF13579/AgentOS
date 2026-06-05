# M61 Hardening Regression Runner

## 1. Purpose
Определить M61-уровень регрессионной оркестрации (оркестрация = координация уже существующих проверок) для проверки согласованности M60/M61 hardening-артефактов после 61.5.

## 2. Runner Role
scripts/check-m61-hardening-regression.py is an orchestration runner over M60/M61 hardening checks.
It does not create new task acceptance authority.
It does not approve completion.
It does not replace existing M60 checkers.
It aggregates and verifies existing hardening evidence.

## 3. Inputs Checked
Runner проверяет наличие/валидность:
- M60 completion/evidence/action/integration artifacts
- M61 intake/architecture/risk-map/plan/gap-map/repair-report
- required boundary lines in M61 repair report

## 4. Checks Performed
- наличие обязательных артефактов
- наличие `FINAL_STATUS:` в обязательных markdown-источниках
- парсинг `reports/m60-cleanup-action-review.json`
- проверка boundary-полей в `reports/m61-checker-repair-report.md`
- попытка безопасного вызова M60 checker’ов (`--help`, `--json`)

## 5. Premature Artifact Detection
Runner блокирует ранние M61 файлы:
- `reports/m61-hardening-integration-summary.md`
- `reports/m61-hardening-action-review.json`
- `reports/m61-hardening-evidence-report.md`
- `reports/m61-completion-review.md`

## 6. M62 Artifact Detection
Runner блокирует любые обнаруженные M62 acceptance artifacts, включая:
- `scripts/check-agent-task-result.py`
- `scripts/check-task-acceptance.py`
- `schemas/task-result.schema.json`
- `schemas/agent-evidence.schema.json`
- `docs/TASK-VALIDATION-CONTRACT.md`
- `docs/TASK-OUTPUT-EVIDENCE-MODEL.md`
- `docs/ACCEPTANCE-CRITERIA-CHECKER.md`
и любые пути с `m62` в контролируемых директориях.

## 7. Result Values
- `M61_HARDENING_REGRESSION_PASS`
- `M61_HARDENING_REGRESSION_PASS_WITH_WARNINGS`
- `M61_HARDENING_REGRESSION_BLOCKED`

## 8. Exit Codes
- `0`: PASS или PASS_WITH_WARNINGS
- `1`: BLOCKED
- `2`: malformed input / runner error / unsafe state

## 9. JSON Output Contract
`--json` возвращает объект минимум с полями:
- `result`
- `strict`
- флаги `*_checked` для M60/M61 обязательных артефактов
- `registry_checker_result`
- `reusable_chain_checker_result`
- `regression_runner_result`
- `premature_m61_artifacts_found`
- `premature_m62_artifacts_found`
- `m62_artifacts_found`
- `task_acceptance_logic_found`
- `human_review_required`
- `warnings`
- `blockers`

Если optional checker нельзя безопасно вызвать или распарсить, runner пишет warning и использует `NOT_RUN_UNSUPPORTED`.

## 10. Non-Authority Boundary
M61 hardening regression runner is not approval.
M61 hardening regression runner does not start M62.
M61 hardening regression runner does not validate completed agent tasks as a production gate.
M61 hardening regression runner does not define task acceptance semantics.
M61 hardening regression runner does not mutate lifecycle state.
M61 hardening regression runner does not authorize merge, push, or release.
Human review remains required.

## 11. Limitations
- Runner read-only и не чинит данные.
- Runner не создаёт отчёты автоматически.
- Unsupported optional checker calls дают warnings, а не PASS.
- Этот runner не является authority-слоем и не заменяет решения человека.

## 12. Final Status
FINAL_STATUS: M61_HARDENING_REGRESSION_RUNNER_DEFINED
