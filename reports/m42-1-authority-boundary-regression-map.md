## PASS / Approval Boundary
- PASS must remain a validation signal only.
- PASS must never be represented as approval grant.

## Summary / Evidence Boundary
- Summary output is guidance for users.
- Summary output is not evidence authority.

## Registry / Policy Boundary
- Fixture registry orchestrates command execution.
- Registry is not policy authority.

## Strict Validation / Authorization Boundary
- strict validation affects validation outcome only.
- strict validation must not authorize release/merge/push.

## Warning / Clean PASS Boundary
- warnings may be non-blocking in configured flows.
- warning must never be called clean PASS.

## Source Token / Unified Token Boundary
- unified token provides navigation layer.
- source token meaning remains authoritative for domain semantics.

## Regression Examples
BAD: PASS replaces human approval.
BAD: Checker PASS is approval.
BAD: INTEGRITY_WARNING is clean PASS.
BAD: Summary output is evidence authority.
BAD: Registry is policy authority.
BAD: all --strict authorizes release.
BAD: Unified status replaces source token.

GOOD: PASS is a validation signal, not authorization.
GOOD: Checker PASS is validation signal, not approval.
GOOD: INTEGRITY_WARNING is not clean PASS.
GOOD: Summary output is user guidance, not evidence authority.
GOOD: Fixture registry is navigation metadata, not policy, proof, or approval.
GOOD: Human approval remains above every PASS.

## Required Future Checks
- CLI text regression checks for BAD phrases.
- summary-mode regression checks for approval wording.
- strict aggregation regression checks for warning semantics.
- source-token preservation regression checks in JSON outputs.

Authority-boundary regression is P0 if it creates false approval, false authorization, or false clean PASS.
