# AgentOS Workflow Review (M32.2)

## Purpose

M32.2 проверяет реальный рабочий поток AgentOS и выявляет пробелы стабилизации до этапа hardening (hardening = усиление надёжности) в M33.

Это обзор рисков, а не внедрение исправлений.

## Reviewed Workflow Path

Полный ожидаемый путь:

`task request` → `task contract` → `context selection` → `status` → `why / explanation` → `next safe action` → `validation` → `execution corridor` → `evidence` → `human review` → `completion`

Короткий операционный путь:

`status` → `why` → `next` → `validate` → `audit` → `evidence` → `review` → `completion`

## Workflow Inventory

| Step | Expected Input | Expected Output | Responsible File/Script | Human Visible? | Gate? | Risk |
|---|---|---|---|---|---|---|
| Task request | Запрос пользователя | Решение: запускать задачу или уточнять | `workflow/MAIN.md` (правило plan gate), `tasks/active-task.md` | Yes | Yes | Неясные критерии старта могут дать ранний запуск |
| Task contract | Черновик/описание задачи | Активный контракт с scope (scope = разрешённые границы) | `tasks/active-task.md`, `scripts/validate-task.py`, `scripts/validate-active-task.py` | Yes | Yes | Задача может стать активной с неполным контрактом |
| Context selection | Активный контракт + контекстные правила | Context Pack (контекстный набор) и запись выбора | `scripts/select-context.py`, `reports/context-pack.md`, `reports/context-selection-record.md`, `reports/context-verification.md` | Yes | Yes | Можно использовать неполный или устаревший контекст |
| Status | Активная задача + контекст | Машинный статус | `scripts/agentos-status.py`, `scripts/agentos-view-model.py` | Yes | Yes | `UNKNOWN` может быть воспринят как условный `OK` |
| Why / explanation | Статус и причины | Пояснение человеку | `scripts/agentos-explain.py` | Yes | No | Слишком технический вывод может скрыть блокировку |
| Next safe action | Текущий статус | Следующий безопасный шаг | `scripts/agentos-next-step.py`, `scripts/agent-next.py` | Yes | Yes | "next" может быть воспринят как команда выполнения |
| Validation | Контракт + файлы задачи | PASS/FAIL по проверкам | `scripts/agentos-validate.py`, `scripts/validate-task.py`, `scripts/check-pr-quality.py` | Yes | Yes | Разные валидаторы могут дать несогласованный итог |
| Execution corridor | PASS + допуски | Разрешённый коридор выполнения | `workflow/MAIN.md`, `security/MAIN.md`, `tasks/active-task.md` | Partial | Yes | Исполнение может начаться без полного набора допусков |
| Audit | Результаты проверки и состояние репо | Отчёт аудита | `scripts/audit-agentos.py`, `reports/audit.md` | Yes | Yes | Audit может быть пропущен перед completion |
| Evidence | Результаты validate/audit/review | Доказательная база выполнения | `reports/verification.md`, `reports/*evidence*.md`, `reports/*completion-review*.md` | Yes | Yes | Старые evidence могут быть приняты как свежие |
| Human review | Evidence + выводы | Решение человека (approve/block/rework) | `reports/*completion-review*.md`, `scripts/validate-review.py`, `scripts/agentos-human-gate.py` | Yes | Yes | Review может стать формальной галочкой |
| Completion | Одобренный review + свежие evidence | Статус DONE/завершение | `scripts/complete-active-task.py`, `scripts/check-completion-readiness.py`, `scripts/agent-complete.py` | Yes | Yes | Завершение возможно без строгой проверки свежести |
| Decision card / explicit human gate | Данные по риску и переходу | Явная запись решения | `scripts/agentos-human-gate.py` (наличие), отдельная карточка: `NOT FOUND` | Partial | Yes | Решение может быть неаудируемым или неявным |

## Gate Analysis

### task request → task contract

- Что позволяет перейти: оформленный контракт в `tasks/active-task.md`.
- Что блокирует: невалидный/неполный контракт.
- Машинная проверка: да (`scripts/validate-task.py`).
- Нужен человек: да, для постановки задачи и рамок.
- Approval явный или подразумеваемый: обычно явный, но формат может отличаться.
- Можно ли пропустить шаг: риск есть при ручном редактировании без процесса активации.
- Риск stale evidence: низкий на этом шаге.
- Может ли warning выглядеть как approval: да, если текст не разделяет "предупреждение" и "разрешение".

