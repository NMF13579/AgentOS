---
type: canonical
module: m25
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Required Check Names

## Purpose
This document defines the stable required check names that branch protection can require.
It keeps the enforcement contract aligned with GitHub check names and prevents silent breakage when names change.
This document does not enable branch protection by itself.
This document does not make CI blocking by itself.

## Stable required check names
Required check names are part of the enforcement contract.
Required check names must not be renamed casually.
Renaming required checks can break branch protection.
Changing check names requires policy update and platform evidence update.

## Required check name table
| Type | Stable value |
|---|---|
| Workflow name | AgentOS Validate |
| Job ID | agentos-validate |
| Job display name | agentos-validate |
| Required check name | AgentOS Validate / agentos-validate |

## GitHub branch protection usage
GitHub branch protection should reference the stable required check name.
The check name must match the workflow/job naming contract exactly.
Platform enforcement depends on the repository configuration in GitHub, not on this document alone.

## Rename policy
Required check names are stable by design.
If a rename is unavoidable, this document and platform evidence must be updated together.
Renaming without platform updates can break merge gating silently.

## Non-goals
- No branch protection configuration.
- No CI blocking logic.
- No automatic approval.
- No auto-merge.
- No workflow behavior changes.

## Relationship to M25
M25 closes merge-gate enforcement.
M26 handles the pre-merge agent execution corridor.
This document supports M25 by stabilizing check names before platform enforcement is enabled.

