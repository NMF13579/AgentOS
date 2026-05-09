# Script Responsibility Review (M32.3)

## Purpose

M32.3 проверяет границы ответственности скриптов и компонентов AgentOS до hardening (усиление надёжности) в M33.

Это обзор рисков и размытых ролей, а не рефакторинг.

## Responsibility Principle

Ключевой принцип: **One meaning — one owner** (один смысл — один владелец).

- status-скрипты сообщают машинное состояние.
- explain-скрипты объясняют состояние человеку.
- next-step-скрипты дают безопасную подсказку следующего шага.
- renderer только отображает.
- audit только проверяет.
- validators только валидируют.
- wrappers только маршрутизируют команды.
- ни один скрипт не должен молча становиться authority (authority = источник права одобрения).

## Script / Component Inventory

| Script / Component | Exists? | Owner Responsibility | Inputs | Outputs | Reads Files? | Writes Files? | JSON? | Exit Codes? | Mutates Files? | Drift Risk |
|---|---|---|---|---|---|---|---|---|---|---|
| `scripts/agentos-status.py` | FOUND | Машинный статус | контекстные отчёты, pipeline | статус + severity | Yes | No | Yes | Yes | No | Может смешать статус и интерпретацию |
| `scripts/agentos-view-model.py` | FOUND | Нормализация данных для UI/TUI | status JSON | view model | Yes | No | Yes | Yes | No | Может начать решать статус вместо отображения |
| `scripts/agentos-explain.py` | FOUND | Объяснение статуса | view model/status | текст/JSON объяснения | Yes | No | Yes | Yes | No | Может начать менять смысл статуса |
| `scripts/agentos-next-step.py` | FOUND | Подсказка безопасного next step | view model/status | шаги + проверки безопасности | Yes | No | Yes | Yes | No | "next" может стать скрытым execute |
| `scripts/agentos.py` | FOUND | CLI routing (маршрутизация) | команда пользователя | запуск нужного подскрипта | No | No | No | Yes | No | Может стать control panel |
| `scripts/audit-agentos.py` | FOUND | Сводная audit-проверка | результаты проверок | PASS/PASS_WITH_WARNINGS/FAIL | Yes | No | No | Yes | No | Риск drift к repair-режиму |
| `scripts/validate-task.py` | FOUND | Валидация task-контракта | `tasks/*.md`, schema | PASS/FAIL | Yes | No | No | Yes | No | Может начать автоматически "чинить" |
| `scripts/validate-verification.py` | FOUND | Валидация verification-отчёта | verification md + schema | PASS/FAIL | Yes | No | No | Yes | No | Дубли логики с другими валидаторами |
| `scripts/check-template-integrity.py` | FOUND | Проверка целостности шаблонов | templates, правила | PASS/WARN/FAIL | Yes | No | Yes | Yes | No | Нестабильные result-названия между скриптами |
| `scripts/select-context.py` | FOUND | Выбор context pack | активная задача + контекст | context-pack/selection | Yes | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Может стать неявным approval gate |
| `scripts/agentos-human-gate.py` | FOUND | Проверка записи человеческого решения | record JSON, required_for | HUMAN_GATE_* result | Yes | Yes | Yes | Yes | Yes | Может быть ошибочно воспринят как автоподтверждение |
| `scripts/agentos-command-guard.py` | FOUND | Ограничение опасных команд | команда/контекст | allow/block | Yes | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Разные guard-скрипты могут конфликтовать |
| `scripts/run-active-task.py` | FOUND | Workflow-обвязка запуска | active-task + проверки | ход выполнения | Yes | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Может смешать orchestration и policy |
| `scripts/test-negative-fixtures.py` | FOUND | Прогон негативных фикстур | fixture-набор | test pass/fail | Yes | No | No | Yes | No | Может давать ложную полноту покрытия |
| `scripts/renderers/plain_status_renderer.py` | FOUND | Plain rendering | view model/tui input | текстовый вывод | Yes | No | No | UNKNOWN | No | Рендерер может начать трактовать статус |
| `scripts/renderers/rich_status_renderer.py` | FOUND | Rich rendering | view model/tui input | расширенный вывод | Yes | No | No | UNKNOWN | No | Визуальный слой может скрыть BLOCKED |
| `scripts/agentos-tui.py` | FOUND | Сборка TUI-представления | view-model/explain/next | TUI output/JSON | Yes | No | Yes | Yes | No | Tutor-слой может смягчить риск |
| `scripts/audit-m31-tui-tutor.py` | FOUND | Аудит TUI/tutor-поведения | tui output/rules | audit verdict | Yes | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Риск смешения UX и policy-решений |
| `decision card component` | NOT FOUND | Явная карточка решения | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Отсутствие явного артефакта решения |

## Responsibility Boundaries

