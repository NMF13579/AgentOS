---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-04
task_id: 26.4.1
milestone: M26
---

# Write Allowlist Policy

## Purpose

The Write Allowlist Policy defines where an agent may write within the
pre-merge execution corridor, where writing is conditional, and where
writing is forbidden.

This document establishes:

- The defined write path categories available to an agent
- What each category allows and forbids
- When approval is required before a write may occur
- How write rules relate to permission levels
- How write rules relate to command categories
- How write rules relate to scope, commit/push, and M25
- How write approvals are recorded

**This document is a policy contract, not an implementation.**
It does not implement a write enforcement script.
It does not authorize enforcement, auto-merge, or automatic approval.

---

## Relationship to Pre-Merge Execution Corridor

The Write Allowlist Policy operates within the Pre-Merge Execution Corridor
defined in `docs/PRE-MERGE-EXECUTION-CORRIDOR.md`.

Write path categories do not expand corridor boundaries.
Write path categories do not replace corridor rules.
An allowed write path does not authorize actions outside the corridor.

The corridor remains the governing contract.
This policy is a supporting structure within the corridor.

---

## Relationship to Agent Permission Model

Write path categories intersect with permission levels defined in
`docs/AGENT-PERMISSION-MODEL.md`.

An agent must hold at minimum `LOCAL_EDIT` permission before any write
may occur.

Permission level defines the ceiling of allowed write operations.
Write path category defines the ceiling of allowed write destinations.

Effective write authorization = intersection of:

- Active permission level
- Active task scope
- Write path category
- Command category policy
- Approval records
- M25 enforcement constraints

An allowed write path does not expand declared scope.
An allowed write path does not authorize command execution.
An allowed write path does not authorize commit or push.
An allowed write path does not authorize modifying evidence.
An allowed write path does not override M25.
Write permission is not approval.

---

## Relationship to Command Allowlist Policy

Write path categories intersect with command categories defined in
`docs/COMMAND-ALLOWLIST-POLICY.md`.

A `WRITE_LOCAL` command may only write to `ALLOWED_WRITE_PATH` or
`CONDITIONAL_WRITE_PATH` if approved, within declared scope.

Both constraints must be satisfied for a write to be authorized:

- Command category must permit writing
- Write path must be `ALLOWED_WRITE_PATH` or approved `CONDITIONAL_WRITE_PATH`
- The write must remain within declared scope
- No higher-priority restriction may apply

A `WRITE_LOCAL` command targeting a `FORBIDDEN_WRITE_PATH` is a violation
regardless of permission level.
A `WRITE_LOCAL` command targeting a `PROTECTED_ZONE` without owner approval
is a violation regardless of permission level.

---

## Core Principle

> **Write path category is a maximum allowed write destination boundary.**
>
> Actual write authorization still depends on:
> - Active permission level
> - Active task scope
> - Command category policy
> - Approval records
> - M25 enforcement constraints
> - Active violations

A write to an allowed path does not grant rights beyond task scope.
A write to an allowed path does not bypass M25 enforcement.
A write to an allowed path does not constitute approval.

**Write permission is not approval.**
**Write approval is not merge approval.**
**Write approval is not push approval.**
**Allowed write path does not expand task scope.**
**Allowed write path does not authorize forbidden commands.**
**Allowed write path does not override M25.**
**Allowed write path does not authorize evidence tampering.**

---

## Write Path Categories

Seven write path categories are defined for M26:

| Category | Default Status | Requires Approval |
|---|---|---|
| `ALLOWED_WRITE_PATH` | Allowed within task scope | No, if within declared scope |
| `CONDITIONAL_WRITE_PATH` | Requires additional approval | Yes |
| `FORBIDDEN_WRITE_PATH` | Blocked for normal agent execution | Not authorizable as silent agent write |
| `PROTECTED_ZONE` | Blocked by default | Yes - explicit owner-controlled exception |
| `EVIDENCE_ARTIFACT` | Protected | Append-only if in-progress; read-only if completed |
| `GENERATED_ARTIFACT` | Allowed if task-scoped and documented | Depends on task policy |
| `TEMP_ARTIFACT` | Allowed if uncommitted and documented | No, if documented |

