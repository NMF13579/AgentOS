## Executive Summary
M42 regression layer is operational as validation infrastructure. Core commands run, JSON contracts validate, negative fixture self-test passes, and strict integration is present. Known failures remain explicit.

Regression evidence is validation evidence, not approval.

## M42 Chain Reviewed
- M42.1: `M42_1_REGRESSION_BASELINE_COMPLETE_WITH_GAPS`
- M42.2: `M42_2_REGRESSION_RUNNER_COMPLETE_WITH_GAPS`
- M42.3: `M42_3_NEGATIVE_REGRESSION_FIXTURES_COMPLETE_WITH_GAPS`
- M42.4: `M42_4_REGRESSION_CLI_INTEGRATION_COMPLETE_WITH_GAPS`

## Regression Baseline Evidence
- Baseline reports and command contract exist and are readable.
- Authority boundary baseline exists and is readable.

## Regression Runner Evidence
- `python3 scripts/test-integrity-regression.py --json`
- Observed exit: `1`
- Observed result: `INTEGRITY_REGRESSION_FAILED`
- Fail detail: `summary-json-conflict`
- Needs review detail: `warning-not-clean-pass`
- Classification: known previously recorded gap.

## Negative Fixture Self-Test Evidence
- `python3 scripts/test-integrity-regression.py --self-test-fixtures --json`
- Observed exit: `0`
- Observed result: `INTEGRITY_REGRESSION_OK`
- Summary: `passed=11 failed=0 needs_review_expected=2 blocked=0`

## Official CLI Wrapper Evidence
- `python3 scripts/agentos-validate.py integrity-regression --json`
- Observed exit: `1`
- Observed result: `INTEGRITY_REGRESSION_FAILED`
- Same failure profile as direct runner.

## Recursion-Safe Strict Path Evidence
- `python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check`
- Observed exit: `1`
- Observed result: `INTEGRITY_REGRESSION_FAILED`
- Skip flag is accepted and command remains functional.

## Authority Boundary Evidence
- M42.2 runner includes authority-boundary phrase checks.
- M42.3 negative fixtures include false-approval detection.
- M42.4 wrapper preserved non-approval boundary language.

## Validation Commands Run
Command | Expected Exit | Observed Exit | Output Artifact | Status | Notes
--- | --- | --- | --- | --- | ---
`python3 scripts/test-integrity-regression.py --json` | non-zero allowed | 1 | `/tmp/agentos-m42-5-runner.json` | `PASS_WITH_GAPS` | Known fail (`summary-json-conflict`) and known needs-review (`warning-not-clean-pass`)
`python3 scripts/test-integrity-regression.py --self-test-fixtures --json` | 0 | 0 | `/tmp/agentos-m42-5-self-test.json` | `PASS` | Fixture self-test clean
`python3 scripts/agentos-validate.py integrity-regression --json` | mirrors runner | 1 | `/tmp/agentos-m42-5-wrapper.json` | `PASS_WITH_GAPS` | Mirrors runner failures honestly
`python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check` | mirrors runner | 1 | `/tmp/agentos-m42-5-wrapper-skip.json` | `PASS_WITH_GAPS` | Recursion-safe mode available
`python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --json` | 0 | 0 | `/tmp/agentos-m42-5-wrapper-self-test.json` | `PASS` | Wrapper self-test works
`python3 scripts/agentos-validate.py all --strict` | non-zero allowed | 1 | `/tmp/agentos-m42-5-all-strict.txt` | `KNOWN_GAP` | Existing strict baseline failures remain
`python3 scripts/agentos-validate.py all --strict --json` | non-zero allowed | 1 | `/tmp/agentos-m42-5-all-strict.json` | `PASS_WITH_GAPS` | JSON output valid
`python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --fixture-root /tmp/agentos-missing-integrity-regression-fixtures --json` | non-zero safety behavior | 1 | stdout JSON | `PASS` | Expected blocked safety behavior

NOT_RUN is not PASS.

## Evidence Matrix
Layer | Artifact | Command | Expected Result | Observed Result | Status | Evidence Source
--- | --- | --- | --- | --- | --- | ---
M42.1 baseline map | `reports/m42-1-*.md` | read artifacts | baseline documented | present | `PASS` | M42.1 completion review
M42.2 regression runner | `scripts/test-integrity-regression.py` | `... --json` | executable runner | runs with known fail profile | `PASS_WITH_GAPS` | `/tmp/agentos-m42-5-runner.json`
M42.2 regression runner JSON | runner JSON contract | `python3 -m json.tool /tmp/agentos-m42-5-runner.json` | valid JSON | valid JSON | `PASS` | command output
M42.3 self-test fixtures | `tests/fixtures/integrity-regression/` | `... --self-test-fixtures --json` | self-test pass | `INTEGRITY_REGRESSION_OK` | `PASS` | `/tmp/agentos-m42-5-self-test.json`
M42.3 self-test JSON | self-test JSON contract | `python3 -m json.tool /tmp/agentos-m42-5-self-test.json` | valid JSON | valid JSON | `PASS` | command output
M42.4 official CLI wrapper | `integrity-regression` subcommand | `... integrity-regression --json` | wrapper executes runner | executes with known fail profile | `PASS_WITH_GAPS` | `/tmp/agentos-m42-5-wrapper.json`
M42.4 wrapper JSON | wrapper JSON contract | `python3 -m json.tool /tmp/agentos-m42-5-wrapper.json` | valid JSON | valid JSON | `PASS` | command output
M42.4 wrapper self-test fixtures | wrapper forwarding | `... integrity-regression --self-test-fixtures --json` | forward and execute | `INTEGRITY_REGRESSION_OK` | `PASS` | `/tmp/agentos-m42-5-wrapper-self-test.json`
M42.4 recursion-safe option | skip-all-strict flag | `... --json --skip-all-strict-check` | works without recursion loop | works, still reports known failures | `PASS_WITH_GAPS` | `/tmp/agentos-m42-5-wrapper-skip.json`
all --strict regression integration | strict aggregate | `python3 scripts/agentos-validate.py all --strict` | regression check included | included, overall fail | `KNOWN_GAP` | `/tmp/agentos-m42-5-all-strict.txt`
all --strict --json if supported | strict JSON aggregate | `... all --strict --json` | valid JSON | valid JSON, overall fail | `PASS_WITH_GAPS` | `/tmp/agentos-m42-5-all-strict.json`
authority boundary checks | text boundary controls | runner internal checks + fixtures | boundary preserved | no new boundary break | `PASS` | M42.2/M42.3 evidence
negative fixture coverage | M42.3 fixtures | self-test execution | required negatives covered | covered in self-test pass | `PASS` | `/tmp/agentos-m42-5-self-test.json`
known gap handling | known gap classification | review M42.1–M42.4 | explicit/non-misleading | explicit and consistent | `PASS` | M42.1–M42.4 reviews

## Result Summary
- Runner executes and emits valid JSON.
- Self-test executes and passes.
- Official wrapper executes and preserves behavior.
- Recursion-safe option is available.
- `all --strict` integration is present but overall strict result remains failed due known baseline gaps.
- No new hidden approval/authorization claims detected.
