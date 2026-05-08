# M27 Runtime Boundary Contract

## Purpose
M27 runtime boundary means risky actions must go through M27 runtime checks before execution.
Agent may request an action, but runtime guard scripts decide whether the action is allowed, blocked, or needs review/approval.

## Enforcement Scripts
The M27 runtime boundary is enforced by these scripts:
- `scripts/agentos-permission-state.py`
- `scripts/agentos-command-guard.py`
- `scripts/agentos-write-guard.py`
- `scripts/agentos-git-guard.py`
- `scripts/agentos-audit-log.py`
- `scripts/agentos-human-gate.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-enforce.py`

## Boundary Rules
- Guards are mandatory boundaries, not optional helper scripts.
- Agent may request actions.
- Agent may not directly execute risky actions.
- Agent must not bypass runtime guards.

## What M27 Does NOT Do
- M27 does not bypass M25.
- M27 preserves M26 corridor boundaries.
- M27 does not grant approval.
- M27 does not grant merge authorization.
- Level 2 disabled does not fail Level 1.

## Optional Level 2 State
`SKIPPED_LEVEL_2_NOT_ENABLED` is a valid state when Level 2 is not enabled.
This state is optional-level behavior and must not fail Level 1 completion.

## Related Policies
- [AGENT-IDENTITY-BOUNDARY-POLICY.md](/Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/AGENT-IDENTITY-BOUNDARY-POLICY.md)
- [AGENT-TOKEN-SCOPE-POLICY.md](/Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/AGENT-TOKEN-SCOPE-POLICY.md)
- [IMMUTABLE-AUDIT-LOG-POLICY.md](/Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/IMMUTABLE-AUDIT-LOG-POLICY.md)
- [HUMAN-GATE-CHECKPOINT-POLICY.md](/Users/muhammednazyrov/Documents/GitHub/AgentOS/docs/HUMAN-GATE-CHECKPOINT-POLICY.md)

## Non-Authorization
This document is not approval.
This document does not authorize commit, push, merge, or release.