### task contract → context selection

- Что позволяет перейти: активный контракт с допустимым scope.
- Что блокирует: отсутствие контракта или несоответствие контекста задаче.
- Машинная проверка: частично (`check-context-*`, `select-context.py`).
- Нужен человек: да, при спорном контексте.
- Approval: чаще подразумеваемый.
- Можно ли пропустить: да, если перейти к запуску проверок напрямую.
- Риск stale evidence: средний (можно взять старый context pack).
- Warning как approval: да.

### context selection → execution

- Что позволяет перейти: выбранный контекст + понятный next safe action.
- Что блокирует: `BLOCKED/UNKNOWN`, отсутствующий Context Pack.
- Машинная проверка: частично.
- Нужен человек: да, если риск выше LOW.
- Approval: нередко подразумеваемый.
- Можно ли пропустить: да, при ручном запуске команд.
- Риск stale evidence: высокий.
- Warning как approval: высокий риск.

### validation → execution

- Что позволяет перейти: PASS по обязательным проверкам.
- Что блокирует: FAIL/BLOCKED/непройденные проверки.
- Машинная проверка: да.
- Нужен человек: для рискованных записей и спорных FAIL.
- Approval: должен быть явным на рискованных шагах.
- Можно ли пропустить: да, если исполнять команды напрямую.
- Риск stale evidence: средний.
- Warning как approval: да.

### execution → evidence

- Что позволяет перейти: завершённый шаг выполнения + зафиксированный результат.
- Что блокирует: отсутствие проверяемого результата.
- Машинная проверка: частично.
- Нужен человек: для подтверждения смысловой корректности.
- Approval: обычно подразумеваемый.
- Можно ли пропустить: да, если не оформить evidence.
- Риск stale evidence: высокий.
- Warning как approval: средний.

### evidence → review

- Что позволяет перейти: полный набор evidence.
- Что блокирует: дырки в доказательствах.
- Машинная проверка: частично.
- Нужен человек: да.
- Approval: явный.
- Можно ли пропустить: риск есть.
- Риск stale evidence: высокий.
- Warning как approval: высокий.

### review → completion

- Что позволяет перейти: одобрение review и отсутствие критических блокеров.
- Что блокирует: незакрытые риски/провалы в проверках.
- Машинная проверка: частично (`check-completion-readiness.py`, `validate-review.py`).
- Нужен человек: да.
- Approval: должен быть явным.
- Можно ли пропустить: риск есть.
- Риск stale evidence: высокий.
- Warning как approval: высокий.

### blocked → unblocked

- Что позволяет перейти: устранённая причина блокировки + повторная проверка.
- Что блокирует: отсутствие причины/доказательства снятия блока.
- Машинная проверка: частично.
- Нужен человек: да, если блок связан с границами или риском.
- Approval: часто неявный.
- Можно ли пропустить: да, очисткой статуса без обоснования.
- Риск stale evidence: средний.
- Warning как approval: средний.

### failed → retry

- Что позволяет перейти: зафиксированная причина сбоя и план повтора.
- Что блокирует: повтор без анализа причины.
- Машинная проверка: ограниченно.
- Нужен человек: для решения "повторять/менять подход".
- Approval: часто подразумеваемый.
- Можно ли пропустить: да.
- Риск stale evidence: средний.
- Warning как approval: средний.

### completed → done/report

- Что позволяет перейти: completion review + свежие evidence + актуальный audit.
- Что блокирует: устаревшие/неполные доказательства.
- Машинная проверка: частично.
- Нужен человек: да, финальное решение.
- Approval: должен быть явным.
- Можно ли пропустить: риск есть.
- Риск stale evidence: высокий.
- Warning как approval: высокий.

## Human Checkpoint Review