---

## Category Definitions

### ALLOWED_WRITE_PATH

A path explicitly permitted by the active task scope and declared in
`allowed_write_paths`.

- Agent may write to this path when holding `LOCAL_EDIT` or higher
- Write must remain within `declared_scope`
- Write must be recorded in the execution review
- Write does not authorize commit or push

**Typical AgentOS examples:**

- `docs/` - when task explicitly scopes documentation changes
- `templates/` - when task explicitly scopes template changes
- `reports/milestone-26-*.md` - for in-progress M26 evidence updates

---

### CONDITIONAL_WRITE_PATH

A path that requires additional approval before a write may occur.

- Agent may not write to this path without documented approval
- Approval must be recorded in a write scope record
- Approval must be explicit and human-reviewed
- Risk level must be assessed at MEDIUM or above

**Conditions may include:**

- Human reviewer approval
- Explicit task contract permission for the specific path
- Risk assessment documented at MEDIUM or higher
- Scope boundary confirmation

**Typical examples:**

- `docs/` subdirectories not explicitly listed in declared scope
- `reports/` directories for in-progress milestones not owned by this task
- Configuration files not protected but not explicitly scoped

---

### FORBIDDEN_WRITE_PATH

A path that must not be written by the agent during normal M26 corridor execution.

- Agent may not write to this path during normal M26 corridor execution
- Agent may not write to this path silently
- Agent may not write to this path only because it is adjacent to allowed scope
- Any attempted write to a `FORBIDDEN_WRITE_PATH` is a corridor violation

Owner approval does not convert a forbidden write path into a normal agent write.

If owner-approved maintenance requires changing such a path, it must be handled as a separate owner-controlled task or explicitly reviewed exception, not as silent agent write.

**Includes at minimum:**

- `.github/workflows/` - CI/CD workflow files
- `.github/` configuration files
- `scripts/` - enforcement and utility scripts
- `tests/` - test fixtures and smoke tests
- `reports/milestone-25-*` - completed M25 evidence
- `reports/platform-required-checks-evidence.md`
- `docs/PRE-MERGE-EXECUTION-CORRIDOR.md`
- `docs/AGENT-PERMISSION-MODEL.md`
- `docs/COMMAND-ALLOWLIST-POLICY.md`
- `docs/ENFORCEMENT-OVERRIDE-POLICY.md`
- `templates/enforcement-review.md`
- Branch protection configuration files
- Completed milestone evidence reports from prior milestones

---

### PROTECTED_ZONE

A high-risk system path that requires explicit owner approval before any write.

Protected zones are not normal write targets.

- Protected zones are blocked by default
- Owner approval may authorize a reviewed, task-scoped, owner-controlled exception
- Owner approval does not convert protected-zone writes into normal agent writes
- Owner approval does not authorize silent agent write
- Owner approval does not authorize bypassing M25
- Owner approval must be recorded before the write occurs

If a path is both `FORBIDDEN_WRITE_PATH` and `PROTECTED_ZONE`, the stricter rule applies:

- Normal agent write remains blocked
- Any exception requires owner-controlled review
- The write must be explicitly task-scoped
- The exception must be recorded in a write scope record
- The exception must not modify completed evidence artifacts unless a separate owner-controlled evidence correction process exists

**Protected zones include at minimum:**

- `.github/workflows/`
- `scripts/`
- `docs/ENFORCEMENT-OVERRIDE-POLICY.md`
- `templates/enforcement-review.md`
- `reports/milestone-25-*`
- `reports/platform-required-checks-evidence.md`
- Completed milestone evidence reports
- Branch protection docs

**Owner approval requirements:**

