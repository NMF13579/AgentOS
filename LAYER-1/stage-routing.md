> Trigger: неясно, на каком этапе жизненного цикла задача  
> Read-time: ~3 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `stages/*/BOOT.md`

# Stage Routing

У проекта на фреймворке **4 этапа**. Каждую задачу отнести к этапу и открыть `BOOT.md`.

## Карта

| Этап | Папка | BOOT.md | Когда |
|------|--------|---------|--------|
| 0 — Discovery | `stages/00-discovery/` | `BOOT.md` | Новый проект, цели, интервью |
| 1 — Planning | `stages/01-planning/` | `BOOT.md` | Архитектура, стек, roadmap |
| 2 — Build | `stages/02-build/` | `BOOT.md` | Разработка, фичи |
| 3 — Deploy | `stages/03-deploy/` | `BOOT.md` | CI/CD, релиз, мониторинг |

## Как маршрутизировать

1. Определить этап до начала задачи.
2. Прочитать `BOOT.md` этапа.
3. Следовать чеклисту внутри.
4. Если неясно — один вопрос: «Это этап [N] или [N+1]?»

## Переход

- Не переходить к следующему этапу, пока не закрыт чеклист текущего.
- При переходе: `HANDOFF.md`, `LAYER-3/project-status.md`, согласование с владельцем.
- Отложенное → `LAYER-3/deferred-decisions.md`.

## Сквозные ссылки

- Спеки: `LAYER-2/specs/`
- Решения: `LAYER-3/deferred-decisions.md`
- Уроки: `LAYER-3/lessons.md`
