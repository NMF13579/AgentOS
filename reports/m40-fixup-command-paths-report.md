# M40 Fixup — Clean Template Command Path Consistency

## Source Gap

M40 dogfooding found a path consistency gap in the clean template documentation. When the AgentOS clean template was copied into an external project under an isolated namespace (`agentos/`), the first-user command paths listed in the documentation (like `python3 agentos/scripts/new-task.py`) were incorrect from the perspective of the external project root. Users had to guess the correct paths (e.g., `agentos/agentos/scripts/...`), creating confusion.

## Files Changed

- `templates/agentos-clean/README.md`
- `templates/agentos-clean/agentos/docs/quickstart.md`
- `templates/agentos-clean/agentos/docs/bootstrap.md`
- `templates/agentos-clean/agentos/docs/use-template.md`

## Path Modes Documented

The documentation now explicitly distinguishes between two execution contexts:
- **Mode A: inside copied template root** - Commands are executed from within the template directory itself (e.g., `python3 agentos/scripts/...`).
- **Mode B: external project root with namespace install** - Commands are executed from the external project root when AgentOS is installed under an isolated `agentos/` subdirectory (e.g., `python3 agentos/agentos/scripts/...`). This is explicitly marked as the recommended path for M40-style external testing.

## Commands Documented

The following corrected commands are now documented for project-root usage (Mode B):
- `python3 agentos/agentos/scripts/new-task.py "Task title"` (or "Improve README")
- `python3 agentos/agentos/scripts/agentos-validate.py all`
- `python3 agentos/agentos/scripts/check-bootstrap-readiness.py`

## Validation Output Summary

- **grep for "Where am I running"**: Successfully found in `README.md`, `use-template.md`, `quickstart.md`, and `bootstrap.md`.
- **grep for "agentos/agentos/scripts"**: Confirmed present in all updated files, correctly defining the Mode B paths.
- **grep for "agentos/scripts"**: Confirmed present in all updated files, correctly defining the Mode A paths.
- **git status --short**:
  M templates/agentos-clean/README.md
  M templates/agentos-clean/agentos/docs/bootstrap.md
  M templates/agentos-clean/agentos/docs/quickstart.md
  M templates/agentos-clean/agentos/docs/use-template.md

## Remaining Gaps

None identified.

## Final Result

COMMAND_PATHS_FIX_PASS

## Safety Confirmation

- no scripts modified: CONFIRMED
- no dogfood sandbox modified: CONFIRMED
- no dependency install: CONFIRMED
- no full validation run: CONFIRMED
- no task created: CONFIRMED
- no commit: CONFIRMED
- no push: CONFIRMED
- no unrelated files modified: CONFIRMED
