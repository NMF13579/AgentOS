# MVP Task Result Input Contract

## 1. Purpose
Определить минимальный входной пакет данных для M62 MVP-проверки результата задачи агента.

## 2. M62 Position in the Roadmap
M62 задаёт тонкий контролируемый MVP-уровень.
Он подготавливает входы для проверки, но не задаёт полную производственную модель валидации.

## 3. Dependency on M62 Architecture
Зависимость: `docs/TASK-ACCEPTANCE-MVP-ARCHITECTURE.md`.
Наблюдаемый архитектурный статус: `FINAL_STATUS: M62_TASK_ACCEPTANCE_MVP_ARCHITECTURE_DEFINED`.

## 4. Contract Scope
Этот контракт определяет только минимальные входные поля и их смысл для MVP.
Этот контракт не определяет логику принятия решения и не определяет полную модель production-валидации.

## 5. Minimal MVP Input Package
Обязательные поля:
- `task_id`
- `task_brief_path`
- `declared_allowed_scope`
- `declared_forbidden_changes`
- `expected_artifacts`
- `actual_changed_files`
- `changed_files_json_path`
- `diff_reference`
- `agent_evidence_path`
- `validation_commands_claimed`
- `human_review_required`

Дополнительные (необязательные) поля:
- `task_title`
- `task_risk_level`
- `known_limitations`
- `warnings_declared_by_agent`

Дополнительные поля не становятся обязательными для M62 MVP.

## 6. Field Definitions
field_name: task_id
type: string
required: true
description: Стабильный идентификатор задачи из task brief.
MVP purpose: Связать пакет входов, evidence и changed files с одной задачей.
example value: "62.4"
must_not_mean: Одобрение задачи или завершение lifecycle.

field_name: task_brief_path
type: string (repository-relative path)
required: true
description: Путь к документу task brief, на основе которого выполняется проверка.
MVP purpose: Дать проверяемый источник границ задачи.
example value: "tasks/active-task.md"
must_not_mean: Полный контракт M63.

field_name: declared_allowed_scope
type: array of string
required: true
description: Список путей/областей, где изменения разрешены задачей.
MVP purpose: Сопоставить фактические изменения с заявленной областью.
example value: ["docs/", "reports/"]
must_not_mean: Полная семантика diff-анализа M65.

field_name: declared_forbidden_changes
type: array of string
required: true
description: Список запретных путей, операций, утверждений или действий.
MVP purpose: Выявить базовые нарушения границ задачи.
example value: ["scripts/check-task-acceptance-mvp.py", "authorize merge"]
must_not_mean: Финальное policy-решение production-уровня.

field_name: expected_artifacts
type: array of string
required: true
description: Ожидаемые выходные файлы/артефакты задачи.
MVP purpose: Проверить наличие ожидаемых результатов на базовом уровне.
example value: ["reports/m62-task-acceptance-mvp-evidence-report.md"]
must_not_mean: Полное подтверждение acceptance criteria.

field_name: actual_changed_files
type: array of string
required: true
description: Нормализованный список фактически изменённых файлов в репозитории.
MVP purpose: Сверка фактических изменений с заявленной областью и запретами.
example value: ["docs/TASK-ACCEPTANCE-MVP-ARCHITECTURE.md"]
must_not_mean: Полная correctness-проверка diff.

field_name: changed_files_json_path
type: string (repository-relative path)
required: true
description: Путь к JSON-файлу с changed files.
MVP purpose: Детерминированно загрузить вход changed-files из файла.
example value: "reports/fixtures/m62-changed-files.json"
must_not_mean: Inline JSON в теле контракта или автоматическое одобрение изменений.

field_name: diff_reference
type: string
required: true
description: Ссылка/идентификатор diff-источника для контекста проверки.
MVP purpose: Зафиксировать, к какому diff относится пакет входов.
example value: "git:HEAD~1..HEAD"
must_not_mean: Доказательство корректности изменений.

field_name: agent_evidence_path
type: string (repository-relative path)
required: true
description: Путь к минимальному evidence-файлу агента.
MVP purpose: Получить заявленные данные о выполнении задачи в читаемом виде.
example value: "reports/m62-task-result-evidence.md"
must_not_mean: Полная M64-модель evidence.

field_name: validation_commands_claimed
type: array of string
required: true
description: Команды, которые агент заявляет как выполненные проверки.
MVP purpose: Сохранить заявленные проверки как входные данные.
example value: ["test -f docs/example.md", "git status --short"]
must_not_mean: Доказательство завершения задачи само по себе.

field_name: human_review_required
type: boolean
required: true
description: Флаг обязательной ручной проверки.
MVP purpose: Зафиксировать обязательную передачу результата человеку.
example value: true
must_not_mean: Возможность отключить ручной обзор.

field_name: task_title
type: string
required: false
description: Короткое название задачи.
MVP purpose: Упростить чтение пакета входов человеком.
example value: "MVP Task Result Input Contract"
must_not_mean: Бизнес-одобрение или приоритет в roadmap.

