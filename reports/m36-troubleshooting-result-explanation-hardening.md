# M36 Troubleshooting / Result Explanation Hardening

**Task ID:** task-m36-troubleshooting-hardening
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-troubleshooting-error-message-inspection.md` exists and is complete: PASS
- Inspection did not block hardening: PASS

## Files Modified or Created
- `docs/troubleshooting.md` (Hardened)
- `docs/limitations.md` (Hardened)
- `docs/mvp-checklist.md` (Hardened)
- `examples/scenarios/failed-validation.md` (Created)

## Findings From 36.5.0 Addressed
- **P0_TROUBLESHOOTING_BLOCKER:** Language barrier resolved. `docs/troubleshooting.md` and `docs/limitations.md` are now fully in English.
- **P1_RESULT_CONFUSION:** Created `examples/scenarios/failed-validation.md` to provide a clear walkthrough of resolving a real failure.
- **P2_DOCS_POLISH:** Updated `docs/mvp-checklist.md` to be accessible to external users.

## Result Meaning Guidance Added or Improved
- Added a comprehensive Result Meaning Table to `docs/troubleshooting.md` covering PASS, WARN, BLOCKED, NOT_READY, FAIL, INCONCLUSIVE, COMMAND_NOT_AVAILABLE, INPUT_NOT_AVAILABLE, and VALIDATION_GAP.
- Included explicit first-user actions for each status.

## Command-to-Report Mapping Added or Improved
- Added a mapping table in `docs/troubleshooting.md` linking major scripts (`validate-task`, `run-all`, `agentos-validate`, `audit-mvp-readiness`) to their purpose, failure interpretation, and evidence locations.

## Failure Guidance Added or Improved
- Added a clear 8-step failure handling path in `docs/troubleshooting.md`.
- Added a "Safe Rerun Procedure" checklist.

## Human Review Guidance Added or Improved
- Defined specific triggers for requesting human review (e.g., BLOCKED status, modifying core schemas/policies).

## Remaining Gaps
- `examples/scenarios/failed-verification.md` is still in its old state (deferred to later task).

## Deferred Findings
- AI prompt guide hardening (36.6.1).

## Non-Claims
- This hardening does not make AgentOS externally usable by itself.
- This hardening does not run install smoke.
- This hardening does not run example smoke.
- This hardening does not approve release publication.
- This hardening does not authorize UI dashboard, hosted diagnostics, IDE plugin, cloud/server, vector DB, or M37 feature work.
- This hardening does not replace M36 completion review.

## Final Status
`M36_TROUBLESHOOTING_HARDENING_COMPLETE`
