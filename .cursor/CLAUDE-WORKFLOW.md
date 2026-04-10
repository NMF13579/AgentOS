# Cursor → дальнейший воркфлоу (как у Claude Code)

В **Cursor** этот репозиторий по-прежнему подхватывает правила из [`.cursor/rules/`](./rules/).  
**Эталон поведения агента и поэтапный поток** описаны в корневом **[`../CLAUDE.md`](../CLAUDE.md)** — открывай и следуй ему, как в Claude Code.

## С чего начать

1. **[`CLAUDE.md`](../CLAUDE.md)** — роль, автозапуск, **Plan → Confirm → Execute**, приоритет источников, автосохранение шаблона.
2. **[`README-NEW-ARCHITECTURE.md`](../README-NEW-ARCHITECTURE.md)** — краткая карта системы для человека.
3. **[`project/PROJECT.md`](../project/PROJECT.md)** — единое живое ТЗ продукта (Discovery, UX, Specs, Deploy, Decisions).

## Этапы (узкий контекст)

Запускай так же, как в Claude Code: попроси агента **прочитать нужный `BOOT.md`**.

| Этап | Файл |
|------|------|
| Интервью | [`stages/01-interview/BOOT.md`](../stages/01-interview/BOOT.md) |
| UX | [`stages/02-ux/BOOT.md`](../stages/02-ux/BOOT.md) |
| Разработка | [`stages/03-dev/BOOT.md`](../stages/03-dev/BOOT.md) |
| Деплой | [`stages/04-deploy/BOOT.md`](../stages/04-deploy/BOOT.md) |

Общие правила всех этапов: [`shared/`](../shared/README.md). Перед релизом: [`CHECKLIST.md`](../CHECKLIST.md).

## Классический маршрут шаблона (LAYER-*)

Точка входа по темам: [`llms.txt`](../llms.txt) → [`HANDOFF.md`](../HANDOFF.md) → файлы в `LAYER-1/` … `LAYER-3/`.

---

*Имеет смысл держать этот файл открытым или вставить путь к `CLAUDE.md` в заметки проекта в Cursor.*
