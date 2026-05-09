# M34 Install Smoke Report

## Summary
Проведён install smoke в рамках разрешённого scope. Базовая установка в временный git-проект работает, но есть функциональный разрыв в example smoke и общий результат классифицируется как `INSTALL_SMOKE_PASS_WITH_GAPS`.

## Preconditions
Проверки выполнены успешно:
- `reports/m34-release-readiness-intake.md` содержит `M34_RELEASE_READINESS_INTAKE_COMPLETE`
- `reports/m34-install-smoke-inspection.md` содержит `M34_INSTALL_SMOKE_INSPECTION_COMPLETE`
- в inspection-отчёте есть секция `Files Allowed for 34.2.1`

## Inspection Report Used
- `reports/m34-install-smoke-inspection.md`

## Files Allowed by 34.2.0
- `install.sh`
- `scripts/test-install.sh`
- `scripts/test-example-project.sh`
- `scripts/run-all.sh`
- `scripts/agentos-validate.py`
- `scripts/check-template-integrity.py`
- `examples/simple-project/README.md`
- `examples/simple-project/run-example.sh`
- `docs/quickstart.md`
- `docs/RU-QUICKSTART.md`
- `docs/usage.md`
- `docs/release-checklist.md`
- `reports/m34-install-smoke-implementation.md`

## Files Modified
- `reports/m34-install-smoke-report.md`

## Smoke Scenarios Attempted
- minimal template install into temporary git project
- example project install+run+validation path
- local `run-all.sh`
- local `agentos-validate.py all`
- local `audit-agentos.py`

## Temporary Project Behavior
Временные директории создавались внутри smoke-скриптов. Установка выполнялась в disposable (одноразовом) окружении; в рабочем репозитории прямых мутаций от smoke-скриптов не зафиксировано.

## Install Script Result
Команда: `bash scripts/test-install.sh || true`
Результат: PASS
Ключевые маркеры:
- `PASS: AgentOS template installed`
- `PASS: install smoke test passed`

## Minimal Template Result
Команда: `bash scripts/test-install.sh || true`
Результат: PASS
Минимальный набор файлов был установлен в fresh temp project и прошёл базовую проверку сценария скрипта.

## Full Template Result
В этом запуске full-template сценарий отдельной командой не запускался. Статус: NOT_RUN (в рамках имеющихся скриптов не выделен как отдельная успешная ветка).

## Example Project Result
Команда: `bash scripts/test-example-project.sh || true`
Результат: FAIL
Наблюдение:
- `PASS: task validation passed`
- `FAIL: verification validation failed`
- ошибка YAML/markdown структуры verification:
  `mapping values are not allowed here ... line 6 column 10 proof: "TODO"`

## Validation Command Result
Команда: `python3 scripts/agentos-validate.py all || true`
Результат: FAIL
Маркеры:
- `Overall result: FAIL`
- `Checks run: 3`
- `Failed checks: 1`
- `Human action required: YES`

## Run-All Result
Команда: `bash scripts/run-all.sh || true`
Результат: FAIL
Причина: `tasks/active-task.md` не проходит текущую schema validation (additional properties not allowed).

## Generated Files Impact
По итогам smoke-исполнения в рабочем дереве не появилось новых обязательных production-артефактов установки. Основные изменения в репозитории остаются историческими/предсуществующими; текущая задача добавила только этот отчёт.

## Install Smoke Classification
`INSTALL_SMOKE_PASS_WITH_GAPS`

Обоснование:
- core install path (минимальная установка) работает;
- но example smoke и unified validation показывают реальные проблемы;
- есть известные наследуемые gaps из M33/M34, влияющие на итог.

## Known Gaps
- example project smoke не проходит из-за ошибки в verification-файле сценария.
- `run-all.sh` падает на schema mismatch active-task формата.
- `agentos-validate.py all` даёт FAIL (1 критичный failing check).
- в задаче не подтверждён отдельный full-template smoke PASS.

## Release Readiness Impact
Итог install smoke подтверждает работоспособность базового install-пути, но не даёт оснований заявлять release-ready состояние. Требуется закрытие выявленных gaps в следующих scoped задачах.

## Validation Evidence
До изменений:
- `test -f reports/m34-install-smoke-inspection.md`
- `grep -q "M34_INSTALL_SMOKE_INSPECTION_COMPLETE" reports/m34-install-smoke-inspection.md`
- `grep -q "Files Allowed for 34.2.1" reports/m34-install-smoke-inspection.md`

После изменений:
- `test -f reports/m34-install-smoke-report.md`
- `grep -q "M34_INSTALL_SMOKE_COMPLETE" reports/m34-install-smoke-report.md`
- `grep -q "Install Smoke Classification" reports/m34-install-smoke-report.md`
- `grep -Eq "INSTALL_SMOKE_PASS|INSTALL_SMOKE_PASS_WITH_GAPS|INSTALL_SMOKE_FAIL|INSTALL_SMOKE_BLOCKED|INSTALL_SMOKE_INCONCLUSIVE" reports/m34-install-smoke-report.md`
- `grep -q "Known Gaps" reports/m34-install-smoke-report.md`
- `grep -q "Release Readiness Impact" reports/m34-install-smoke-report.md`
- `git diff --check`
- `git status --short`

Команды smoke/validation:
- `bash scripts/test-install.sh || true` -> PASS
- `bash scripts/test-example-project.sh || true` -> FAIL
- `bash scripts/run-all.sh || true` -> FAIL
- `python3 scripts/agentos-validate.py all || true` -> FAIL
- `python3 scripts/audit-agentos.py || true` -> PASS_WITH_WARNINGS

## Final Status
`M34_INSTALL_SMOKE_COMPLETE`
