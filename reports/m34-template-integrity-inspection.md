# M34 Template Integrity Inspection

## Summary
Проверка показала, что структура шаблонов в репозитории присутствует: есть минимальный и полный шаблон, есть отдельный скрипт проверки целостности шаблонов и есть тестовые фикстуры (фикстуры = заранее подготовленные тестовые примеры) для этой проверки. Основа для задачи 34.3.1 существует.

## Preconditions
- `reports/m34-release-readiness-intake.md` найден, маркер `M34_RELEASE_READINESS_INTAKE_COMPLETE` найден.
- `reports/m34-install-smoke-inspection.md` найден, маркер `M34_INSTALL_SMOKE_INSPECTION_COMPLETE` найден.
- `reports/m34-install-smoke-report.md` найден, маркер `M34_INSTALL_SMOKE_COMPLETE` найден.
- Классификация install smoke в отчёте 34.2.1 присутствует.

## Inspection Method
Использованы только read-only команды: `find`, `grep`, `test`, `ls`.
Проверялись:
- наличие каталогов шаблонов;
- состав каталогов минимального и полного шаблонов;
- наличие скрипта проверки целостности шаблонов;
- наличие тестовых материалов для проверки шаблонов;
- упоминания в документации и скриптах.

## Template Directories Found
- `templates/` — FOUND
- `templates/agentos-minimal/` — FOUND
- `templates/agentos-full/` — FOUND
- `templates/dist/minimal/` — FOUND
- `templates/dist/full/` — FOUND

## Minimal Template Structure
Обнаружены ключевые части минимального шаблона:
- `templates/agentos-minimal/README.md`
- `templates/agentos-minimal/requirements.txt`
- `templates/agentos-minimal/scripts/run-all.sh`
- `templates/agentos-minimal/scripts/validate-task.py`
- `templates/agentos-minimal/scripts/validate-verification.py`
- `templates/agentos-minimal/tasks/templates/*`
- `templates/agentos-minimal/reports/templates/*`
- `templates/agentos-minimal/templates/task.md`
- `templates/agentos-minimal/templates/verification.md`

## Full Template Structure
Обнаружены ключевые части полного шаблона:
- `templates/agentos-full/README.md`
- `templates/agentos-full/requirements.txt`
- `templates/agentos-full/scripts/run-all.sh`
- `templates/agentos-full/tasks/templates/*`
- `templates/agentos-full/reports/templates/*`
- `templates/agentos-full/docs/*`
- `templates/agentos-full/examples/*`
- `templates/agentos-full/.github/*`
- `templates/agentos-full/.githooks/*`

## Required Template Files Found
Найдены обязательные базовые файлы шаблонов:
- README
- requirements
- run-all
- task/report templates
- core scripts для базовой валидации

## Missing Template Files
На уровне структуры по текущей проверке критичных пропусков не выявлено.

## Full-Only Components in Minimal Template
Явных full-only компонентов в `templates/agentos-minimal/` не обнаружено.
`docs/`, `examples/`, `.github/`, `.githooks/` присутствуют в полном шаблоне и не найдены в минимальном.

## Template Validation Commands Found
Найдены:
- `scripts/check-template-integrity.py`
- `scripts/run-all.sh`
- `scripts/agentos-validate.py`
- `scripts/test-install.sh`

Также найдены связанные проверки/обвязка:
- `scripts/test-template-integrity-fixtures.py`
- `scripts/test-negative-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/audit-template-packaging.py`

## Existing Template Integrity Checker
- `scripts/check-template-integrity.py` — FOUND
- В документах есть явные ссылки на запуск strict-режима.
- В тестовых фикстурах есть наборы для негативных/пограничных кейсов.

## Template Integrity Readiness Classification
- templates directory: READY_FOR_CHECKER
- minimal template: READY_FOR_CHECKER
- full template: READY_FOR_CHECKER
- minimal required files: PARTIALLY_READY
- full required files: PARTIALLY_READY
- template scripts: READY_FOR_CHECKER
- template docs: PARTIALLY_READY
- task templates: READY_FOR_CHECKER
- report templates: READY_FOR_CHECKER
- validation scripts: READY_FOR_CHECKER
- install scripts: PARTIALLY_READY
- example project compatibility: PARTIALLY_READY
- template integrity checker: READY_FOR_CHECKER
- template integrity fixtures: READY_FOR_CHECKER
- template integrity docs: READY_FOR_CHECKER

## Template Integrity Risks
- Есть риск ложного ощущения готовности, если проверка структуры проходит, но install smoke/пример проекта остаются с пробелами.
- В части “PARTIALLY_READY” нужна доработка критериев для однозначного PASS/FAIL по M34.

## Recommended Scope for 34.3.1
Рекомендуемая область для 34.3.1: доработка уже существующего чекера целостности шаблонов и его тестовой обвязки без изменения самих шаблонов.

## Files Allowed for 34.3.1
- `scripts/check-template-integrity.py`
- `scripts/test-template-integrity-fixtures.py`
- `scripts/audit-template-packaging.py`
- `tests/fixtures/template-integrity/valid-template/INIT.md`
- `tests/fixtures/template-integrity/missing-core-file/INIT.md`
- `tests/fixtures/template-integrity/forbidden-auto-runner/INIT.md`
- `tests/fixtures/template-integrity/missing-gitignore-drafts/INIT.md`
- `tests/fixtures/template-integrity/missing-fixtures-warning/INIT.md`
- `tests/fixtures/template-integrity/missing-optional-report-warning/INIT.md`

## Files Forbidden for 34.3.1
- `templates/agentos-minimal/**`
- `templates/agentos-full/**`
- `templates/dist/**`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`
- `data/context-index.json`
- `tasks/active-task.md`
- любые M33 отчёты
- текущий отчёт 34.3.0

## Potential New Files Requiring Human Decision
- `tests/fixtures/template-integrity/missing-minimal-readme/INIT.md`
- `tests/fixtures/template-integrity/minimal-contains-full-only/INIT.md`
- `tests/fixtures/template-integrity/full-missing-examples-readme/INIT.md`

## Validation Evidence
Использованы команды:
- `find templates -maxdepth 5 -type f | sort`
- `find templates -maxdepth 5 -type d | sort`
- `find scripts -maxdepth 3 -type f | sort`
- `find examples -maxdepth 4 -type f | sort`
- `find docs -maxdepth 3 -type f | sort`
- `find tests -maxdepth 4 -type f | sort`
- `test -d templates`
- `test -d templates/agentos-minimal`
- `test -d templates/agentos-full`
- `test -f scripts/check-template-integrity.py`
- `grep -R "agentos-minimal" ...`
- `grep -R "agentos-full" ...`
- `grep -R "template integrity" ...`
- `grep -R "check-template-integrity" ...`
- `grep -R "minimal template" ...`
- `grep -R "full template" ...`
- `ls scripts/check-template-integrity.py`
- `ls scripts/run-all.sh`
- `ls scripts/agentos-validate.py`
- `ls scripts/test-install.sh`

## Known Gaps
- В этой задаче не запускались реальный install smoke и внешние сценарии (это отдельно по плану M34).
- Классификация `PARTIALLY_READY` требует явных проходных критериев в 34.3.1.
- Для некоторых новых негативных фикстур может потребоваться отдельное человеческое решение по добавлению новых путей.

## Final Status
M34_TEMPLATE_INTEGRITY_INSPECTION_COMPLETE
