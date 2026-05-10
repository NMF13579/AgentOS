# M35 Unified Validation Green Path Repair

**Task ID:** task-m35-unified-validation-repair
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m35-unified-validation-inspection.md` exists and is complete.
- `scripts/agentos-validate.py` exists.
- Inspection did not block repair.

## Files Modified
- `tasks/active-task.md`
- `scripts/audit-mvp-readiness.py` (New File)

## Root Cause From 35.4.0
- `UNIFIED_VALIDATION_P0_FAILURE`: `agentos-validate all` failed because the `scope` check required a `scope_control` block in `tasks/active-task.md`, which was missing in the minimal M35 contract.
- `MISSING_MVP_AUDIT_ENTRYPOINT`: Absence of a standalone `scripts/audit-mvp-readiness.py` script.

## M35-Scoped Failures Repaired
1. **Added `scope_control` block:** Restored the mandatory scope block to `tasks/active-task.md` with correct formatting for the internal parser.
2. **Created `audit-mvp-readiness.py`:** Added a standalone wrapper script for the MVP readiness audit.

## Deferred Findings Preserved
- M33 inherited gaps (context pipeline fail-closed state, incomplete negative fixture coverage) remain visible in the project history but do not block the unified validation green path.

## Repair Applied
- Modified `tasks/active-task.md` to include a fully defined `scope_control` block.
- Created `scripts/audit-mvp-readiness.py` as a Python wrapper for `audit-agentos.py`.
- Reverted unexpected changes to `data/context-index.json` and related `reports/` files that were causing accidental scope violations.

## Validation Commands Run
1. `python3 scripts/agentos-validate.py all --json`
2. `bash scripts/run-all.sh`
3. `bash scripts/test-example-project.sh`
4. `python3 scripts/validate-task.py tasks/active-task.md`

## Validation Results
| Command | Result | Notes |
|---|---|---|
| `agentos-validate` | PASS_WITH_WARNINGS | `result: WARN` due to sensitive path change (`schemas/task.schema.json`). No FAIL blockers remain. |
| `run-all` | PASS | No regressions. |
| `test-example-project` | PASS | No regressions. |
| `validate-task` | PASS | Frontmatter and new body blocks are valid. |

## Remaining Failures
- None (P0 blockers resolved). One non-blocking `WARN` in scope compliance.

## Non-Claims
- This repair does not make AgentOS MVP-ready by itself.
- This repair does not approve a release.
- This repair does not hide deferred M33 gaps.
- This repair does not authorize M36.
- This repair does not replace M35 full revalidation.
- This repair does not replace M35 completion review.

## Final Status
`M35_UNIFIED_VALIDATION_REPAIR_COMPLETE_WITH_WARNINGS`

**Result:** `UNIFIED_VALIDATION_PASS_WITH_WARNINGS`
