# M27 Command Enforcement Runtime (27.3.1)

## Purpose

`scripts/agentos-command-guard.py` is a read-only guard that evaluates command requests and returns policy decisions.
The guard does not execute commands.

## Relationship to M27 Runtime Boundary

This guard is Level 1 runtime enforcement for command routing.
Agent requests commands, runtime guard decides allowed/blocked/review/approval.

## Relationship to M26 Command Allowlist Policy

M26 defined command corridor and violation classes.
M27 command guard enforces those constraints at request time before execution.

## Relationship to 27.2.1 Permission State

When permission state is required or provided, this guard calls:
`python3 scripts/agentos-permission-state.py check <file> --requires <LEVEL>`

If permission check is blocked/denied/invalid/review, command is denied fail-closed.

## Command Categories

- `SAFE_READ`
- `SAFE_VALIDATE`
- `SAFE_TEST`
- `WRITE_LOCAL`
- `GIT_LOCAL`
- `GIT_REMOTE`
- `DANGEROUS`
- `FORBIDDEN`
- `UNKNOWN`

## Command Content Priority Rule

Declared `--category` is a hint only.
Command content has priority.
Content-based blocker overrides declared category.

## Evaluation Order

1. Parse arguments.
2. Validate category string.
3. Check TIER_1 blockers.
4. Apply category hard blocks (`FORBIDDEN`, `UNKNOWN`, `GIT_REMOTE`).
5. Check TIER_2 blockers.
6. Apply `WRITE_LOCAL` special rule.
7. Check `DANGEROUS` approval record.
8. Check permission state (if required or provided).
9. Return final decision.

## Two-Tier Content Blocking

TIER_1 blockers (all categories, including `DANGEROUS`):
- `git commit`
- `git push`
- `git merge`
- `gh pr merge`
- `sudo rm`
- `chmod -R 777`
- approval simulation writes

TIER_2 blockers:
- `rm -rf` variants

TIER_2 behavior:
- non-`DANGEROUS`: `COMMAND_POLICY_VIOLATION`
- `DANGEROUS`: go to approval flow

## Blocked Command Content Patterns

Examples:
- `git commit -m test`
- `git push origin dev`
- `gh pr merge 100 --squash`
- `sudo rm -rf /tmp/x`
- `chmod -R 777 .`

## Approval Simulation Write Rule

Write/overwrite/append/delete actions that target approval-like paths or names are policy violations.
Read-only commands like `cat`, `grep`, `rg`, `sed -n` are not simulation by themselves.

## Decision Model

- `COMMAND_ALLOWED`
- `COMMAND_BLOCKED`
- `COMMAND_NEEDS_APPROVAL`
- `COMMAND_NEEDS_REVIEW`
- `COMMAND_POLICY_VIOLATION`
- `PERMISSION_BLOCKED`
- `PERMISSION_INVALID`
- `PERMISSION_DENIED`

## Dangerous Command Approval Rule

`DANGEROUS` requires `--approval-record` with valid JSON fields:
- `approved: true`
- `task_id`
- `approved_by`

Without valid record: `COMMAND_NEEDS_APPROVAL`.
With valid record and clean checks: `COMMAND_ALLOWED`.

## Approval Record Requirements

Example file:
`tests/fixtures/m27-command-guard/valid-approval.json`

Record must not be treated as authorization for push/merge/release.

## Unknown Command Fail-Closed Rule

Unknown/unrecognized category returns `COMMAND_NEEDS_REVIEW`.
Ambiguous high-risk content also returns `COMMAND_NEEDS_REVIEW`.

## Raw Git Commit / Push Prohibition

Raw `git commit` and raw `git push` are always blocked by content enforcement.

## WRITE_LOCAL Boundary with 27.4.1

`WRITE_LOCAL` requires `--permission-state`.
Path-level write enforcement is out of scope here and belongs to `27.4.1`.

## CLI Output Examples

```text
RESULT: COMMAND_ALLOWED
REASON: command passed guard checks
```

```text
RESULT: COMMAND_POLICY_VIOLATION
REASON: tier 1 blocker: tier_1_command_blocker
```

```text
RESULT: COMMAND_NEEDS_APPROVAL
REASON: dangerous command requires approval record
```

## Non-Authorization Clauses

- This script does not authorize git commit.
- This script does not authorize git push.
- This script does not authorize git merge.
- This script does not authorize release.
- `COMMAND_ALLOWED` does not bypass M25.
- `COMMAND_ALLOWED` does not override M26 corridor boundaries.
- `COMMAND_ALLOWED` does not authorize push, merge, or release.
- Approval records accepted by this guard do not authorize remote operations.

## Execution Safety

This guard never executes the requested command.
