# HEALTH-SCORE — оценка здоровья проекта

> Role: project-record
> Status: not-started
> Filled by: agent
> Needs approval: no
> Next: —

> Это простой светофор состояния проекта.
> Агент обновляет этот файл после каждого значимого изменения.
> Не требует подтверждения пользователя, но должен отражать реальность.

## Шкала

- 🟢 Хорошо — слой понятен и поддерживается.
- 🟡 Есть пробелы — слой в целом живой, но требует внимания.
- 🔴 Риск — слой слабый или почти не описан.

## Правило светофора для слоя Discovery

| Условие | Индикатор |
|---|---|
| `discovery/INTERVIEW-SUMMARY.md` = `accepted` | 🟢 Хорошо |
| `discovery/INTERVIEW-SUMMARY.md` = `draft` или `pending-approval` | 🟡 Есть пробелы |
| Файл отсутствует или `not-started` | 🔴 Риск |

> Связка: если `INTERVIEW-SUMMARY.md = accepted` в `PROJECT-STATUS.md`,
> слой **Discovery** (Продукт) получает 🟢 в таблице слоёв ниже.

## Оценка слоёв

| Слой | Оценка | Комментарий |
|---|---|---|
| Продукт (Discovery) | — | [🟢 если INTERVIEW-SUMMARY = accepted / 🟡 если draft / 🔴 если не существует] |
| Архитектура | — | [вписать после specs] |
| Процесс | — | [вписать после processes] |
| Качество | — | [вписать после qa] |
| Безопасность | — | [вписать после specs] |
| Передача контекста | — | [вписать после первой сессии] |

## Статус ключевых файлов

> Агент синхронизирует эту таблицу с `docs/PROJECT-STATUS.md`.

| Файл | Статус |
|---|---|
| discovery/VISION.md | not-started |
| discovery/MVP-SCOPE.md | not-started |
| discovery/INTERVIEW-SUMMARY.md | not-started |
| specs/ARCHITECTURE.md | not-started |
| specs/SPEC.md | not-started |

## Как использовать

После оценки агент должен:

1. Назвать 1 красную зону.
2. Назвать 1 жёлтую зону.
3. Назвать 1 сильную сторону проекта.
4. Предложить один ближайший шаг.
