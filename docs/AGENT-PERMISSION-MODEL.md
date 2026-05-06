---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-03
task_id: 26.2.1
milestone: M26
---

# Agent Permission Model

## Purpose

The Agent Permission Model defines what level of capability an agent holds during
pre-merge execution within the M26 corridor.

This document establishes:

- The defined permission levels available to an agent
- What each level allows and forbids
- When permission may be increased or must be reduced
- How permissions relate to scope, commands, writes, commit, push, and M25
- How permission decisions are recorded

**This document is a policy contract, not an implementation.**
It does not authorize enforcement, auto-merge, or automatic approval.
It does not implement any permission enforcement script.

---

## Relationship to Pre-Merge Execution Corridor

The Agent Permission Model operates within the Pre-Merge Execution Corridor
defined in `docs/PRE-MERGE-EXECUTION-CORRIDOR.md`.

Permission levels do not expand corridor boundaries.
Permission levels do not replace corridor rules.
Permission levels define the maximum capability ceiling within the corridor.

The corridor remains the governing contract.
The permission model is a supporting structure within the corridor.

---

## Core Principle

> **Permission level is a maximum allowed capability.**
>
> Actual action still depends on:
> - Active task scope
> - Declared scope boundaries
> - Command classification policy
> - Write allowlist policy
> - Approval records
> - M25 enforcement constraints
> - Active violations

A higher permission level does not grant more rights than the task scope allows.
A higher permission level does not bypass M25 enforcement.
A higher permission level does not constitute approval.

**Permission is not approval.**
**Permission is not enforcement.**
**Permission is not merge authorization.**
**Permission is not push authorization.**

---

## Permission Levels

Seven permission values are defined for M26:

| Permission | Default Capability |
|---|---|
| `READ_ONLY` | Inspect and summarize only |
| `PATCH_PROPOSE` | Propose patch text; no file writes |
| `LOCAL_EDIT` | Edit allowed files within scope |
| `LOCAL_TEST` | Run safe validation and test commands |
| `COMMIT_REQUEST` | Prepare commit proposal for human review |
| `PUSH_REQUEST` | Request push approval from human or runner |
| `BLOCKED` | Execution stopped; human review required |

### Important: Permission Values Are Not a Strict Linear Ladder

Permission values are capability states, not a strict linear hierarchy.

- `LOCAL_TEST` may be granted independently of `LOCAL_EDIT`
- An agent may hold `LOCAL_TEST` without `LOCAL_EDIT`
- An agent may hold `LOCAL_EDIT` without `LOCAL_TEST` if test commands are not authorized
- `COMMIT_REQUEST` requires `LOCAL_EDIT` to be meaningful, but does not imply it
- `PUSH_REQUEST` requires `COMMIT_REQUEST` to be meaningful, but does not imply it
- `BLOCKED` overrides all other values regardless of what was previously granted

Effective capability = intersection of permission value + task scope + command policy + write policy + approval records.

---

## Permission Level Definitions

### READ_ONLY

The agent may:

- Read files and directories permitted by the task contract
- Inspect repository structure
- Summarize file contents
- Produce a diff proposal as text output, not a file write
- Record observations for audit purposes

The agent may not:

- Write any file
- Run write commands
- Run validation or test scripts
- Stage or commit
- Push

### PATCH_PROPOSE

The agent may do everything in `READ_ONLY`, plus:

- Generate a proposed patch or diff as text
- Describe intended changes for human review
- Produce structured change proposals

The agent may not:

- Write any file directly
- Apply the patch without explicit task permission and human review
- Run validation or test scripts
- Stage or commit
- Push

### LOCAL_EDIT

The agent may do everything in `READ_ONLY` and `PATCH_PROPOSE`, plus:

- Edit files within declared scope and allowed write paths
- Create new files within declared scope
- Delete files within declared scope if task explicitly authorizes deletion

The agent may not:

- Edit files outside declared scope
- Edit protected zone files without explicit approval
- Run validation or test scripts unless `LOCAL_TEST` is also granted
- Stage or commit
- Push

