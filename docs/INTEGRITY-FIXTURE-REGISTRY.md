# Integrity Fixture Registry

## Purpose
Define deterministic fixture discovery for `integrity --fixtures` execution.

Fixture registry is navigation metadata, not policy, proof, or approval.
Registry entries must preserve source tokens.
Registry-driven integrity checks must not call integrity recursively.
The registry may point to existing fixtures; it must not create missing fixtures.
Human approval remains above every PASS.

## Default Registry Path
`tests/fixtures/integrity-fixture-registry.json`

## Registry Format
Top-level fields:
- `registry_version`
- `description`
- `entries`

Each entry includes:
- `id`
- `suite`
- `command`
- `args`
- `input_path`
- `required`
- `strict_safe`
- `expected_source_tokens`

## Deterministic Discovery
- Registry order is preserved and used as execution order.
- `integrity --list-fixtures` reads entries without executing checks.
- `integrity --fixtures` executes entries in declared order.

## Fixture-safe Commands
Entry `command` must reference existing `agentos-validate.py` subcommands.
Disallowed in registry entries:
- `integrity`
- `all`

## Input Path Handling
If `input_path` is non-null, CLI must pass it as:
`--input <input_path>`
not as a positional argument.

## Recursion Prevention
Any registry entry that references `integrity` or `all` is blocked with recursion failure class.

## Source-token Preservation
Aggregated output keeps:
- source command
- source result token
- source failure class
- source output

## Limitation Boundary
- Registry cannot repair missing fixtures.
- Registry-driven mode does not create fixtures.
- Registry is orchestration metadata only.

## Non-approval Boundary
M41.3 does not create new validators.
M41.3 does not create new M40 fixtures.
M41.3 does not replace source-token semantics.
