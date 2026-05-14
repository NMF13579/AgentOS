# M40.10 Runtime Bypass Smoke Report

## M40.9 Status Inspected
- Source: `reports/m40-9-completion-review.md`
- Status: `M40_9_STRICT_MODE_READY_WITH_GAPS`

## Files Created
- `scripts/test-m40-runtime-bypass-smoke.py`
- `docs/M40-RUNTIME-BYPASS-SMOKE.md`
- `tests/fixtures/m40-runtime-bypass/` and required subgroup directories
- `reports/m40-10-runtime-bypass-smoke-report.md`
- `reports/m40-10-completion-review.md`

## Fake Binaries Implemented
- git, rm, sh, bash, gh, curl, wget
- marker-based detection only, no dangerous real execution

## Scenario Groups Implemented
- raw command bypass
- raw write bypass
- raw git bypass
- approval simulation
- permission state tampering
- retry reset
- audit tampering
- unified CLI downgrade
- token exposure boundary

## Commands Run
- `python3 scripts/test-m40-runtime-bypass-smoke.py --help`
- `python3 scripts/test-m40-runtime-bypass-smoke.py --explain`
- `python3 scripts/test-m40-runtime-bypass-smoke.py`
- `python3 scripts/test-m40-runtime-bypass-smoke.py --keep-sandbox`
- `python3 scripts/test-m40-runtime-bypass-smoke.py --json`
- JSON validation via `python3 -m json.tool`

## JSON Validation
- valid JSON: yes
- `sandbox_used: true`: yes
- `production_sandbox_claimed: false`: yes
- `secret_values_printed: false`: yes

## Marker Summary
Markers detected for raw git/rm/shell/gh/curl/wget attempts.

## Protected Canary Hash Summary
No unexpected protected canary hash changes detected.

## Token Exposure Summary
Only presence classification recorded; token values not printed and not stored.

## Final Harness Result
`BYPASS_TEST_PASS_WITH_WARNINGS`

## Known Gaps
- Smoke simulation only, not production isolation.
- No cryptographic audit authority.

## Deferred Items
- M40.11 validator authority boundary
- M40.12 evidence immutability
- M40.13 closure review

## Required Explicit Statements
M40.10 creates a runtime bypass smoke harness only.
M40.10 does not implement production-grade sandboxing.
M40.10 does not prove full physical isolation.
M40.10 does not implement validator authority boundary.
M40.10 does not implement evidence immutability.
M40.10 does not replace human approval.
Controlled bypass findings in M40.10 are smoke-simulation findings, not proof of production-grade interception.
