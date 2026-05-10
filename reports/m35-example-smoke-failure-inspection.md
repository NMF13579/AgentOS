# M35 Example Project Smoke Failure Inspection

**Task ID:** task-m35-example-smoke-failure-inspection
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m35-fixup-intake.md` exists and is complete.
- `reports/m35-active-task-run-all-repair.md` exists and is complete.
- `scripts/test-example-project.sh` exists.
- `scripts/validate-verification.py` exists.

## Command Run
`bash scripts/test-example-project.sh`

## Root Cause Summary
| Command | Exit Code | Result | Root Cause Classification | Evidence |
|---|---|---|---|---|
| `test-example-project.sh` | 1 | FAIL | EXAMPLE_VERIFICATION_YAML_INVALID | `mapping values are not allowed here` at line 6, column 10 (`proof: "TODO"`) in the generated `reports/verification.md`. |

## Example Smoke Findings
- **Status:** FAIL
- **Point of Failure:** The smoke test fails during `bash scripts/run-all.sh` within the temporary example project.
- **Step:** `bash scripts/validate-verification.py reports/verification.md` fails.

## YAML / Verification Findings
- **Root Cause File:** `templates/agentos-minimal/reports/verification.md`
- **Error Detail:** The `status:` and `proof:` fields are incorrectly indented relative to the gate keys (e.g., `gate_1:`).
- **Malformed Segment:**
  ```yaml
    gate_1:
      name: "Structure / Schema"
  status: TODO
      proof: "TODO"
  ```
  (The `status:` line is at the same indentation level as `gate_1:`, which is invalid inside the `verification:` object according to the schema and YAML rules).

## Failure Classification
`EXAMPLE_VERIFICATION_YAML_INVALID`

## Files Allowed for 35.3.1
- `templates/agentos-minimal/reports/verification.md`
- `templates/agentos-full/reports/verification.md`
- `reports/verification.md`

## Deferred Findings
- No new deferred findings. All previously deferred findings from 35.2.0 remain deferred to their respective tasks.

## Non-Claims
- This inspection does not repair example-project smoke.
- This inspection does not modify example files.
- This inspection does not modify templates.
- This inspection does not modify validators.
- This inspection does not make AgentOS MVP-ready.
- This inspection does not approve a release.
- This inspection does not authorize M36.
- This inspection does not replace M35 completion review.

## Final Status
`M35_EXAMPLE_SMOKE_INSPECTION_COMPLETE`
