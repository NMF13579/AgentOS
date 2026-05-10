<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- SOURCE_OF_TRUTH: no -->

# HANDOFF.md — Session Handoff Contract

HANDOFF is session context only.
It does not override canonical modules.

## Terminal Snapshot

- Milestone 36 (External MVP Usability) is COMPLETE.
- Current status: `M36_EXTERNAL_MVP_USABLE_WITH_GAPS`.
- Pipeline status: `PASS` (all validators and smoke tests green).
- Startup route: `llms.txt` -> `state/MAIN.md` -> `workflow/MAIN.md`.
- Current blockers: none. P0 M35 blockers repaired.
- Use `core-rules/MAIN.md` for authority conflicts.
- Use `quality/MAIN.md` before claiming completion.
- Use `security/MAIN.md` when sensitive data or access boundaries are involved.

## Next Agent First Step

1. Read `llms.txt`.
2. Confirm state through `state/MAIN.md`.
3. Verify project is ready for M37 planning.
4. Update `tasks/active-task.md` with new M37 task before execution.

## Persistent Context

Project type: AgentOS — governed workspace for AI-agent-driven development.
Stack: Markdown, GitHub, agent environments.
Architecture: canonical module routing.
Primary route: `llms.txt` and `ROUTES-REGISTRY.md`.
