# M35 Full Revalidation Matrix

**Task ID:** task-m35-revalidation-matrix
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m35-fixup-intake.md` exists.
- `reports/m35-active-task-run-all-repair.md` exists.
- `reports/m35-example-smoke-repair.md` exists.
- `reports/m35-unified-validation-repair.md` exists.
- `reports/m35-mvp-audit-entrypoint-report.md` exists.
- `reports/m34-completion-review.md` exists and confirms `M34_MVP_NOT_READY`.

## Commands Run
1. `python3 scripts/validate-task.py tasks/active-task.md`
2. `python3 scripts/validate-verification.py reports/verification.md`
3. `bash scripts/run-all.sh`
4. `python3 scripts/agentos-validate.py all`
5. `bash scripts/test-install.sh`
6. `bash scripts/test-example-project.sh`
7. `python3 scripts/check-template-integrity.py`
8. `python3 scripts/audit-mvp-readiness.py`

## Revalidation Matrix
| Area | Command | Exit Code | Result | Classification | Evidence |
|---|---|---:|---|---|---|
| Active Task Validation | `python3 scripts/validate-task.py tasks/active-task.md` | 0 | `PASS` | `M35_P0_PASS` | "PASS: task validation passed" |
| Verification Report Validation | `python3 scripts/validate-verification.py reports/verification.md` | 0 | `PASS` | `M35_P0_PASS` | "PASS: verification validation passed" |
| Run-All Validation | `bash scripts/run-all.sh` | 0 | `PASS` | `M35_P0_PASS` | "PASS: task validation passed", "PASS: verification validation passed" |
| Unified AgentOS Validation | `python3 scripts/agentos-validate.py all` | 1 | `FAIL` | `M35_P0_FAIL` | "Reason: scope violations detected: new file outside allowed_new_files: reports/m35-mvp-audit-entrypoint-report.md" |
| Install Smoke | `bash scripts/test-install.sh` | 0 | `PASS` | `M35_P0_PASS` | "PASS: install smoke test passed" |
| Example Project Smoke | `bash scripts/test-example-project.sh` | 0 | `PASS` | `M35_P0_PASS` | "PASS: example project validation passed" |
| Template Integrity | `python3 scripts/check-template-integrity.py` | 0 | `PASS` | `M35_P0_PASS` | "TEMPLATE_INTEGRITY_RESULT: PASS" |
| MVP Readiness Audit | `python3 scripts/audit-mvp-readiness.py` | 0 | `PASS_WITH_WARNINGS` | `M35_P1_WARNING` | "Result: PASS_WITH_WARNINGS" (future milestones skipped) |

## Required P0 Summary
- `validate-task`: PASS
- `run-all`: PASS
- `agentos-validate`: **FAIL**
- `test-example-project`: PASS
- `audit-mvp-readiness`: PASS (with warnings)

## Regression Check
- `NO_RUN_ALL_REGRESSION`
- `NO_EXAMPLE_SMOKE_REGRESSION`
- `UNIFIED_VALIDATION_REGRESSION_DETECTED` (Regressed from `WARN` in 35.4.1 to `FAIL` due to new report files not being added to `active-task.md` scope).
- `NO_MVP_AUDIT_ENTRYPOINT_REGRESSION`

## Remaining Gaps
| Gap | Classification | Notes |
|---|---|---|
| `active-task.md` scope violation | `P0_BLOCKS_MVP` | `agentos-validate` fails because `reports/m35-mvp-audit-entrypoint-report.md` and `reports/m35-revalidation-matrix.md` are not in `allowed_new_files`. |
| `audit-mvp-readiness` warnings | `P1_RELEASE_WARNING` | Future milestone checks are skipped. |
| M33 inherited gaps | `DEFER_TO_M36` | Context pipeline fail-closed state. |

## Overall Revalidation Classification
`M35_REVALIDATION_FAIL`

**Reason:** `agentos-validate.py all` fails due to scope violations caused by newly created M35 reports. While the original M34 structural blockers are repaired, the unified validation suite cannot return a green state without an `active-task.md` scope update.

## Non-Claims
- This revalidation matrix does not repair failures.
- This revalidation matrix does not approve a release.
- This revalidation matrix does not make AgentOS MVP-ready by itself.
- This revalidation matrix does not authorize M36.
- This revalidation matrix does not replace M35 evidence report.
- This revalidation matrix does not replace M35 completion review.

## Final Status
`M35_REVALIDATION_MATRIX_FAILED`
