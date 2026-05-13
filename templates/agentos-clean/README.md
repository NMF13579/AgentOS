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

Advanced users may run:

python3 agentos/scripts/new-task.py "Improve README"
python3 agentos/scripts/agentos-validate.py all

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
