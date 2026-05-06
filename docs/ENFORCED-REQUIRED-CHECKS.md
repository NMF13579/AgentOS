---
type: canonical
module: m25
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Enforced Required Checks

## Purpose
This document defines the source-of-truth contract for enforced AgentOS required checks.
It says which results block merge, which results require human review, and why approval cannot be inferred from PASS alone.
It defines the merge-gate contract for M25, but it does not enable enforcement by itself.

## Enforcement boundary
Enforcement depends on GitHub protected branch settings plus required checks settings.
This document defines the contract, not the platform switch.
Repository files can describe policy, but platform settings must enforce it.

## Required checks contract
Stable required check names are defined for the merge gate.
The intended required checks are:
- `scope`
- `scope-fixtures`
- `execution-audit`
- `ci-evidence`
- `m24-evidence-report`
- `m24-completion-review`

Result to merge policy:

| Result | Merge decision |
|---|---|
| PASS | merge technically allowed, but not automatic approval |
| WARN | merge blocked until human enforcement review is documented |
| FAIL | merge blocked |
| ERROR | merge blocked |
| NOT_RUN | merge blocked |
| INCOMPLETE | merge blocked |

Evidence report is not approval.
CI PASS is not human approval.
Required checks do not replace owner review.
Skipped / neutral / missing AgentOS validation must not be treated as PASS.

## Stable required check names policy
Required check names must remain stable across policy updates.
Names must be explicit, short, and tied to check purpose.
Renaming a required check is a policy change and needs human review.
Required checks are documented names for platform enforcement and must not be treated as optional labels.

## Result-to-merge policy
PASS means the check completed successfully, but it is not approval.
WARN means the check completed with warnings and the merge gate remains blocked until documented human enforcement review exists.
FAIL means the check failed and merge is blocked.
ERROR means the check could not complete correctly and merge is blocked.
NOT_RUN means a required check did not run and merge is blocked.
INCOMPLETE means required evidence is missing and merge is blocked.

## Human review policy for WARN
WARN does not equal FAIL, but WARN must not be merged silently.
WARN requires a documented human enforcement review before merge can proceed.
Human enforcement review may allow proceeding with WARN, but must not authorize auto-merge or automatic approval.

## NOT_RUN / INCOMPLETE handling
NOT_RUN is not PASS.
INCOMPLETE is not PASS.
Skipped, neutral, or missing AgentOS validation must not be treated as PASS.
NOT_RUN and INCOMPLETE block merge until a human review records how the gap is handled.

## PASS is not approval
PASS is not approval.
PASS means merge may be technically allowed, but it does not replace human review.
PASS does not prove implementation correctness.
PASS does not authorize automatic merge.
PASS does not authorize automatic approval.

## Automatic approval forbidden
Automatic approval forbidden.
Automatic approval must not be inferred from PASS, required checks, or CI evidence.
Any approval must be explicit and recorded by a human reviewer.

## Auto-merge forbidden
Auto-merge forbidden.
Merge automation must not override human review or required checks policy.
Auto-merge cannot substitute for platform enforcement or human approval.

## Platform branch protection dependency
GitHub protected branch settings are the platform mechanism that can make checks mandatory.
M25 cannot be considered fully enforced unless platform evidence confirms required checks are enabled.
Policy text alone is not enough to enforce merge gating.

## Manual GitHub settings boundary
A human or authorized platform tool must configure GitHub branch protection.
AgentOS repository files describe the policy, but they do not change GitHub settings directly.
This document must not imply that AgentOS can modify branch protection by itself.

## Repository state vs platform state
Repository state = files in repo.
Platform state = GitHub branch protection / required checks settings.
Repository state can define the contract, but platform state enforces it.
M25 cannot be considered fully enforced unless platform evidence confirms required checks are enabled.

## Non-goals
- No automatic merge.
- No automatic approval.
- No merge blocking without platform settings.
- No branch protection changes in repository files.
- No runner logic in this document.
- No changes to existing M24 behavior.

## Relationship to M24 and M26
M24 = advisory CI visibility.
M25 = merge-gate enforcement.
M26 = pre-merge agent execution corridor.
M24 prepared the enforcement foundation.
M24 did not enable enforcement.
M25 may introduce enforced CI/protected branch required checks.

