---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-04
task_id: 26.9.1
milestone: M26
---

# Bounded Retry Loop Policy

> M26 Policy Document — Task 26.9.1  
> This document does not authorize push, commit, merge, or release.  
> This document does not override M25.  
> Retry record is not approval.  
> Retry does not authorize commit, push, or merge.  
> Retry does not bypass M25.

---

## Purpose

This policy defines when an agent may retry a failed action, how many retries
are permitted, under what conditions retry is allowed or blocked, and when
retry must stop pending human review.

Retry is not approval. Retry must be bounded. Retry must not bypass violations.
Retry must not become self-healing autonomy. Agent must stop after retry
boundary is reached.

This document is a policy contract only. Retry automation is not implemented
by this task.

---

## Relationship to Pre-Merge Execution Corridor

The Pre-Merge Execution Corridor (`docs/PRE-MERGE-EXECUTION-CORRIDOR.md`)
defines the sequence of checks required before any merge.

Under this policy:

- Retry does not advance corridor status.
- Retry does not satisfy a failed corridor check.
- Retry does not authorize merge.
- A successful retry must re-run all required corridor checks before merge may be considered.

---

## Relationship to Agent Permission Model

The Agent Permission Model (`docs/AGENT-PERMISSION-MODEL.md`) defines
permission levels available to an agent.

Under this policy:

- Retry with reduced permissions must use a lower permission level than the failed attempt.
- Agent cannot choose its own reduced permission level.
- Agent cannot restore prior permission after a reduced retry without human decision.
- `COMMIT_REQUEST` and `PUSH_REQUEST` are forbidden permission targets for retry after a violation, unless explicitly restored by human reviewer after violation resolution.

---

## Relationship to Commit / Push Control Script

The Commit / Push Control Script (Task 26.7.1) produces precondition check
results used before commit or push.

Under this policy:

- `NEEDS_APPROVAL` from 26.7.1 is not a retry failure by itself. Action must stop until approval is obtained.
- `NEEDS_REVIEW` from 26.7.1 is not a retry failure by itself. Action must stop until review is complete.
- `BLOCKED` from 26.7.1 caused by agent action may produce a violation record under 26.8.1 and must not be retried without human decision.
- Retry after a `BLOCKED` result requires a violation record reference in the retry attempt record.

---

## Relationship to Agent Violation Policy

The Agent Violation Policy (`docs/AGENT-VIOLATION-POLICY.md`) defines how
violations are recorded, classified, and sanctioned.

Under this policy:

- Retry after any violation requires a violation record reference.
- Retry after any violation requires human review decision.
- Retry after a `CRITICAL` violation is blocked unless the owner explicitly authorizes reset or restart.
- `RETRY_WITH_REDUCED_PERMISSIONS` sanction from 26.8.1 must use a permission level from the allowed reduced permission list defined in this policy.
- Agent cannot self-authorize retry after violation.

---

## Core Principle

Retry is not approval.  
Retry must be bounded.  
Retry must not bypass violations.  
Retry must not become self-healing autonomy.  
Agent must stop after retry boundary is reached.  
Agent cannot reset retry count.  
Agent cannot self-authorize retry after violation.  
Retry record is not approval.

---

## Retry Decision States

The following retry decision states are defined:

| State | Meaning |
|---|---|
| `RETRY_ALLOWED` | Retry may proceed within policy bounds |
| `RETRY_ALLOWED_WITH_CONDITIONS` | Retry may proceed only if listed conditions are met |
| `NEEDS_HUMAN_REVIEW` | Retry cannot proceed until human reviewer decides |
| `RETRY_BLOCKED` | Retry must not proceed |
| `RETRY_EXHAUSTED` | Retry limit reached; task must stop pending human review |

---

## Retry Attempt Outcomes

The following retry attempt outcomes are defined:

| Outcome | Meaning |
|---|---|
| `RETRY_SUCCESS` | Retry completed and resolved the immediate issue |
| `RETRY_FAILED` | Retry ran but did not resolve the issue |
| `RETRY_BLOCKED` | Retry was stopped by policy or precondition |
| `RETRY_ABORTED` | Retry stopped voluntarily before a risky action |
| `NEEDS_REVIEW` | Retry result is ambiguous or requires human review |

