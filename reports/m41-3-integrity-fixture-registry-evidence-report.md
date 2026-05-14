# M41.3 Integrity Fixture Registry Evidence Report

## M41.2 status inspected
- Source: `reports/m41-2-completion-review.md`
- Status found: `M41_2_UNIFIED_INTEGRITY_CLI_COMPLETE_WITH_GAPS`

## Summary
M41.3 replaces hardcoded fixture paths with deterministic registry-driven fixture discovery.
M41.3 does not create new validators.
M41.3 does not create new M40 fixtures.
Fixture registry is navigation metadata, not policy, proof, or approval.
Schema validity is structural evidence, not proof of trust or approval.
Registry entries must preserve source tokens.
INTEGRITY_WARNING is not clean PASS.

## Artifacts created
- `docs/INTEGRITY-FIXTURE-REGISTRY.md`
- `schemas/integrity-fixture-registry.schema.json`
- `tests/fixtures/integrity-fixture-registry.json`

## CLI changes made
- Modified: `scripts/agentos-validate.py`
- Added registry-based behavior for `integrity`:
  - `--list-fixtures`
  - `--registry <path>`
  - default registry path: `tests/fixtures/integrity-fixture-registry.json`
- `integrity --fixtures` now executes entries from registry order, not hardcoded individual fixture paths.

## registry entries summary
- `honest-pass-fixtures`
- `runtime-bypass-smoke`
- `validator-authority-positive`
- `role-separation-positive`
- `evidence-immutability-positive`
- `evidence-amendments-positive`

## input_path to --input behavior
- For registry entries with `input_path`, CLI constructs wrapped command with `--input <input_path>`.
- `input_path` is not passed as raw positional argument.

## source token preservation summary
- Each subcheck output keeps source token under `source_result`.
- Wrapped payload is preserved under `source_output`.
- Unified result is navigation metadata on top of source token.

## recursion prevention behavior
- Registry entries with command `integrity` or `all` are blocked.
- Failure class: `INTEGRITY_REGISTRY_RECURSION_FORBIDDEN`.

## unknown command behavior
- Unknown entry command is blocked.
- Failure class: `INTEGRITY_REGISTRY_COMMAND_UNKNOWN`.

## missing fixture behavior
- Missing entry `input_path` is blocked.
- Failure class: `INTEGRITY_REGISTRY_INPUT_MISSING`.
- Missing fixtures are not created.

## Commands run
- `python3 scripts/agentos-validate.py integrity --help` (exit 0)
- `python3 scripts/agentos-validate.py honest-pass --help` (exit 0)
- `python3 scripts/agentos-validate.py integrity --list-fixtures --json` (exit 0, `INTEGRITY_OK`)
- `python3 scripts/agentos-validate.py integrity --fixtures --json` (exit 0, `INTEGRITY_WARNING`)
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --json` (exit 0, `INTEGRITY_WARNING`)
- `python3 scripts/agentos-validate.py integrity --fixtures --registry tests/fixtures/integrity-fixture-registry.json --json` (exit 0, `INTEGRITY_WARNING`)
- `python3 scripts/agentos-validate.py all --strict` (exit 1)
- `python3 -m json.tool schemas/integrity-fixture-registry.schema.json >/dev/null` (exit 0)
- `python3 -m json.tool tests/fixtures/integrity-fixture-registry.json >/dev/null` (exit 0)
- Dependency path checks for 4 required fixture directories (pass)

## Result snapshots
- `integrity --list-fixtures --json`: `INTEGRITY_OK`
- `integrity --fixtures --json`: `INTEGRITY_WARNING`
- `integrity --strict --fixtures --json`: `INTEGRITY_WARNING`
- explicit `--registry`: `INTEGRITY_WARNING`

## all --strict result or integration gap
- `all --strict` executes and includes strict integrity stage.
- Overall result is non-zero (`FAIL`) due baseline checks outside M41.3 scope.

## validation gaps
- No M41.3-specific execution gap.
- Existing repository baseline failures still affect `all --strict` global result.

## known limitations
- Registry is local metadata, not proof authority.
- Source tokens remain mixed-family by design; unified token is a navigation layer.

## recommended M41.4 action
- Add deterministic registry validation against schema at runtime.
- Add clearer per-subcheck next-safe-action messages.
