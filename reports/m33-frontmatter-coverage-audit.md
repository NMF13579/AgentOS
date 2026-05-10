## Summary

Это audit-only отчёт (только аудит) по покрытию frontmatter из Task 33.3.0.
Исправления frontmatter не выполнялись.

## Preconditions

- `test -f reports/m33-p0-stabilization-findings-intake.md` -> passed
- `grep -q "M33_P0_FINDINGS_INTAKE_COMPLETE" reports/m33-p0-stabilization-findings-intake.md` -> passed
- `test -f reports/m33-context-status-mapping.md` -> passed
- `grep -q "M33_CONTEXT_STATUS_MAPPING_COMPLETE" reports/m33-context-status-mapping.md` -> passed
- `test -f reports/m33-frontmatter-coverage-inspection.md` -> passed
- `grep -q "M33_FRONTMATTER_COVERAGE_INSPECTION_COMPLETE" reports/m33-frontmatter-coverage-inspection.md` -> passed

## Source Inspection Used

- `reports/m33-frontmatter-coverage-inspection.md`
- `reports/m33-p0-stabilization-findings-intake.md`
- `reports/m33-context-status-mapping.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`

## Audit Method

1. Взяты числа и списки из read-only inspection (33.3.0).
2. Сверено влияние на цепочку:
   - frontmatter -> context-index -> context-pack -> context-pipeline.
3. Каждая группа проблем классифицирована по риску:
   - `P0_CONTEXT_BLOCKING`
   - `P1_CONTEXT_DEGRADING`
   - `P2_METADATA_INCOMPLETE`
   - `P3_LOW_IMPACT`
   - `NEEDS_HUMAN_REVIEW`
   - `OUT_OF_SCOPE`

## Risk Classification Rules

- `P0_CONTEXT_BLOCKING` = проблема может привести к пропуску обязательного контекста или к блокировке выполнения.
- `P1_CONTEXT_DEGRADING` = проблема снижает качество/точность выбора контекста.
- `P2_METADATA_INCOMPLETE` = frontmatter есть, но ключевые поля неполные.
- `P3_LOW_IMPACT` = низкое влияние на выполнение и выбор контекста.
- `NEEDS_HUMAN_REVIEW` = автоматическая классификация/починка небезопасна.
- `OUT_OF_SCOPE` = файл не обязателен для frontmatter в рамках M33 hardening.

Обязательные правила аудита:
- Missing frontmatter in source-of-truth files must not be silently accepted.
- Malformed frontmatter must not be auto-fixed without scoped repair rules.
- Incomplete frontmatter must not be treated as valid searchable context unless required fields are present.
- Context-index completeness depends on valid frontmatter coverage.
- Frontmatter repair must be separate from audit.

## P0 Context-Blocking Findings

Количество: `8`

Файлы:
- `tasks/task-20260426-brief-readiness-check/TASK.md` (`MISSING_FRONTMATTER`)
- `tasks/task-20260426-brief-readiness-check/REVIEW.md` (`MISSING_FRONTMATTER`)
- `tasks/task-20260426-brief-readiness-check/TRACE.md` (`MISSING_FRONTMATTER`)
- `tasks/task-20260426-brief-to-contract-manual-guide/TASK.md` (`MISSING_FRONTMATTER`)
- `tasks/queue/QUEUE.md` (`MISSING_FRONTMATTER`)
- `tasks/drafts/execution-contract-ready.md` (`INCOMPLETE_FRONTMATTER`)
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md` (`INCOMPLETE_FRONTMATTER`)
- `reports/context-selection-record.md` (`MISSING_FRONTMATTER`)

Причина P0:
- эти файлы напрямую участвуют в состоянии задач, выборе контекста или доказательствах контекста.

## P1 Context-Degrading Findings

Количество: `5`

Файлы:
- `docs/AGENTOS-STATUS.md` (`MISSING_FRONTMATTER`)
- `docs/AGENTOS-WORKFLOW-REVIEW.md` (`MISSING_FRONTMATTER`)
- `docs/SCRIPT-RESPONSIBILITY-REVIEW.md` (`MISSING_FRONTMATTER`)
- `docs/NEGATIVE-FIXTURE-COVERAGE.md` (`MISSING_FRONTMATTER`)
- `docs/STABILIZATION-AUDIT-DESIGN.md` (`MISSING_FRONTMATTER`)

Причина P1:
- это ключевые документы для понимания статуса/процесса; их отсутствие в качественном индексировании ухудшает выбор релевантного контекста.

## P2 Metadata-Incomplete Findings

Количество: `3`

Файлы:
- `tasks/queue/20260428-queue-schema-check.md` (нет `state`)
- `tasks/queue/20260428-runner-human-checkpoints.md` (нет `state`)
- `tasks/templates/task-contract.md` (нет `task_id`, `state`)

## P3 Low-Impact Findings

Количество: `4`

Файлы:
- `reports/milestone-28-completion-review.md` (`MISSING_FRONTMATTER`)
- `reports/milestone-28-evidence-report.md` (`MISSING_FRONTMATTER`)
- `reports/milestone-29-completion-review.md` (`MISSING_FRONTMATTER`)
- `reports/milestone-29-evidence-report.md` (`MISSING_FRONTMATTER`)

Причина P3:
- исторические отчёты с низким прямым влиянием на текущий M33 runtime-контур.

## Needs Human Review

Количество: `5`

Файлы:
- `tasks/drafts/execution-contract-ready.md`
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`
- `tasks/templates/task-contract.md`