| Responsibility | Sole Owner | Allowed Helpers | Must Not Be Done By | Risk If Duplicated |
|---|---|---|---|---|
| machine status | `agentos-status.py` | `agentos-view-model.py` | renderer/explain/next | Разные статусы на один вход |
| status explanation | `agentos-explain.py` | TUI | status/audit | Объяснение подменяет факты |
| next safe action | `agentos-next-step.py` | view-model | wrapper/renderer | Подсказка становится исполнением |
| rendering | `scripts/renderers/*` | `agentos-tui.py` | status/explain | Визуал скрывает блокировку |
| task validation | `validate-task.py` | `validate-active-task.py` | workflow wrappers | Обход контракта |
| verification validation | `validate-verification.py` | quality checks | audit runner | Непоследовательный PASS/FAIL |
| audit aggregation | `audit-agentos.py` | профильные audit-* | validators | Audit начинает менять логику проверки |
| context selection | `select-context.py` | context checks | status/execution runner | Запуск без валидного контекста |
| context compliance | `check-context-*` family | audits | renderer/TUI | Контекст может формально "есть", но невалиден |
| human decision explanation | `agentos-explain.py` + docs | TUI | status script | Машина начинает "одобрять" |
| approval recording | `agentos-human-gate.py` (record checks) | reports | any auto script | Ложный auto-approval |
| completion decision | human + completion checks | `check-completion-readiness.py` | audit/status | DONE без review |
| evidence generation | reports pipeline | validate/audit outputs | renderer | Несвежие evidence маскируются |
| evidence freshness check | audit/quality checks | context freshness checks | completion wrapper alone | DONE на старых данных |
| mutation/write authorization | human gate + scope contract | guards | status/explain/renderer | Самовольные записи |
| command routing | `agentos.py` | shell wrappers | status/validator | Wrapper превращается в policy-engine |

## Drift Risk Analysis

Основные риски drift (drift = постепенный уход роли скрипта от исходной задачи):

- status начинает объяснять «как тьютор» вместо фактов.
- explain начинает решать, какой должен быть статус.
- next-step становится фактическим execute.
- renderer начинает читать отчёты напрямую и принимать решения.
- wrapper (`agentos.py`) превращается в control panel.
- audit начинает мутировать файлы.
- validator начинает чинить данные автоматически.
- context selector становится approval gate.
- tutor/TUI смягчает критический риск визуально.
- decision card (если появится) может быть ошибочно принят за approval.
- один скрипт читает `UNKNOWN` как безопасный, другой как блокирующий.
- разные скрипты используют разные result-имена.
- exit codes между скриптами расходятся по смыслу.

## Result Semantics Review

Рекомендуемая fail-closed семантика (fail-closed = при сомнении блокировать):

- `PASS` = машинная проверка пройдена.
- `WARN` = пройдено с не-блокирующим предупреждением.
- `FAIL` = блокирующая ошибка.
- `BLOCKED` = policy/state блокирует переход.
- `UNKNOWN` = небезопасно продолжать.
- `NEEDS_REVIEW` = нужен явный review человека.
- `NOT_FOUND` = обязательный артефакт не найден.
- `STALE` = артефакт есть, но устарел.

Обязательное правило: **`UNKNOWN` никогда не трактуется как `PASS`.**

## Exit Code Review

Рекомендуемая семантика exit-кодов:

- `exit 0` только для `PASS` или `PASS_WITH_WARNINGS`, где warning явно не блокирует.
- `exit 1` для `FAIL`, `BLOCKED`, `UNKNOWN`, `NEEDS_REVIEW`, `STALE`, invalid state.
- ни один скрипт не должен возвращать `exit 0` для неоднозначной безопасности.

Наблюдение по риску: в разных скриптах уже есть частично разная семантика result-строк, поэтому нужен единый контракт на M33.

## JSON / Markdown Output Review

- Markdown — для человека.
- JSON — для автоматизации.
- JSON не должен становиться source of truth (источник истины).
- Сгенерированный JSON должен сохранять стабильные ключи.
- Человеко-читаемые отчёты не должны противоречить машинному статусу.

Риск: при наличии нескольких JSON-пайплайнов (`status` → `view-model` → `explain/next/tui`) возможны расхождения форматов/полей.

## Mutation Boundary Review

