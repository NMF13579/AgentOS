# Execution Verification Reusable Checks

## Purpose

Define the minimal reusable execution verification checks approved for M60.8.

## Scope

Only consolidate-now checks are implemented in `scripts/check-execution-verification-chain.py`.

## Relationship to M60.7 Plan

This implementation follows `reports/m60-validator-consolidation-plan.md` and includes only checks classified as consolidate-now.

## Implemented Checks

- registry
- non-authority
- source-artifact-existence
- no-premature-downstream-artifacts
- schema-json-validity
- policy-version-presence
- final-status-presence

M60 phase-aware downstream artifact detection:
- `no-premature-downstream-artifacts` теперь учитывает завершённую фазу M60 по `FINAL_STATUS` в уже созданных M60-артефактах.
- После подтверждённого завершения 60.9 не блокируется `reports/m60-documentation-pruning-plan.md`.
- После подтверждённого завершения 60.10 не блокируется `reports/m60-documentation-consolidation-report.md`.
- После появления `docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md` с `FINAL_STATUS: M60_REGRESSION_RUNNER_DEFINED` не блокируются артефакты 60.11 regression runner.
- После появления `reports/m60-cleanup-integration-summary.md` с `FINAL_STATUS: M60_INTEGRATION_PASS`, `FINAL_STATUS: M60_INTEGRATION_PASS_WITH_WARNINGS` или `FINAL_STATUS: M60_INTEGRATION_BLOCKED` не блокируется сам артефакт 60.12.
- После появления `reports/m60-cleanup-action-review.json` с `final_status` из семейства `M60_CLEANUP_ACTION_REVIEW_*` не блокируется сам артефакт 60.13.
- После появления `reports/m60-cleanup-evidence-report.md` с `FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE`, `FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE_WITH_WARNINGS` или `FINAL_STATUS: M60_CLEANUP_EVIDENCE_BLOCKED` не блокируется сам артефакт 60.14.
- После появления `reports/m60-completion-review.md` с `FINAL_STATUS: M60_CLEANUP_COMPLETE`, `FINAL_STATUS: M60_CLEANUP_COMPLETE_WITH_WARNINGS` или `FINAL_STATUS: M60_CLEANUP_BLOCKED` не блокируется сам артефакт 60.15.
- Преждевременные downstream-артефакты 60.12–60.15 продолжают блокироваться.
- Реальные M61/M62 артефакты продолжают блокироваться по наличию `m61`/`m62` в пути.

## Checks Not Implemented

Not implemented in 60.8:
- checks classified as leave-local
- checks classified as unsafe-to-consolidate
- checks classified as future-candidate
- checks classified as manual-review-required

## CLI Usage

```bash
python3 scripts/check-execution-verification-chain.py --help
python3 scripts/check-execution-verification-chain.py --json
python3 scripts/check-execution-verification-chain.py --strict --json
python3 scripts/check-execution-verification-chain.py --check all --json
python3 scripts/check-execution-verification-chain.py --check registry --json
```

## Result Values

- `EXECUTION_VERIFICATION_CHAIN_VALID`
- `EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS`
- `EXECUTION_VERIFICATION_CHAIN_INVALID`

## Exit Code Mapping

- `EXECUTION_VERIFICATION_CHAIN_VALID` -> `0`
- `EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS` -> `0`
- `EXECUTION_VERIFICATION_CHAIN_INVALID` -> `2`

## JSON Output

With `--json`, checker outputs valid JSON only and includes result, exit code, checks, warnings/blockers, and non_authority statements.

## Strict Mode

`--strict` may promote warnings to blockers for critical uncertainty.
`--strict` never downgrades blockers and never converts invalid input into pass.

## Non-Authority Boundary

Execution verification reusable checks are not approval.
Execution verification reusable checks do not start cleanup execution.
Execution verification reusable checks do not mutate lifecycle state.
Execution verification reusable checks do not authorize merge, push, or release.
Execution verification reusable checks do not change M56–M59 safety semantics.
Execution verification reusable checks do not replace human review.
Execution verification reusable checks do not verify a real execution result.
Execution verification reusable checks do not authorize starting 60.9 automatically.

## Semantics Preservation Boundary

The checker preserves existing pass/fail/block semantics and does not redefine policy/status/authority semantics.

## Forbidden Uses

- using checker output as approval
- using checker output as execution authorization
- using checker output to replace human review

## Known Limitations

- local milestone-specific checks intentionally remain outside reusable scope
- some policy version nuances remain warning-level unless strict mode escalates

## Final Reusable Checks Status

FINAL_STATUS: M60_REUSABLE_CHECKS_DEFINED

This means only that minimal reusable checks exist.
It does not mean documentation pruning started.
It does not mean regression runner exists.
It does not mean M60 is complete.
