# M31 Renderer Architecture (31.6)

## Зачем разделение
Логика статуса и отображение разделены.

- Vocabulary и status JSON задают смысл.
- Renderer только показывает.

Rich is replaceable.
Vocabulary and status JSON are not replaceable.

## Вход рендера
Рендеры принимают уже готовые dict/JSON:
- Status View Model
- Tutor Explanation
- Next Safe Step

Рендеры не читают raw reports и не читают словарь напрямую.

## Запрещено рендеру
- решать severity/authority;
- выбирать следующий шаг;
- выполнять команды;
- писать файлы;
- создавать approval.

## Plain Renderer
`plain_status_renderer.py`
- работает без внешних зависимостей;
- поддерживает ascii/no-color;
- безопасный fallback.

## Rich Renderer
`rich_status_renderer.py`
- использует Rich при наличии;
- если Rich недоступен или упал — fallback в plain;
- не ломает весь вывод.

## Accessibility
- no icon-only status
- no color-only risk signal
- ascii fallback обязателен

## Non-Approval Boundary
Renderer output is not approval.
Renderer output is not proof by itself.
