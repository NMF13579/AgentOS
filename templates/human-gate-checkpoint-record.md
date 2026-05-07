# Human Gate Checkpoint Record Template

## JSON Example

```json
{
  "schema_version": "1.0",
  "gate_id": "gate-000001",
  "task_id": "27.8.1",
  "agent_id": "agent-local-001",
  "required_for": "DANGEROUS_COMMAND",
  "requested_action": "DANGEROUS_COMMAND",
  "reason": "needs risky operation review",
  "decision": "UNKNOWN",
  "requested_at": "2026-05-07T10:00:00Z",
  "decided_at": "",
  "expires_at": "",
  "human_decider_id": "",
  "human_decider_type": "HUMAN_REVIEWER_IDENTITY",
  "decision_source": "human_pending",
  "scope": "DANGEROUS_COMMAND",
  "non_authorization_warning": "request is not approval"
}
```

## Field Descriptions

- `schema_version`: record schema.
- `gate_id`: checkpoint record id.
- `task_id`: task reference.
- `agent_id`: requesting agent id.
- `required_for`: risk checkpoint category.
- `requested_action`: requested action class.
- `reason`: why checkpoint is requested.
- `decision`: human gate decision value.
- `requested_at`: request timestamp UTC.
- `decided_at`: decision timestamp UTC.
- `expires_at`: approval expiration timestamp or `never` (owner/admin only).
- `human_decider_id`: human decider id.
- `human_decider_type`: human identity type.
- `decision_source`: explicit decision source.
- `scope`: decision scope.
- `non_authorization_warning`: explicit warning text.

## Human Identity Warning

Human decision identity must be separate from `agent_id`.

## Agent Self-Approval Warning

If `human_decider_id == agent_id`, record is simulated and invalid.

## Expiration Warning

Expired approvals are invalid for execution and must fail closed.

## Scope Warning

Approval is valid only for exact `required_for` and `requested_action` scope.

## Non-Authorization Warning

This record is not approval by itself and does not authorize commit, push, merge, release, or Level 2 platform changes.
