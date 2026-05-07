# Agent Identity Boundary Policy

## Status

- This is a policy document only.
- This is not approval.
- This is not implementation.
- This is not authorization for commit, push, merge, release, or approval.

## Core Principle

- Agent identity and human identity are separate.
- Agent may request actions.
- Human may approve actions.
- Agent must not approve its own work.
- Agent must not impersonate human reviewer or owner.

## Identity Types

- `AGENT_IDENTITY`
- `HUMAN_REVIEWER_IDENTITY`
- `OWNER_ADMIN_IDENTITY`
- `RUNTIME_SYSTEM_IDENTITY`
- `UNKNOWN_IDENTITY`

## Required Rules

- Agent must not impersonate human reviewer.
- Agent must not use admin identity.
- Agent must not fill reviewer fields.
- Agent must not create approval records on behalf of humans.
- Agent must not mark own work as human-reviewed.
- Agent must not change `approved_by` fields.
- Agent must not clear or downgrade identity violations.
- Agent identity must be visible in decision records.
- Runtime-generated records must distinguish `agent_id` from `approved_by`.

## Approval Boundary

- Human approval cannot be simulated.
- Approval requires human-controlled identity.
- Approval record must identify `approved_by` separately from `agent_id`.
- Agent-created approval record is invalid.
- Approval is not commit authorization.
- Approval is not push authorization.
- Approval is not merge authorization.
- Approval does not bypass M25.

## Audit Traceability

Future runtime decision records must include:
- `task_id`
- `agent_id`
- `actor_type`
- `requested_action`
- `decision`
- `timestamp`
- `identity_source`
- `approved_by`, only when human approval exists
- `reviewer_id`, only when human review exists

Allowed `actor_type` values:
- `AGENT_IDENTITY`
- `HUMAN_REVIEWER_IDENTITY`
- `OWNER_ADMIN_IDENTITY`
- `RUNTIME_SYSTEM_IDENTITY`
- `UNKNOWN_IDENTITY`

## Violation Categories

- `HUMAN_IMPERSONATION`
- `APPROVAL_SIMULATION`
- `REVIEWER_FIELD_TAMPERING`
- `ADMIN_IDENTITY_USE`
- `IDENTITY_SOURCE_MISSING`
- `AGENT_SELF_APPROVAL`
- `UNKNOWN_IDENTITY_USE`

## Relationship to M27 Guards

This policy applies to:
- `27.2.1` Permission State Store
- `27.3.1` Command Enforcement Runtime
- `27.4.1` Write Enforcement Runtime
- `27.5.1` Commit / Push Runtime Guard

Guard requirements from this policy:
- Guards must treat agent-created approval as invalid.
- Guards must fail closed when required identity source is missing.
- Guards must preserve identity traceability.

## Relationship to M25 and M26

- This policy does not bypass M25.
- This policy preserves M26 violation policy.
- Identity violations may trigger M26 sanctions.
- M27 enforces identity boundaries before risky actions.

## Non-Authorization Clauses

- This policy is not approval.
- This policy does not authorize commit.
- This policy does not authorize push.
- This policy does not authorize merge.
- This policy does not authorize release.
- This policy does not create Level 2 platform enforcement.
- This policy does not override M25.
- This policy does not override M26.

## Non-Goals

- Do not implement token scope policy.
- Do not implement approval records.
- Do not implement human gate.
- Do not implement audit log.
- Do not implement runtime scripts.
- Do not modify existing guards.
- Do not create fixtures.
- Do not create GitHub platform settings.
