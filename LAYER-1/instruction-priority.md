> Trigger: конфликт инструкций  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `shared/priority-order.md`

# Document Priority — приоритет источников

Репозиторий — источник правды. Канон иерархии: [`shared/priority-order.md`](../shared/priority-order.md).

При конфликте следовать порядку из того файла (кратко: задача → PROJECT + HANDOFF + project-status → stages BOOT → shared scope/agent → LAYER-1/2 → `CLAUDE.md` / `system-prompt.md`).

Если два источника **одного** уровня противоречат — **спросить владельца**, не выбирать молча.

## Перед ответом о проекте

- Свериться с иерархией, искать ответ в репозитории.
- Ссылаться на файл явно.
- При пробеле данных — указать, чего не хватает и куда добавить.

## Чеклист перед ответом с кодом

- [ ] Релевантный `BOOT.md` этапа?
- [ ] `LAYER-2/specs/architecture.md` для стека?
- [ ] `LAYER-3/deferred-decisions.md`?
- [ ] Согласовано с текущим контекстом в `HANDOFF.md`?
- [ ] В рамках подтверждённого скоупа?

Если «нет» — дочитать документ, затем отвечать.
