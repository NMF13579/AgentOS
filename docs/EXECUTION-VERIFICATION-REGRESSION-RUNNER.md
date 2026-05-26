# Execution Verification Regression Runner

## Purpose

Provide a read-only regression runner that checks preservation of M56–M59 execution-verification mechanics and M60 cleanup foundations.

## Scope

This runner validates artifacts, final-status markers, non-authority boundaries, source existence, and downstream safety boundaries.
It does not mutate files and does not execute real task flows.

## Relationship to M56–M59

The runner checks that required M59 artifacts exist directly and that M56–M58 artifact coverage remains discoverable from canonical sources.

## Relationship to M60 Cleanup

The runner validates required M60 artifacts up to 60.10, then checks registry and reusable-chain checkers as dependencies.
It blocks premature downstream outputs beyond allowed phase boundaries.
`no-premature-downstream` is phase-aware through 60.15: after `reports/m60-cleanup-integration-summary.md` exists with `FINAL_STATUS: M60_INTEGRATION_PASS`, `FINAL_STATUS: M60_INTEGRATION_PASS_WITH_WARNINGS`, or `FINAL_STATUS: M60_INTEGRATION_BLOCKED`, the 60.12 report itself is treated as a valid current-phase artifact and is not blocked by existence alone. After `reports/m60-cleanup-action-review.json` exists and parses with `final_status` in `M60_CLEANUP_ACTION_REVIEW_PASS`, `M60_CLEANUP_ACTION_REVIEW_PASS_WITH_WARNINGS`, or `M60_CLEANUP_ACTION_REVIEW_BLOCKED`, the 60.13 report itself is treated as a valid current-phase artifact and is not blocked by existence alone. After `reports/m60-cleanup-evidence-report.md` contains `FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE`, `FINAL_STATUS: M60_CLEANUP_EVIDENCE_COMPLETE_WITH_WARNINGS`, or `FINAL_STATUS: M60_CLEANUP_EVIDENCE_BLOCKED`, the 60.14 report itself is treated as a valid current-phase artifact and is not blocked by existence alone. After `reports/m60-completion-review.md` contains `FINAL_STATUS: M60_CLEANUP_COMPLETE`, `FINAL_STATUS: M60_CLEANUP_COMPLETE_WITH_WARNINGS`, or `FINAL_STATUS: M60_CLEANUP_BLOCKED`, the 60.15 report itself is treated as a valid current-phase artifact and is not blocked by existence alone.

## Implemented Checks

- `m56-artifacts`
- `m57-artifacts`
- `m58-artifacts`
- `m59-artifacts`
- `m60-artifacts`
- `registry`
- `reusable-chain`
- `non-authority`
- `final-status`
- `no-premature-downstream`

## CLI Usage

```bash
python3 scripts/check-execution-verification-regression.py --help
python3 scripts/check-execution-verification-regression.py --json
python3 scripts/check-execution-verification-regression.py --strict --json
python3 scripts/check-execution-verification-regression.py --check all --json
python3 scripts/check-execution-verification-regression.py --check registry --json
python3 scripts/check-execution-verification-regression.py --check no-premature-downstream --json
python3 scripts/check-execution-verification-regression.py --explain
```

## Result Values

- `EXECUTION_VERIFICATION_REGRESSION_PASS`
- `EXECUTION_VERIFICATION_REGRESSION_PASS_WITH_WARNINGS`
- `EXECUTION_VERIFICATION_REGRESSION_BLOCKED`

## Exit Code Mapping

- `EXECUTION_VERIFICATION_REGRESSION_PASS` -> `0`
- `EXECUTION_VERIFICATION_REGRESSION_PASS_WITH_WARNINGS` -> `0`
- `EXECUTION_VERIFICATION_REGRESSION_BLOCKED` -> `2`

## JSON Output

With `--json`, output is valid JSON only.
JSON includes result, exit_code, strict, root, registry_path, schema_path, requested/run checks, warnings/blockers, status fields, dependency results, and `non_authority` exact statements.

## Strict Mode

`--strict` may escalate uncertainty warnings to blockers for required artifact existence, final status markers, non-authority boundaries, registry/reusable validity, or downstream safety.
`--strict` never downgrades blockers and never converts invalid input into pass.

## Non-Authority Boundary

Execution verification regression runner is not approval.
Execution verification regression runner does not verify a real execution result.
Execution verification regression runner does not start cleanup execution.
Execution verification regression runner does not mutate lifecycle state.
Execution verification regression runner does not authorize merge, push, or release.
Execution verification regression runner does not change M56–M59 safety semantics.
Execution verification regression runner does not replace human review.
Execution verification regression runner does not start M61 or M62.
Execution verification regression runner does not authorize starting 60.12 automatically.

## Semantics Preservation Boundary

The runner validates preservation; it does not redefine policy decisions, status mappings, approval semantics, or result-verification semantics.

## Validation Assumption

Positive validation expects repository state consistent with completed 60.10.
If state is corrupted or contradictory, blocked result is expected and required.

## Forbidden Uses

- Treating runner output as task approval
- Treating runner output as lifecycle mutation authorization
- Treating runner output as human-review replacement
- Treating runner output as real execution-result verification

## Known Limitations

- M56–M58 artifact checks may warn when exact canonical paths are not deterministically discoverable from current canonical sources.
- Runner depends on registry and reusable-chain local checkers for part of validation.

## Final Regression Runner Status

FINAL_STATUS: M60_REGRESSION_RUNNER_DEFINED

This means only that regression runner and documentation exist.
It does not mean cleanup is approved.
It does not mean M60 is complete.
It does not mean M61 or M62 may start.