- Approval must come from the repository owner or designated maintainer
- Approval must be recorded in a write scope record with decision `WRITE_SCOPE_APPROVED`
- Approval must be time-stamped and linked to the active task
- Approval cannot be simulated by the agent
- Approval cannot be granted by CI

---

### EVIDENCE_ARTIFACT

A report, audit record, or evidence file that must be protected from tampering.

Evidence artifacts are protected, but not all evidence artifacts are immutable at all times.

Mutability depends on milestone status:

- In-progress evidence reports are append-only for authorized task entries
- Existing completed entries must not be modified
- Completed milestone evidence artifacts are read-only
- Completed milestone evidence artifacts must not be deleted
- Completed milestone evidence artifacts must not be overwritten
- Evidence deletion is forbidden

A file with `type: evidence` in YAML frontmatter is protected, not automatically immutable.

### In-Progress Evidence Rules

New evidence entries may be appended to in-progress evidence reports only when:

- The active task is authorized to append the new entry
- The append is explicitly within task scope
- The append does not alter existing completed entries
- The append does not rewrite prior evidence
- The append is recorded in the execution review

### Completed Evidence Rules

Completed evidence artifacts must not be modified except through a separate owner-controlled evidence correction process.

Any unauthorized modification to a completed evidence artifact is evidence tampering.

Evidence tampering is a `FORBIDDEN` action and results in `BLOCKED` state.

**Evidence artifact examples:**

- `reports/milestone-25-*`
- `reports/platform-required-checks-evidence.md`
- Completed entries within `reports/milestone-26-evidence-report.md`
- Any file classified as `type: evidence` in its YAML frontmatter

---

### GENERATED_ARTIFACT

A file generated as intended output of task execution.

Generated artifacts differ from temp artifacts in persistence:

- `GENERATED_ARTIFACT` may persist after task completion if task-scoped and documented
- `TEMP_ARTIFACT` must not persist after task completion unless cleanup is unsafe or not required by task policy

**Rules:**

- Generation must be explicitly within task scope
- Generated artifact path must be listed in `expected_generated_artifacts`
  in the write scope record or execution review
- Generated artifact may be committed only if it is an intended task output, inside declared scope, and listed in `expected_generated_artifacts`
- Generated artifact must not overwrite an evidence artifact
- Generated artifact must not be placed in a protected zone
- Generation rule must not be used to bypass write allowlist by labeling
  substantive source changes as "generated"

**Typical examples:**

- Built documentation output
- Generated schema files scoped to the task
- Rendered reports explicitly created by the task

---

### TEMP_ARTIFACT

A temporary, cache, or test artifact created as incidental output of
command execution.

Temp artifacts differ from generated artifacts in persistence:

- `TEMP_ARTIFACT` must not be committed
- `TEMP_ARTIFACT` should not persist after task completion unless cleanup is unsafe or not required by task policy
- `GENERATED_ARTIFACT` may persist if task-scoped and documented

**Rules:**

- Temp artifact path must be listed in the pre-merge execution review
- Temp artifact path must be listed in the write scope record or command
  approval record if approval was required
- Temp artifact must not be committed to the repository
- Temp artifact must be cleaned up after task or command completes
  when cleanup is safe and required by task policy
- If cleanup is not required or not safe, artifact must remain uncommitted
  and explicitly documented in the execution review
- Temp artifact must not be placed in a protected zone
- Temp artifact must not overwrite an evidence artifact

**Typical examples:**

- `.coverage` - Python coverage data
- `htmlcov/` - HTML coverage report directory
- `.pytest_cache/` - pytest cache
- `__pycache__/` - Python bytecode cache
- `*.pyc` files
- Any `.tmp` or `.log` file created by a test or validation command
- Dependency directories created by local install/test commands only if explicitly documented; they must remain uncommitted

---

## Allowed Write Paths

The following paths are allowed by default when explicitly included in
`declared_scope` for the active task:

