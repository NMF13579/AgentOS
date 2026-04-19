# TASK-001 — Доработка механики подтверждения интервью и связка статусов

---

## FSM-статус

| Поле | Значение |
|------|----------|
| **MODE** | `PLAN` |
| **STATE** | `done` (шаблон: артефакты и правила закреплены; сценарий вживую — на копии проекта) |

---

## Контекст

Репозиторий `Vibe-coding-docs` содержит `LAYER-1/interview-system.md` и `LAYER-2/discovery/project-interview.md`, определяющие поведение агента на этапе Discovery. В шаблоне закреплены явный stop-point, секция **Confirmation** и связка со статусом в `LAYER-3/project-status.md`.

## Цель

Добавить в `LAYER-2/discovery/project-interview.md` явный stop-point и секцию `## Confirmation`, обновить `LAYER-3/project-status.md` и при необходимости раздел «Чеклист аудита» в `LAYER-1/audit.md` (HEALTH-SCORE), а также карту в `LAYER-1/tools/template-sync-index.md` / `README.md`, чтобы статус `accepted` выставлялся только после явного согласия пользователя.

## Шаги

1. Открыть `LAYER-2/discovery/project-interview.md`, найти конец блока интервью
2. Добавить stop-point перед фиксацией:
   ```
   > STOP: Покажи саммари пользователю и дождись явного подтверждения,
   > прежде чем фиксировать файл в LAYER-2/discovery/interview-summary.md.
   ```
3. Добавить в конец `LAYER-2/discovery/project-interview.md` секцию:
   ```markdown
   ## Confirmation
   Агент задаёт вопрос: «Согласен ли пользователь с этой суммаризацией?»
   Только при ответе "Да" → обновить `LAYER-3/project-status.md`:
   `LAYER-2/discovery/interview-summary.md` = accepted (и при необходимости поле Approved by)
   ```
4. В `LAYER-3/project-status.md` добавить колонку `Approved by` в таблицу статусов (или эквивалент в тексте)
5. В `LAYER-1/audit.md` обновить правило: `interview-summary.md` = accepted → Discovery 🟢
6. В `LAYER-1/tools/template-sync-index.md` (или `README.md`) дополнить блок Discovery пунктом о подтверждении интервью
7. Провести тестовый сценарий (см. «Критерии готовности»)

## Критерии готовности

- [x] Стоп-поинт и явное правило до записи в `interview-summary.md` — в [`LAYER-2/discovery/project-interview.md`](../LAYER-2/discovery/project-interview.md)
- [x] Секция `## Confirmation` с логикой вопроса/ответа — там же
- [x] `LAYER-3/project-status.md` — таблица **Подтверждение ключевых артефактов** с колонкой **Approved by**
- [x] `LAYER-1/audit.md` — критерий по подтверждённому `interview-summary.md` (в разделе «Чеклист аудита»); в основном тексте `audit.md` — правило 🟢 по оси «итог интервью зафиксирован»
- [x] Карта: процедура подтверждения — в [`LAYER-1/tools/template-sync-index.md`](../LAYER-1/tools/template-sync-index.md) (блок Discovery); вход с `START.md` — в [`README.md`](../README.md)
- [ ] Тестовый сценарий пройден полностью на **живой копии проекта**:
  1. Агент создает саммари → 2. Пользователь подтверждает → 3. `accepted` в `LAYER-3/project-status.md` → 4. 🟢 в HEALTH-SCORE (`audit.md`, раздел чеклиста)

## Зависимости

- Требует: существование `LAYER-2/discovery/project-interview.md`, `LAYER-3/project-status.md`, `LAYER-1/audit.md`, `LAYER-1/tools/template-sync-index.md` или `README.md`
- Блокирует: корректная визуализация прогресса Discovery в HEALTH-SCORE
- Тип: `improvement` | Приоритет: `high`

## Self-check (заполняет агент перед закрытием)

- [x] Цель достигнута в шаблоне: stop-point, Confirmation, таблица статусов, аудит
- [x] Артефакты из шагов обновлены (кроме ручного теста на копии)
- [x] Побочных изменений вне scope нет
- [x] HANDOFF.md обновлён

## Заметки агента

_2026-04-16 — В исходном шаблоне закреплены: усиленный STOP в `project-interview.md`, таблица в `LAYER-3/project-status.md`, правила в `audit.md` (протокол и чеклист), онбординг с `START.md` в `ONBOARDING-WIZARD.md`, `QUICK-START.md`, `README.md`, `QUICK-START-NOVICE.md`._
