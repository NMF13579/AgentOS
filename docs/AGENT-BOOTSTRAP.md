## С чего начинает агент (bootstrap)

Перед началом работы по любой задаче агент должен:

1. Прочитать:
   - `README.md`
   - `START.md`
   - `HANDOFF.md`
   - `memory-bank/project-status.md`

2. Если сессия не первая — заглянуть в:
   - `memory-bank/lessons-learned.md` — применимые уроки
   - `memory-bank/fixes.md` — повторяемые фиксы
   - `memory-bank/features.md` — список фич

3. В зависимости от того, через какой инструмент идёт работа:
   - Claude Code → учесть правила из `CLAUDE.md` и доступные `.claude/agents/*`
   - Cursor → учитывать `.cursor/rules/*`
   - GitHub Copilot → учитывать `.github/copilot-instructions.md`
   - Gemini → учитывать `GEMINI.md`

4. Кратко пересказать владельцу:
   - что сейчас с проектом;
   - где мы остановились;
   - какие 1–3 варианта есть для следующего шага.

Только после этого переходить к конкретной задаче.