# GEMINI.md

This repository uses a docs-first structure for vibe coding.

## Read first

1. `README.md`
2. `START.md`
3. `CLAUDE.md`
4. `HANDOFF.md`

## Session lifecycle

At the start of every session (automatic, no command needed):
1. Read `HANDOFF.md` and `memory-bank/project-status.md`
2. Read `memory-bank/lessons-learned.md` if it exists
3. If the same task appears unclosed again — warn: «⚠️ Задача [название] идёт уже несколько сессий. Разбить на части или продолжить?»
4. Summarize in 3–5 lines: current state, what was done last, 1–3 next options
5. Wait for owner's choice — do not write code until confirmed

After every completed task:
1. Update `HANDOFF.md` — what was done, where stopped, what's next
2. Update `memory-bank/project-status.md`
3. Update additional files per the table in `CLAUDE.md` (Автосохранение section)
4. Confirm: «Контекст сохранён ✅»

Remind to save («⚠️ Контекст не сохранялся. Сохранить сейчас?») if:
- 10 or more file edits since last `HANDOFF.md` update, OR
- A plan of 3+ steps completed without updating `HANDOFF.md`

## Behavior

- Explain things in simple language.
- Ask one question at a time when the task is unclear.
- Prefer repository docs over assumptions.
- Keep answers practical and supportive.

## Route by task

- Startup (new project or existing code) → `START.md` Этап 0, `docs/AGENT-BOOTSTRAP.md`
- Communication → `docs/PM-DIALOG-STYLE.md`, `docs/EXPLAINER-GLOSSARY.md`
- Planning → `docs/PLANNING.md`, `docs/ROADMAP.md`
- Architecture → `docs/ARCHITECTURE.md`, `docs/STACK-PRESETS.md`
- Review → `docs/REVIEW-CHECKLIST.md`, `docs/TASK-REVIEW-PROTOCOL.md`
- Audit → `docs/AUDIT-GUIDE.md`, `docs/HEALTH-SCORE.md`
- Security → `docs/SECURITY_POLICY.md`, `memory-bank/security.md`
- Product suggestions → `docs/FEATURE-RADAR.md`, `memory-bank/features.md`
- Recovery → `docs/CONTEXT-LOSS-RECOVERY.md`

## Sub-agent equivalents (doc-based)

| Trigger | Action |
|---|---|
| «проверь проект», «аудит», «здоровье» | Run `docs/AUDIT-GUIDE.md` protocol |
| «что добавить», «что дальше», after phase close | Read `docs/FEATURE-RADAR.md` + `memory-bank/features.md`, suggest top 3 |
| 10+ edits or 3+ step plan without saving | Remind to save context |

## Update after major changes

- `HANDOFF.md`
- `memory-bank/project-status.md`
- `memory-bank/fixes.md` — если найден баг или откат
- `memory-bank/deferred-decisions.md` — если решение отложено
