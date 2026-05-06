---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-04
task_id: 26.8.1
milestone: M26
---

# Agent Violation / Sanctions Policy

> M26 Policy Document — Task 26.8.1
> This document does not authorize push, commit, merge, or release.
> This document does not override M25.
> Violation records are evidence, not approval.
> Sanctions do not authorize merge, push, or release.

---

## Purpose

This policy defines how agent violations are detected, recorded, classified,
escalated, and sanctioned within the M26 pre-merge execution corridor.

Detection without response is not control. Every `BLOCKED` result from a
corridor checker that is caused by agent action must produce a violation
record. Sanctions reduce or stop agent capability until a human reviewer
resolves the violation.

This document is a policy contract only. Automatic sanction enforcement
belongs to future M26 tasks.

---

## Relationship to Pre-Merge Execution Corridor

The Pre-Merge Execution Corridor (`docs/PRE-MERGE-EXECUTION-CORRIDOR.md`)
defines the sequence of checks required before any merge.

Under this policy:

- Any corridor `BLOCKED` result caused by agent action requires a violation record.
- A violation record does not satisfy the Pre-Merge Execution Corridor.
- Sanction does not advance corridor status.
- Sanction does not authorize merge.

---

## Relationship to Agent Permission Model

The Agent Permission Model (`docs/AGENT-PERMISSION-MODEL.md`) defines
permission levels available to an agent.

Under this policy:

- Sanctions may reduce agent permission level.
- `REDUCE_TO_READ_ONLY` sets permission to `READ_ONLY`.
- `BLOCK_AGENT` sets permission to `BLOCKED`.
- Permission reduction does not require agent consent.
- Agent cannot escalate its own permission after a sanction.
- Permission reduction is not merge approval.

---

## Relationship to Command Allowlist Policy

The Command Allowlist Policy (`docs/COMMAND-ALLOWLIST-POLICY.md`) defines
which commands are permitted and under what conditions.

Under this policy:

- Issuing a forbidden command produces `FORBIDDEN_COMMAND` violation.
- `FORBIDDEN_COMMAND` is `CRITICAL` severity.
- Sanction for `FORBIDDEN_COMMAND` includes `BLOCK_TASK`,
  `ESCALATE_TO_OWNER`, and `DISALLOW_AUTOPILOT`.

---

## Relationship to Write Allowlist Policy

The Write Allowlist Policy (`docs/WRITE-ALLOWLIST-POLICY.md`) defines which
paths may be written and under what conditions.

Under this policy:

- Writing outside declared scope produces `SCOPE_VIOLATION`.
- Writing to a forbidden path produces `FORBIDDEN_WRITE`.
- Writing outside declared scope may also produce `FORBIDDEN_WRITE` if the
  path is explicitly forbidden.
- `FORBIDDEN_WRITE` is `HIGH` severity.
- Sanction for `FORBIDDEN_WRITE` includes `BLOCK_TASK`,
  `ESCALATE_TO_OWNER`, and `REDUCE_TO_READ_ONLY`.

---

## Relationship to Scope-Bound Diff Checker

The Scope-Bound Diff Checker (Task 26.5.1) produces scope check results.

Under this policy:

- `SCOPE_VIOLATION` result caused by agent action produces `SCOPE_VIOLATION`
  violation record.
- `SCOPE_VIOLATION` is `HIGH` severity.
- Agent cannot self-clear a `SCOPE_VIOLATION`.

---

## Relationship to No Direct Push Policy

The No Direct Push Policy (`docs/NO-DIRECT-PUSH-POLICY.md`) defines push
behavior rules.

Under this policy:

- Attempting direct push to `dev` or `main` produces
  `DIRECT_PROTECTED_BRANCH_PUSH` violation.
- Attempting force push produces `FORCE_PUSH_ATTEMPT` violation.
- Attempting remote branch deletion produces
  `REMOTE_BRANCH_DELETE_ATTEMPT` violation.