---

## Retry Limits

Default limits:

```yaml
default_max_attempts_per_task: 3
default_max_attempts_same_failure: 2
max_attempts_after_warning: 1
max_attempts_after_violation_without_human_review: 0
max_attempts_after_critical_violation: 0
```

Rules:

- Retry count is per active task, not per attempt type.
- Retry count must include failed attempts, aborted attempts after material changes, and blocked retry attempts.
- Read-only diagnostic checks without material changes do not count as retry attempts unless they are part of a retry plan.
- Agent cannot reset retry count.
- Agent cannot start a new task only to reset retry count.
- Retry exhaustion (`RETRY_EXHAUSTED`) requires human review before any continuation.

### Retry Count Verification

Retry count is determined by counting all `retry-attempt-record` files for the
active `task_id`.

Agent cannot determine count by self-report. Human reviewer verifies count by
reviewing all retry-attempt-record files for the task.

Creating a new record with `previous_attempt_count: 0` when prior records exist
is a violation of this policy and may produce a `PERMISSION_ESCALATION_ATTEMPT`
violation.

### Material Change Definition

A material change is any file write, mutating command execution, state-changing
API call, or command that changes repository, task, evidence, permission,
approval, retry, or validation state.

Non-mutating `SAFE_READ` diagnostic commands do not count as material changes
unless they are explicitly part of a retry plan.

Aborted attempts that included a material change must be counted in the retry
total.

---

## Retry Allowed Conditions

Retry may proceed only when all of the following are true:

```text
active task exists
retry attempt count is below limit
no open CRITICAL violation
no unresolved BLOCKED state from prior attempt
retry is within declared scope
retry does not require forbidden command
retry does not require forbidden write
retry does not bypass M25
retry does not push, commit, or merge automatically
retry plan is recorded in retry attempt record before retry begins
any open non-critical violation has explicit human retry authorization
```

---

## Retry Blocked Conditions

Retry must be blocked if any of the following are true:

```text
retry limit reached
open CRITICAL violation exists
EVIDENCE_TAMPERING occurred
APPROVAL_SIMULATION occurred
AUTO_MERGE_ATTEMPT occurred
DIRECT_PROTECTED_BRANCH_PUSH occurred
FORCE_PUSH_ATTEMPT occurred
REMOTE_BRANCH_DELETE_ATTEMPT occurred
VALIDATION_BYPASS occurred
agent is in BLOCKED state
human reviewer denied retry
unresolved open violation exists
open violation exists without explicit human retry authorization
retry would expand scope silently
retry would run a command not in the allowlist without approval
retry would write to a forbidden path
retry would bypass M25 validation
retry would perform commit or push automatically
```

---

## Retry With Reduced Permissions

`RETRY_WITH_REDUCED_PERMISSIONS` requires a human decision. Agent cannot
initiate reduced-permission retry without explicit authorization.

Rules:

- Reduced retry must use a lower permission level than the failed attempt.
- Agent cannot choose its own reduced permission level.
- Agent cannot restore prior permission after reduced retry without human decision.
- Retry with reduced permissions must be recorded in a retry attempt record.

Allowed reduced permission levels for retry after violation:

```text
READ_ONLY
PATCH_PROPOSE
LOCAL_EDIT
LOCAL_TEST
```

Forbidden permission levels for retry after violation unless explicitly restored
by human reviewer after violation resolution:

```text
COMMIT_REQUEST
PUSH_REQUEST
```

---

## Human Review Boundary

The following decisions are exclusively human:

- Allow retry after violation.
- Allow retry after retry exhaustion.
- Allow retry after `BLOCKED`.
- Set `retry_allowed: yes`.
- Set retry conditions.
- Increase retry limit.
- Reset retry counter.
- Restore permission after reduced retry.
- Mark retry result as successful after violation.
- Close retry record.

Agent must not simulate any of these decisions.

---

## Violation Interaction Rules

