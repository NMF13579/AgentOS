# M41.4 Integrity Result UX Evidence Report

## M41.3 status inspected
- Source: `reports/m41-3-completion-review.md`
- Status found: `M41_3_FIXTURE_REGISTRY_COMPLETE_WITH_GAPS`

## Summary
M41.4 creates a user-facing integrity result UX layer.
M41.4 does not create new validators.
M41.4 does not create new security policy.
M41.4 does not change source-token semantics.
UX explains results. UX must not change authority.
Summary output is user guidance, not evidence authority.
Summary mode formats parsed JSON results; it must not parse human-readable subcommand output.
Schema validity is structural evidence, not proof of trust or approval.
Human approval remains above every PASS.
INTEGRITY_WARNING is not clean PASS.

## dependency precondition results
- `python3 scripts/agentos-validate.py integrity --help` -> exit 0
- `python3 scripts/agentos-validate.py integrity --list-fixtures --json` -> exit 0
- `python3 scripts/agentos-validate.py integrity --fixtures --json` -> exit 0

## artifacts created
- `docs/INTEGRITY-RESULT-UX.md`
- `templates/integrity-result-summary.md`
- `schemas/integrity-result-summary.schema.json`

## CLI changes made
- Added `--summary` output mode for integrity runs.
- Added `--explain-results` and `--explain-result <TOKEN>`.
- Added summary/json conflict block: `Use either --summary or --json, not both.`
- Added `allow_abbrev=False` to prevent ambiguous short flags.

## result explanation map summary
Implemented and exposed plain-language meanings and next-safe-actions for:
- `INTEGRITY_OK`
- `INTEGRITY_WARNING`
- `INTEGRITY_VIOLATION`
- `INTEGRITY_NEEDS_REVIEW`
- `INTEGRITY_BLOCKED`

## summary mode behavior
- `integrity --fixtures --summary` prints final result, clean pass, strict mode flag, source token preservation, counts, next safe action, approval boundary, limitations.
- `integrity --strict --fixtures --summary` does the same and includes: `INTEGRITY_WARNING is not clean PASS.`

## summary internal JSON execution behavior
Summary mode formats the parsed object returned by the same integrity execution path used by JSON mode (`run_integrity`).
It does not parse human-readable subcommand output.

## argparse abbreviation safety
- Parser uses `allow_abbrev=False`.
- Similar flags `--explain-results` and `--explain-result` cannot be abbreviated.

## argparse abbreviation runtime check
- `python3 scripts/agentos-validate.py integrity --explain-r INTEGRITY_WARNING` -> exit 2 (unrecognized arguments), expected safe failure.

## UX command results
- `python3 scripts/agentos-validate.py integrity --explain-results` -> exit 0
- `python3 scripts/agentos-validate.py integrity --explain-result INTEGRITY_WARNING` -> exit 0
- `python3 scripts/agentos-validate.py integrity --explain-result UNKNOWN_TOKEN` -> exit 1 and prints `Unknown integrity result token.`
- `python3 scripts/agentos-validate.py integrity --fixtures --summary` -> exit 0, result `INTEGRITY_WARNING`
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --summary` -> exit 0, result `INTEGRITY_WARNING`
- `python3 scripts/agentos-validate.py integrity --fixtures --summary --json` -> exit 1 and blocked conflict message

## commands run
- `test -f ...` checks for M41.4 files
- `python3 -m json.tool schemas/integrity-result-summary.schema.json >/dev/null`
- Dependency checks from task
- UX CLI checks from task
- Required grep and negative grep checks from task
- `python3 scripts/agentos-validate.py all --strict`

## validation gaps
- `all --strict` remains exit 1 due known baseline failures outside M41.4 scope.

## known limitations
- UX layer explains and summarizes; it does not add authority.
- Warning remains non-blocking by design in M41.4.

## recommended M41.5 action
- Add structured `next_safe_action` field optionally into JSON payload on demand.
- Add consistent per-subcheck limitation summaries in aggregate output.
