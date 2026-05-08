# M27 Commit / Push Runtime Guard

## Purpose

`scripts/agentos-git-guard.py` checks commit/push requests before execution.
The guard is read-only and does not execute git operations.

## Relationship to M27 Runtime Boundary

This guard is a mandatory Level 1 runtime boundary for git actions.

## Relationship to M26 No Direct Push Policy

M26 forbids direct unsafe push.
M27 guard enforces blocking before action.

## Relationship to M26 Commit/Push Precondition Checker

M26 checker output is consumed as input.
Checker pass is not human approval.

## Relationship to 27.2.1 Permission State

Permission state is checked via subprocess call to `scripts/agentos-permission-state.py`.

## Action Types

- `commit`
- `push`
- `merge`
- `tag`
- `remote-delete`
- `force-push`
- `status`

## Target Types

- `local`
- `feature_branch`
- `dev`
- `main`
- `protected_branch`
- `unknown`

## Evaluation Order

1. Parse arguments.
2. Normalize action/target/branch.
3. Block absolute violations.
4. Validate action and target.
5. Validate branch safety.
6. Check permission state.
7. Check precondition result.
8. Check approval record.
9. Check commit message and task id.
10. Return decision.

## Decision Model

- `GIT_ALLOWED`
- `GIT_BLOCKED`
- `GIT_NEEDS_APPROVAL`
- `GIT_NEEDS_REVIEW`
- `GIT_POLICY_VIOLATION`
- `PRECONDITION_INVALID`
- `PERMISSION_BLOCKED`
- `PERMISSION_INVALID`
- `PERMISSION_DENIED`

## Protected Branch Rules

Push to `dev`, `main`, or `protected_branch` is blocked.

## Branch Safety Rules

Unsafe branch content is blocked/reviewed (`..`, `$(`, backticks, `;`, `&&`, `||`, `>`, `<`, newline).

## Force Push Rule

`force-push` is always `GIT_POLICY_VIOLATION`.

## Remote Branch Deletion Rule

`remote-delete` is always `GIT_POLICY_VIOLATION`.

## Direct Dev/Main Push Rule

Direct push to `dev` or `main` is always `GIT_POLICY_VIOLATION`.

## Commit Precondition Rule

`commit` requires precondition result `COMMIT_ALLOWED`.
Missing precondition => `GIT_NEEDS_REVIEW`.

## Push Precondition Rule

`push` requires precondition result `PUSH_ALLOWED`.
Missing precondition => `GIT_NEEDS_REVIEW`.

## Approval Record Requirements

Approval record (supporting evidence only) must include:
- `approved: true`
- `task_id`
- `approved_by`
- `approval_scope`

Approval does not authorize force push, remote delete, direct protected push, merge, release, or M25 bypass.

## Commit Message / Task ID Rule

`commit` requires `--commit-message`.
`--task-id` is required unless task id is extractable from commit message.
Valid message is not approval.

## CLI Output Examples

```text
RESULT: GIT_ALLOWED
REASON: status check is allowed
```

```text
RESULT: GIT_POLICY_VIOLATION
REASON: direct push to dev is blocked
```

## Non-Authorization Clauses

- This guard is not approval.
- This guard does not authorize commit execution.
- This guard does not authorize push execution.
- This guard does not authorize merge.
- This guard does not authorize release.
- `GIT_ALLOWED` is not merge approval.
- `GIT_ALLOWED` does not bypass M25.

## Execution Boundary

The guard does not execute git commit, git push, or git merge.
