# Fix Idle-State CI Handling — Verification Report

**Task ID:** task-m40-fix-idle-ci
**Date:** 2026-05-13
**Status:** COMPLETED

## Summary

Fixed idle-state CI failures by adding `is_idle_task_file()` early-return guards
to all three CI-blocking scripts. Scripts now return PASS/OK/VALID immediately when
`active-task.md` contains no active task.

## Changes Made

### scripts/check-context-pipeline.py
- Added `is_idle_task_file(path: Path) -> bool` helper function
- Added idle-state shortcut in `main()` **before** gate subprocess calls
- Returns `CONTEXT_PIPELINE_OK` with exit code 0 when idle

### scripts/check-required-context-pack.py
- Added `is_idle_task_file(path: Path) -> bool` helper function
- Added idle-state shortcut at entry of `main()` after `args = ap.parse_args()`
- Returns `CONTEXT_PACK_VALID` with exit code 0 when idle

### scripts/check-required-context-compliance.py
- Added `is_idle_task_file(path)` helper function
- Added idle-state shortcut at entry of `main()` after `a = ap.parse_args()`
- Returns `CONTEXT_COMPLIANCE_PASS` with exit code 0 when idle

### scripts/check-scope-compliance.py
- Already contained correct `is_idle_state()` implementation and wiring
- No changes needed

### tasks/active-task.md
- Added `status: none` YAML front-matter to explicitly mark idle state

### tests/fixtures/scope-compliance/idle-*/
- `idle-no-active-task/` — "No active task" text → expect PASS
- `idle-status-none/` — `status: none` frontmatter → expect PASS
- `idle-status-idle/` — `status: idle` frontmatter → expect PASS
- `idle-empty-file/` — no scope_control, no Contract → expect PASS

## Idle-State Detection Logic

A file is considered idle if ANY of these conditions hold:
1. Contains "no active task" (case-insensitive)
2. YAML front-matter contains `status: none` or `status: idle`
3. Does NOT contain `scope_control:` AND does NOT contain `## Contract` or `contract:`

## Safety Guarantees

- Files with `scope_control:` violations: FAIL behavior **unchanged**
- Files with real contracts and `state !=` idle: existing behavior **preserved**
- All pre-existing fixture tests: **not modified**
- `.github/workflows/` files: **NOT touched**
- `scripts/agentos-validate.py` orchestrator: **NOT modified**
- `tasks/done/`: **NOT touched**

## Acceptance Criteria Status

- [x] `check-scope-compliance.py` returns PASS + exit 0 for idle state
- [x] `check-context-pipeline.py --strict --json` returns CONTEXT_PIPELINE_OK + exit 0 for idle state
- [x] `agentos-validate.py all` returns PASS for idle state (all sub-checks pass)
- [x] All checks still FAIL/BLOCK for real contract violations
- [x] Idle-state fixtures added to test-scope-compliance-fixtures.py discovery path
- [x] No workflow .yml files modified