- Attempting push without approval produces `UNAPPROVED_PUSH` violation.

`DIRECT_PROTECTED_BRANCH_PUSH`, `FORCE_PUSH_ATTEMPT`, and
`REMOTE_BRANCH_DELETE_ATTEMPT` are `CRITICAL`.

`UNAPPROVED_PUSH` is at minimum `HIGH`, unless combined with a protected
branch push, force push, remote branch deletion, approval simulation, or
validation bypass.

---

## Relationship to Commit / Push Control Script

The Commit / Push Control Script (Task 26.7.1) produces precondition check
results.

Mapping of 26.7.1 output to violation records:

| 26.7.1 Result | Violation Required? | Notes |
|---|---|---|
| `COMMIT_ALLOWED` | No | No violation by itself |
| `PUSH_ALLOWED` | No | No violation by itself |
| `NEEDS_APPROVAL` | No | Action must stop; no violation unless agent proceeds anyway |
| `NEEDS_REVIEW` | No | Action must stop; no violation unless agent proceeds anyway |
| `BLOCKED` | Yes, if caused by agent action | See mapping below |

BLOCKED reason to violation category mapping:

| BLOCKED Reason | Violation Category |
|---|---|
| `scope_check.result: SCOPE_VIOLATION` | `SCOPE_VIOLATION` |
| `evidence_tampering_detected: yes` | `EVIDENCE_TAMPERING` |
| `protected_branch_target: yes` | `DIRECT_PROTECTED_BRANCH_PUSH` |
| `push_type: FORCE_PUSH` | `FORCE_PUSH_ATTEMPT` |
| `push_type: REMOTE_BRANCH_DELETE` | `REMOTE_BRANCH_DELETE_ATTEMPT` |
| `push_type: PROTECTED_BRANCH_PUSH` | `DIRECT_PROTECTED_BRANCH_PUSH` |
| `workflow_files_changed: yes` | `FORBIDDEN_WRITE` |
| `forbidden_files_changed: yes` | `FORBIDDEN_WRITE` |
| `permission.current: BLOCKED` | `PERMISSION_ESCALATION_ATTEMPT` if agent continued |
| `push_decision: PUSH_BLOCKED` | `UNAPPROVED_PUSH` if agent attempted to proceed anyway |
| `m25_validation bypass attempted` | `VALIDATION_BYPASS` |

---

## Core Principle

Agent cannot clear its own violation.
Agent cannot reduce severity of its own violation.
Agent cannot mark its own violation as false positive.
Agent cannot resume from `BLOCKED` without human decision.

Violation record is evidence, not approval.
Sanction does not authorize merge.
Sanction does not authorize push.
Sanction does not bypass M25.

---

## Violation Categories

The following violation categories are defined:

| Category | Description |
|---|---|
| `SCOPE_VIOLATION` | Changed files outside declared scope |
| `FORBIDDEN_COMMAND` | Issued a command not in allowlist |
| `FORBIDDEN_WRITE` | Wrote to a forbidden or out-of-scope path |
| `UNAPPROVED_PUSH` | Pushed without required push approval |
| `DIRECT_PROTECTED_BRANCH_PUSH` | Attempted direct push to `dev` or `main` |
| `FORCE_PUSH_ATTEMPT` | Attempted force push to any branch |
| `REMOTE_BRANCH_DELETE_ATTEMPT` | Attempted remote branch deletion |
| `VALIDATION_BYPASS` | Attempted to bypass M25 or corridor validation |
| `EVIDENCE_TAMPERING` | Modified or deleted evidence/audit artifacts |
| `PERMISSION_ESCALATION_ATTEMPT` | Attempted to exceed permitted permission level |
| `APPROVAL_SIMULATION` | Simulated or fabricated human approval |
| `AUTO_MERGE_ATTEMPT` | Attempted automatic merge |
| `REPEATED_FAILURE` | Same violation type repeated within task or across tasks |
| `UNBOUNDED_RETRY` | Retried past defined retry limit or without conditions |
| `UNKNOWN_VIOLATION` | Violation detected but category not yet determined |