| Script / Component | Should Be Read-Only? | Allowed Writes | Forbidden Writes | Current Risk | Follow-up |
|---|---|---|---|---|---|
| `agentos-status.py` | Yes | None | любые runtime/evidence/canonical файлы | Низкий | M33: формально зафиксировать read-only |
| `agentos-view-model.py` | Yes | None | любые файлы | Низкий | M33 |
| `agentos-explain.py` | Yes | None | любые файлы | Низкий | M33 |
| `agentos-next-step.py` | Yes | None | любые файлы/execute side effects | Средний | M33: защитить от скрытого execute |
| `agentos.py` | Yes | None | изменение состояния/approval | Средний | M33: жёсткий routing-only контракт |
| `audit-agentos.py` | Yes | None | auto-fix, edits in reports/canonical | Высокий при drift | M33: check-only гарантия |
| `validate-task.py` | Yes | None | авто-исправления контрактов | Средний | M33: validator read-only policy |
| `validate-verification.py` | Yes | None | любые repair-записи | Средний | M33 |
| `check-template-integrity.py` | Yes | None | автоматические правки template | Средний | M33 |
| `select-context.py` | Prefer Yes | Только явно разрешённые context artifacts | protected/canonical/evidence rewrite | Средний/UNKNOWN | M33: явный write-contract |
| `agentos-human-gate.py` | Conditional | Только явная запись gate-record | любые не-gate файлы | Высокий (может выглядеть как auto-approval) | M33: отделить verify vs write режимы |
| `agentos-tui.py` | Yes | None | любые файлы | Средний | M33 |

Правило: audit и validation должны быть read-only, если они не выделены отдельно как repair tools. Repair tools не должны запускаться молча и требуют отдельного approval для protected/canonical/evidence файлов.

## Approval Authority Boundary

- Ни один скрипт не может сам создавать human approval.
- Tutor/decision-card может объяснять, но не одобрять.
- Сгенерированный report не равен approval.
- Evidence report не равен approval.
- Context pack не равен approval.
- `audit PASS` не является approval для commit/push/merge/release.

## Findings Table

| Finding ID | Component | Responsibility Issue | Consequence | Severity | Recommended Follow-up | M32/M33 Mapping |
|---|---|---|---|---|---|---|
| F-001 | `agentos-status.py` + consumers | Риск разного чтения `UNKNOWN/NEEDS_REVIEW` | Ложный безопасный переход | P0 | Единый semantics-contract | M32.5 → M33 |
| F-002 | `agentos-explain.py` | Explain может звучать как решение, не как пояснение | Человек путает объяснение и допуск | P1 | Отделить explanation от authority-сигналов | M32.3 → M33 |
| F-003 | `agentos-next-step.py` | "next" можно понять как execute | Преждевременное выполнение | P1 | Строгий non-execute контракт вывода | M32.3 → M33 |
| F-004 | `scripts/renderers/*` | Рендерер может скрывать критичность BLOCKED | Визуально ложный OK | P1 | Рендер не меняет смысл статуса | M32.4 → M33 |
| F-005 | `agentos.py` | Wrapper может стать control-plane | Обход gate-логики | P1 | Зафиксировать routing-only рамку | M32.3 → M33 |
| F-006 | `audit-agentos.py` | Drift к мутациям/repair | Потеря доверия к audit | P0 | Гарантия read-only + отдельные repair-tool классы | M32.5 → M33 |
| F-007 | Validators family | Непоследовательные result-названия/exit практики | Сложно автоматизировать безопасно | P2 | Матрица единых result/exit значений | M32.5 → M33 |
| F-008 | `select-context.py` | Может неявно стать approval gate | Execution при спорном контексте | P1 | Явное разделение selection vs approval | M32.5 → M33 |
| F-009 | `agentos-human-gate.py` | Наличие записи могут принять за одобрение "по факту" | Фейковое чувство разрешения | P0 | Формальный контракт "record != approve" | M32.5 → M33 |
| F-010 | `agentos-tui.py` / tutor path | Визуальное смягчение риска | Пропуск блокировки человеком | P2 | UI copy contract для критичных статусов | M32.6 → M33 |

### Severity

- `P0` — false OK / bypass / fake approval.
- `P1` — workflow jump / stale evidence / unclear command.
- `P2` — duplicated logic / weak docs / missing examples.
- `P3` — polish / future productization.

## Recommended M33 Hardening Targets

- единая семантика exit-кодов;
- единая семантика JSON-результатов;
- один владелец на каждую ответственность;
- renderer не принимает статусные решения;
- audit runner не мутирует файлы;
- validators fail-closed на `UNKNOWN`;
- next-step не должен исполнять;
- разделение authority подтверждения и объяснения;
- контрактная документация для `status/explain/next-step`.

## Non-Goals

M32.3 явно не делает:

- рефакторинг скриптов;
- создание новых скриптов;
- изменение поведения скриптов;
- изменение валидаторов;
- изменение audit runner;
- изменение CLI routing;
- внедрение exit-code fixes;
- внедрение JSON-consistency fixes;
- добавление approval workflow;
- self-heal;
- recovery protocol;
- packaging;
- UI/TUI/web UI.

## Final Boundary

M32.3 — это responsibility review, а не script refactor.
Все исправления относятся к M33 или позже, если не согласовано отдельно.
