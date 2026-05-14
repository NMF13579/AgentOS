# AgentOS Bootstrap

## Purpose

Bootstrap validation checks that this repository is a clean AgentOS project instance.

## Bootstrap Checks

- AgentOS validation
- bootstrap readiness
- clean history
- Simple Mode default
- issue template exists
- no forbidden history artifacts

## Validation Compatibility

### Where am I running this from?

Command paths depend on your installation. Do not mix these modes.

**Mode A — Inside copied template root**
The preferred command is:
`python3 agentos/scripts/agentos-validate.py all`
Fallback: `python3 agentos/scripts/agentos-validate.py`

**Mode B — From external project root with namespace install**
If AgentOS is installed under `agentos/` (recommended for external testing), run from the project root:
`python3 agentos/agentos/scripts/agentos-validate.py all`
Fallback: `python3 agentos/agentos/scripts/agentos-validate.py`
Check readiness: `python3 agentos/agentos/scripts/check-bootstrap-readiness.py`

Fallback is allowed only when no-argument validation passes.

## Safety Boundary

Bootstrap is read-only.

Bootstrap does not approve, commit, push, merge, or modify files.

## Result Tokens

- BOOTSTRAP_READY
- BOOTSTRAP_READY_WITH_WARNINGS
- BOOTSTRAP_NOT_READY
- BOOTSTRAP_BLOCKED

- CLEAN_HISTORY_OK
- CLEAN_HISTORY_OK_WITH_WARNINGS
- CLEAN_HISTORY_DIRTY
- CLEAN_HISTORY_BLOCKED
