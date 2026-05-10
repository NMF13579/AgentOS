# M37 Task ID Sync Hardening Report

**Task ID:** task-m37-1-0-task-id-sync-hardening
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Goal
Implement three levels of task ID sync hardening to prevent CI failures related to mismatched `task_id` and `task.id` fields in `tasks/active-task.md` and `reports/verification.md`.

## Files Created
- `scripts/sync-task-ids.py`
- `reports/m37-task-id-sync-hardening-report.md`

## Files Modified
- `tasks/templates/task-contract.md`
- `.github/workflows/agentos-validate.yml`
- `tasks/active-task.md` (contract activation)

## Actions Taken
- **Level 1 (Templates):** Updated `tasks/templates/task-contract.md` to use the `{{TASK_ID}}` placeholder for `task.id`, encouraging immediate synchronization when a new task is generated.
- **Level 2 (Script):** Created `scripts/sync-task-ids.py` which extracts the top-level `task_id` from `tasks/active-task.md` and enforces it on the `task.id` property inside the YAML block, as well as the `verification.task_id` property in `reports/verification.md`.
- **Level 3 (CI):** Modified `.github/workflows/agentos-validate.yml` to execute `python scripts/sync-task-ids.py` automatically before running `agentos-validate.py all`, ensuring the CI environment will automatically sync IDs and avoid false-positive failures.

## Validation Commands Run
1. `python3 scripts/validate-task.py tasks/active-task.md`
2. `python3 scripts/agentos-validate.py all`

## Validation Results
All validation checks passed with a `WARN` due to the expected modification of sensitive paths (`.github/workflows/agentos-validate.yml` and `scripts/sync-task-ids.py`). No blocking violations were detected.

## Final Status
`M37_TASK_ID_SYNC_HARDENING_COMPLETE`
