<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- SOURCE_OF_TRUTH: no -->

# HANDOFF.md — Session Handoff Contract

HANDOFF is session context only.
It does not override canonical modules.

## Terminal Snapshot

- Milestone 40 (External Portability & Installer MVP) is COMPLETE.
- Template Initialization Hardening is COMPLETE.
- Current status: `M40_EXTERNAL_PORTABILITY_SAFE`.
- Pipeline status: `PASS` (all validators and smoke tests green).
- Major changes:
    - Fixed clean template `--help` semantics (P1 safety gap).
    - Fixed dotfiles portability documentation (explicit `cp -a` instructions).
    - Fixed command path consistency in docs (Mode A vs Mode B namespace install).
    - Implemented `install.sh` (Interactive Installer MVP for non-programmers).
    - Generated all M40 fixup and final evidence reports.
- Startup route: `llms.txt` -> `state/MAIN.md` -> `workflow/MAIN.md`.
- Current blockers: none.

## Next Agent First Step

1. Read `llms.txt`.
2. Confirm state through `state/MAIN.md`.
3. Check `reports/m40-final-report.md` for portability validation results.
4. Prepare for the next milestone (M41).

## Persistent Context

Project type: AgentOS — governed workspace for AI-agent-driven development.
Stack: Markdown, GitHub, agent environments.
Architecture: canonical module routing.
Primary route: `llms.txt` and `ROUTES-REGISTRY.md`.
