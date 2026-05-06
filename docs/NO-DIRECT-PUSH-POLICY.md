---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-04
task_id: 26.6.1
milestone: M26
---

# No Direct Push Policy

## Purpose

This policy defines the rules for remote push behavior in the AgentOS repository.
It states which branches are protected, what approval is required before a push,
and how push decisions relate to M26 policy documents and M25 enforcement.

This is a policy contract only.
Machine enforcement of push preconditions belongs to Task 26.7.1.

This document does not authorize push, commit, merge, release, auto-merge, or
automatic approval. It does not override M25.

## Relationship to Pre-Merge Execution Corridor

The Pre-Merge Execution Corridor in `docs/PRE-MERGE-EXECUTION-CORRIDOR.md`
governs agent behavior before merge.

- `PUSH_APPROVED` does not satisfy the full corridor.
- `PUSH_APPROVED` does not authorize merge or release.
- Completing a push does not approve a PR.
- Completing a push does not bypass M25.

## Relationship to Agent Permission Model

The Agent Permission Model in `docs/AGENT-PERMISSION-MODEL.md` defines which
actions an agent may request.

- Remote push is a `GIT_REMOTE` remote-write action.
- `PUSH_REQUEST` does not authorize push by itself.
- `PUSH_REQUEST` only authorizes requesting push approval.
- Permission level does not bypass scope, command, write, push, or M25 rules.

Permission is not approval.
Push permission is not merge approval.
Push permission is not M25 override.

## Relationship to Command Allowlist Policy

The Command Allowlist Policy in `docs/COMMAND-ALLOWLIST-POLICY.md` defines
command categories and command approval requirements.

- `GIT_REMOTE` remote-read actions such as `git fetch` or `git clone` are
  governed by the Command Allowlist Policy and are not push approval.
- `GIT_REMOTE` remote-write actions such as `git push`, remote branch creation,
  tag push, or remote branch deletion are governed by this policy.
- `git push` is restricted.
- `git push --force` is blocked.
- `git push origin :<branch>` or equivalent remote branch deletion is blocked.
- Command approval is not push approval unless it explicitly covers the
  specific remote-write action, branch, and commit.

## Relationship to Scope-Bound Diff Checker

The Scope-Bound Diff Checker from Task 26.5.1 verifies changed files against
declared scope.

- `SCOPE_OK` is not push approval.
- `SCOPE_WARNING` is not push approval.
- `SCOPE_VIOLATION` blocks push.
- `NEEDS_REVIEW` blocks push until ambiguity is resolved.

## Core Principle

Agent must not push directly to `dev` or `main` under any circumstances.
Agent must not push to any remote branch without explicit push approval.

Every remote-write push requires:

1. A completed scope check with `SCOPE_OK` or resolved `SCOPE_WARNING`.
2. A valid M25 validation result of `PASS`, or an explicit M25 override record.
3. An explicit push approval from a human reviewer.
4. A completed push request record.
5. No open violations.
6. No protected-branch direct push target.

## Protected Branch Rule

The following branches are protected:

| Branch | Direct Push | Force Push | Delete |
|---|---|---|---|
| `main` | BLOCKED | BLOCKED | BLOCKED |
| `dev` | BLOCKED | BLOCKED | BLOCKED |

- Direct push to `dev` is blocked.
- Direct push to `main` is blocked.
- No approval record may authorize direct push to `dev` or `main`.
- Protected branch changes must go through PR and M25 merge-gate enforcement.

## Remote Branch Rule

Feature branches and other non-protected remote branches are not free-write
targets.

- Push approval is per branch, per commit, and time-limited.
- Approval for one branch does not apply to another branch.
- Approval for one commit does not apply to another commit.
- Expired approval reverts to `NEEDS_HUMAN_REVIEW`.

## Push Approval Rule

Push approval is explicit human authorization for a specific push operation.

Push approval requires:

- Scope check completed.
- M25 validation result `PASS`, or a valid M25 override under M25 policy.
- Push request record completed.
- Human reviewer identified.
- No open `SCOPE_VIOLATION`.
- No open unresolved `PUSH_BLOCKED`.
- No open M25 `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` without override.
- Target is not `dev` or `main`.

Push approval does not mean PR approval, merge approval, release approval,
scope override, command override, or write override.

## Remote Branch Creation Rule

Creating a new remote branch is a high-risk operation.

- Remote branch creation requires explicit authorization.
- Remote branch creation requires `push_type: REMOTE_BRANCH_CREATE`.
- The push request record must set `remote_branch_creation_requested: yes`.
- Risk level for remote branch creation is at least `HIGH`.

## Runner-Controlled Push

Runner-controlled push is policy intent only in this task.
Implementation belongs to Task 26.7.1.

- The runner must verify push preconditions before push.
- The runner must not push if any precondition is unsatisfied.
- The runner must not push directly to `dev` or `main`.
- The runner must not self-approve push requests.
- The runner must not simulate human reviewer approval.

## Human-Controlled Push

- Human must confirm scope check result before push.
- Human must confirm M25 validation or M25 override status before push.
- Human must complete or reference a push request record.
- Human must not directly push to `dev` or `main`.

## Forbidden Push Actions

| Action | Status |
|---|---|
| Direct push to `dev` | `PUSH_BLOCKED` |
| Direct push to `main` | `PUSH_BLOCKED` |
| `PROTECTED_BRANCH_PUSH` | `PUSH_BLOCKED` |
| Force push to any branch | `PUSH_BLOCKED` |
| Remote branch deletion | `PUSH_BLOCKED` |
| Push after `SCOPE_VIOLATION` | `PUSH_BLOCKED` |
| Push with unresolved `NEEDS_REVIEW` | `PUSH_BLOCKED` |
| Push with M25 `FAIL` without override | `PUSH_BLOCKED` |
| Push with M25 `WARN` without override | `PUSH_BLOCKED` |
| Push with M25 `ERROR` without override | `PUSH_BLOCKED` |
| Push with M25 `NOT_RUN` without override | `PUSH_BLOCKED` |
| Push with M25 `INCOMPLETE` without override | `PUSH_BLOCKED` |
| Silent remote branch creation | `PUSH_BLOCKED` |
| Tag push without explicit authorization | `PUSH_BLOCKED` |
| Auto-merge | `PUSH_BLOCKED` |
| Automatic push approval | `PUSH_BLOCKED` |
| Agent-simulated human approval | `PUSH_BLOCKED` |
| Push after expired approval without renewal | `PUSH_BLOCKED` |

## Push Preconditions

Before any push may proceed, all of the following must be satisfied:

- scope_check_result is `SCOPE_OK`, or `SCOPE_WARNING` with conditions met.
- scope_check_result is not `SCOPE_VIOLATION`.
- scope_check_result is not unresolved `NEEDS_REVIEW`.
- m25_validation_result is `PASS`, or an M25 override record is valid.
- m25_validation_result is not `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` without override.
- push_request_record is completed.
- push_approval is `PUSH_APPROVED` or `PUSH_APPROVED_WITH_CONDITIONS`.
- approval_expiration is not expired.
- protected_branch_target is `no`.
- push_type is not `PROTECTED_BRANCH_PUSH`.
- push_type is not `FORCE_PUSH`.
- push_type is not `REMOTE_BRANCH_DELETE`.
- remote_branch_creation_requested is authorized if yes.
- tag push is explicitly authorized if push_type is `TAG_PUSH`.
- violations_open is `no`.

## Push Decision States

