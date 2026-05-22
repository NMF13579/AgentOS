## Purpose
Plan safe CLI/entrypoint simplification without changing scripts.

## Current CLI Surface
- Multiple direct script commands exist (`agentos-validate.py`, `check-*`, `test-*`, `audit-*`, shell wrappers).
- Entrypoint surface is broad and can confuse first-time operators.

## Desired User-Facing Command Surface
- `python3 scripts/agentos-validate.py all --strict` (supported in M41/M42 reports).
- `python3 scripts/agentos-validate.py integrity --fixtures --json` (supported in M41 reports).
- `python3 scripts/agentos-validate.py integrity-regression --json` (supported in M42 reports).

## Safe Wrapper Candidates
- selected `audit-*` scripts that already aggregate checks.
- selected `test-*` scripts that mirror unified CLI subcommands.
A wrapper must preserve source tokens, exit semantics, and diagnostic detail.

## Scripts That Must Remain Standalone
- `scripts/check-validator-authority-boundary.py`
- `scripts/check-role-separation.py`
- `scripts/check-evidence-immutability.py`
- `scripts/test-integrity-regression.py`
Not every checker should be hidden behind a unified CLI.

## Scripts That May Be Unified Later
- helper-level wrappers where source output can be preserved exactly.

## all --strict Relationship
- `all --strict` stays aggregate; it must not hide source checker outcomes.

## integrity / integrity-regression Relationship
- `integrity` = fixture/validator integrity layer.
- `integrity-regression` = regression drift and known-gap guard.

## Backward Compatibility Requirements
Future script simplification must preserve documented existing commands unless a migration path is approved.
Do not remove standalone scripts merely because a unified CLI exists.

## Human Review Gates
- Gate 1: exit code parity check.
- Gate 2: JSON/text output parity check.
- Gate 3: source-token parity check.
- Gate 4: security-sensitive script review before wrapping.

## Proposed M43.6 Action
Execute post-consolidation validation review with command-compatibility checks.
