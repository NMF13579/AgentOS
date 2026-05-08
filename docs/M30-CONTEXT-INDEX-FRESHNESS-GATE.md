# M30 Context Index Freshness Gate

## Purpose
- This document defines Task 30.2.
- Context Index Freshness Gate checks whether `data/context-index.json` is fresh enough for M28/M30 navigation.
- Context Index Freshness Gate is not approval.
- Context Index Freshness Gate does not authorize protected actions.
- Context Index Freshness Gate does not replace Human Gate.
- Context Index Freshness Gate does not replace M27 runtime enforcement.
- Context Index Freshness Gate does not weaken M28 context control.
- Context Index Freshness Gate does not weaken M29 bypass resistance boundaries.
- Human Gate remains approval authority.

## CLI
- `python3 scripts/check-context-index-freshness.py`
- `python3 scripts/check-context-index-freshness.py --json`
- `python3 scripts/check-context-index-freshness.py --root <repo-root>`
- `python3 scripts/check-context-index-freshness.py --index data/context-index.json`
- `python3 scripts/check-context-index-freshness.py --mode hash-check`
- `python3 scripts/check-context-index-freshness.py --mode compare-after-rebuild`
- `python3 scripts/check-context-index-freshness.py --mode auto`

Rules:
- checker is read-only
- checker must not modify data/context-index.json
- checker must not auto-commit generated files
- checker must not update SQLite

## Result Values
- `CONTEXT_INDEX_FRESH`
- `CONTEXT_INDEX_FRESH_WITH_WARNINGS`
- `CONTEXT_INDEX_STALE`
- `CONTEXT_INDEX_MISSING`
- `CONTEXT_INDEX_INVALID`
- `CONTEXT_INDEX_INCOMPLETE`
- `CONTEXT_INDEX_NEEDS_REVIEW`
- `CONTEXT_INDEX_BLOCKED`

## Exit Semantics
- `CONTEXT_INDEX_FRESH => exit 0`
- all other results => `exit 1`
- Required gates must require both explicit `CONTEXT_INDEX_FRESH` and exit 0.
- exit 0 without `CONTEXT_INDEX_FRESH` in stdout or JSON is not success.

## Freshness Modes
- hash-check and compare-after-rebuild are different freshness modes.
- `hash-check` validates committed `source_hash` vs current source files.
- `compare-after-rebuild` compares regenerated deterministic output with committed JSON.
- `auto` prefers deterministic rebuild and tracks fallback/skip/disagreement.
- If both modes are available and disagree, result must be `CONTEXT_INDEX_NEEDS_REVIEW`.
- A freshness gate cannot be considered enforceable unless the index can be regenerated or deterministically checked.

## hash-check
Checks:
- index exists
- JSON parseable
- entries iterable
- repository-relative source paths
- no absolute paths
- source files exist
- hash format is `sha256:<hex>`
- source hash matches source file bytes
- generated metadata does not claim semantic authority

## compare-after-rebuild
Checks:
- generator exists and runs
- rebuild into temp output (no overwrite of committed file)
- deterministic output check by running generator twice
- compare normalized generated JSON vs committed JSON
- Diff after rebuild means stale index.
- Nondeterminism definition: two consecutive runs on same files produce different output.

## auto
- uses compare-after-rebuild if generator exists
- fallback to hash-check allowed only when generator is absent or rebuild capability unavailable
- Generator failure must not silently fall back to hash-check.
- If the context index generator script is missing, the gate must fail with INCOMPLETE, not skip silently.

## Generator Handling
- expected generator: `scripts/build-context-index.py`
- if missing in compare-after-rebuild: `CONTEXT_INDEX_INCOMPLETE`
- if exists but fails unexpectedly: `CONTEXT_INDEX_NEEDS_REVIEW` or `CONTEXT_INDEX_INCOMPLETE`
- missing generator must not be treated as success

## Context Index Structure Checks
Required expectations:
- top-level JSON object
- metadata fields present for generated index
- entries list exists
- each entry has source path
- each path is repository-relative and safe
- `source_hash` uses `sha256:<hex>` when present
- entry must not claim approval
- entry must not claim semantic authority

## Path Safety Checks
Reject:
- POSIX absolute paths
- Windows absolute paths
- `../` escape
- path escape through symlink/root traversal
- home paths `~/...`

Unsafe path result: `CONTEXT_INDEX_INVALID`.

## Source-of-Truth Boundary Checks
Forbidden claims in generated JSON:
- semantic source of truth claim
- generated JSON overrides Markdown/YAML
- generated JSON approval claim
- SQLite is source of truth claim

Blocked result: `CONTEXT_INDEX_BLOCKED`.

Mandatory formulas:
- Markdown/YAML = meaning
- JSON = navigation
- SQLite = speed

## SQLite Boundary
- SQLite is optional cache
- SQLite is not source of truth
- SQLite freshness must not override Markdown/YAML or data/context-index.json freshness
- SQLite freshness must not override committed context-index freshness checks
- SQLite being newer than JSON does not make SQLite authoritative
- SQLite stale or fresh state must never replace the committed context-index freshness check

## Output Behavior
Human-readable output includes:
- result value
- mode
- index path
- checked entry count
- warnings
- errors
- findings summary

## JSON Output
`--json` prints valid JSON with fields:
- `result`
- `mode`
- `index_path`
- `checked_entries`
- `warnings`
- `errors`
- `findings`

Finding severity mapping rules:
- severity: blocking must correspond to result `CONTEXT_INDEX_BLOCKED` or `CONTEXT_INDEX_INVALID`.
- severity: needs_review must correspond to result `CONTEXT_INDEX_NEEDS_REVIEW` or stricter non-ready result.
- severity: error must not correspond to `CONTEXT_INDEX_FRESH`.
- Finding severity must not imply success when result is non-ready.

## Fixture Scenarios
Root: `tests/fixtures/context-index-freshness/`.
Each fixture includes:
- `fixture-notes.md`
- `expected-result.txt`

## No-Write Behavior
Checker must not:
- modify committed context index
- create reports
- create or update SQLite cache
- run git add/commit/push

## Non-Authorization Boundary
- Context Index Freshness Gate is not approval.
- Context Index Freshness Gate does not authorize commit, push, merge, release, deployment, or protected changes.
- Context Index Freshness Gate does not authorize bypassing AgentOS guardrails.
- Context Index Freshness Gate does not replace Human Gate.
- Context Index Freshness Gate does not weaken, disable, or reduce any guardrail.
- Context Index Freshness Gate must not weaken M27 runtime enforcement.
- Context Index Freshness Gate must not weaken M28 context control.
- Context Index Freshness Gate must not weaken M29 bypass resistance boundaries.
- Human Gate remains approval authority.

## Limitations
- Deterministic static checker, not semantic AI evaluator.
- compare-after-rebuild relies on generator behavior.
- Ambiguous cases produce `CONTEXT_INDEX_NEEDS_REVIEW`.
- `CONTEXT_INDEX_FRESH_WITH_WARNINGS applies only to non-critical conditions`.
- `READY_WITH_WARNINGS is exit 1 by design`.
- `CI must not infer context compliance from test results alone`.
- `exit 0 without CONTEXT_INDEX_FRESH` is not success.
- `context index generator script is missing` must not be silently skipped.

- || true may be used only for evidence collection
- Required gates must require both explicit CONTEXT_INDEX_FRESH and exit 0.