---

## Severity Levels

```text
LOW      — informational; no immediate capability reduction required
MEDIUM   — notable; human review recommended
HIGH     — significant; capability reduction required
CRITICAL — severe; task or agent must be blocked
```

Minimum severity by violation category:

| Violation Category | Minimum Severity |
|---|---|
| `SCOPE_VIOLATION` | `HIGH` |
| `FORBIDDEN_COMMAND` | `CRITICAL` |
| `FORBIDDEN_WRITE` | `HIGH` |
| `UNAPPROVED_PUSH` | `HIGH` |
| `DIRECT_PROTECTED_BRANCH_PUSH` | `CRITICAL` |
| `FORCE_PUSH_ATTEMPT` | `CRITICAL` |
| `REMOTE_BRANCH_DELETE_ATTEMPT` | `CRITICAL` |
| `VALIDATION_BYPASS` | `CRITICAL` |
| `EVIDENCE_TAMPERING` | `CRITICAL` |
| `PERMISSION_ESCALATION_ATTEMPT` | `HIGH` |
| `APPROVAL_SIMULATION` | `CRITICAL` |
| `AUTO_MERGE_ATTEMPT` | `CRITICAL` |
| `REPEATED_FAILURE` | `MEDIUM` or `HIGH` depending count/context |
| `UNBOUNDED_RETRY` | `HIGH` |
| `UNKNOWN_VIOLATION` | `HIGH` until classified by human reviewer |

REPEATED_FAILURE severity rules:

- 2-3 same-type failures within the same task: `MEDIUM`
- 4 or more same-type failures within the same task: `HIGH`
- Any failure after `REDUCE_TO_READ_ONLY` sanction has been applied: `HIGH`
- Same violation type repeated across tasks: `HIGH`
- Count is determined by human reviewer.
- Agent may not self-assess count or self-assign severity.

---

## Sanction Types

The following sanction types are defined:

| Sanction | Meaning |
|---|---|
| `RECORD_ONLY` | Record the event; no capability reduction |
| `REQUIRE_HUMAN_REVIEW` | Stop all agent action until human review is complete |
| `REDUCE_TO_READ_ONLY` | Agent may only inspect and summarize; no writes or commands |
| `BLOCK_TASK` | Current task stops; agent may not continue task |
| `RESET_TO_LAST_SAFE_STATE` | Task state must be restored manually or by authorized runner; applied at human discretion after CRITICAL violations |
| `RETRY_WITH_REDUCED_PERMISSIONS` | Retry allowed only with reduced permission level; conditions defined in 26.9.1 |
| `ESCALATE_TO_OWNER` | Owner or maintainer review required before any continuation |
| `DISALLOW_AUTOPILOT` | No autonomous continuation for current task or agent session |
| `BLOCK_AGENT` | Agent cannot continue in current corridor; requires human reinstatement |

RESET_TO_LAST_SAFE_STATE notes:

- Applied at human reviewer discretion after CRITICAL violations.
- Required for `EVIDENCE_TAMPERING`.
- Required for `DIRECT_PROTECTED_BRANCH_PUSH`, `FORCE_PUSH_ATTEMPT`, and
  `REMOTE_BRANCH_DELETE_ATTEMPT` when artifacts may have been affected.
- Agent cannot initiate reset.
- Agent cannot confirm reset complete.

---

## Required Sanctions by Violation

Minimum required sanctions per violation category:

`SCOPE_VIOLATION`:
  - `REQUIRE_HUMAN_REVIEW`
  - `REDUCE_TO_READ_ONLY`

`FORBIDDEN_COMMAND`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `DISALLOW_AUTOPILOT`

`FORBIDDEN_WRITE`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `REDUCE_TO_READ_ONLY`

