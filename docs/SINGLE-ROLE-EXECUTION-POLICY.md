# Single-Role Execution Policy

## Purpose
Prevent role mixing and unsafe self-verification in AI agent workflows. Enforce that each agent execution operates under exactly one declared role with deterministic boundaries.

## Single-Role Execution Rule
Each agent execution must operate under exactly one declared role. The declared role defines allowed actions, forbidden actions, writable paths, required evidence, and final report format.

If another role is needed, the agent must stop and create a role handoff request.

## Allowed Roles
- **planner**: Creates plans and task drafts.
- **implementor**: Modifies files allowed by task scope and provides evidence.
- **auditor**: Performs read-only checks and identifies findings.
- **verifier**: Runs validation and confirms acceptance criteria.
- **tutor**: Explains status and next safe actions.
- **researcher**: Collects sources and summarizes findings.
- **maintainer**: Modifies AgentOS core logic/policy only when explicitly authorized.

## Allowed Modes
- `read_only`
- `scoped_write`
- `explain_only`
- `research_only`
- `maintenance_scoped`

## Role Boundaries

### planner
- **May:** Create plans, task drafts, decomposition notes.
- **Must Not:** Modify production code, validators, or protected evidence.

### implementor
- **May:** Modify scoped files, create implementation evidence, run validators.
- **Must Not:** Approve own work, final-audit own work, weaken validation authority.

### auditor
- **May:** Read files, run read-only checks, write finding reports.
- **Must Not:** Modify code, validators, task contracts, or fix issues.

### verifier
- **May:** Run validation commands, compare results, write verification reports.
- **Must Not:** Patch code, fix failures, or approve own implementation.

### tutor
- **May:** Explain status/risk, suggest next actions.
- **Must Not:** Approve/deny, lower risk, or modify any files.

### researcher
- **May:** Collect sources, summarize findings, suggest best practices.
- **Must Not:** Apply implementation changes or update approved requirements.

### maintainer
- **May:** Modify AgentOS policy/docs/scripts if in scope.
- **Must Not:** Bypass approval or modify rules authorizing its own role in the same run.

## Validation Authority Boundary
An implementor must not weaken or modify the validation authority used to judge its own current task. Modification of validators, schemas, or fixtures requires a HIGH risk level and human approval.

## Path Matching
Enforcement uses normalized POSIX-style repository-relative paths. Forbidden matches always win over allowed matches. Broad paths (e.g., `.`, `/`, `*`) are forbidden for write-scope.
