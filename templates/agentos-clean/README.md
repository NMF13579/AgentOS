# AgentOS Clean Project

This repository was created from the AgentOS clean template.

AgentOS starts in Simple Mode by default.

## Start in 2 steps

1. Create an AgentOS task:
   New issue → AgentOS Task Request

2. Follow the task result and validation reports.

## Simple Mode

Simple Mode shows only the basic path:

- what task is active
- what risk exists
- what the next safe action is
- where validation results appear

## Want more control?

Read:

- agentos/docs/user-modes.md

Advanced and Full modes reveal more details, but they do not grant the agent extra permissions.

## Optional local command

### Where am I running this from?

Depending on how you installed AgentOS, your command paths will differ. Do not mix these modes.

**Mode A — Inside copied template root**
If you are running commands from inside the copied AgentOS root directory:
```bash
python3 agentos/scripts/new-task.py "Improve README"
python3 agentos/scripts/agentos-validate.py all
```

**Mode B — From external project root with namespace install**
If you copied AgentOS into an isolated namespace (e.g., `agentos/`) inside your existing project, run these commands from your external project root:
```bash
python3 agentos/agentos/scripts/new-task.py "Improve README"
python3 agentos/agentos/scripts/agentos-validate.py all
python3 agentos/agentos/scripts/check-bootstrap-readiness.py
```
*Note: Keeping AgentOS isolated under `agentos/` and running from the project root is the recommended path for M40-style external testing.*

## Local Copy

When copying this template into a local project, ensure hidden dotfiles (`.agentos/` and `.github/`) are preserved.

Use a dotfile-preserving command:

```bash
cp -a templates/agentos-clean/. <target>/
```

Do not use `cp -r * <target>/`.

## What this template is

AgentOS is a repo-based guardrail framework for AI coding workflows.

## What this template is not

It is not production-grade sandboxing.
It does not guarantee safe AI output.
It does not replace human review.
It does not authorize bypassing validation or human gates.

## Bootstrap Validation

Bootstrap validation runs automatically through GitHub Actions when available.
It ensures that the project structure is clean and correctly configured.

To learn more:

- agentos/docs/use-template.md
- agentos/docs/bootstrap.md

Bootstrap validation runs automatically through GitHub Actions when available.

To learn more:

- agentos/docs/use-template.md
- agentos/docs/bootstrap.md
