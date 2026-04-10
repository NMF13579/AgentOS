# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз

- **Validation:** в `LAYER-2/specs/validation.md` и `validation-rules.md` — статус `active`, триггеры в шапке, перекрёстные ссылки; в `llms.txt` добавлены отдельные маршруты на оба файла.
- **Интервью:** в `LAYER-2/discovery/project-interview.md` в таблицу «После интервью» добавлены `roles.md` и `processes.md`, обновлён порядок заполнения (USER-PROFILE → roles → processes → VISION → MVP-SCOPE).
- **UX-чеклисты:** уже разбиты на четыре файла `LAYER-1/ux-checklist-{core,accessibility,medical,interactions}.md` (монолит `ux-checklist.md` отсутствует); маршруты в `llms.txt` актуальны.

## Что уже работает

- Маршрут агента: `llms.txt` → `HANDOFF.md` → при необходимости один файл из `LAYER-1/` по ситуации.
- Интервью и страж: `LAYER-1/interview-system.md`, маршрут в `LAYER-2/discovery/project-interview.md`, адаптеры в `LAYER-1/tools/adapters/`.

## Где мы остановились

- Документы validation, таблица после интервью и маршруты в `llms.txt` обновлены. При желании — прогон сценариев в IDE и подчистка `LAYER-1/navigation.md`.

## Следующий лучший шаг

- Прогон «Начнём» / «Восстанови контекст» в Cursor или другой среде.
- По итогам — укоротить дубликаты в `LAYER-1/navigation.md` (наследие INDEX + DOCS-MAP).

## Риски и вопросы

- Внешние ссылки на старые пути `docs/*` / `memory-bank/*` вне репозитория могут отвалиться — при миграции проектов обновить ссылки вручную.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
