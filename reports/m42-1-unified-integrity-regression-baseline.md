## Purpose
Define the stable regression baseline for unified integrity after M41 closure.

Regression baseline is a stability contract, not approval authority.
M42.1 does not implement regression runner.
M42.1 does not modify agentos-validate.py.

## M41 Closure Status
- M41.6 status: `M41_6_UNIFIED_INTEGRITY_CONSOLIDATION_COMPLETE_WITH_GAPS`.

## Stable CLI Surface
- `python3 scripts/agentos-validate.py integrity --help`
- `python3 scripts/agentos-validate.py integrity --list-fixtures --json`
- `python3 scripts/agentos-validate.py integrity --fixtures --json`
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --json`
- `python3 scripts/agentos-validate.py integrity --fixtures --summary`
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --summary`
- `python3 scripts/agentos-validate.py integrity --explain-results`
- `python3 scripts/agentos-validate.py integrity --explain-result INTEGRITY_WARNING`
- `python3 scripts/agentos-validate.py all --strict`
- `python3 scripts/agentos-validate.py all --strict --json` (supported in current state, still non-zero due known baseline failures)

## Stable Result Tokens
- INTEGRITY_OK
- INTEGRITY_WARNING
- INTEGRITY_VIOLATION
- INTEGRITY_NEEDS_REVIEW
- INTEGRITY_BLOCKED

Unified status is navigation metadata, not replacement for source token.

## Stable JSON Fields
Stable minimum fields for integrity JSON baseline:
- suite
- result
- exit_code
- generated_at
- details
- source_result
- source_failure_class
- source_output

Notes:
- Some commands expose a subset; this is accepted if documented in report-level contract.
- `details` field presence is baseline-stable.
- Ordering/structure inside `details` is deferred to M42.2.

## Stable Summary Output Fields
- Integrity Result:
- Clean PASS:
- Strict Mode:
- Source Tokens Preserved:
- Warnings:
- Violations:
- Needs Review:
- Blocked:
- Next Safe Action:
- Human Approval:
- Limitations:

## Stable Authority Boundary Phrases
- PASS is a validation signal, not authorization.
- Checker PASS is validation signal, not approval.
- Human approval remains above every PASS.
- INTEGRITY_WARNING is not clean PASS.
- Summary output is user guidance, not evidence authority.
- Fixture registry is navigation metadata, not policy, proof, or approval.
- all --strict may include integrity checks, but it must not turn validation PASS into human approval.

## Known Gaps To Preserve
- `all --strict` is non-zero in this repository due pre-existing baseline failures outside M41/M42.1 scope.
- `all --strict --json` is valid JSON but remains aggregate-style (not a dedicated integrity envelope).
- Some human-readable `all --strict` source details remain summarized.
- Runtime schema-enforcement of fixture registry remains a documented gap.

## Regression Blocking Rules
Treat as blocking regressions:
- missing `integrity` command
- invalid JSON from `integrity --fixtures --json`
- source tokens no longer preserved
- `INTEGRITY_WARNING` treated as clean PASS
- summary output implies approval
- fixture registry treated as policy authority
- `all --strict` drops integrity integration without documented gap
- unknown token gets invented meaning
- `--summary` and `--json` conflict no longer blocks
- `shell=True` appears in `scripts/agentos-validate.py`

## Deferred M42 Implementation Tasks
- M42.2: implement automated regression runner and fixture assertions from this baseline.
- M42.3: deepen JSON-field contract checks and non-order-sensitive `details` validation.
- M42.4+: extend authority-boundary static checks across docs/CLI outputs.
