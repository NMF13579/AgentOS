# M34 Install Smoke Inspection

## Summary
Проведена read-only проверка готовности к внешнему install smoke (проверка установки) и example-project smoke (проверка примера проекта). Базовая структура для smoke уже есть, но есть риски и пробелы из M33, которые влияют на честную release readiness (готовность к выпуску).

## Preconditions
Проверки выполнены успешно:
- `reports/m34-release-readiness-intake.md` существует
- найден маркер `M34_RELEASE_READINESS_INTAKE_COMPLETE`
- найдено `M34 = installable + understandable + auditable + honest`

## Inspection Method
- Использованы только read-only команды: `find`, `grep`, `test`, `ls`.
- install/example smoke не запускались.
- внешние копии проектов не создавались.

## Repository Structure Inspected
Проверены:
- `scripts/`
- `templates/`
- `examples/`
- `docs/`
- `prompts/`
- `.github/`
- `README.md`, `CHANGELOG.md`, `VERSION`, `requirements.txt`, `pyproject.toml`

## Install Scripts Found
Найдено:
- `install.sh` (корневой installer)
- `scripts/test-install.sh`
- `scripts/test-example-project.sh`
- `scripts/install-hooks.sh`

## Templates Found
Найдено:
- минимальный template: `templates/agentos-minimal/*`
- полный template: `templates/agentos-full/*`
- distributable templates: `templates/dist/minimal/*`, `templates/dist/full/*`
- template validation entrypoint: `scripts/check-template-integrity.py`

## Examples Found
Найдено:
- `examples/simple-project/README.md`
- `examples/simple-project/run-example.sh`
- сценарные примеры в `examples/scenarios/*.md`
- общий индекс примеров: `examples/README.md`

## Quickstart / Installation Docs Found
Найдено:
- `docs/quickstart.md`
- `docs/RU-QUICKSTART.md`
- `docs/usage.md`
- `README.md`
- `docs/release-checklist.md`
- `docs/TEMPLATE-PACKAGING-AUDIT.md`

## Validation Commands Found
Найдено:
- `scripts/run-all.sh`
- `scripts/agentos-validate.py`
- `scripts/audit-agentos.py`
- `scripts/check-template-integrity.py`
- `scripts/test-install.sh`
- `scripts/test-example-project.sh`

## External Smoke Readiness Classification
- install script: `READY_FOR_SMOKE`
- minimal template: `READY_FOR_SMOKE`
- full template: `READY_FOR_SMOKE`
- example project: `READY_FOR_SMOKE`
- quickstart docs: `READY_FOR_SMOKE`
- installation docs: `READY_FOR_SMOKE`
- validation command: `READY_FOR_SMOKE`
- run-all command: `PARTIALLY_READY`
- template integrity command: `READY_FOR_SMOKE`
- external project smoke command: `READY_FOR_SMOKE`
- example smoke command: `READY_FOR_SMOKE`
- known limitations docs: `READY_FOR_SMOKE`
- release checklist docs: `READY_FOR_SMOKE`

## Missing Install Readiness Pieces
Явно отсутствует:
- `pyproject.toml` (если нужен Python packaging путь как отдельный канал дистрибуции)

Не отсутствует, но требует проверки в 34.2.1:
- устойчивость `run-all.sh` в “чистой внешней копии” при текущем формате `tasks/active-task.md`

## Release Readiness Risks
- M33 gap: `CONTEXT_PIPELINE_STILL_BLOCKED`.
- M33 gap: `run-all.sh` может падать на schema mismatch `tasks/active-task.md`.
- M33 gap: `scripts/test-negative-fixtures.sh` отсутствует.
- M33 gap: неполный wiring части негативных сценариев.
- Риск расхождения между documented install path и фактическим поведением в внешнем проекте.

## Recommended Scope for 34.2.1
Сделать узкий шаг: подтвердить install/example smoke в контролируемом сценарии без изменения production-логики, с честной фиксацией PASS/FAIL/WARN и переносом M33 gaps как release constraints (ограничения выпуска).

## Files Allowed for 34.2.1
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

## Files Forbidden for 34.2.1
- `tasks/active-task.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`
- `scripts/check-context-pipeline.py`
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`
- `tests/`
- `templates/agentos-minimal/tasks/active-task.md`
- `templates/agentos-full/tasks/active-task.md`

## Potential New Files Requiring Human Decision
- `scripts/test-install-external-copy.sh`
- `scripts/test-example-project-external-copy.sh`
- `reports/m34-install-smoke-results.md`

## Validation Evidence
Команды, выполненные в задаче:
- precondition checks (`test -f` + `grep -q`)
- `find scripts -maxdepth 3 -type f | sort`
- `find templates -maxdepth 4 -type f | sort`
- `find examples -maxdepth 4 -type f | sort`
- `find docs -maxdepth 3 -type f | sort`
- `find prompts -maxdepth 3 -type f | sort`
- `find .github -maxdepth 4 -type f | sort`
- `test -f README.md|VERSION|CHANGELOG.md|requirements.txt|pyproject.toml`
- `grep -R "install|quickstart|template|example|smoke|run-all|validate" ...`
- `ls scripts/run-all.sh scripts/agentos-validate.py scripts/audit-agentos.py scripts/check-template-integrity.py scripts/test-install.sh scripts/test-example-project.sh`
- `test -f install.sh`

## Known Gaps
- Внешний smoke (в отдельной копии проекта) ещё не подтверждён запуском в M34 (эта задача была только inspection).
- Есть наследуемые M33 gaps, влияющие на release readiness.
- Нет `pyproject.toml` как альтернативного packaging entrypoint.

## Final Status
`M34_INSTALL_SMOKE_INSPECTION_COMPLETE`

## Required Behavior for Future 34.2.1
34.2.1 может только:
- использовать exact paths из секции `Files Allowed for 34.2.1`;
- реализовывать install smoke только в разрешённом scope;
- запускать smoke только после явного определения сценария;
- не менять templates без явного разрешения;
- не заявлять release readiness только по install smoke.

34.2.1 не должна:
- тихо создавать новый packaging system;
- строить full product packaging;
- создавать web UI;
- создавать server/cloud platform;
- массово переписывать templates;
- заявлять, что AgentOS release-ready, без M34 evidence report и completion review.