Причина:
- изменения полей в `tasks/*` могут менять смысл потока задач и требуют ручного подтверждения.

## Out-of-Scope Findings

Категория: `OUT_OF_SCOPE`

- В 33.3.0 за пределами целевых директорий отмечено `1797` markdown-файлов.
- Эти файлы не включаются в M33 frontmatter hardening scope на этом шаге.

## Context Index Impact

- `data/context-index.json` содержит только `1` запись.
- Это указывает на низкую полноту индекса и потенциальную потерю релевантного контекста.
- Для M33 это прямой риск деградации контекстного выбора.

## Context Pack Impact

- `reports/context-pack.md` отражает старую задачу (`task-m22-gate-contract-artifacts`) и пустой выбранный контекст.
- `reports/context-selection-record.md`: `selected_count: 0`, `CONTEXT_NEEDS_REVIEW`.
- `reports/context-pipeline.json`: `CONTEXT_PIPELINE_INVALID`.

Вывод:
- проблемы покрытия frontmatter коррелируют с неполным индексом и слабым context-pack качеством.

## Auto-Repair Eligibility

К авто-ремонту в будущем можно допускать только неканоничные файлы, где безопасно поставить нейтральные значения без изменения смысла задачи.

Условно eligible для будущего planning (не ремонт сейчас):
- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`

## Non-Auto-Repairable Findings

Нельзя авто-чинить:
- `tasks/active-task.md` (активное состояние)
- `reports/context-selection-record.md` (доказательство выбора контекста)
- `tasks/task-20260426-brief-readiness-check/TASK.md`
- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
- `tasks/task-20260426-brief-readiness-check/TRACE.md`
- `tasks/templates/task-contract.md` (шаблон с риском смены семантики)
- `docs/FRONTMATTER-STANDARD.md` (policy-стандарт)

## Recommended Scope for 33.3.2

В 33.3.2 делать только узкий planning scope:
1. подтвердить целевые обязательные поля для `tasks/*`;
2. отдельно разметить safe/unsafe ремонтные кандидаты;
3. подготовить пофайловый patch-план без фактического ремонта.

## Files Allowed for 33.3.2

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

## Files Forbidden for 33.3.2

- `tasks/active-task.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-pipeline.json`
- `reports/m33-p0-stabilization-findings-intake.md`
- `reports/m33-status-layer-inspection.md`
- `reports/m33-context-status-mapping.md`
- `reports/m33-frontmatter-coverage-inspection.md`
- `reports/m33-frontmatter-coverage-audit.md`

## Validation Evidence

Команды:
- `test -f reports/m33-frontmatter-coverage-audit.md`
- `grep -q "M33_FRONTMATTER_COVERAGE_AUDIT_COMPLETE" reports/m33-frontmatter-coverage-audit.md`
- `grep -q "P0 Context-Blocking Findings" reports/m33-frontmatter-coverage-audit.md`
- `grep -q "P1 Context-Degrading Findings" reports/m33-frontmatter-coverage-audit.md`
- `grep -q "Auto-Repair Eligibility" reports/m33-frontmatter-coverage-audit.md`
- `grep -q "Files Allowed for 33.3.2" reports/m33-frontmatter-coverage-audit.md`
- `git status --short`

## Known Gaps

- Полный список из `240` missing-файлов в этом аудите агрегирован по рисковым группам, а не приведён целиком.
- `MALFORMED_FRONTMATTER` в 33.3.0 не найдено; нужен отдельный прогон, если появятся новые файлы.

## Final Status

M33_FRONTMATTER_COVERAGE_AUDIT_COMPLETE
