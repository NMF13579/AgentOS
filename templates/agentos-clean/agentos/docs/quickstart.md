# Quickstart

## Local Installation

When copying this template into a local project, you must ensure hidden dotfiles (`.agentos/` and `.github/`) are copied.

Use a dotfile-preserving command:

```bash
cp -a templates/agentos-clean/. <target>/
```

Do not use `cp -r * <target>/` as it will skip the required dotfiles.

## Local Usage

### Where am I running this from?

Command paths depend on your installation. Do not mix these modes.

**Mode A — Inside copied template root**
If you are inside the copied template directory:

1. Create a task:
   `python3 agentos/scripts/new-task.py "Task title"`

2. Run validation:
   `python3 agentos/scripts/agentos-validate.py all`

**Mode B — From external project root with namespace install**
If you copied AgentOS into an isolated `agentos/` subdirectory, run these from your external project root (this is the recommended path for external testing):

1. Create a task:
   `python3 agentos/agentos/scripts/new-task.py "Task title"`

2. Run validation:
   `python3 agentos/agentos/scripts/agentos-validate.py all`

3. Check readiness:
   `python3 agentos/agentos/scripts/check-bootstrap-readiness.py`

## GitHub Usage

1. Go to Issues.
2. New issue → AgentOS Task Request.
3. Label as \`agentos-task\`.
