# M27 CODEOWNERS Policy

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

- CODEOWNERS identifies review ownership for sensitive paths.
- GitHub platform enforcement requires branch protection or ruleset configuration.
- Only owner/admin can enable required CODEOWNERS review.
- Ordinary users do not configure GitHub settings.

## What This Task Creates

- `.github/CODEOWNERS`
- `docs/M27-CODEOWNERS-POLICY.md`

## What This Task Does Not Do

- does not enable branch protection
- does not configure required reviews
- does not configure required checks
- does not restrict bypass permissions
- does not disable force push
- does not disable branch deletion
- does not create secrets
- does not authorize merge

## Protected Path Coverage

Protected because these paths define or enforce workflow/runtime boundaries and verification behavior:
- `.github/workflows/`
- `.github/CODEOWNERS`
- `scripts/agentos-*.py`
- `scripts/*enforce*.py`
- `scripts/*guard*.py`
- `docs/*POLICY*.md`
- `docs/M27-*.md`
- `templates/*record*.md`
- `templates/*review*.md`
- `reports/milestone-*`
- `tests/fixtures/m27-*/`

## Owner Placeholder Policy

- Placeholders are allowed only until owner/admin setup.
- Agent must not invent owner handles.
- Owner/admin must replace placeholder during guided setup.
- Placeholder does not mean review is enforced.

## Level 2 Status Behavior

- `LEVEL_2_AVAILABLE` when CODEOWNERS artifact exists but platform settings are not enabled.
- `SKIPPED_LEVEL_2_NOT_ENABLED` when owner/admin has not enabled Level 2.
- `PLATFORM_ENFORCED` only after platform verification confirms required CODEOWNERS review is enabled.

## Relationship to 27.12.1 GitHub CI Gate

- CODEOWNERS complements the M27 Enforcement workflow.
- Workflow existence and CODEOWNERS existence are not enough for platform enforcement.
- Both become blocking only through owner/admin platform settings.

## Relationship to Level 1

- Level 1 remains required.
- Level 2 disabled does not fail Level 1.
- CODEOWNERS does not replace Level 1 runtime guards.
- CODEOWNERS does not bypass local AgentOS enforcement runtime.

## Relationship to M25 and M26

- CODEOWNERS does not bypass M25.
- CODEOWNERS does not replace M25 merge gates.
- CODEOWNERS preserves M26 corridor boundaries.
- CODEOWNERS review is not approval for merge by itself.

## Owner/Admin Setup Boundary

- Enabling required CODEOWNERS review requires owner/admin action.
- Agent must not simulate owner/admin setup.
- Agent must not claim platform enforcement is enabled unless verified by later platform check.

## Non-Authorization Clauses

- This CODEOWNERS file is not approval.
- This CODEOWNERS file does not authorize commit.
- This CODEOWNERS file does not authorize push.
- This CODEOWNERS file does not authorize merge.
- This CODEOWNERS file does not authorize release.
- This CODEOWNERS file does not enable Level 2 platform enforcement by itself.
- This CODEOWNERS file does not override M25.
- This CODEOWNERS file does not override M26.
- This CODEOWNERS file does not override M27 runtime guards.

## Non-Goals

- Do not implement branch protection policy.
- Do not implement platform setup guide.
- Do not implement platform enforcement check.
- Do not create platform evidence report.
- Do not modify GitHub settings.
- Do not make CODEOWNERS review required.
- Do not create secrets or credentials.
- Do not implement new runtime guard logic.
