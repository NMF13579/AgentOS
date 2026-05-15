## M42.1 status inspected
- Source: `reports/m42-1-completion-review.md`
- Status found: `M42_1_REGRESSION_BASELINE_COMPLETE_WITH_GAPS`

## Summary
M42.2 creates an executable regression runner for unified integrity.
M42.2 does not create new Honest PASS behavior.
M42.2 does not modify agentos-validate.py.
Regression runner detects drift; it does not grant approval.
Regression runner result is validation evidence, not approval.
Known gaps are not clean regression PASS.
Human approval remains above every PASS.

## runner created
- `scripts/test-integrity-regression.py`

## command existence checks
Implemented checks for:
- integrity help
- integrity list-fixtures json
- integrity fixtures json
- integrity strict fixtures json
- integrity registry json
- integrity explain-results
- integrity explain-result INTEGRITY_WARNING
- integrity fixtures summary
- integrity strict fixtures summary
- all strict

## JSON validity checks
Implemented and executed for:
- list-fixtures json
- fixtures json
- strict fixtures json
- explicit registry json

## stable JSON field checks
Implemented minimum-field checks (`suite`, `result`, `generated_at`, `details`) for fixtures json and strict fixtures json.
Optional source fields are handled safely and recorded in details if absent.

## token checks
Implemented allowed token contract check:
- INTEGRITY_OK
- INTEGRITY_WARNING
- INTEGRITY_VIOLATION
- INTEGRITY_NEEDS_REVIEW
- INTEGRITY_BLOCKED

## summary output checks
Implemented semantic field checks for summary outputs.
Implemented case-insensitive summary phrase matching to avoid false regressions on capitalization-only formatting changes.

## case-insensitive summary phrase matching
- Implemented via case-insensitive substring search.
- Result: working.

## unknown token behavior
- `integrity --explain-result UNKNOWN_TOKEN` checked.
- Expected non-zero behavior enforced.

## abbreviation safety behavior
- `integrity --explain-r INTEGRITY_WARNING` checked.
- Expected non-zero behavior enforced.

## summary/json conflict behavior
- `integrity --fixtures --summary --json` checked.
- Drift detected: command returns non-zero, but expected conflict message is missing in output path currently observed by runner.
- Reported as `SUMMARY_JSON_CONFLICT_REGRESSION`.

## authority-boundary text checks
Implemented required-good and forbidden-bad phrase scan.
Educational `BAD:` lines are ignored to avoid false positives.

## authority-boundary scanned files availability result
- Files available for scan: 5
- No authority-boundary files available for scan. (fallback message implemented in runner for missing-file scenario)

## shell=True check
Implemented static scan over `scripts/agentos-validate.py` without embedding forbidden literal in runner source.
Result: PASS (no forbidden usage detected).

## known gaps
- `all --strict` remains non-zero due known repository baseline failures (outside M42.2 scope).
- `warning-not-clean-pass` check produced `NEEDS_REVIEW` in one path because phrase is validated strongly in summary output and weakly in JSON details.

## SKIPPED_KNOWN_GAP overall-result behavior
- Runner supports `SKIPPED_KNOWN_GAP` status and elevates overall result to at least `INTEGRITY_REGRESSION_NEEDS_REVIEW` when such status appears.

## validation commands run
- `python3 scripts/test-integrity-regression.py --help`
- `python3 scripts/test-integrity-regression.py`
- `python3 scripts/test-integrity-regression.py --json`
- `python3 -m json.tool /tmp/agentos-m42-integrity-regression.json >/dev/null`
- required grep checks from task

## runner result
- Final result: `INTEGRITY_REGRESSION_FAILED`
- Main fail class observed: `SUMMARY_JSON_CONFLICT_REGRESSION`
- Needs-review class observed: `SUMMARY_CONTRACT_REGRESSION`

## recommended M42.3 action
- Align `integrity --fixtures --summary --json` output-path behavior with conflict-message contract.
- Decide whether warning-not-clean-pass must be asserted exclusively from summary output rather than JSON details.
- Add dedicated known-gap registry for runner skips when approved by milestone policy.
