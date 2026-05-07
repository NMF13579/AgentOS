# Permission State Store (M27 Level 1)

## Purpose

`scripts/agentos-permission-state.py` validates and checks agent permission state files in fail-closed mode.
It only reads state and returns a decision result.

## Relationship to M27 Runtime Boundary

M27 Level 1 requires runtime guard routing.
Permission state is an input boundary for guarded execution decisions.
This store does not execute commands, does not approve risky actions, and does not bypass human gate.

## Relationship to M26 Permission Model

M26 defined policy and violation model.
This store applies those constraints at runtime input level:
- blocked and invalid states are denied;
- open violations require review on guarded checks;
- agent cannot self-authorize through malformed state.

## State File Schema

Required fields:
- `schema_version`
- `active_task_id`
- `agent_id`
- `current_permission`
- `permission_record`
- `open_violations`
- `retry_count`
- `blocked_state`
- `expiration`
- `last_decision`
- `updated_at`

## Allowed Permission Levels

Rank order:
- `BLOCKED`: 0
- `READ_ONLY`: 1
- `PATCH_PROPOSE`: 2
- `LOCAL_EDIT`: 3
- `LOCAL_TEST`: 4
- `COMMIT_REQUEST`: 5
- `PUSH_REQUEST`: 6

## Blocked-State Rules

If `blocked_state == true`, result is `PERMISSION_BLOCKED`.
If `current_permission == "BLOCKED"`, result is `PERMISSION_BLOCKED`.

## Expiration Rules

Allowed expiration values:
- ISO 8601 UTC timestamp string
- `never`

`null` expiration is treated as expired.
Past timestamp is expired.
Expired result: `PERMISSION_EXPIRED`.

## Retry Count Ownership

`retry_count` must be integer and must be `>= 0`.
Negative or non-integer values are invalid.
Agent cannot reset retry count through this tool.

## Violation Visibility

`open_violations` must be a list.
- `validate`: non-empty list is allowed.
- `check --requires LEVEL`: non-empty list returns `NEEDS_REVIEW`.

Agent cannot self-clear violations through this tool.

## Fail-Closed Behavior

- Missing file: `NEEDS_REVIEW`
- Invalid JSON: `PERMISSION_INVALID`
- Missing field: `PERMISSION_INVALID`
- Unknown permission: `PERMISSION_INVALID`
- Blocked state or blocked permission: `PERMISSION_BLOCKED`
- Expired or null expiration: `PERMISSION_EXPIRED`
- Invalid retry count: `PERMISSION_INVALID`
- Invalid `open_violations` type: `PERMISSION_INVALID`
- Insufficient rank in `check`: `PERMISSION_DENIED`
- Open violations in `check`: `NEEDS_REVIEW`
- All valid checks passed: `PERMISSION_OK`

## Valid Example

```json
{
  "schema_version": "1.0",
  "active_task_id": "27.2.1",
  "agent_id": "agent-local-001",
  "current_permission": "LOCAL_EDIT",
  "permission_record": "records/permission-001.md",
  "open_violations": [],
  "retry_count": 0,
  "blocked_state": false,
  "expiration": "never",
  "last_decision": "PERMISSION_OK",
  "updated_at": "2026-05-07T10:00:00Z"
}
```

## Invalid Example

```json
{
  "schema_version": "1.0",
  "agent_id": "agent-local-001",
  "current_permission": "SUPER_ADMIN",
  "permission_record": "records/permission-001.md",
  "open_violations": "none",
  "retry_count": -1,
  "blocked_state": false,
  "expiration": null,
  "last_decision": "PERMISSION_OK",
  "updated_at": "2026-05-07T10:00:00Z"
}
```

## Non-Authorization Clauses

- This document is not approval.
- This document does not authorize commit.
- This document does not authorize push.
- This document does not authorize merge.
- This document does not authorize release.
- This document does not override M25.
- This document does not replace M26 corridor boundaries.
- Documentation alone does not enforce runtime behavior.
