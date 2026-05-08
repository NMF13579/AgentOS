# M27 GitHub CI Enforcement Gate

## Status

- Level 2 artifact.
- Optional.
- Disabled by default.
- Guided setup required.
- Not required for Level 1 completion.
- Not approval.
- Not merge authorization.
- Not platform enforcement by itself.

## Core Principle

- Repo workflow can run checks.
- GitHub platform enforcement requires required-check configuration.
- Only owner/admin can enable blocking behavior.
- Ordinary users do not configure GitHub settings.

## What This Task Creates

- `.github/workflows/m27-enforcement.yml`
- `docs/M27-GITHUB-CI-GATE.md`

## What This Task Does Not Do

- Does not enable branch protection.
- Does not configure required checks.
- Does not configure CODEOWNERS.
- Does not restrict bypass permissions.
- Does not disable force push.
- Does not disable branch deletion.
- Does not create secrets.
- Does not authorize merge.

## Required Check Name

Expected check name:
- `M27 Enforcement`

This name may later be configured by owner/admin as a required check in 27.12.3 / 27.12.4.

## Level 2 Status Behavior

- `LEVEL_2_AVAILABLE` when workflow artifact exists but platform settings are not enabled.
- `SKIPPED_LEVEL_2_NOT_ENABLED` when owner/admin has not enabled Level 2.
- `PLATFORM_ENFORCED` only after platform verification confirms required check is enabled.

## Relationship to Level 1

- Level 1 remains required.
- Level 2 disabled does not fail Level 1.
- Level 2 workflow does not replace Level 1 runtime guards.
- Level 2 CI does not bypass local AgentOS enforcement runtime.

## Relationship to M25 and M26

- M27 CI does not bypass M25.
- M27 CI does not replace M25 merge gates.
- M27 CI preserves M26 corridor boundaries.
- CI PASS is not approval.

## Owner/Admin Setup Boundary

- Enabling required checks requires owner/admin action.
- Agent must not simulate owner/admin setup.
- Agent must not claim platform enforcement is enabled unless verified by later platform check.

## Non-Authorization Clauses

- This workflow is not approval.
- This workflow does not authorize commit.
- This workflow does not authorize push.
- This workflow does not authorize merge.
- This workflow does not authorize release.
- This workflow does not enable Level 2 platform enforcement by itself.
- This workflow does not override M25.
- This workflow does not override M26.
- This workflow does not override M27 runtime guards.

## Non-Goals

- Do not implement CODEOWNERS.
- Do not implement branch protection policy.
- Do not implement platform setup guide.
- Do not implement platform enforcement check.
- Do not create platform evidence report.
- Do not modify GitHub settings.
- Do not make the check required.
- Do not create secrets or credentials.
- Do not implement new runtime guard logic.
