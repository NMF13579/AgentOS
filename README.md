# AgentOS

AgentOS is a programmable guardrail layer for AI-assisted coding workflows.
It helps structure tasks, scope, validation, evidence, and human checkpoints.

## Who is AgentOS for?

AgentOS is for developers and teams using AI coding assistants (like Cursor, GitHub Copilot, or Claude Code) who want to enforce structured task boundaries, mandatory validation, and explicit human approval before accepting AI-generated changes.

## What AgentOS is not

**Important boundaries:**
- AgentOS is **not a full autonomous** agent platform.
- AgentOS is **not a backend** service.
- AgentOS is **not a vector** database or full RAG backend.
- AgentOS is **not** a web UI, cloud platform, dashboard, or marketplace.
- AgentOS **does not guarantee** bug-free AI output.
- AgentOS does **not** replace human approval or act as production deployment approval.
- AgentOS does **not** currently feature LangGraph, CrewAI, multi-agent orchestration, or a self-heal platform.

## First Safe Commands

To start using AgentOS or verify your repository state, run these commands in order:

```bash
# 1. Validate the active task contract
python3 scripts/validate-task.py tasks/active-task.md

# 2. Run the core validation suite (tasks and verification)
bash scripts/run-all.sh

# 3. Run the official full unified validation
python3 scripts/agentos-validate.py all

# 4. Check MVP release readiness
python3 scripts/audit-mvp-readiness.py
```
*(If a command is not available, ensure you have run the installation script or cloned the full repository).*

## Understanding Validation Results

When you run validation commands, you will see one of the following results:

- **PASS:** The checked area passed completely.
- **PASS_WITH_WARNINGS:** The checked area is usable, but known (non-blocking) gaps remain.
- **BLOCKED:** Execution or readiness is stopped until a specific blocker is resolved.
- **NOT_READY:** The system is not ready for the claimed use yet.
- **INCONCLUSIVE:** The check could not produce trustworthy evidence.

**If validation fails:**
- Do **not** treat failure as success.
- Read the command output carefully.
- Check the relevant generated report in the `reports/` directory.
- Fix only the scoped blocker.
- Rerun the exact same command to verify the fix.
- Do **not** proceed to release or deployment based on failed validation.

## Where to read more

- **Installation Guide:** [docs/installation.md](docs/installation.md)
- **First Project Onboarding:** [docs/first-project-onboarding.md](docs/first-project-onboarding.md)
- **Getting Started:** [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md)
- **Quickstart:** [docs/quickstart.md](docs/quickstart.md)
- **Validation Guide:** [docs/VALIDATION.md](docs/VALIDATION.md)
- **Safety Boundaries:** [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md)

## Example Projects

To see how AgentOS works in practice, inspect the example project:
- `examples/simple-project/` (Run `bash scripts/test-example-project.sh` to test it).

---
*The current architecture is canonical-module driven: agents and owners navigate through a small set of runtime modules instead of scattered rule files.*

## Core Principles

- **Markdown-first:** All configuration, contracts, and reports are human-readable Markdown files
- **Human-approved execution boundaries:** Execution requires explicit human approval at defined checkpoints
- **Explicit task contracts:** Task contracts are explicit and human-readable
- **Single executable contract:** `tasks/active-task.md` is the only executable task contract
- **Non-executable briefs:** Task Briefs (TASK.md) are not executable; they require validation and approval first
- **Automation follows validation:** Automation only proceeds after manual validation and human approval
- **Read-only checks by default:** Checkers and runners are read-only unless explicitly documented otherwise
- **No autonomous execution:** No part of AgentOS executes tasks without human checkpoints

## Current Capabilities

- Project initialization and discovery layer
- Spec wizard and task brief flow
- Task brief validation
- Review and trace artifacts
- Contract draft generation
- Queue lifecycle scaffolding
- Runner dry-run protocol
- Task health metrics
- Unified validation wrapper for official validation entrypoint
- **Template integrity checker** – validates required project structure
- **Negative fixture runner** – ensures invalid inputs are rejected
- **Guard failure runner** – aggregates guard and failure checks
- **Audit runner** – aggregates release-readiness validation

## Quick Start

Run validation checks in order:

```bash
# Official full validation entrypoint
python3 scripts/agentos-validate.py all

# Official machine-readable validation entrypoint
python3 scripts/agentos-validate.py all --json
```

Focused validation commands remain available for debugging specific checks:

```bash
python3 scripts/agentos-validate.py template
python3 scripts/agentos-validate.py negative
python3 scripts/agentos-validate.py guard
python3 scripts/agentos-validate.py audit
python3 scripts/agentos-validate.py queue
python3 scripts/agentos-validate.py runner
```

See [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) for detailed getting started guide.

## Validation and Audit

AgentOS provides validation at multiple layers:

| Level | Tool | Purpose |
|---|---|---|
| **Unified Validation** | `scripts/agentos-validate.py all` | Official human-readable full validation |
| **Unified Validation JSON** | `scripts/agentos-validate.py all --json` | Official machine-readable validation |
| **Focused Validation** | `scripts/agentos-validate.py template`, `negative`, `guard`, `audit`, `queue`, `runner` | Debugging focused checks |
| **Underlying Validators** | `scripts/check-template-integrity.py --strict`, `scripts/test-negative-fixtures.py`, `scripts/test-guard-failures.py`, `scripts/audit-agentos.py`, `scripts/validate-queue.py`, `scripts/validate-runner-protocol.py` | Advanced validator-specific reference |

