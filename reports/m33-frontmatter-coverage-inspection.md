## Summary

Выполнен только read-only осмотр frontmatter (frontmatter = верхний YAML-блок между `---`).
Ремонта frontmatter не делалось.

## Preconditions

- `test -f reports/m33-p0-stabilization-findings-intake.md` -> passed
- `grep -q "M33_P0_FINDINGS_INTAKE_COMPLETE" reports/m33-p0-stabilization-findings-intake.md` -> passed
- `test -f reports/m33-status-layer-inspection.md` -> passed
- `grep -q "M33_STATUS_LAYER_INSPECTION_COMPLETE" reports/m33-status-layer-inspection.md` -> passed
- `test -f reports/m33-context-status-mapping.md` -> passed
- `grep -q "M33_CONTEXT_STATUS_MAPPING_COMPLETE" reports/m33-context-status-mapping.md` -> passed

## Inspection Method

- `find . -name "*.md" -not -path "./.git/*" | sort`
- Python read-only классификация:
  - наличие frontmatter
  - корректность закрывающего блока `---`
  - минимальная полнота полей для `tasks/*` и канонических `*/MAIN.md`
- Проверка влияния на контекст:
  - `cat data/context-index.json`
  - `cat reports/context-pack.md`
  - `cat reports/context-selection-record.md`
  - `cat reports/context-pipeline.json`
- Дополнительно: `python3 scripts/validate-frontmatter.py || true` (без аргумента -> usage error, это зафиксировано как факт)

## Directories Inspected

- `docs/`
- `tasks/`
- `templates/`
- `reports/`
- `memory-bank/`
- `handoff/`
- `workflow/`
- `quality/`
- `security/`
- `core-rules/`
- `state/`

## Directories Missing

- отсутствующих из целевого списка нет

## Required Frontmatter Standard Found

База стандарта найдена:
- `docs/FRONTMATTER-STANDARD.md`
- `docs/M28-CONTEXT-FRONTMATTER-STANDARD.md`
- `templates/context-frontmatter-example.md`

## Total Markdown Files

- всего `.md`: `2121`
- в целевом наборе директорий: `324`

## Valid Frontmatter Files

Категория: `VALID_FRONTMATTER`

- количество: `79`
- примеры:
  - `core-rules/MAIN.md`
  - `workflow/MAIN.md`
  - `quality/MAIN.md`
  - `security/MAIN.md`
  - `state/MAIN.md`
  - `tasks/active-task.md`
  - `reports/context-pack.md`

## Missing Frontmatter Files

Категория: `MISSING_FRONTMATTER`

- количество: `240`
- примеры (высокая важность для контекстного конвейера):
  - `docs/AGENTOS-STATUS.md`
  - `docs/AGENTOS-WORKFLOW-REVIEW.md`
  - `docs/SCRIPT-RESPONSIBILITY-REVIEW.md`
  - `docs/NEGATIVE-FIXTURE-COVERAGE.md`
  - `docs/STABILIZATION-AUDIT-DESIGN.md`
  - `reports/context-selection-record.md`
  - `reports/m33-p0-stabilization-findings-intake.md`
  - `reports/m33-status-layer-inspection.md`
  - `reports/m33-context-status-mapping.md`
  - `tasks/task-20260426-brief-readiness-check/TASK.md`

## Malformed Frontmatter Files

Категория: `MALFORMED_FRONTMATTER`

- количество: `0`
- явных malformed (сломанный YAML-блок/нет закрытия `---`) не найдено в целевом наборе

## Incomplete Frontmatter Files

Категория: `INCOMPLETE_FRONTMATTER`

- количество: `5`
- точные файлы:
  - `tasks/drafts/execution-contract-ready.md` (нет `state`)
  - `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md` (нет `state`)
  - `tasks/queue/20260428-queue-schema-check.md` (нет `state`)
  - `tasks/queue/20260428-runner-human-checkpoints.md` (нет `state`)
  - `tasks/templates/task-contract.md` (нет `task_id`, `state`)

