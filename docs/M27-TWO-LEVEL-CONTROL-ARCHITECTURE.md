# M27 Two-Level Agent Control Architecture

## Core Principle

M27 introduces two-level runtime control boundaries for AgentOS.

- Level 1 is enabled by default and enforces control from repo/git/runtime.
- Ordinary users configure nothing for Level 1.
- Level 2 is optional GitHub Platform Control and is enabled only by repository owner/admin.
- M26 checked and recorded policy corridor behavior.
- M27 blocks and enforces runtime boundaries.

M27 preserves M25 merge gates and M26 corridor boundaries.
M27 does not override human approval.
M27 does not authorize push, merge, release, or approval.

## Control Levels

### Level 1 — Repo/Git Runtime Control

- `default`: enabled
- `required_for_m27_completion`: yes
- `user_setup_required`: no
- `ordinary_user_involved`: no
- `enforcement_location`: AgentOS repo/git/runtime scripts
- `expected_control`: about 65–70%

Level 1 is the required baseline for M27 completion.

### Level 2 — GitHub Platform Control

- `default`: disabled
- `required_for_level_1_completion`: no
- `setup_required`: yes
- `setup_actor`: repository_owner_or_admin
- `ordinary_user_involved`: no
- `enforcement_location`: GitHub required checks, branch protection, CODEOWNERS
- `expected_control_with_level_1`: about 82–85%

Level 2 is optional and platform-side.
Level 2 is not required for Level 1 completion.

## Responsibility Boundary

- Agent may request guarded actions.
- Agent must not directly bypass runtime guards.
- Runtime decides: allowed / blocked / needs review.
- Human gate controls risky escalation.
- Repository owner/admin controls GitHub platform settings.

## Level 1 Completion Rule

M27 Level 1 can be complete even when Level 2 is disabled.

## Level 2 Skip Rule

Status: `SKIPPED_LEVEL_2_NOT_ENABLED`

This status is valid when repository owner/admin has not enabled Level 2.
This status must not fail Level 1.

## Final Statuses

- `M27_LEVEL_1_COMPLETE_PLATFORM_OPTIONAL`
- `M27_LEVEL_2_PLATFORM_ENFORCED`
- `M27_INCOMPLETE`
- `M27_BLOCKED`

## Non-Authorization Clauses

- This architecture document is not approval.
- This architecture document does not authorize commit.
- This architecture document does not authorize push.
- This architecture document does not authorize merge.
- This architecture document does not override M25.
- This architecture document does not enable Level 2 by itself.

## Non-Goals

- Do not implement enforcement runtime.
- Do not implement permission state.
- Do not implement command guard.
- Do not implement write guard.
- Do not implement git guard.
- Do not implement audit scripts.
- Do not implement GitHub platform setup.
- Do not create smoke fixtures.
