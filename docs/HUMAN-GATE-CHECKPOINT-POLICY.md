# Human Gate Checkpoint Policy

## Purpose

Define mandatory human checkpoint behavior before risky escalation in M27.

## Relationship to M27 Runtime Boundary

Human gate is a stop point in runtime boundary: agent requests, human decides, runtime validates.
Human gate request is not approval.

## Relationship to 27.6.1 Identity Boundary

Human decision identity must be separate from agent identity.
Agent self-approval is invalid and treated as simulation.

## Relationship to 27.6.2 Token Scope Policy

Token boundaries must not simulate human decision.
Token scope does not replace human checkpoint.

## Relationship to 27.7.1 Audit Log

Human gate decisions are designed to be traceable and later auditable via immutable audit records.

## Human Gate Required Cases

- DANGEROUS command
- protected zone write
- evidence artifact access
- COMMIT_REQUEST escalation
- PUSH_REQUEST escalation
- push approval
- retry after violation
- exit from BLOCKED
- M25 override
- branch protection or workflow modification
- token scope escalation
- identity boundary exception
- violation severity reduction
- permission restoration after violation

## Decision Values

- `APPROVED`
- `REJECTED`
- `NEEDS_CLARIFICATION`
- `EXPIRED`
- `INVALID`
- `SIMULATED`
- `UNKNOWN`

## Result Values

- `HUMAN_GATE_APPROVED`
- `HUMAN_GATE_REJECTED`
- `HUMAN_GATE_NEEDS_CLARIFICATION`
- `HUMAN_GATE_REQUIRED`
- `HUMAN_GATE_EXPIRED`
- `HUMAN_GATE_INVALID`
- `HUMAN_GATE_SIMULATED`
- `HUMAN_GATE_NEEDS_REVIEW`

## Record Fields

- `schema_version`
- `gate_id`
- `task_id`
- `agent_id`
- `required_for`
- `requested_action`
- `reason`
- `decision`
- `requested_at`
- `decided_at`
- `expires_at`
- `human_decider_id`
- `human_decider_type`
- `decision_source`
- `scope`
- `non_authorization_warning`

## Evaluation Order

1. Parse arguments.
2. Load record file when required.
3. Validate required fields.
4. Validate `required_for` value.
5. Validate decision value.
6. Validate `human_decider_type`.
7. Detect agent-created or simulated approval.
8. Check expiration.
9. Check scope matches `required_for` and `requested_action`.
10. Return final result.

## Request Behavior

- `request` may create checkpoint request record.
- `request` must not set decision to `APPROVED`.
- `request` sets decision to `UNKNOWN` or `NEEDS_CLARIFICATION`.
- `request` includes `agent_id`.
- `request` does not provide human approval evidence.
- request command is not approval.

## Validation Behavior

- valid `APPROVED` => `HUMAN_GATE_APPROVED`, exit 0
- `REJECTED` => `HUMAN_GATE_REJECTED`, exit 1
- `NEEDS_CLARIFICATION` => `HUMAN_GATE_NEEDS_CLARIFICATION`, exit 1
- `UNKNOWN` => `HUMAN_GATE_REQUIRED`, exit 1
- expired => `HUMAN_GATE_EXPIRED`, exit 1
- missing field => `HUMAN_GATE_INVALID`, exit 1
- invalid decider type => `HUMAN_GATE_INVALID`, exit 1
- simulated => `HUMAN_GATE_SIMULATED`, exit 1

## Simulation Detection

Fail closed for simulated or agent-created approvals:
- `human_decider_type` is `AGENT_IDENTITY`
- `human_decider_id` equals `agent_id`
- `decision_source` contains `agent`, `self`, `auto`, `simulated`, `generated`, or `synthetic`
- missing `human_decider_id` for approved decision
- missing `decided_at` for approved decision

Approval cannot be inferred from comments, commit messages, or task text.

## Scope Rules

Approval applies only to exact `required_for` and `requested_action` scope.
Examples:
- DANGEROUS command approval does not approve push.
- PUSH approval does not approve merge.
- protected zone write approval does not approve evidence tampering.
- retry approval does not clear violations.

## Expiration Rules

- `expires_at` is required for `APPROVED`.
- expired approved decision fails closed.
- `expires_at: never` allowed only for `OWNER_ADMIN_IDENTITY`.
- missing `expires_at` for approved => `HUMAN_GATE_INVALID`.

## `--now` Test-Time Override

- `--now <iso-timestamp>` is only for test-time expiration evaluation.
- if provided, expiration uses `--now`.
- if missing, expiration uses current UTC time.
- invalid `--now` => `HUMAN_GATE_INVALID`.
- `--now` does not modify record.

## CLI Output Examples

```text
RESULT: HUMAN_GATE_APPROVED
REASON: human gate approved within scope
```

```text
RESULT: HUMAN_GATE_SIMULATED
REASON: agent_id equals human_decider_id
```

```text
RESULT: HUMAN_GATE_REQUIRED
REASON: checkpoint request created; decision pending
```

## Non-Authorization Clauses

- This policy is not approval.
- This policy does not authorize commit.
- This policy does not authorize push.
- This policy does not authorize merge.
- This policy does not authorize release.
- This policy does not authorize M25 override.
- This policy does not authorize Level 2 platform change.
- This task does not create production approval authority by itself.

## Approval Boundary Statement

Human gate request is not approval.
Human approval does not authorize push, merge, or release by itself.
