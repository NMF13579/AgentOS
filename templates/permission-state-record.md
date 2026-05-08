# Permission State Record Template

## JSON Example Record

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

## Field Descriptions

- `schema_version`: record schema version.
- `active_task_id`: active task identifier.
- `agent_id`: unique agent identifier.
- `current_permission`: current permission level.
- `permission_record`: link/path to supporting permission record.
- `open_violations`: list of unresolved violation IDs.
- `retry_count`: retry count for current task context.
- `blocked_state`: hard blocked state flag.
- `expiration`: ISO 8601 UTC timestamp or `never`.
- `last_decision`: last permission decision.
- `updated_at`: last update timestamp in UTC.

## Warnings

- Agent cannot self-declare permission.
- Agent cannot self-clear `BLOCKED`.
- Agent cannot reset `retry_count`.
- Permission state is not approval for commit, push, merge, or release.
