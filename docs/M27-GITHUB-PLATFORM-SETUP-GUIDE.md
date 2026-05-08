# M27 GitHub Platform Setup Guide

## Status

- Level 2 setup guide.
- Optional.
- Disabled by default.
- Owner/admin action required.
- Not required for Level 1 completion.
- Not approval.
- Not merge authorization.
- Not platform enforcement by itself.

## Core Principle

- Level 2 is optional GitHub Platform Control.
- Only owner/admin can enable it.
- AgentOS may guide setup but must not perform or simulate owner/admin action.
- Ordinary users do not configure GitHub settings.

## Prerequisites

- `27.12.1` M27 GitHub CI Gate exists.
- `27.12.2` CODEOWNERS exists.
- `27.12.3` Branch Protection Policy exists.
- Owner/admin access to repository settings.
- No secrets or admin tokens should be shared with agent.

## Setup Flow

1. Confirm current Level 2 status.
Status options:
- Level 2 disabled
- Level 2 available
- Level 2 setup in progress
- Level 2 needs owner action
- Level 2 platform enforced

2. Verify repo-side artifacts exist:
- `.github/workflows/m27-enforcement.yml`
- `.github/CODEOWNERS`
- `docs/M27-GITHUB-CI-GATE.md`
- `docs/M27-CODEOWNERS-POLICY.md`
- `docs/M27-BRANCH-PROTECTION-POLICY.md`

3. Open GitHub repository settings.
- Go to Branches / Rulesets.
- Target branches: `dev`, `main`.

4. Configure required pull request rules.
- Require pull request before merging.
- Require approvals before merge.
- Require conversation resolution if available.

5. Configure required status checks.
- Require status checks before merge.
- Require `M27 Enforcement`.
- Require `M25 Validation`, if present.
- Require branches to be up to date before merge if available.

6. Configure CODEOWNERS review.
- Require review from CODEOWNERS.
- Replace placeholder owners in `.github/CODEOWNERS` before enforcement.
- Ensure enforcement-sensitive paths have valid owners.

7. Disable dangerous branch actions.
- Disable force pushes.
- Disable branch deletion.
- Prevent direct pushes to `dev`/`main` where available.

8. Restrict bypass permissions.
- Restrict who can bypass branch protection/rulesets.
- Ensure agent identity has no bypass permission.
- Ensure agent token cannot edit branch protection.
- Document owner/admin bypass exceptions, if any.

9. Confirm secret/token safety.
- Do not paste secrets into chat.
- Do not store token values in templates.
- Runner credentials must remain outside agent context.

10. Run platform verification handoff.
- `27.13.1` verifies actual platform state.
- Do not claim `PLATFORM_ENFORCED` until verification passes.

11. Record setup session.
- Fill `templates/m27-platform-setup-session.md`.
- Record owner/admin actor.
- Record settings configured.
- Record known gaps.
- Record verification status.

## Branch Targets

- `dev`
- `main`

## Required Checks

- `M27 Enforcement`
- `M25 Validation`, if present

- Check names must match GitHub check names exactly.
- Required-check setup must be verified later by `27.13.1`.
- CI PASS is not approval.

## CODEOWNERS Setup

- Placeholder owners must be replaced by owner/admin.
- CODEOWNERS review must be required in GitHub settings.
- CODEOWNERS existence alone is not enforcement.

## Branch Protection / Ruleset Setup

- Require PR before merge.
- Require status checks.
- Require CODEOWNERS review.
- Disable force push.
- Disable branch deletion.
- Restrict bypass permissions.
- Prevent direct pushes where available.

## Secret / Token Safety

- Do not paste tokens into agent/chat.
- Do not store secrets in repository.
- Do not record secret values in setup session.
- Runner privileged credentials must remain outside agent context.

## Platform Verification Handoff

- `27.13.1` verifies actual GitHub Platform Control.
- Until `27.13.1` confirms `PLATFORM_ENFORCED`, status is not `PLATFORM_ENFORCED`.
- Partial setup should produce `LEVEL_2_NEEDS_OWNER_ACTION` or `PLATFORM_PARTIAL`.

## Level 2 Status Behavior

- `SKIPPED_LEVEL_2_NOT_ENABLED`
- `LEVEL_2_AVAILABLE`
- `LEVEL_2_SETUP_IN_PROGRESS`
- `LEVEL_2_NEEDS_OWNER_ACTION`
- `PLATFORM_PARTIAL`
- `PLATFORM_ENFORCED`

## Relationship to Level 1

- Level 1 remains required.
- Level 2 disabled does not fail Level 1.
- Level 2 setup does not replace Level 1 runtime guards.
- GitHub platform controls complement local AgentOS runtime controls.

## Relationship to M25 and M26

- Level 2 does not bypass M25.
- Level 2 complements M25 merge gates.
- Level 2 preserves M26 corridor boundaries.
- Level 2 setup does not authorize merge.

## Non-Authorization Clauses

- This guide is not approval.
- This guide does not authorize commit.
- This guide does not authorize push.
- This guide does not authorize merge.
- This guide does not authorize release.
- This guide does not enable Level 2 platform enforcement by itself.
- This guide does not override M25.
- This guide does not override M26.
- This guide does not override M27 runtime guards.
