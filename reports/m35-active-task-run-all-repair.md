# M35 Active Task / run-all Repair

**Task ID:** task-m35-active-task-run-all-repair
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m35-validation-failure-inspection.md` exists and is complete.
- `tasks/active-task.md` exists.
- `scripts/run-all.sh` exists.
- Inspection did not block repair.

## Files Modified
- `schemas/task.schema.json`

## Root Cause From 35.2.0
- `ACTIVE_TASK_SCHEMA_MISMATCH`: The JSON schema `schemas/task.schema.json` did not support the new minimal M35 active-task frontmatter fields and had `additionalProperties: false`.

## Repair Applied
- Updated `schemas/task.schema.json` to include the new M35 fields (`task_number`, `task_name`, `milestone`, `mode`, `repository`, `branch`) in the top-level `properties`.
- Added a new branch to `anyOf` in the schema to explicitly allow and require this minimal M35 contract.

## Validation Commands Run
1. `python3 scripts/validate-task.py tasks/active-task.md`
2. `bash scripts/run-all.sh`
3. `python3 scripts/agentos-validate.py all`

## Validation Results
| Command | Result | Notes |
|---|---|---|
| `validate-task` | PASS | The M35 active-task frontmatter now conforms to the updated schema. |
| `run-all` | PASS | All checks within `run-all.sh` (task and verification validation) passed. |
| `agentos-validate` | FAIL | Expected; deferred to Task 35.4.0. |

## Remaining Failures
- `agentos-validate.py all` still fails due to unrelated downstream checks (likely scope or execution audit issues).

## Deferred Findings
- **Example Project Smoke:** Fails due to YAML parsing error in `reports/verification.md`. (Deferred to 35.3.0).
- **Unified Validation:** Unrelated failures in `agentos-validate.py`. (Deferred to 35.4.0).

## Non-Claims
- This repair does not make AgentOS MVP-ready.
- This repair does not repair example-project smoke.
- This repair does not repair all unified validation failures unless they share the same root cause.
- This repair does not approve a release.
- This repair does not authorize M36.
- This repair does not replace M35 completion review.

## Final Status
`M35_RUN_ALL_REPAIR_COMPLETE`

**Result:** `RUN_ALL_PASS`
