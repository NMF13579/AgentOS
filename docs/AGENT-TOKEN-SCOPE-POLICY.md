# Agent Token Scope Policy

## Status

- This is a policy document only.
- This is not approval.
- This is not implementation.
- This is not a secret store.
- This is not authorization for commit, push, merge, release, approval, or GitHub platform change.

## Core Principle

- Agent identity and privileged credentials must be separated.
- Agent may request guarded actions.
- Runner may execute approved guarded actions.
- Privileged credentials belong to controlled runtime/runner, not agent context.
- If the agent has admin token, runtime boundary is bypassable.

## Token Classes

- `AGENT_RUNTIME_TOKEN`
- `RUNNER_PRIVILEGED_TOKEN`
- `HUMAN_OWNER_ADMIN_TOKEN`
- `READ_ONLY_TOKEN`
- `CI_CHECK_TOKEN`
- `UNKNOWN_TOKEN`

## Allowed Agent Token Capabilities

Safe or conditionally safe capabilities:
- repository read
- branch read
- issue/PR read
- status read
- checks read
- local runtime request submission
- artifact read where permitted by policy

Rules:
- Allowed capability is not approval.
- Allowed capability does not authorize push.
- Allowed capability does not authorize merge.
- Allowed capability does not bypass M25/M26/M27.

## Forbidden Agent Token Capabilities

- admin
- branch protection write
- ruleset write
- required checks bypass
- unrestricted workflow write
- secrets write
- environment protection bypass
- direct push to dev/main
- force push
- branch deletion
- merge permission
- PR approval permission
- CODEOWNERS bypass
- release publish
- package publish unless explicitly approved outside this policy

## Runner Credential Boundary

- Runner may hold privileged credentials only inside controlled runtime.
- Privileged credentials must not be exposed to agent prompt/context/logs.
- Agent may request action; runner decides and executes through guards.
- Runner credentials must be scoped to the minimum required action.
- Runner credential use must be traceable.
- Runner credential use must not bypass human gate.
- Runner credential use must not bypass M25.

## Level 1 / Level 2 Relationship

- Level 1 Repo/Git Runtime Control works without ordinary-user GitHub setup.
- Level 2 GitHub Platform Control is optional and owner/admin-enabled.
- Level 2 disabled must not fail Level 1.
- Level 2 disabled status may be `SKIPPED_LEVEL_2_NOT_ENABLED`.
- Token policy applies to both levels.
- Level 2 setup requires owner/admin action and must not be simulated by agent.

## Identity Boundary Relationship

Reference: `27.6.1` Agent Identity Boundary Policy.

- Agent token must map to agent identity, not human reviewer identity.
- Human reviewer/owner/admin identity must not be impersonated by token use.
- Token use must preserve actor traceability.
- `approved_by` must not be derived from agent token.

## Runtime Guard Relationship

References:
- `27.2.1` Permission State Store
- `27.3.1` Command Enforcement Runtime
- `27.4.1` Write Enforcement Runtime
- `27.5.1` Commit / Push Runtime Guard

Requirements:
- Guards must fail closed when token boundary is violated.
- Token scope must not override permission state.
- Token scope must not override command/write/git guard decisions.
- Token scope must not clear violations.
- Token scope must not reset retry count.

## Token Scope Review Requirements

Review record must include:
- `task_id`
- `agent_id`
- `token_class`
- `requested_scope`
- `allowed_scope`
- `forbidden_scope_check`
- `credential_owner`
- `runner_boundary_status`
- `identity_boundary_status`
- `approval_required`
- `reviewer_id`
- `decision`
- `timestamp`
- non-authorization warning

## Violation Categories

- `AGENT_ADMIN_TOKEN_EXPOSURE`
- `BRANCH_PROTECTION_SCOPE_EXPOSURE`
- `REQUIRED_CHECKS_BYPASS_SCOPE`
- `WORKFLOW_WRITE_SCOPE_EXCESS`
- `SECRET_EXPOSURE`
- `HUMAN_TOKEN_IMPERSONATION`
- `RUNNER_CREDENTIAL_LEAK`
- `DIRECT_PUSH_SCOPE_EXPOSURE`
- `MERGE_PERMISSION_EXPOSURE`
- `PR_APPROVAL_SCOPE_EXPOSURE`
- `UNKNOWN_TOKEN_SCOPE`

## Non-Authorization Clauses

- This policy is not approval.
- This policy does not authorize commit.
- This policy does not authorize push.
- This policy does not authorize merge.
- This policy does not authorize release.
- This policy does not create or store secrets.
- This policy does not enable Level 2 platform enforcement.
- This policy does not override M25.
- This policy does not override M26.
- This policy does not override M27 runtime guards.

## Non-Goals

- Do not implement token provisioning.
- Do not implement secret storage.
- Do not implement GitHub settings.
- Do not implement branch protection.
- Do not implement CODEOWNERS.
- Do not implement runtime credential injection.
- Do not implement human gate.
- Do not implement audit log.
- Do not implement scripts.
- Do not create fixtures.