| Path Pattern | Notes |
|---|---|
| `docs/*.md` | Documentation files within task scope |
| `templates/*.md` | Template files within task scope |
| `reports/milestone-26-*.md` | In-progress M26 evidence updates |
| `reports/command-approvals/` | Command approval records |
| `reports/permissions/` | Permission records |
| `reports/write-scope/` | Write scope records |

**These paths are allowed only when:**

- The active task explicitly declares them in `declared_scope`
- The agent holds `LOCAL_EDIT` or higher
- No open violations exist
- The write is recorded in the execution review

Inclusion in this table does not authorize writing without task scope declaration.

---

## Conditional Write Paths

The following paths require additional approval before a write may occur:

| Path Pattern | Condition Required |
|---|---|
| `docs/` paths not in declared scope | Human reviewer approval |
| `reports/` directories for other milestones | Task contract permission + human review |
| Config files outside protected zones | Risk assessment at MEDIUM; task scope confirmation |
| Any path with `authority: canonical` in frontmatter | Explicit owner approval |

If a path is not in `declared_scope` and not in the conditional table,
it defaults to `FORBIDDEN_WRITE_PATH` for that task execution.

---

## Forbidden Write Paths

The following paths are forbidden for normal agent writes:

| Path Pattern | Reason |
|---|---|
| `.github/workflows/` | CI/CD system files |
| `.github/` | Repository configuration |
| `scripts/` | Enforcement and utility scripts |
| `tests/` | Test fixtures and smoke tests |
| `reports/milestone-25-*` | Completed milestone evidence |
| `reports/platform-required-checks-evidence.md` | Platform evidence artifact |
| `docs/PRE-MERGE-EXECUTION-CORRIDOR.md` | Locked corridor contract |
| `docs/AGENT-PERMISSION-MODEL.md` | Locked permission model |
| `docs/COMMAND-ALLOWLIST-POLICY.md` | Locked command policy |
| `docs/ENFORCEMENT-OVERRIDE-POLICY.md` | Enforcement override policy |
| `templates/enforcement-review.md` | Enforcement review template |
| Branch protection docs | Repository governance |
| Completed milestone evidence reports | Evidence integrity |

Any normal agent write to a forbidden path is a corridor violation.
Any corridor violation from a forbidden write results in permission reduction or `BLOCKED` state.

Owner-controlled exceptions must be handled through protected-zone review and must not be silent agent writes.

---

## Protected Zones

Protected zones are high-risk paths requiring explicit owner approval.

| Zone | Owner Approval Required |
|---|---|
| `.github/workflows/` | Repository owner |
| `scripts/` | Repository owner or designated maintainer |
| `docs/ENFORCEMENT-OVERRIDE-POLICY.md` | Repository owner |
| `templates/enforcement-review.md` | Repository owner |
| `reports/milestone-25-*` | Repository owner |
| `reports/platform-required-checks-evidence.md` | Repository owner |
| Completed milestone evidence reports | Repository owner |
| Branch protection docs | Repository owner |

Owner approval rules:

- Must be from human repository owner or designated maintainer
- Must be recorded in write scope record
- Must be time-stamped and task-linked
- Cannot be simulated or granted by agent or CI
- Does not convert the write into a normal agent write
- Does not authorize M25 bypass

---

## Evidence and Audit Artifact Protection

Evidence and audit artifacts have high protection in M26.

### Rules

- In-progress evidence reports are append-only for authorized task entries
- Existing completed entries must not be modified
- Completed milestone evidence artifacts must not be modified
- Completed evidence artifacts must not be deleted
- Completed evidence artifacts must not be overwritten
- Evidence deletion is forbidden
- In-progress evidence reports may receive new appended entries only when:
  - The active task is the evidence report owner for that entry
  - The append is explicitly within task scope
  - The append does not alter existing completed entries
- Any alteration of a completed entry is evidence tampering
- Evidence tampering is a `FORBIDDEN` action
- Evidence tampering results in `BLOCKED` state

### Evidence Artifact Identification

A file is an evidence artifact if any of the following are true:

- The file has `type: evidence` in its YAML frontmatter
- The file is in `reports/milestone-*` and the milestone is completed
- The file is `reports/platform-required-checks-evidence.md`
- The file is explicitly designated as an evidence artifact in a task contract

`type: evidence` means protected. It does not always mean immutable while the milestone is in progress.

---

## Deletion Rules

File deletion within task scope requires explicit task authorization.

- Deletion is not implied by `LOCAL_EDIT` permission
- Deletion must be explicitly stated in the task contract
- Deletion target must be within `declared_scope`
- Deletion of evidence artifacts is forbidden unless handled by separate owner-controlled correction process
- Deletion of protected zone files is forbidden during normal agent execution
- Deletion must be recorded in `deletions_requested` in the write scope record
- Deletion of temp artifacts during cleanup is permitted when task policy allows

---

## Generated Artifact Rules

- Generated artifact must be explicitly within task scope
- Path must be listed in `expected_generated_artifacts`
- Generated artifact may be committed only if it is an intended task output, inside declared scope, and listed in `expected_generated_artifacts`
- Must not overwrite evidence artifacts
- Must not be placed in a protected zone
- Generation rule must not be used to bypass write allowlist by labeling
  outputs as "generated" when they are substantive source changes

---

## Temp Artifact Rules

- Path must be listed in pre-merge execution review
- Must not be committed
- Must be cleaned up after task or command completion when safe and required
- If cleanup is not safe or not required, must remain uncommitted and documented
- Must not be placed in a protected zone
- Must not overwrite evidence artifacts
- Persistence after task completion requires explicit documentation

---

## Approval Requirements

| Write Category | Approval Required | Approver |
|---|---|---|
| `ALLOWED_WRITE_PATH` | No, if in declared scope | N/A |
| `CONDITIONAL_WRITE_PATH` | Yes | Human reviewer or task contract |
| `FORBIDDEN_WRITE_PATH` | Not authorizable as silent agent write | Not applicable |
| `PROTECTED_ZONE` | Yes - explicit owner-controlled exception | Repository owner |
| `EVIDENCE_ARTIFACT` | Append-only if in-progress; read-only if completed | Task owner / repository owner depending on status |
| `GENERATED_ARTIFACT` | Depends on task policy | Human reviewer or task contract |
| `TEMP_ARTIFACT` | No, if documented and uncommitted | N/A |

**Approval rules:**

- Approval cannot be simulated by the agent
- Approval cannot be granted by CI
- Approval cannot be derived from evidence reports
- Approval cannot be automatic or anonymous
- Approval must be recorded in a write scope record when required
- Write approval is not merge approval
- Write approval does not satisfy M25 override requirements
- Owner approval does not authorize silent agent write

---

## Relationship to Scope Control

Write path category does not expand declared scope.

- An agent may only write to paths within `declared_scope`
- An `ALLOWED_WRITE_PATH` outside `declared_scope` is not authorized
- A `CONDITIONAL_WRITE_PATH` outside `declared_scope` requires scope
  expansion approval in addition to conditional write approval
- Scope remains the primary boundary
- Write path category is a destination constraint within that boundary

Scope checking is planned in `scripts/check-pre-merge-scope.py` - Task 26.5.1.

---

## Relationship to Command Control

Write path category intersects with command category policy.

- `WRITE_LOCAL` commands are the primary command category for writes
- Write path category further constrains where `WRITE_LOCAL` may target
- Both command category and write path category must authorize a write
- A `WRITE_LOCAL` command to a `FORBIDDEN_WRITE_PATH` is always a violation
- A `WRITE_LOCAL` command to a `PROTECTED_ZONE` without owner approval
  is always a violation

Command allowlist policy is defined in `docs/COMMAND-ALLOWLIST-POLICY.md`.

---

## Relationship to Commit / Push Boundary