| State | Meaning |
|---|---|
| `PUSH_APPROVED` | Explicit human decision approving an approvable push after all preconditions are satisfied. |
| `PUSH_APPROVED_WITH_CONDITIONS` | Explicit human decision approving an approvable push subject to listed conditions. |
| `NEEDS_HUMAN_REVIEW` | Preconditions incomplete or ambiguous; human review required before push. |
| `PUSH_DENIED` | Push explicitly denied; new request required. |
| `PUSH_BLOCKED` | Push blocked; no approval path available under this policy. |

## Push Risk Levels

| Scenario | Risk Level |
|---|---|
| Push to existing feature branch, SCOPE_OK, M25 PASS | `MEDIUM` |
| Push to existing feature branch after resolved SCOPE_WARNING | `HIGH` |
| Remote branch creation | `HIGH` |
| Tag push with explicit authorization | `HIGH` |
| Push with M25 override | `CRITICAL` |
| Push after SCOPE_VIOLATION | `PUSH_BLOCKED` |
| Direct push to dev or main | `PUSH_BLOCKED` |
| PROTECTED_BRANCH_PUSH | `PUSH_BLOCKED` |
| Force push to any branch | `PUSH_BLOCKED` |
| Remote branch deletion | `PUSH_BLOCKED` |

## Relationship to Commit / Push Control Script

Task 26.7.1 will implement a machine check of commit and push preconditions.

The Commit / Push Control Script will verify scope, M25 validation, push
request record, protected target, push type, approval expiration, and open
violations before push.

## Relationship to M25 Enforcement

M25 defines merge-gate enforcement and required platform checks.

- M25 validation result must be `PASS` before push approval may be granted,
  unless an M25 override record is separately satisfied under M25 policy.
- M25 `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` blocks push approval
  without override.
- Push approval does not change M25 validation results.
- Push approval does not satisfy M25 override requirements.
- Completing a push does not satisfy M25 required checks.

## Evidence Requirements

Every remote-write push requires a completed push request record using
`templates/push-request-record.md`.

The push request record must reference:

- Active task ID.
- Source branch.
- Target remote.
- Target branch.
- Push type.
- Scope check result and artifact.
- M25 validation result and artifact.
- M25 override record if applicable.
- Commit reference.
- Changed files summary.
- Human reviewer.
- Approval conditions if any.
- Expiration.
- Decision state.

## Non-Goals

This policy does not implement:

- Push control script.
- Git hooks.
- CI/CD workflow changes.
- Branch protection changes.
- Runner-controlled push execution.
- Remote approval app.
- Messenger approvals.
- Agent runner.
- Auto-merge.
- Automatic approval.
- Self-healing commits.
- Production deployment controls.
- Tag signing or release management.

## M26 Follow-Up Tasks

| Task | Title | Relationship |
|---|---|---|
| 26.7.1 | Commit / Push Control Script | Machine-checks commit/push preconditions defined here |
| 26.8.1 | Agent Violation / Sanctions Policy | Defines consequences for push and corridor violations |
| 26.9.1 | Bounded Retry Loop Policy | Defines retry boundaries after blocked push/precondition failure |
| 26.10.1 | Pre-Merge Corridor Audit Script | Audits M26 corridor artifacts |
| 26.11.1 | Pre-Merge Corridor Smoke Fixtures | Adds negative/positive fixtures for corridor behavior |
| 26.12.1 | M26 Evidence Report | Final evidence aggregation |
| 26.13.1 | M26 Completion Review | Final milestone decision |

## Final Reminder

Agent must not push directly to dev or main under any circumstances.
Agent must not push to any remote branch without explicit push approval.
`SCOPE_OK` is not push approval.
`COMMAND_APPROVED` is not push approval unless it explicitly covers a `GIT_REMOTE` remote-write action for the specific branch and commit.
`WRITE_SCOPE_APPROVED` is not push approval.
`PUSH_APPROVED` is not merge approval.
`PUSH_APPROVED` is not release approval.
`PUSH_APPROVED` does not bypass M25.
This document does not authorize any push, commit, merge, release, auto-merge, or automatic approval.
This document does not override M25.