| Checkpoint | Что человек решает | Что человек видит | Риск спутать с чеклистом | Решение записывается? | Аудируемо? | Риск |
|---|---|---|---|---|---|---|
| До старта execution | Можно ли начинать выполнение | Контракт, статус, next | Да | Частично (`tasks/active-task.md`, отчёты) | Частично | Неявный старт без явного решения |
| До рискованной записи | Достаточно ли оснований для записи | Validation/audit результаты | Да | Частично | Частично | Запись может начаться на warning |
| До protected file change | Разрешён ли доступ к защищённым зонам | Scope + security правила | Средний | Частично | Частично | Граница доступа может быть понята неверно |
| До commit request | Готово ли содержимое к фиксации | Evidence + review | Да | Частично | Частично | Commit может быть запрошен без полного review |
| До push request | Готово ли к публикации | Completion + audit | Да | Частично | Частично | Push при неактуальном audit |
| До retry after failure | Повторяем ли мы корректно | Причина сбоя + план retry | Да | Слабо | Слабо | Бесконечные retry без анализа |
| До DONE | Можно ли закрывать задачу | Completion review + свежесть evidence | Да | Да (в отчётах/статусе) | Частично | DONE без жёсткой проверки свежести |

## Evidence Freshness Review

| Evidence Artifact | Freshness Signal | Current Risk | Needed Check | Follow-up Task |
|---|---|---|---|---|
| `reports/verification.md` | Дата/время + привязка к активной задаче | Может относиться к старой задаче | Сверка `task_id` и метки времени с `tasks/active-task.md` | 32.5 |
| `reports/audit.md` | Время запуска аудита | Audit может быть старым | Проверка максимального возраста перед completion | 32.5 |
| `reports/context-pack.md` | Момент генерации + связь с task | Можно запустить execution с прошлым context pack | Принудительная валидация актуальности context pack | 32.5 |
| `reports/context-selection-record.md` | Запись выбора контекста | Выбор контекста может не соответствовать текущему scope | Сверка с текущим контрактом | 32.5 |
| `reports/*evidence*.md` | Связь с шагом/датой/task | Можно повторно использовать старый evidence файл | Правило уникальности evidence для текущей задачи | 32.4 |
| `reports/*completion-review*.md` | Итоговый review timestamp | Completion review может не проверить свежесть audit/validate | Обязательная секция freshness-check в completion review | 32.5 |
| Вывод `validate-*` скриптов | Время запуска и код возврата | Старый PASS может трактоваться как текущий PASS | Повторный запуск перед completion | 32.5 |
| Вывод `audit-agentos.py` | Время запуска + статус | Старый PASS может скрыть новый риск | Блок completion без свежего audit | 32.5 |

## Command Clarity Review

| Команда/действие | Один очевидный вариант? | Конкурирующие команды | Безопасна (read-only = только чтение)? | Может менять файлы? | Dry-run (пробный запуск без изменений) | Читаемый вывод? | Риск |
|---|---|---|---|---|---|---|---|
| Первая команда после создания задачи | Нет | `agentos-status.py`, `agentos.py`, `run-active-task.py`, `agentos-validate.py` | Частично | Некоторые могут менять | UNKNOWN | Частично | Неясный старт |
| Проверка текущей задачи | Частично | `validate-task.py`, `validate-active-task.py`, `agentos-validate.py` | Да | Нет (ожидаемо) | N/A | Да | Дубли и разный охват |
| Объяснение статуса | Да | `agentos-explain.py` vs вывод TUI | Да | Нет | N/A | Да | Разные форматы объяснения |
| Получить следующий безопасный шаг | Частично | `agentos-next-step.py`, `agent-next.py` | Да (ожидаемо) | Нет (ожидаемо) | N/A | Да | "next" может быть прочитан как execute |
| Запустить все проверки | Нет | `run-all.sh`, набор отдельных `validate/check/audit` | Частично | UNKNOWN | UNKNOWN | Частично | Нет единого безопасного маршрута |
| Аудит всего репо | Частично | `audit-agentos.py`, другие `audit-*` | Да (ожидаемо) | Риск если drift | UNKNOWN | Да | Неочевидно, какой audit "главный" |
| Завершить задачу | Нет | `complete-active-task.py`, `agent-complete.py` | Нет | Да/потенциально | UNKNOWN | Частично | Возможен ранний completion |
| Остановить/пометить BLOCKED | Частично | `agent-fail.py`, ручное изменение статуса | Нет | Да/потенциально | UNKNOWN | Частично | Неодинаковая фиксация причины блокировки |