- `NEEDS_APPROVAL` from 26.7.1 is not a retry failure by itself. The action must stop until approval is obtained; no retry failure counted.
- `NEEDS_REVIEW` from 26.7.1 is not a retry failure by itself. The action must stop until review is complete; no retry failure counted.
- `BLOCKED` from 26.7.1 may produce a violation record under 26.8.1. Any retry after a `BLOCKED` result requires a violation record reference in the retry attempt record.
- Retry after any violation requires human review.
- Retry after a `CRITICAL` violation is blocked unless the owner explicitly authorizes reset or restart.
- Retry after an open non-critical violation may proceed only with explicit human retry authorization.

---

## Repeated Failure Rule

This rule aligns with 26.8.1 `REPEATED_FAILURE` definition:

- 2–3 same-type failures within the same task may become `REPEATED_FAILURE` under 26.8.1.
- 4 or more same-type failures within the same task must be treated as `REPEATED_FAILURE`.
- Any repeated failure after `REDUCE_TO_READ_ONLY` sanction must require human review.
- Agent cannot self-classify repeated failure severity.
- Agent cannot determine whether `REPEATED_FAILURE` applies to its own attempts.

---

## Stop Conditions

Agent must stop all retry activity when any of the following are true:

```text
retry count reaches max
same failure type repeats beyond default_max_attempts_same_failure
retry result is RETRY_BLOCKED
retry result is NEEDS_REVIEW
human review is required
unresolved open violation exists
open violation exists without explicit human retry authorization
CRITICAL violation occurred
scope would expand beyond declared task to continue
M25 result is FAIL, ERROR, NOT_RUN, or INCOMPLETE without valid override
required approval is missing
human reviewer denied retry
```

When stopped, agent must:

- Record stop in the retry attempt record.
- Set `stop_required: yes` in `post_retry_state`.
- Set `next_required_action` to `HUMAN_REVIEW_REQUIRED`.
- Not attempt alternative paths to continue.
- Not re-interpret stop condition as a different condition.

---

## Evidence Requirements

Every retry attempt must produce a retry attempt record using:

`templates/retry-attempt-record.md`

Retry attempt records must reference:

- Active task ID.
- Trigger, meaning what caused the retry.
- Related violation record if retry follows a violation.
- Related checker result, such as 26.7.1 output.
- Previous attempt count.
- Same failure count.
- Retry decision and conditions.
- Permission level for retry.
- Retry plan, including intended actions, scope, commands, and paths.
- Retry outcome.
- Post-retry state.

Retry attempt records must be retained as evidence artifacts and must not be
modified or deleted by the agent.

---

## Relationship to M25 Enforcement

M25 defines merge-gate enforcement and required platform checks.

Under this policy:

- Retry does not change M25 validation results.
- Retry does not convert M25 `FAIL` to `PASS`.
- Retry does not bypass M25 required checks.
- If retry produces a new commit or change, M25 validation must be re-run before merge may be considered.
- Retry after M25 `FAIL` is only allowed if the retry plan explicitly addresses the cause of the failure and does not bypass validation.

---

## Non-Goals

This policy does not implement:

- Retry automation.
- Retry loop script.
- Automatic retry execution.
- Automatic sanction application.
- Automatic permission restoration.
- Automatic reset.
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
| 26.10.1 | Pre-Merge Corridor Audit Script | Audits whether M26 corridor artifacts exist and are internally consistent |
| 26.11.1 | Pre-Merge Corridor Smoke Fixtures | Adds negative/positive fixtures for corridor behavior |
| 26.12.1 | M26 Evidence Report | Final evidence aggregation |
| 26.13.1 | M26 Completion Review | Final milestone decision |

---

## Final Reminder

Retry is not approval.  
Retry must be bounded.  
Retry must not bypass violations.  
Retry must not become self-healing autonomy.  
Agent must stop after retry boundary is reached.

Agent cannot reset retry count.  
Agent cannot self-authorize retry after violation.

Retry record is not approval.  
Retry does not authorize commit.  
Retry does not authorize push.  
Retry does not authorize merge.  
Retry does not bypass M25.

This document does not authorize any push, commit, merge, or release.  
This document does not override M25.
