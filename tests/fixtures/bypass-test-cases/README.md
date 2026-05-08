# Bypass Test Case Fixtures

Эта папка хранит только статичные и безопасные fixture-файлы для M29.

Правила:
- Только inert (неисполняемые) markdown/json файлы.
- Никаких .sh и .py файлов.
- Никаких shebang (`#!`) строк.
- Никаких реальных секретов, токенов, прод-целей и сетевых атак.

Структура:
- `m27-forbidden-command/fixture-notes.md`
- `m28-missing-context-pack/fixture-notes.md`
- `authority-fake-approval-claim/fixture-notes.md`
- `source-of-truth-derived-artifact-claim/fixture-notes.md`
