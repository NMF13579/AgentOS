# Thin Task Acceptance Runner

## 1. Purpose
Определить и зафиксировать работу тонкого read-only runner для MVP-проверки упакованного результата задачи.

## 2. Runner Role
Runner проверяет только MVP-уровень: структура входов, границы изменений, базовые evidence-проверки и non-authority ограничения.
Runner не является production gate.

## 3. CLI
Обязательные команды:
```bash
python3 scripts/check-task-acceptance-mvp.py \
  --task <task-file> \
  --evidence <evidence-file> \
  --changed-files <changed-files-json-file> \
  --json
```

```bash
python3 scripts/check-task-acceptance-mvp.py --help
```

Опционально:
```bash
python3 scripts/check-task-acceptance-mvp.py \
  --task <task-file> \
  --evidence <evidence-file> \
  --changed-files <changed-files-json-file> \
  --strict \
  --json
```

`--changed-files` принимает только путь к JSON-файлу. Inline JSON не допускается.

## 4. Inputs
Runner принимает:
- task brief (`--task`)
- evidence file (`--evidence`)
- changed-files JSON (`--changed-files`)

Пакет проверяется как упакованный набор входов, а не как полная проверка всего репозитория.

## 5. Changed Files JSON
Минимальная форма:
```json
{
  "changed_files": [
    "docs/example.md",
    "reports/example-report.md"
  ]
}
```

Проверки:
- файл существует;
- JSON читается;
- поле `changed_files` существует;
- `changed_files` — список;
- каждый элемент — строка;
- абсолютные пути блокируются;
- traversal-пути (`..`) блокируются;
- принимаются только repository-relative пути.

## 6. Repository-Relative Path Rules
Правила нормализации:
- путь, начинающийся с `/`, запрещён;
- путь с `..` после нормализации запрещён;
- путь `./docs/example.md` нормализуется в `docs/example.md`, если безопасен;
- путь, выходящий за пределы корня репозитория, блокируется;
- backslash-пути (`\\`) обрабатываются консервативно и принимаются только при безопасной нормализации.

## 7. Human Review Handling
Системная политика AgentOS: ручной обзор обязателен всегда.

JSON-поля:
- `human_review_required: true` — системное требование;
- `input_attempted_to_disable_human_review: true|false` — вход пытался отключить ручной обзор или нет.

Если вход содержит попытку отключить ручной обзор (`human_review_required: false`, `human review not required`, `human review can be skipped`), результат должен быть `TASK_VALIDATION_BLOCKED`.

## 8. MVP Checks
Runner выполняет:
- проверку наличия task file;
- проверку наличия evidence file;
- проверку changed-files JSON;
- проверку repository-relative путей;
- проверку expected artifacts (если детерминированно извлекаются);
- проверку forbidden paths;
- проверку forbidden claims;
- проверку ранних M63-M67 артефактов в changed files;
- фиксацию политики `human_review_required: true`.

Runner не выполняет:
- полную семантику acceptance criteria;
- полную схему evidence;
- полную diff-семантику;
- completion gate;
- full false PASS suite;
- production readiness оценку.

## 9. Forbidden Claim Detection
Runner блокирует подтверждающие запрещённые claims (например approval/merge/push/release/lifecycle mutation/human-review bypass).

Если фраза встречается только в явном policy/example/non-authority контексте, это может быть предупреждение.
Если нельзя надёжно отличить реальный claim от примера, результат должен быть `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`.

## 10. Future Milestone Artifact Detection
Runner блокирует случаи, когда `changed_files` включает ранние артефакты M63-M67, например:
- `schemas/task-result.schema.json`
- `schemas/agent-evidence.schema.json`
- `docs/TASK-VALIDATION-CONTRACT.md`
- `docs/TASK-OUTPUT-EVIDENCE-MODEL.md`
- `docs/ACCEPTANCE-CRITERIA-CHECKER.md`
- `scripts/check-agent-task-result.py`
- `scripts/check-task-acceptance.py`

## 11. Result Values
Допустимы только:
- `TASK_VALIDATION_PASS`
- `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `TASK_VALIDATION_BLOCKED`
- `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`

## 12. Result Priority
Порядок приоритета:
1. `TASK_VALIDATION_BLOCKED`
2. `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`
3. `TASK_VALIDATION_PASS_WITH_WARNINGS`
4. `TASK_VALIDATION_PASS`

Блокер всегда имеет приоритет над любым другим исходом.

## 13. Exit Codes
- `0` — `TASK_VALIDATION_PASS` или `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `1` — `TASK_VALIDATION_BLOCKED` или `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`
- `2` — внутренняя ошибка runner/некорректный запуск

## 14. JSON Output Contract
При `--json` runner возвращает JSON в stdout.
Минимальные поля:
```json
{
  "result": "TASK_VALIDATION_PASS",
  "strict": false,
  "task_checked": true,
  "evidence_checked": true,
  "changed_files_checked": true,
  "expected_artifacts_checked": true,
  "forbidden_paths_checked": true,
  "forbidden_claims_checked": true,
  "future_milestone_artifacts_checked": true,
  "task_file": "",
  "evidence_file": "",
  "changed_files_file": "",
  "changed_files": [],
  "human_review_required": true,
  "input_attempted_to_disable_human_review": false,
  "warnings": [],
  "blockers": []
}
```

`human_review_required` всегда `true` по политике AgentOS.

## 15. Limitations
Runner intentionally thin:
- не читает полный production-контракт M63;
- не применяет полную evidence-модель M64;
- не заменяет M65/M66/M67;
- использует консервативную текстовую оценку для MVP-условий.

## 16. Non-Authority Boundary
M62 thin task acceptance runner is not approval.
M62 thin task acceptance runner does not replace human review.
M62 thin task acceptance runner does not complete the task.
M62 thin task acceptance runner does not validate completed agent tasks as a production gate.
M62 thin task acceptance runner does not define the full task validation contract.
M62 thin task acceptance runner does not define the full evidence model.
M62 thin task acceptance runner does not authorize merge, push, or release.
M62 thin task acceptance runner does not start M63.
Human review remains required.

## 17. Final Status
FINAL_STATUS: M62_THIN_TASK_ACCEPTANCE_RUNNER_DEFINED