### LOCAL_TEST

The agent may:

- Run commands classified as `SAFE_READ`
- Run commands classified as `SAFE_VALIDATE`
- Run commands classified as `SAFE_TEST`

The agent may not:

- Run `WRITE_LOCAL`, `GIT_LOCAL`, `GIT_REMOTE`, `DANGEROUS`, or `FORBIDDEN` commands
- Write files unless `LOCAL_EDIT` is also granted
- Stage or commit
- Push

**Note:** `LOCAL_TEST` is a capability value independent of `LOCAL_EDIT`.
An agent may hold `LOCAL_TEST` without `LOCAL_EDIT` and vice versa.
Both may be granted together when the task requires editing and validation.

### COMMIT_REQUEST

The agent may do everything in `LOCAL_EDIT` and `LOCAL_TEST` if those permissions are also granted, plus:

- Prepare a commit proposal for human review
- Stage files locally as preparation for a commit proposal
- Request human review of a proposed local commit

The agent may not:

- Execute `git commit` without task permission and commit preconditions
- Execute `git commit` without satisfying conditions defined in Task 26.7.1
- Push to any remote branch
- Create remote branches

**COMMIT_REQUEST does not authorize git commit.**
COMMIT_REQUEST authorizes the agent to prepare a commit proposal and request human review.

Actual git commit requires:

- Explicit task contract permission
- Commit preconditions satisfied as defined in Task 26.7.1
- No open violations
- Scope check passed

Until Task 26.7.1 is implemented, commit permission must be reviewed manually per task.

### PUSH_REQUEST

The agent may do everything in `COMMIT_REQUEST` if that permission is also granted, plus:

- Request push approval from a human or authorized runner
- Prepare push context for reviewer

The agent may not:

- Push to any remote branch without explicit push approval
- Push directly to `dev` or `main` under any circumstances
- Create remote branches without authorization
- Bypass M25 validation before push

**PUSH_REQUEST does not authorize push.**
PUSH_REQUEST authorizes the agent to request push approval.

Actual push requires:

- Explicit push approval from a human or authorized runner
- Approval recorded in an approval record
- M25 validation passed, or a separate M25 override record exists under M25 policy
- No open violations

M26 permission records do not satisfy M25 override requirements.
M26 permission records do not convert M25 outcomes into PASS.
Push approval does not imply merge approval.

### BLOCKED

The agent must:

- Stop all execution immediately
- Record the reason for the blocked state
- Await explicit human decision before resuming

The agent may not:

- Take any action except recording the blocked state
- Retry execution without human authorization
- Request permission escalation while blocked
- Simulate human review to exit blocked state

**BLOCKED overrides all other permission values.**
An agent in BLOCKED state has no capability except recording its state.

---

## Permission Escalation

Permission may be increased when all of the following conditions are satisfied:

- An active task exists and is the authorization anchor
- Declared scope is defined and within corridor boundaries
- A risk assessment has been performed and recorded
- Human approval has been obtained where required by the requested permission
- A permission record has been created using `templates/agent-permission-record.md`
- No unresolved violations exist
- The requested permission is appropriate for the task requirements
- M25 constraints are not violated by the escalation

### Escalation Risk by Permission Change

| Escalation | Risk Level | Human Approval Required |
|---|---|---|
| Any → `READ_ONLY` | LOW | No |
| `READ_ONLY` → `PATCH_PROPOSE` | LOW | No |
| `PATCH_PROPOSE` → `LOCAL_EDIT` | MEDIUM | Recommended |
| `LOCAL_EDIT` → `LOCAL_TEST` | LOW | No |
| Any → `COMMIT_REQUEST` | HIGH | Yes |
| Any → `PUSH_REQUEST` | HIGH | Yes |
| Any → `BLOCKED` | N/A | Not applicable — `BLOCKED` is a reduction |

---

## Permission Reduction

Permission must be reduced after any of the following:

- Scope violation: agent wrote outside declared scope
- Forbidden write: agent wrote to a forbidden path or protected zone
- Forbidden command: agent ran a `FORBIDDEN`-class command
- Unapproved push attempt: agent attempted push without approval
- Evidence tampering: agent modified an audit or evidence artifact
- Validation bypass attempt: agent attempted to suppress or mask validation output
- Repeated failure: agent failed the same precondition three or more times
- Human reviewer decision: reviewer explicitly reduces permission
- Task completion: permission resets to default at task close

### Reduction Outcomes

| Trigger | Minimum Resulting Permission |
|---|---|
| Scope violation | `READ_ONLY` pending review |
| Forbidden write | `READ_ONLY` pending review |
| Forbidden command | `BLOCKED` |
| Unapproved push attempt | `BLOCKED` |
| Evidence tampering | `BLOCKED` |
| Validation bypass attempt | `BLOCKED` |
| Repeated failure | Human decision required |
| Human reviewer decision | As specified by reviewer |
| Task completion | Reset to task default |

---

## Blocked State

`BLOCKED` is not a permission level in the capability sense.
`BLOCKED` is a forced stop state that overrides all other permissions.

### Entry Conditions

An agent enters `BLOCKED` after:

- A `FORBIDDEN`-class command is executed
- An unapproved push is attempted
- Evidence tampering is detected
- A validation bypass is attempted
- An explicit `BLOCKED` decision is recorded by a human reviewer

### Exit Conditions

An agent may exit `BLOCKED` only when:

- A human reviewer has reviewed the violation record
- The human reviewer has recorded an explicit exit decision
- The exit decision is recorded in a permission record with decision `PERMISSION_GRANTED` or `PERMISSION_GRANTED_WITH_CONDITIONS`
- All conditions in the exit decision are satisfied

**An agent may not exit BLOCKED state autonomously.**
**An agent may not simulate human review to exit BLOCKED state.**

---

## Human Approval Boundary

The following permission changes require explicit human approval:

- Escalation to `COMMIT_REQUEST`
- Escalation to `PUSH_REQUEST`
- Exit from `BLOCKED` state
- Any escalation after an open violation
- Any escalation to a protected zone write

Human approval cannot be:

- Simulated by the agent
- Granted by CI
- Derived from evidence reports
- Implied by permission value
- Automatic or autonomous

Human approval must be:

- Explicit and documented
- Traceable to a human reviewer
- Recorded in a permission record
- Time-stamped and linked to the active task

---

## Relationship to Scope Control

Permission value does not expand declared scope.

An agent with `LOCAL_EDIT` may only edit files within `declared_scope`.
An agent with `LOCAL_EDIT` may not edit files outside `declared_scope` regardless of permission value.
An agent with `PUSH_REQUEST` may not push files outside `declared_scope`.

Scope remains the primary boundary.
Permission value is a capability ceiling within that boundary.

Scope checking is planned in `scripts/check-pre-merge-scope.py` — Task 26.5.1.

---

## Relationship to Command Control

Permission value maps to command categories as follows:

| Permission | Allowed Command Categories |
|---|---|
| `READ_ONLY` | `SAFE_READ` only |
| `PATCH_PROPOSE` | `SAFE_READ` only |
| `LOCAL_EDIT` | `SAFE_READ`, `WRITE_LOCAL` within scope |
| `LOCAL_TEST` | `SAFE_READ`, `SAFE_VALIDATE`, `SAFE_TEST` |
| `COMMIT_REQUEST` | `SAFE_READ`, `WRITE_LOCAL`, `SAFE_VALIDATE`, `SAFE_TEST`, `GIT_LOCAL` with preconditions |
| `PUSH_REQUEST` | All above + `GIT_REMOTE` with push approval record |
| `BLOCKED` | None |

`DANGEROUS` commands always require explicit human approval regardless of permission value.
`FORBIDDEN` commands are always blocked regardless of permission value.

Command allowlist policy is planned in `docs/COMMAND-ALLOWLIST-POLICY.md` — Task 26.3.1.

---

## Relationship to Write Control

Permission value maps to write capability as follows:

| Permission | Write Capability |
|---|---|
| `READ_ONLY` | No writes |
| `PATCH_PROPOSE` | No writes |
| `LOCAL_EDIT` | Writes within `allowed_write_paths` only |
| `LOCAL_TEST` | No writes unless `LOCAL_EDIT` is also granted |
| `COMMIT_REQUEST` | Writes within `allowed_write_paths`; stage only |
| `PUSH_REQUEST` | Writes within `allowed_write_paths`; stage and push only with approval |
| `BLOCKED` | No writes |

Protected zones may never be written without explicit owner approval, regardless of permission value.

Write allowlist policy is planned in `docs/WRITE-ALLOWLIST-POLICY.md` — Task 26.4.1.

---

## Relationship to Commit / Push Boundary

### Commit

- `COMMIT_REQUEST` does not authorize `git commit`
- `git commit` requires: task permission + commit preconditions from Task 26.7.1 + no open violations
- Until Task 26.7.1 is implemented, commit permission must be reviewed manually per task

### Push

- `PUSH_REQUEST` does not authorize push
- Push requires: explicit push approval + M25 validation passed or separate M25 override under M25 policy + no open violations
- M26 permission records do not satisfy M25 override requirements
- Push to `dev` or `main` is never authorized by permission value alone
- Push approval does not imply merge approval

Commit/push control is planned in `scripts/check-commit-push-preconditions.py` — Task 26.7.1.

---

## Relationship to M25 Enforcement

Permission values operate within M25 enforcement boundaries.

A permission value does not:

- Change or override M25 outcomes
- Convert FAIL, ERROR, WARN, NOT_RUN, or INCOMPLETE to PASS
- Authorize bypassing M25 required checks
- Authorize merge without M25 passing or without a separate M25 override record under M25 policy
- Authorize ignoring M25 enforcement policy
- Satisfy M25 override requirements

`PUSH_REQUEST` does not authorize push if M25 validation has not passed and no separate M25 override record exists under M25 policy.
`PUSH_REQUEST` does not authorize overriding a FAIL or ERROR outcome.

M25 enforcement remains active and unchanged.
M26 permission values are additive constraints within M25, not alternatives to it.

---

## Evidence Requirements

Every permission change must be recorded using `templates/agent-permission-record.md`.

The following must be traceable for each permission change:

- Permission record ID
- Active task ID at time of change
- Current permission value before change
- Requested permission value
- Reason for change
- Declared scope at time of change
- Risk level assessment
- Whether human approval was required and obtained
- Approval record reference if applicable
- Conditions attached to the permission grant
- Expiration of the permission
- Open violations at time of change
- Decision outcome
- Reviewer identity

**Permission record is not approval.**
**PERMISSION_GRANTED is not approval.**
**Permission record does not authorize merge.**
**Permission record does not authorize push.**

---

## Non-Goals

This document does not implement:

- Permission enforcement script
- Command allowlist enforcement script
- Write allowlist enforcement script
- Scope diff checker
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

- Claim that permission enforcement is implemented
- Claim that permission values are machine-enforced
- Suggest that a higher permission value bypasses scope or M25
- Define command allowlist specifics, which belong to Task 26.3.1
- Define write allowlist specifics, which belong to Task 26.4.1
- Define scope diff check logic, which belongs to Task 26.5.1
- Define commit/push precondition logic, which belongs to Task 26.7.1

---

## M26 Follow-Up Tasks

| Task | Title | Creates |
|---|---|---|
| 26.3.1 | Command Allowlist Policy | `docs/COMMAND-ALLOWLIST-POLICY.md` |
| 26.4.1 | Write Allowlist / Forbidden Zones | `docs/WRITE-ALLOWLIST-POLICY.md` |
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

Permission enforcement is not implemented by this document.
This document establishes the M26 permission model contract only.
Enforcement artifacts are created in follow-up tasks 26.3.1 through 26.13.1.

Until 26.5.1, 26.7.1, 26.10.1, and 26.11.1 are complete,
permission boundaries cannot be machine-verified.
