# M27 Write Enforcement Runtime

## Purpose

`scripts/agentos-write-guard.py` checks write requests before execution.
It returns a decision and never performs file writes.

## Relationship to M27 Runtime Boundary

This guard is a mandatory Level 1 runtime boundary.
Agent requests a write; runtime decides allow/block/review/approval.

## Relationship to M26 Write Allowlist Policy

M26 defined allowed, conditional, forbidden, and protected write zones.
M27 write guard enforces those boundaries in runtime.

## Relationship to M26 Scope-Bound Diff Checker

M26 defined scope-bound checking.
M27 write guard applies pre-write scope decision using `--scope-file` input.

## Relationship to 27.2.1 Permission State

If `--permission-state` is provided, guard calls:
`python3 scripts/agentos-permission-state.py check <file> --requires LOCAL_EDIT`

Blocked/invalid/denied permission blocks write request.

## Operation Types

- `create`
- `modify`
- `append`
- `delete`
- `move`
- `overwrite`

## Path Classes

- `ALLOWED_WRITE_PATH`
- `CONDITIONAL_WRITE_PATH`
- `FORBIDDEN_WRITE_PATH`
- `PROTECTED_ZONE`
- `EVIDENCE_ARTIFACT`
- `GENERATED_ARTIFACT`
- `TEMP_ARTIFACT`
- `UNKNOWN_PATH`

## Evaluation Order

1. Parse arguments.
2. Normalize path.
3. Block traversal and absolute paths.
4. Apply hard path blocks.
5. Apply operation rules.
6. Check scope (`--scope-file`) when needed.
7. Check permission state when provided.
8. Check approval record when required.
9. Return final decision.

## Decision Model

- `WRITE_ALLOWED`
- `WRITE_BLOCKED`
- `WRITE_NEEDS_APPROVAL`
- `WRITE_NEEDS_REVIEW`
- `WRITE_POLICY_VIOLATION`
- `PERMISSION_BLOCKED`
- `PERMISSION_INVALID`
- `PERMISSION_DENIED`

## Scope Behavior

- `CONDITIONAL_WRITE_PATH` without `--scope-file` => `WRITE_NEEDS_REVIEW`
- `CONDITIONAL_WRITE_PATH` with scope but out of list => `WRITE_BLOCKED`
- `CONDITIONAL_WRITE_PATH` with scope and in list => continue checks
- `UNKNOWN_PATH` fails closed

Scope file must be read-only input with `allowed_write_paths` list.

## Protected Zone Rules

`PROTECTED_ZONE` requires approval record.
Even with valid approval, this guard returns review path (no direct write authorization).

## Evidence Artifact Tampering Rule

For `EVIDENCE_ARTIFACT`:
- `modify`, `delete`, `overwrite` => blocked/policy violation
- `append` => requires approval/audit path; not directly allowed here

## Deletion Rule

`delete` requires explicit approval record.
Without it: `WRITE_NEEDS_APPROVAL`.
With it: `WRITE_NEEDS_REVIEW` (still no direct execution).

## Move Operation Rule

`move` is treated as delete + create.
Same approval boundary as deletion.
No direct move authorization by this guard.

## Completed Milestone Artifact Rule

Modification of completed milestone artifacts is blocked.

## Permission State Integration

Permission check is subprocess-only.
No import of permission script as Python module.
Guard does not modify permission state files.

## Approval Record Requirements

Approval file must:
- exist
- be valid JSON object
- include `approved: true`
- include `task_id`
- include `approved_by`

Approval record does not authorize commit/push/merge/release.

## CLI Output Examples

```text
RESULT: WRITE_ALLOWED
REASON: write request passed guard checks
```

```text
RESULT: WRITE_NEEDS_APPROVAL
REASON: protected zone requires approval
```

```text
RESULT: WRITE_POLICY_VIOLATION
REASON: evidence artifact tampering is forbidden
```

## Non-Authorization Clauses

- This script is not approval.
- This script does not authorize commit.
- This script does not authorize push.
- This script does not authorize merge.
- This script does not authorize release.
- This script does not override M25.
- This script does not override M26.
- Documentation alone does not enforce runtime behavior.

## Execution Boundary

The write guard does not perform writes.
