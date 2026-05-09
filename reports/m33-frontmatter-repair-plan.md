## Summary

Это plan-only отчёт (только план) для будущего scoped repair frontmatter.
Фактический ремонт frontmatter в этой задаче не выполнялся.

## Preconditions

- `test -f reports/m33-frontmatter-coverage-inspection.md` -> passed
- `grep -q "M33_FRONTMATTER_COVERAGE_INSPECTION_COMPLETE" reports/m33-frontmatter-coverage-inspection.md` -> passed
- `test -f reports/m33-frontmatter-coverage-audit.md` -> passed
- `grep -q "M33_FRONTMATTER_COVERAGE_AUDIT_COMPLETE" reports/m33-frontmatter-coverage-audit.md` -> passed
- `grep -q "Files Allowed for 33.3.2" reports/m33-frontmatter-coverage-audit.md` -> passed

## Source Audit Used

- `reports/m33-frontmatter-coverage-inspection.md`
- `reports/m33-frontmatter-coverage-audit.md`

## Repair Planning Method

1. Взят точный список `Files Allowed for 33.3.2` (10 файлов).
2. Для каждого файла определено:
   - можно ли безопасно добавить минимальный frontmatter без изменения смысла;
   - нужен ли человек для подтверждения;
   - запрещён ли авто-ремонт.
3. Зафиксированы границы для будущей задачи 33.3.3.

## Safe Scoped Repair Candidates

Категория: `SAFE_SCOPED_REPAIR_CANDIDATES`

Количество: `2`

- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`

Почему safe:
- файлы из очереди задач;
- дефицит полей локальный (`state`), можно добавить нейтрально;
- нет прямых полей approval/completion evidence.

## Human Review Required

Категория: `HUMAN_REVIEW_REQUIRED`

Количество: `3`

- `tasks/drafts/execution-contract-ready.md`
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
- `tasks/templates/task-contract.md`

Почему нужен человек:
- draft/шаблонные документы могут менять смысл task-протокола;
- в шаблоне нельзя безопасно угадать `task_id`/`state` без явного решения владельца.

## Non-Auto-Repairable Findings

Категория: `NON_AUTO_REPAIRABLE`

Количество: `5`

- `tasks/queue/QUEUE.md`
- `tasks/task-20260426-brief-readiness-check/TASK.md`
- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
- `tasks/task-20260426-brief-readiness-check/TRACE.md`
- `reports/context-selection-record.md`

Почему non-auto-repairable:
- эти файлы связаны с task-историей, review/trace-смыслом и evidence цепочкой;
- автоматическая вставка frontmatter может исказить meaning/authority.

## Out-of-Scope Findings

Категория: `OUT_OF_SCOPE`

- все файлы вне `Files Allowed for 33.3.2` из отчёта 33.3.1.
- особенно: `tasks/active-task.md`, `data/context-index.json`, `reports/context-pack.md`, `reports/context-pipeline.json`.

## Proposed Minimal Frontmatter Pattern

Допустимый нейтральный шаблон только для `SAFE_SCOPED_REPAIR_CANDIDATES`:

```yaml
---
status: draft
authority: supporting
last_validated: unknown
tags: []
---
```

Ограничения:
- не добавлять fake значения для approval/owner decision/completion/security authority/canonical authority/risk acceptance;
- не менять body content;
- не менять смысл задачи.

## File-by-File Repair Plan

- `tasks/queue/20260428-queue-schema-check.md`
  - действие в 33.3.3: добавить минимальный frontmatter block с нейтральными полями.
  - режим: safe scoped.

- `tasks/queue/20260428-runner-human-checkpoints.md`
  - действие в 33.3.3: добавить минимальный frontmatter block с нейтральными полями.
  - режим: safe scoped.

- `tasks/drafts/execution-contract-ready.md`
  - действие в 33.3.3: только после human approval на точные поля.
  - режим: human review required.

- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
  - действие в 33.3.3: только после human approval на точные поля.
  - режим: human review required.

- `tasks/templates/task-contract.md`
  - действие в 33.3.3: только после human approval на schema-совместимые поля шаблона.
  - режим: human review required.

- `tasks/queue/QUEUE.md`
  - действие: не авто-ремонтировать.
  - режим: non-auto-repairable.

- `tasks/task-20260426-brief-readiness-check/TASK.md`
  - действие: не авто-ремонтировать.
  - режим: non-auto-repairable.

- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
  - действие: не авто-ремонтировать.
  - режим: non-auto-repairable.

- `tasks/task-20260426-brief-readiness-check/TRACE.md`
  - действие: не авто-ремонтировать.
  - режим: non-auto-repairable.

- `reports/context-selection-record.md`
  - действие: не авто-ремонтировать.
  - режим: non-auto-repairable.

## Exact Scope for 33.3.3

Будущая 33.3.3 может:
- изменять только файлы из `Files Allowed for 33.3.3`;
- добавлять/исправлять только минимальный frontmatter;
- не менять body content;
- не менять смысл задач/approval/evidence;
- не перестраивать context-index без отдельной задачи.

33.3.3 не может:
- ремонтировать файлы вне точного списка;
- менять `tasks/active-task.md`;
- менять milestone/evidence файлы без отдельного human approval;
- создавать approval evidence;
- заявлять, что context pipeline полностью исправлен до валидации.

## Files Allowed for 33.3.3

- `tasks/queue/20260428-queue-schema-check.md`
- `tasks/queue/20260428-runner-human-checkpoints.md`

## Files Forbidden for 33.3.3

- `tasks/drafts/execution-contract-ready.md`
- `tasks/drafts/task-20260426-brief-readiness-check-contract-draft.md`
- `tasks/templates/task-contract.md`
- `tasks/queue/QUEUE.md`
- `tasks/task-20260426-brief-readiness-check/TASK.md`
- `tasks/task-20260426-brief-readiness-check/REVIEW.md`
- `tasks/task-20260426-brief-readiness-check/TRACE.md`
- `reports/context-selection-record.md`
- `tasks/active-task.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-pipeline.json`
- `reports/m33-frontmatter-coverage-inspection.md`
- `reports/m33-frontmatter-coverage-audit.md`
- `reports/m33-frontmatter-repair-plan.md`

## Validation Required After Repair

После 33.3.3 обязательно выполнить:

```bash
python3 scripts/validate-frontmatter.py tasks/queue/20260428-queue-schema-check.md
python3 scripts/validate-frontmatter.py tasks/queue/20260428-runner-human-checkpoints.md
python3 scripts/check-context-pipeline.py || true
python3 scripts/agentos-status.py || true
grep -q "result" reports/context-pipeline.json || true
git status --short
```

Интерпретация:
- если `check-context-pipeline.py` остаётся invalid, это фиксируется как оставшийся риск;
- нельзя объявлять full fix без подтверждённой валидации.

## Known Gaps

- План основан на отчётах 33.3.0/33.3.1 и не включает полный повторный repo-scan.
- Для `tasks/templates/task-contract.md` безопасные значения нельзя вывести автоматически; нужен отдельный human decision.

## Final Status

M33_FRONTMATTER_REPAIR_PLAN_COMPLETE
