# Use This Template

## Purpose

This document explains how to start a clean AgentOS project from this template.

## Start

1. Click "Use this template" in GitHub.
2. Create your repository.
3. Open a new issue using "AgentOS Task Request".

AgentOS starts in Simple Mode by default.

## Local Copy

If you are copying this template into an existing project locally, you **must** include hidden dotfiles (`.agentos/` and `.github/`).

Do not use unsafe copy commands like `cp -r * <target>/`.

Instead, use a dotfile-preserving command:

```bash
cp -a templates/agentos-clean/. <target>/
```

### Where am I running this from?

Depending on how you copied AgentOS (`<target>/`), your command paths will differ. Do not mix these modes.

**Mode A — Inside copied template root**
If your target was the project root, commands look like:
`python3 agentos/scripts/agentos-validate.py all`

**Mode B — From external project root with namespace install**
If you isolated AgentOS into an `agentos/` subdirectory (`<target>` was `agentos/`), run commands from your external project root (recommended for external testing):
`python3 agentos/agentos/scripts/agentos-validate.py all`
`python3 agentos/agentos/scripts/check-bootstrap-readiness.py`
`python3 agentos/agentos/scripts/new-task.py "Task title"`


## What Happens Automatically

The bootstrap workflow checks:

- clean project structure
- Simple Mode default
- no previous AgentOS project history
- no old milestone reports
- no old tasks
- no old evidence reports

## What Does Not Happen Automatically

The bootstrap workflow does not:

- approve actions
- commit files
- push changes
- change AgentOS mode
- grant extra permissions
- clean dirty source history
- replace human review

## Advanced / Full Mode

Advanced and Full modes reveal more information.

They do not grant the agent extra permissions.

## Non-Claims

This template does not claim:

- production readiness
- production-grade sandboxing
- guaranteed safe AI output
- automatic approval safety
- SaaS readiness
