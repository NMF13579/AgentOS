# GitHub Copilot repository instructions

This repository is a docs-first operating system for vibe coding.

## How to work in this repository

- Prefer existing repository docs over assumptions.
- Explain things in simple language.
- Ask one question at a time when requirements are unclear.
- Keep suggestions practical and prioritized.
- Avoid introducing unnecessary complexity.

## Session lifecycle

At the start of every session (automatic, no command needed):
1. Read `HANDOFF.md` and `LAYER-3/project-status.md`
2. Read `LAYER-3/lessons.md` if it exists
3. If the same task appears unclosed again — warn: «⚠️ Задача [название] идёт уже несколько сессий. Разбить на части или продолжить?»
4. Summarize in 3–5 lines: current state, what was done last, 1–3 next options
5. Wait for owner's choice — do not write code until confirmed

After every completed task:
1. Update `HANDOFF.md` — what was done, where stopped, what's next
2. Update `LAYER-3/project-status.md`
3. Update additional files per the table in `CLAUDE.md` (Автосохранение section)
4. Confirm: «Контекст сохранён ✅»

Remind to save («⚠️ Контекст не сохранялся. Сохранить сейчас?») if:
- 10 or more file edits since last `HANDOFF.md` update, OR
- A plan of 3+ steps completed without updating `HANDOFF.md`

## Read first

1. `README.md`
2. `llms.txt` и `LAYER-1/workflow.md`
3. `CLAUDE.md`
4. `HANDOFF.md`

## Plan Gate

NEVER write code, create files, or run commands before a plan is confirmed.

Required cycle for every task:
1. **PLAN** — numbered list: what will change, which files, why
2. **REVIEW** — risks, alternatives, what will NOT be changed
3. **CONFIRM** — wait for explicit owner approval («да», «ok», «go», «делай»)
4. **EXECUTE** — only after confirmation

Triggers that require a new plan:
- Any new feature or change request
- Switching to a different file than planned
- Discovering the task is larger than described
- Any doubt about scope

Hard blocks:
- Do NOT start executing if the plan was not confirmed
- Do NOT expand scope mid-task — stop and ask
- Do NOT create new files outside the confirmed plan
- Do NOT refactor code that was not part of the plan

Format:
```
📋 ПЛАН
1. [файл/действие] — [почему]
2. ...

⚠️ РИСКИ
- ...

Подтверждаешь? (да / нет / изменить)
```

## Scope Guard

Do exactly what was confirmed. Nothing more.

Hard rules:
- **One task at a time** — complete current task before accepting the next
- **No silent refactoring** — if you notice an improvement outside scope, log it, do not do it
- **No new dependencies** — do not add packages, libraries, or services not in the plan
- **No file creation outside plan** — every new file must be in the confirmed plan
- **No config changes** — do not touch `.env`, CI, or infra files unless explicitly confirmed

When scope grows during execution — stop immediately and report:
```
🚧 СТОП — задача оказалась шире плана

Обнаружил: [что нашёл]
Это затрагивает: [файлы/компоненты]

Варианты:
А) Продолжить только текущий план, остальное — в следующую задачу
Б) Обновить план и подтвердить снова

Что делаем?
```

Every out-of-scope improvement must be logged:
- `LAYER-3/deferred-decisions.md` — architectural choices
- `LAYER-3/features.md` — feature ideas
- `LAYER-3/fixes.md` — known bugs or tech debt

## Document Priority

Repository documents are the single source of truth. Internal model knowledge is a fallback only.

Priority order:
1. `LAYER-3/` — project-specific context (status, decisions, features, fixes)
2. `LAYER-2/specs/` — architecture, stack, roadmap, planning
3. `LAYER-1/` — framework rules and protocols
4. `CLAUDE.md` + `llms.txt` — framework entry points
5. Model internal knowledge — last resort only

Before answering any question about the project:
- Check if the answer exists in the docs above
- Cite the file: «По `LAYER-3/project-status.md`:...»
- If docs conflict — flag it, do not silently pick one
- If docs are missing info — say what is missing and where it should be added

Self-verification before every code response:
- [ ] Did I read the relevant BOOT.md for this stage?
- [ ] Did I check `LAYER-2/specs/architecture.md` for stack decisions?
- [ ] Did I check `LAYER-3/deferred-decisions.md` for relevant postponed choices?
- [ ] Is my plan consistent with `HANDOFF.md` current task?
- [ ] Am I within confirmed scope?

If any item is unchecked → read the missing doc first, then reply.

## Interview control (GitHub Copilot)

When conducting the product interview per `LAYER-2/discovery/project-interview.md`, follow `LAYER-1/tools/adapters/COPILOT-INTERVIEW-CONTROL.md`: after **every** interviewer message, include a full **СТРАЖ** self-check table from `LAYER-1/interview-system.md`. On critical **❌**, do not ask the next route question until corrected (stop-block). Log steps in `LAYER-3/interview-session.md` with `control-mode: copilot-self-check`.

## Route by task

- Project startup (new project or existing code) → `llms.txt` / `LAYER-1/workflow.md` Этап 0, `LAYER-1/agent-bootstrap.md`
- Communication style → `LAYER-1/dialog-style.md`, `LAYER-1/glossary.md`
- Planning → `LAYER-2/specs/planning.md`, `LAYER-2/specs/roadmap.md`
- Architecture → `LAYER-2/specs/architecture.md`, `LAYER-1/stack-presets.md`
- Review → `LAYER-1/task-protocol.md`
- Audit → `LAYER-1/audit.md` + `LAYER-1/audit-checklist.md`
- Security → `LAYER-1/security.md`, `LAYER-3/security.md`
- Product suggestions → `LAYER-1/feature-radar.md`, `LAYER-3/features.md`
- Recovery after confusion → `LAYER-1/context-recovery.md`

## Sub-agent equivalents (doc-based)

| Trigger | Action |
|---|---|
| «проверь проект», «аудит», «здоровье» | Run `LAYER-1/audit.md` protocol; use `LAYER-1/audit-checklist.md` for checklist + HEALTH-SCORE |
| «что добавить», «что дальше», after phase close | Read `LAYER-1/feature-radar.md` + `LAYER-3/features.md`, suggest top 3 |
| 10+ edits or 3+ step plan without saving | Remind to save context |

## Update after major changes

- `HANDOFF.md`
- `LAYER-3/project-status.md`
- `LAYER-3/deferred-decisions.md` if a decision is postponed
- `LAYER-3/fixes.md` if a reusable fix was found
