<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- SOURCE_OF_TRUTH: no -->

# HANDOFF.md — Session Handoff Contract

HANDOFF is session context only.
It does not override canonical modules.

## Terminal Snapshot

- Milestone 36 (External MVP Usability) is COMPLETE.
- Template Initialization Hardening is COMPLETE.
- Current status: `M36_TEMPLATE_INITIALIZATION_SAFE`.
- Pipeline status: `PASS` (all validators and smoke tests green).
- Major changes:
    - Implemented `setup-repository.yml`: safe one-shot setup with self-destruct.
    - Cleaned up `.github/workflows/`: moved dev-only CI to `dev-only/`.
    - Removed `init-project.sh`: logic integrated into GitHub Action.
    - Updated `README.md`: simplified setup for template owners.
    - Fixed `agentos-validate.yml`: now correctly uses `requirements.txt`.
- Startup route: `llms.txt` -> `state/MAIN.md` -> `workflow/MAIN.md`.
- Current blockers: none.

## Next Agent First Step

1. Read `llms.txt`.
2. Confirm state through `state/MAIN.md`.
3. Verify that `setup-repository.yml` correctly handles repository names for new clones.
4. Prepare for M37 (External Pilot Readiness) planning.

## Persistent Context

Project type: AgentOS — governed workspace for AI-agent-driven development.
Stack: Markdown, GitHub, agent environments.
Architecture: canonical module routing.
Primary route: `llms.txt` and `ROUTES-REGISTRY.md`.