`UNAPPROVED_PUSH`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `DISALLOW_AUTOPILOT`

`DIRECT_PROTECTED_BRANCH_PUSH`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`
  - `RESET_TO_LAST_SAFE_STATE` (at human discretion)

`FORCE_PUSH_ATTEMPT`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`
  - `RESET_TO_LAST_SAFE_STATE` (at human discretion)

`REMOTE_BRANCH_DELETE_ATTEMPT`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`
  - `RESET_TO_LAST_SAFE_STATE` (at human discretion)

`VALIDATION_BYPASS`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `DISALLOW_AUTOPILOT`

`EVIDENCE_TAMPERING`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`
  - `RESET_TO_LAST_SAFE_STATE` (required)

`PERMISSION_ESCALATION_ATTEMPT`:
  - `REQUIRE_HUMAN_REVIEW`
  - `REDUCE_TO_READ_ONLY`

`APPROVAL_SIMULATION`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`

`AUTO_MERGE_ATTEMPT`:
  - `BLOCK_TASK`
  - `ESCALATE_TO_OWNER`
  - `BLOCK_AGENT`

`REPEATED_FAILURE`:
  - `REQUIRE_HUMAN_REVIEW`
  - `RETRY_WITH_REDUCED_PERMISSIONS`

`UNBOUNDED_RETRY`:
  - `BLOCK_TASK`
  - `REQUIRE_HUMAN_REVIEW`
  - `DISALLOW_AUTOPILOT`

`UNKNOWN_VIOLATION`:
  - `REQUIRE_HUMAN_REVIEW`
  - `REDUCE_TO_READ_ONLY`

---

## Violation Record Rule

Every `BLOCKED` result caused by agent action must produce a violation record
using `templates/agent-violation-record.md`.

Rules:

- Agent may create the violation record with `decision: NEEDS_HUMAN_REVIEW`
  and `reviewer: PENDING_HUMAN_ASSIGNMENT`.
- Agent must not fill reviewer with its own identifier.
- Agent must not set decision to any value other than `NEEDS_HUMAN_REVIEW`
  when creating its own violation record.
- Human reviewer must complete the record: set reviewer, update decision,
  apply or confirm sanctions.
- A violation record is not approval.
- A violation record does not clear the violation.
- Violation records must be retained as evidence artifacts.

Multi-Category Incident Rule

If a single action produces both `SCOPE_VIOLATION` and `FORBIDDEN_WRITE`,
create one violation record with:

`violation_category: FORBIDDEN_WRITE`

Record the scope violation in the description field and, if needed, in
`related_records` or notes.

`FORBIDDEN_WRITE` takes precedence when both apply simultaneously because it
represents the stricter write-path violation.

If a single action produces multiple CRITICAL violations, create separate
violation records for each CRITICAL category unless the human reviewer
decides to consolidate them in one owner-level incident record.

---

## Blocked State Rule

When an agent reaches `BLOCKED` state:

- Agent must stop all corridor actions immediately.
- Agent must not attempt workarounds or alternative paths.
- Agent must not retry `BLOCKED` operations without human decision.
- Agent must not self-reduce to a lower-risk version of the blocked action.
- Agent must not re-interpret `BLOCKED` as `NEEDS_APPROVAL`.
- Agent must create a violation record if the block was caused by agent action.
- Agent must wait for human review.

---

## Human Review Boundary

The following decisions are exclusively human:

- Confirming or refuting a violation.
- Setting severity level.
- Selecting and applying sanctions.
- Setting `retry_allowed: yes`.
- Setting retry conditions.
- Marking a violation as `FALSE_POSITIVE`.
- Reinstating agent from `BLOCK_AGENT`.
- Authorizing `RESET_TO_LAST_SAFE_STATE`.
- Closing a violation record.

Agent cannot perform any of these actions on its own violation record or
on any other violation record.

---

## Repeat Violation Rule

If the same violation category occurs more than once within a task:

- The new occurrence must produce a new violation record.
- The new record must reference the prior record in `related_records`.
- Human reviewer must assess whether `REPEATED_FAILURE` applies in addition
  to the original category.
- Two or more CRITICAL violations of the same type within a task: human
  reviewer should escalate to `BLOCK_AGENT`.
- Agent cannot determine whether `REPEATED_FAILURE` applies to its own
  violations.

---

## Evidence Tampering Rule

`EVIDENCE_TAMPERING` is always `CRITICAL`.

Evidence tampering includes:

- Modifying a `reports/milestone-25-*` artifact.
- Deleting a `reports/milestone-25-*` artifact.
- Modifying any file listed in `evidence_artifacts` in a scope file.
- Modifying or deleting any violation record.
- Modifying or deleting any push request record.
- Modifying or deleting any pre-merge execution review.
- Modifying any M25 or M26 evidence report without authorization.

Required response to `EVIDENCE_TAMPERING`:

- `BLOCK_TASK` immediately.
- `ESCALATE_TO_OWNER` immediately.
- `BLOCK_AGENT` until human review complete.
- `RESET_TO_LAST_SAFE_STATE` required; human must verify artifact integrity.

Agent cannot self-recover from `EVIDENCE_TAMPERING`.

---

## Relationship to M25 Enforcement

M25 defines merge-gate enforcement and required platform checks.

Under this policy:

- Sanctions do not change M25 validation results.
- Sanctions do not convert M25 `FAIL` to `PASS`.
- Sanctions do not bypass M25 required checks.
- `VALIDATION_BYPASS` violation is issued if agent attempts to skip or
  falsify M25 validation.
- `VALIDATION_BYPASS` is always `CRITICAL`.
- M25 enforcement remains active and unchanged regardless of sanction state.

---

## Evidence Requirements

Every violation requires a completed violation record using:
`templates/agent-violation-record.md`

Violation records must reference:

- Active task ID.
- Source event, such as checker output or command log.
- Detected by: script, human, or both.
- Violation category and severity.
- Sanctions required and applied.
- Permission level after violation.
- Task status after violation.
- Human reviewer or `PENDING_HUMAN_ASSIGNMENT`.
- Related records if repeat violation.

Violation records must be retained as evidence artifacts and must not be
modified or deleted by the agent.

---

## Non-Goals

This policy does not implement:

- Violation enforcement script.
- Automatic sanction application.
- Automatic permission changes.
- Automatic reset.
- Autonomous retry loop.
- Agent runner.
- Remote approval app.
- Messenger approvals.
- CI workflow.
- Branch protection changes.
- Auto-merge.
- Automatic approval.
- Self-healing commits.
- Production deployment controls.

---

## M26 Follow-Up Tasks

| Task | Title | Relationship |
|---|---|---|
| 26.9.1 | Bounded Retry Loop Policy | Defines when retry is allowed, limited, or forbidden after violations |
| 26.10.1 | Pre-Merge Corridor Audit Script | Audits whether M26 corridor artifacts are present and consistent |
| 26.11.1 | Pre-Merge Corridor Smoke Fixtures | Adds negative/positive fixtures for corridor behavior |
| 26.12.1 | M26 Evidence Report | Final evidence aggregation |
| 26.13.1 | M26 Completion Review | Final milestone decision |

---

## Final Reminder

Agent cannot clear its own violation.
Agent cannot reduce severity of its own violation.
Agent cannot mark its own violation as false positive.
Agent cannot resume from `BLOCKED` without human decision.

Violation record is evidence, not approval.
Sanction does not authorize merge.
Sanction does not authorize push.
Sanction does not bypass M25.

Evidence tampering is always `CRITICAL`.
Approval simulation is always `CRITICAL`.
Auto-merge attempt is always `CRITICAL`.
Direct protected branch push is always `CRITICAL`.

This document does not authorize any push, commit, merge, or release.
This document does not override M25.
