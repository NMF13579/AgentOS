# M27 Branch Protection Policy

## Status

- Level 2 policy artifact.
- Optional.
- Disabled by default.
- Guided setup required.
- Owner/admin action required.
- Not required for Level 1 completion.
- Not approval.
- Not merge authorization.
- Not platform enforcement by itself.

## Core Principle

- Branch protection is a GitHub platform control.
- Only owner/admin can enable it.
- AgentOS may guide setup but must not simulate setup.
- Ordinary users do not configure GitHub settings.

## What This Task Creates

- `docs/M27-BRANCH-PROTECTION-POLICY.md`
- `templates/m27-branch-protection-review.md`

## What This Task Does Not Do

- does not enable branch protection
- does not configure required checks
- does not configure required CODEOWNERS review
- does not modify GitHub settings
- does not restrict bypass permissions by itself
- does not disable force push by itself
- does not disable branch deletion by itself
- does not create secrets
- does not authorize merge

## Required Branches

- `dev`
- `main`

Both `dev` and `main` are protected targets for Level 2 setup.
Direct push to `dev`/`main` must be blocked by platform settings when Level 2 is enabled.

## Required Branch Protection / Ruleset Settings

Owner/admin must configure at minimum:
- require pull request before merging
- require approvals before merge
- require review from CODEOWNERS
- require status checks to pass before merge
- require `M27 Enforcement` check
- require `M25 Validation`, if present
- require branches to be up to date before merge if available
- disable force pushes
- disable branch deletion
- restrict bypass permissions
- restrict who can push to matching branches where appropriate
- prevent direct pushes to `dev`/`main`
- prevent admins bypassing rules unless explicitly accepted by owner/admin policy
- require conversation resolution before merge if available
- require signed commits if adopted by repo policy
- do not allow auto-merge unless separately approved by owner/admin policy

## Required Status Checks

Expected check names:
- `M27 Enforcement`
- `M25 Validation`, if present

These are expected names for later owner/admin setup.
Their presence in policy does not enable required checks.
Required-check enforcement is verified later by `27.13.1`.

- CI PASS is not approval.
- Required checks do not replace human review.
- Required checks do not bypass M25.
- Required checks do not replace Level 1 runtime guards.

## CODEOWNERS Review Requirement

- CODEOWNERS review should be required for enforcement-sensitive paths.
- CODEOWNERS file existence is not enough.
- Required CODEOWNERS review must be enabled by owner/admin.
- Placeholder owners must be replaced during guided setup.

## Force Push / Branch Deletion Restrictions

- Force push must be disabled for `dev`/`main`.
- Branch deletion must be disabled for `dev`/`main`.
- Remote branch deletion must not be allowed as an agent action.
- Approval does not allow force push or branch deletion.

## Bypass Permission Restrictions

- Bypass permissions must be restricted.
- Agent identity must not receive bypass permission.
- Agent token must not bypass required checks.
- Agent token must not edit branch protection.
- Owner/admin bypass policy must be explicit and documented.

## Level 2 Status Behavior

- `LEVEL_2_AVAILABLE` when policy artifacts exist but platform settings are not enabled.
- `SKIPPED_LEVEL_2_NOT_ENABLED` when owner/admin has not enabled Level 2.
- `LEVEL_2_NEEDS_OWNER_ACTION` when settings are partial or missing after setup starts.
- `PLATFORM_ENFORCED` only after platform verification confirms required settings.

## Relationship to 27.12.1 GitHub CI Gate

- M27 Enforcement workflow provides the check artifact.
- Branch protection makes the check blocking only after owner/admin setup.
- Workflow existence alone is not platform enforcement.

## Relationship to 27.12.2 CODEOWNERS

- CODEOWNERS defines sensitive path ownership.
- Branch protection/rulesets make CODEOWNERS review required only after owner/admin setup.
- CODEOWNERS existence alone is not platform enforcement.

## Relationship to Level 1

- Level 1 remains required.
- Level 2 disabled does not fail Level 1.
- Branch protection does not replace Level 1 runtime guards.
- Branch protection does not bypass local AgentOS enforcement runtime.

## Relationship to M25 and M26

- Branch protection does not bypass M25.
- Branch protection complements M25 merge gates.
- Branch protection preserves M26 corridor boundaries.
- Branch protection does not authorize merge by itself.

## Owner/Admin Setup Boundary

- Enabling branch protection requires owner/admin action.
- Agent must not simulate owner/admin setup.
- Agent must not claim platform enforcement is enabled unless verified by `27.13.1`.
- Guided setup is handled later by `27.12.4`.

## Non-Authorization Clauses

- This policy is not approval.
- This policy does not authorize commit.
- This policy does not authorize push.
- This policy does not authorize merge.
- This policy does not authorize release.
- This policy does not enable Level 2 platform enforcement by itself.
- This policy does not override M25.
- This policy does not override M26.
- This policy does not override M27 runtime guards.