- Allowed write path does not authorize commit
- Allowed write path does not authorize push
- Commit requires `COMMIT_REQUEST` permission + preconditions from Task 26.7.1
- Push requires `PUSH_REQUEST` permission + explicit push approval
- Write approval does not imply commit or push approval
- Push to `dev` or `main` is never authorized by write path category alone

Commit/push control is planned in `scripts/check-commit-push-preconditions.py` - Task 26.7.1.

---

## Relationship to M25 Enforcement

Write path categories operate within M25 enforcement boundaries.

A write to any category does not:

- Change or override M25 outcomes
- Convert FAIL, ERROR, WARN, NOT_RUN, or INCOMPLETE to PASS
- Authorize bypassing M25 required checks
- Authorize merge without M25 passing
- Satisfy M25 override requirements

Write approval does not satisfy M25 override requirements.
M25 enforcement remains active and unchanged.

---

## Evidence Requirements

Every write to a `CONDITIONAL_WRITE_PATH`, `PROTECTED_ZONE`, or path
outside default `ALLOWED_WRITE_PATH` must be recorded using
`templates/write-scope-record.md`.

Deletions must always be recorded in the write scope record.

The following must be traceable for each recorded write scope decision:

- Write scope record ID
- Active task ID
- Declared scope
- Allowed write paths
- Conditional write paths with approval records
- Forbidden write paths: confirmation of no normal agent writes
- Protected zones: confirmation of no writes or owner-controlled exception
- Requested write paths
- Expected generated artifacts
- Expected temp artifacts
- Deletions requested
- Risk level
- Whether approval was required and obtained
- Conditions attached to approval
- Expiration of approval
- Open violations at time of decision
- Decision outcome
- Reviewer identity

**Write scope record alone is not approval.**
**Only an explicit human decision inside the record may approve an approvable write scope.**
**WRITE_SCOPE_APPROVED is not merge approval.**
**Write scope record does not authorize push.**
**Write scope record does not satisfy M25 override requirements.**

---

## Non-Goals

This document does not implement:

- Write enforcement script
- Scope diff checker
- Command enforcement script
- Commit/push control script
- Agent runner
- Remote approval application
- Messenger or notification-based approvals
- Autonomous retry loop
- Auto-merge
- Automatic approval
- Self-healing commits
- Branch protection changes

### This Task Must Not

- Claim that write enforcement is implemented
- Claim that write path categories are machine-enforced
- Suggest that an allowed write path bypasses scope or M25
- Define scope diff check logic, which belongs to Task 26.5.1
- Define commit/push precondition logic, which belongs to Task 26.7.1

---

## M26 Follow-Up Tasks

| Task | Title | Creates |
|---|---|---|
| 26.5.1 | Scope-Bound Diff Checker | `scripts/check-pre-merge-scope.py` |
| 26.6.1 | No Direct Push Policy | `docs/NO-DIRECT-PUSH-POLICY.md` |
| 26.7.1 | Commit / Push Control Script | `scripts/check-commit-push-preconditions.py` |
| 26.8.1 | Agent Violation / Sanctions Policy | `docs/AGENT-VIOLATION-POLICY.md` |
| 26.9.1 | Bounded Retry Loop Policy | `docs/BOUNDED-RETRY-POLICY.md` |
| 26.10.1 | Pre-Merge Corridor Audit Script | `scripts/audit-pre-merge-corridor.py` |
| 26.11.1 | Pre-Merge Corridor Smoke Fixtures | `tests/fixtures/pre-merge-corridor/` |
| 26.12.1 | M26 Evidence Report | `reports/milestone-26-evidence-report.md` |
| 26.13.1 | M26 Completion Review | `reports/milestone-26-completion-review.md` |

---

## Final Reminder

Write enforcement is not implemented by this document.
This document establishes the M26 write allowlist policy contract only.
Enforcement artifacts are created in follow-up tasks 26.5.1 through 26.13.1.

Until 26.5.1, 26.7.1, 26.10.1, and 26.11.1 are complete,
write boundaries cannot be machine-verified.