field_name: task_risk_level
type: string
required: false
description: Заявленный уровень риска задачи.
MVP purpose: Добавить контекст риска для ручного обзора.
example value: "MEDIUM"
must_not_mean: Автоматическое решение по результату.

field_name: known_limitations
type: array of string
required: false
description: Известные ограничения выполненной работы.
MVP purpose: Не потерять ограничения при handoff на ручной обзор.
example value: ["MVP checks only structural boundaries"]
must_not_mean: Разрешение игнорировать обязательные проверки.

field_name: warnings_declared_by_agent
type: array of string
required: false
description: Предупреждения, явно заявленные агентом.
MVP purpose: Перенести предупреждения в ручной обзор без скрытия.
example value: ["Deferred risks carried to M63"]
must_not_mean: Блокер или PASS без анализа.

## 7. Changed Files Input
`changed_files_json_path` — это путь к JSON-файлу.
Inline JSON is not allowed.

Минимальная форма JSON:
```json
{
  "changed_files": [
    "docs/example.md",
    "reports/example-report.md"
  ]
}
```

Правила:
- `changed_files` — это список;
- каждый элемент — относительный путь внутри репозитория;
- абсолютные пути запрещены;
- пустой `changed_files` допустим только для validation-only примеров;
- changed-files JSON — это входные evidence-данные, а не approval.

Граница по этапам:
- 62.2 задаёт форму changed-files input;
- 62.4 реализует парсинг;
- 62.5 создаёт controlled fixtures;
- 62.6 проверяет результаты runner.

## 8. Evidence Input
`agent_evidence_path` — путь к минимальному evidence-файлу.
M62 не определяет полную M64-модель evidence.
Для M62 MVP evidence может быть в Markdown или JSON, если runner читает его детерминированно.

Для M62 MVP evidence должен выражать:
- `task_id`
- `human_review_required`
- `summary_of_work`
- `declared_changed_files`
- `declared_validation_commands`
- `known_limitations`

Граница: это MVP-level evidence input; полная модель определяется в M64.

## 9. Task Brief Input
`task_brief_path` — путь к task brief, используемому для проверки.
Task brief должен содержать или ссылаться на:
- `task_id`
- allowed scope
- forbidden changes
- expected artifacts
- validation expectations (если есть)

M62 не требует полный будущий M63 task contract.

## 10. Scope Input
`declared_allowed_scope` и `declared_forbidden_changes` обязательны.

На MVP-уровне:
- `declared_allowed_scope` — это пути/области, которые задаче разрешено менять;
- `declared_forbidden_changes` — это пути, утверждения, операции или смысловые действия, которые запрещены.

Контракт не определяет полную M65 diff-семантику.

## 11. Expected Artifacts Input
`expected_artifacts` — список ожидаемых файлов/выходов задачи.
На MVP-уровне проверяется только наличие или заявленное отсутствие.
Контракт не определяет полное выполнение acceptance criteria.

## 12. Validation Claims Input
`validation_commands_claimed` — команды, которые агент заявляет как выполненные.
На MVP-уровне это claims (заявления), а не доказательство корректности.

Validation claims are evidence inputs.
Validation claims are not approval.
Validation claims do not prove task completion by themselves.
Full validation evidence semantics belong to M64 / M65 / M66.

## 13. Human Review Requirement
Обязательное требование контракта:
- `human_review_required: true`

Любой пакет с `human_review_required: false` находится вне безопасной границы M62 MVP.

Human review is always required.
The MVP input contract must not allow human review to be disabled.

## 14. What This Contract Does Not Define
This contract must not anticipate or pre-define decision model semantics from 62.3.
62.2 defines only the minimum input fields required for MVP validation.
62.2 must not define result values, status mapping, pass/block rules, or approval semantics.

Этот контракт также не задаёт:
- production task acceptance;
- completion gate semantics;
- полную M63/M64/M65/M66/M67 модель.

## 15. Relation to 62.3 Decision Model
62.3 определяет decision model (модель принятия решения).
62.2 только подготавливает минимальный входной пакет для этой модели.

## 16. Relation to M63 Full Contract
M62 input contract is a thin MVP input contract.
M63 defines the full task validation contract.
M62 must not create the full task result schema.
M62 must not create the full agent evidence schema.
M62 must not create production task validation semantics.

## 17. Non-Authority Boundary
M62 MVP input contract is not approval.
M62 MVP input contract does not replace human review.
M62 MVP input contract does not complete the task.
M62 MVP input contract does not validate completed agent tasks as a production gate.
M62 MVP input contract does not define decision semantics.
M62 MVP input contract does not authorize merge, push, or release.
M62 MVP input contract does not start M63.
Human review remains required.

## 18. Final Status
FINAL_STATUS: M62_MVP_TASK_RESULT_INPUT_CONTRACT_DEFINED