## Workflow Jump Risks

| Jump Risk | Example | Consequence | Current Guard | Gap | Severity | Follow-up |
|---|---|---|---|---|---|---|
| Активная задача без валидного контракта | Ручная активация с неполными полями | Ложный старт | `validate-task.py`, process rules | Можно обойти вне формального маршрута | P0 | 32.5 |
| Execution без Context Pack | Запуск после статуса без `context-pack.md` | Работа вне контекста | Контекст-скрипты и правила | Нет жёсткого блока "No Context Pack → No Execution" | P0 | 32.5 |
| Next safe step превращается в execute | Пользователь читает `next` как команду запуска | Непреднамеренные изменения | Разделение ролей в docs | Нет строгой лексики/контракта сообщений | P1 | 32.3 |
| Warning трактуется как pass | Некритичный warning принимают за допуск | Ранний переход дальше | Validation scripts | Нет общего правила "warning != approval" | P1 | 32.5 |
| Audit пропускается перед completion | Завершение только по validate | Старые риски остаются скрыты | Quality module | Нет обязательной связки completion↔fresh audit | P1 | 32.5 |
| Review пропускается | Completion без нормального human review | Формальное DONE без проверки | Workflow/quality правила | Нет жёсткой технической блокировки | P1 | 32.2 |
| Переиспользование stale report | Старый evidence для новой задачи | Ложная уверенность | Отчёты и ручная проверка | Нет общей freshness-проверки | P1 | 32.4 |
| BLOCKED снимается без причины | Состояние очищают вручную | Повторение ошибки | State rules | Нет обязательного поля "причина снятия" | P1 | 32.5 |
| Retry без разбора причины | Повтор после FAIL без анализа | Циклические сбои | Failure route in workflow | Слабая фиксация pre-retry решения | P2 | 32.2 |
| Completion без evidence | DONE по заявлению, без базы доказательств | Ложное завершение | Check-completion scripts | Неполный контроль полноты evidence | P0 | 32.5 |

### Severity Definition

- `P0` — false OK / bypass / fake approval (ложный OK, обход, фейковое подтверждение).
- `P1` — workflow jump / stale evidence / unclear command (прыжок по этапам, устаревшие доказательства, неясная команда).
- `P2` — duplicated logic / weak docs / missing examples (дубли логики, слабая документация, нехватка примеров).
- `P3` — polish / future productization (полировка и будущая продуктовая доработка).

## Recommended Workflow Shape

Рекомендуемая форма (без внедрения в 32.2):

`task contract` → `context pack` → `status` → `explanation` → `next safe action` → `validation` → `dry-run when risky` → `human checkpoint when needed` → `execution` → `verification` → `evidence freshness check` → `completion review` → `done`

Обязательные правила формы:

- No Context Pack → No Execution.
- No Fresh Evidence → No Completion.
- No Human Decision Record → No Risky Transition.

## Follow-up Links to M32 Tasks

- `32.3 Script Responsibility Review`: закрепить границы ролей скриптов и формулировок `status/why/next`.
- `32.4 Negative Fixture Coverage Map`: покрыть негативные сценарии stale evidence, skipped review, invalid transitions.
- `32.5 Stabilization Audit Design`: сделать единый дизайн проверок свежести, gate-переходов и блокировок completion.
- `32.6 Stabilization Priority Plan`: выстроить порядок внедрения исправлений по рискам P0 → P3.

## Non-Goals

M32.2 явно не делает:

- внедрение workflow-изменений;
- добавление скриптов;
- добавление/изменение валидаторов;
- изменение state transitions (логики переходов состояний);
- создание нового approval flow (процесса подтверждения);
- создание self-heal;
- создание recovery protocol;
- создание shadow branches;
- создание git checkpoints;
- создание packaging;
- создание UI/TUI/web UI.

## Final Boundary

M32.2 — это workflow review, а не workflow implementation.
Все исправления относятся к M33 или более позднему шагу, если отдельно не согласовано.