For detailed information, see [docs/VALIDATION.md](docs/VALIDATION.md).

## Safety Boundaries

AgentOS enforces strict safety boundaries:

- **Does not execute tasks automatically**
- **Does not replace `tasks/active-task.md` without explicit human approval**
- **Does not move queue items autonomously**
- **Does not run runner protocol scripts unless explicitly invoked by user**
- **Does not approve execution**
- **Does not act as a release checklist** (yet)

For detailed information, see [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md).

## Repository Map

Key documentation files:

- [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) – Getting started guide and task flow
- [docs/VALIDATION.md](docs/VALIDATION.md) – Validation layers and command reference
- [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md) – Safety boundaries and execution rules
- [tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md](tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md) – Template integrity checker
- [tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md](tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md) – Negative fixture tests
- [tools/guard-failure/TEST-GUARD-FAILURES.md](tools/guard-failure/TEST-GUARD-FAILURES.md) – Guard failure runner
- [tools/audit/AUDIT-AGENTOS.md](tools/audit/AUDIT-AGENTOS.md) – Audit runner
- [repo-map.md](repo-map.md) – Complete repository structure

## Non-Goals

AgentOS does not aim to be:

- An autonomous coding agent
- A backend framework
- A RAG platform
- A general-purpose orchestration platform
- A replacement for human review

## Current Status

**Current milestone:** M39 Release Candidate Freeze

**Previously completed:**
- Milestone 37: External Pilot Readiness
- Milestone 38: Pilot Feedback Hardening
- Single-Role Execution Guard MVP
- Template Integrity – validates required project structure
- Negative Fixtures – ensures invalid inputs are rejected
- Guard Failure Runner – aggregates guard and failure checks
- Audit Runner – release-readiness validation

## Start Here

| Need | Read |
|---|---|
| Quick start with AgentOS | [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) |
| Validation commands | [docs/VALIDATION.md](docs/VALIDATION.md) |
| Safety boundaries | [docs/SAFETY-BOUNDARIES.md](docs/SAFETY-BOUNDARIES.md) |
| Agent startup | `llms.txt` |
| Route overview | `ROUTES-REGISTRY.md` |
| Rule priority and authority | `core-rules/MAIN.md` |
| Current state, recovery, transitions | `state/MAIN.md` |
| Planning and execution flow | `workflow/MAIN.md` |
| Verification and release readiness | `quality/MAIN.md` |
| Sensitive data and access boundaries | `security/MAIN.md` |

## Canonical Runtime Modules

| Module | Owns |
|---|---|
| `core-rules/MAIN.md` | Priority, authority, governance, agent boundaries |
| `state/MAIN.md` | State lifecycle, events, recovery, transitions |
| `workflow/MAIN.md` | Plan gate, scope control, execution boundaries, one-task rule |
| `quality/MAIN.md` | Verification, smoke checks, release blockers, audit output |
| `security/MAIN.md` | Sensitive data, least privilege, compliance, security stop conditions |

## Common Situations

| Situation | Route |
|---|---|
| I need to continue work | `state/MAIN.md` |
| I need a plan before changes | `workflow/MAIN.md` |
| The task is expanding | `workflow/MAIN.md` |
| I need to know which instruction wins | `core-rules/MAIN.md` |
| I need proof that the task is done | `quality/MAIN.md` |
| I am preparing for merge or release | `quality/MAIN.md` and `security/MAIN.md` |
| The task touches personal data, auth, access, API, or database | `security/MAIN.md` |
| The agent is unsure what to read | `ROUTES-REGISTRY.md`, then ask the owner if no route fits |

## Working Rule

- Use `llms.txt` as the only agent startup path.
- Use `ROUTES-REGISTRY.md` only to confirm module ownership.
- Keep runtime behavior inside the five canonical modules.
- Do not treat archive, adapter, support, or notes files as runtime authority.
- If the current module does not answer the situation, stop and ask the owner instead of guessing.
## Example scenarios

Practical documentation scenarios are available in:

- `examples/README.md`
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`

These examples are not executable fixtures. They illustrate expected AgentOS workflows and safety boundaries.

## Prompt packs

Ready-to-use prompt packs are available in:

- `prompt-packs/README.md`
- `prompt-packs/cursor.md`
- `prompt-packs/claude-code.md`
- `prompt-packs/codex-cli.md`
- `prompt-packs/chatgpt.md`

Prompt packs help AI coding tools follow AgentOS safety boundaries, read the right context, and run the right validation commands.

## Release checklist

Release readiness checklist:

- `RELEASE-CHECKLIST.md`
- `tools/release/RELEASE-CHECKLIST.md`
- `reports/release-checklist.md`

Release approval is manual. AgentOS does not approve release automatically.

## Setup

After cloning, run:

```bash
bash scripts/install-hooks.sh
```
