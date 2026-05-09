# M34 Example Scenarios Inspection

## Summary
В репозитории уже есть набор практических сценариев в `examples/` и `examples/scenarios/`. Базовое покрытие есть, но отдельные категории про context pack (пропущенный/пустой) и completion review как явный сценарий описаны неполно.

## Preconditions
- `reports/m34-release-readiness-intake.md` + `M34_RELEASE_READINESS_INTAKE_COMPLETE`: PASS
- `reports/m34-documentation-hardening-report.md` + `M34_DOCUMENTATION_HARDENING_COMPLETE`: PASS

## Inspection Method
Read-only проверка через `test`, `find`, `grep`.

## Example Directories Found
- `examples/` — FOUND
- `examples/scenarios/` — FOUND

## Scenario Files Found
- `examples/README.md`
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`
- `examples/scenarios/simple-docs-change.md`
- `examples/scenarios/risky-deploy-change.md`
- `examples/scenarios/failed-verification.md`
- `examples/scenarios/dangerous-command-detected.md`
- `examples/scenarios/handoff-between-sessions.md`
- `examples/scenarios/repeated-feedback-detected.md`
- `examples/simple-project/README.md`

## Scenario Files Missing
Нет явных отдельных сценариев с названиями:
- missing-context-pack
- empty-context-pack
- completion-review-decision

## Existing Scenario Coverage
- simple documentation change: есть (`examples/scenarios/simple-docs-change.md`)
- risky change blocked: есть (`examples/scenarios/risky-deploy-change.md`, `dangerous-command-detected.md`)
- missing Context Pack: частично (есть правила в docs, но нет явного сценария-файла)
- empty Context Pack: не найден явный сценарий-файл
- failed validation: есть (`examples/scenarios/failed-verification.md`)
- human gate required: частично (упоминания и related scenarios есть)
- completion review: частично (есть ссылки в docs/reports, но нет явного сценария-файла)
- install/template usage: есть (`examples/simple-project/README.md`, `scenario-04-validation-only.md`)
- MVP readiness workflow: частично (границы есть, но отдельный end-to-end сценарий M34 не явный)

## Scenario Readiness Classification
- simple documentation change: READY_FOR_SCENARIO
- risky change blocked: READY_FOR_SCENARIO
- missing Context Pack: PARTIALLY_READY
- empty Context Pack: MISSING
- failed validation: READY_FOR_SCENARIO
- human gate required: PARTIALLY_READY
- TUI / status BLOCKED explanation: PARTIALLY_READY
- completion review: PARTIALLY_READY
- install smoke example: READY_FOR_SCENARIO
- template usage example: PARTIALLY_READY
- MVP readiness example: PARTIALLY_READY
- known limitations example: PARTIALLY_READY

## Missing Scenario Categories
- Явный сценарий missing Context Pack с ожидаемым `BLOCKED`.
- Явный сценарий empty Context Pack с ожидаемым `BLOCKED`.
- Явный сценарий completion review decision path для M34.

## Recommended Scope for 34.6.1
Усилить существующие сценарии и (если разрешат) добавить узкие сценарии для missing/empty context, human gate и completion review без изменения runtime-логики.

## Files Allowed for 34.6.1
- `examples/README.md`
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`
- `examples/scenarios/simple-docs-change.md`
- `examples/scenarios/risky-deploy-change.md`
- `examples/scenarios/failed-verification.md`
- `examples/scenarios/dangerous-command-detected.md`
- `examples/scenarios/handoff-between-sessions.md`
- `examples/scenarios/repeated-feedback-detected.md`
- `examples/simple-project/README.md`

## Files Forbidden for 34.6.1
- `scripts/**`
- `templates/**`
- `docs/**`
- `prompts/**`
- `tasks/active-task.md`
- любые M33 отчёты
- любые M34 отчёты, кроме нового отчёта задачи 34.6.1
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`

## Potential New Files Requiring Human Decision
- `examples/scenarios/missing-context-pack.md`
- `examples/scenarios/empty-context-pack.md`
- `examples/scenarios/completion-review-decision.md`
- `examples/scenarios/human-gate-required.md`

## Required Behavior for 34.6.1
Future 34.6.1 should include in each scenario:
- user request
- task contract or task summary
- expected context
- expected gate
- expected validation
- possible failure
- correct result
- what user should see
- what AgentOS must not claim

Future scenarios must not claim:
- production-grade safety
- bug-free AI output
- autonomous execution without human gate
- release readiness without M34 evidence report
- approval when approval does not exist
- execution allowed without valid Context Pack

Future 34.6.1 may only:
- use exact files listed in `Files Allowed for 34.6.1`
- create/update scenario files only if explicitly allowed
- show practical examples without overstating maturity
- include known limitations and non-claims
- avoid claiming MVP readiness from scenarios alone

Future 34.6.1 must not:
- create product marketing examples
- hide known gaps
- modify install flow
- modify templates
- modify scripts
- claim release readiness without M34 evidence report and completion review

## Validation Evidence
Команды:
- `test -d examples`
- `test -d examples/scenarios`
- `find examples -maxdepth 5 -type f | sort`
- `find docs -maxdepth 3 -type f | sort`
- `find templates -maxdepth 4 -type f | sort`
- `find prompts -maxdepth 3 -type f | sort`
- `grep -R "scenario" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "simple docs" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "risky" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "Context Pack" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "No Context Pack" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "failed validation" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "human gate" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "completion review" -n README.md docs examples templates prompts reports/m34-*.md`
- `grep -R "MVP readiness" -n README.md docs examples templates prompts reports/m34-*.md`

## Known Gaps
- Не хватает явных сценариев про missing/empty context pack.
- Completion review как отдельный сценарий явно не оформлен.
- Сценарии не заменяют M34 evidence report и completion review.

## Final Status
M34_EXAMPLE_SCENARIOS_INSPECTION_COMPLETE
