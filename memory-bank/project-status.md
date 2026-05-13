# memory-bank/project-status.md

Non-runtime project note.

Use `state/MAIN.md` for current state and recovery.
Use `workflow/MAIN.md` for execution boundaries.
Use `quality/MAIN.md` for proof before completion.

Current summary:

- Milestone 36 (External MVP Usability) is COMPLETE (2026-05-10).
- Template Initialization Hardening is COMPLETE (2026-05-13).
- All P0 external usability blockers REPAIRED.
- Project state: `M36_TEMPLATE_INITIALIZATION_SAFE`.
- Pipeline status: GREEN (`PASS` for all core validators).
- Major Implementation:
    - One-shot `setup-repository.yml` with self-destruct logic.
    - CI workflow reorganization (dev-only workflows moved).
    - GitHub Action-based repo initialization.
- AgentOS now routes runtime behavior through five canonical modules.
- `llms.txt` is the only agent startup entry.
- `ROUTES-REGISTRY.md` records canonical module ownership.