## Out-of-Scope Files

Категория: `OUT_OF_SCOPE_NO_FRONTMATTER_REQUIRED`

- количество: `1797`
- это файлы вне целевых директорий (например `.github/`, `tools/`, `tests/`, `examples/` и др.)

Категория: `NEEDS_HUMAN_REVIEW`

- `tasks/drafts/execution-contract-ready.md`
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`
- `tasks/templates/task-contract.md`

Причина: эти файлы из `tasks/*`, и неполный frontmatter может напрямую влиять на последующие проверки и активацию задач.

## Context Index Impact

- `data/context-index.json` содержит только 1 запись (`templates/context-frontmatter-example.md`).
- При таком покрытии многие релевантные markdown-файлы не индексируются.
- Это согласуется с риском: неполный/нестабильный frontmatter -> бедный индекс -> слабый выбор контекста.

## Context Pack Impact

- `reports/context-pack.md` указывает старую задачу `task-m22-gate-contract-artifacts`.
- `reports/context-selection-record.md` показывает `selected_count: 0` и `result: CONTEXT_NEEDS_REVIEW`.
- `reports/context-pipeline.json` показывает `CONTEXT_PIPELINE_INVALID` и `CONTEXT_INDEX_NEEDS_REVIEW`.

## Highest-Risk Missing Files

- `tasks/task-20260426-brief-readiness-check/TASK.md`
- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
- `tasks/task-20260426-brief-readiness-check/TRACE.md`
- `tasks/task-20260426-brief-to-contract-manual-guide/TASK.md`
- `tasks/queue/QUEUE.md`
- `reports/context-selection-record.md`
- `docs/AGENTOS-STATUS.md`
- `docs/FRONTMATTER-STANDARD.md`

## Recommended Scope for 33.3.1

Только аудит/план ремонта без массовой правки:
1. проверить и зафиксировать минимальный обязательный frontmatter для `tasks/*`.
2. отдельно проверить markdown-файлы, влияющие на контекстный конвейер.
3. подготовить пофайловый план исправлений малыми партиями.

## Files Allowed for 33.3.1

- `tasks/drafts/execution-contract-ready.md`
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`
- `tasks/templates/task-contract.md`
- `tasks/queue/QUEUE.md`
- `tasks/task-20260426-brief-readiness-check/TASK.md`
- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
- `tasks/task-20260426-brief-readiness-check/TRACE.md`
- `reports/context-selection-record.md`

## Files Forbidden for 33.3.1

- `tasks/active-task.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-pipeline.json`
- `reports/m33-p0-stabilization-findings-intake.md`
- `reports/m33-status-layer-inspection.md`
- `reports/m33-context-status-mapping.md`
- `reports/m33-frontmatter-coverage-inspection.md`

## Validation Evidence

Выполнено:
- `test -f reports/m33-frontmatter-coverage-inspection.md`
- `grep -q "M33_FRONTMATTER_COVERAGE_INSPECTION_COMPLETE" reports/m33-frontmatter-coverage-inspection.md`
- `grep -q "Missing Frontmatter Files" reports/m33-frontmatter-coverage-inspection.md`
- `grep -q "Malformed Frontmatter Files" reports/m33-frontmatter-coverage-inspection.md`
- `grep -q "Incomplete Frontmatter Files" reports/m33-frontmatter-coverage-inspection.md`
- `grep -q "Files Allowed for 33.3.1" reports/m33-frontmatter-coverage-inspection.md`
- `git status --short`

## Known Gaps

- Классификация сделана эвристикой (правилами осмотра), а не полным контрактом всех бизнес-ролей каждого markdown-файла.
- `scripts/validate-frontmatter.py` без аргумента не даёт полного отчёта по репозиторию (только usage), поэтому нужен отдельный явный прогон по директориям в 33.3.1.

## Final Status

M33_FRONTMATTER_COVERAGE_INSPECTION_COMPLETE
