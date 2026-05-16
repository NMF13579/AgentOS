## Executive Summary
M43.2 does not move, delete, archive, or rewrite reports.
Historical evidence is not runtime authority.
Archive candidate does not authorize deletion.
Reports needed to explain past completion decisions must remain discoverable.
Do not invent references.

## Archive Planning Scope
Read-only planning scope: `reports/m40-*`, `reports/m41-*`, `reports/m42-*`, `reports/m43-1-*`, plus reference checks in `docs/`, `scripts/`, `README.md`, `tasks/active-task.md`.

## Report Count Summary
Total reports reviewed: 71
M40 reports reviewed: 28
M41 reports reviewed: 16
M42 reports reviewed: 23
M43.1 reports reviewed: 4
Active closure references: 5
Historical evidence: 1
Archive candidates: 54
Summary candidates: 21
Unknown needs review: 5

## Enumeration Method
```bash
find reports -maxdepth 1 -type f \( -name 'm40-*' -o -name 'm41-*' -o -name 'm42-*' -o -name 'm43-1-*' \) | sort
```

## M40 Reports
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m40-10-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md;reports/m40-11-validator-authority-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-10-runtime-bypass-smoke-report.md | m40 | HISTORICAL_EVIDENCE | milestone evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | ARCHIVE_LATER | historical chain evidence |
| reports/m40-11-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-12-evidence-immutability-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-11-validator-authority-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-12-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-13-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-12-evidence-immutability-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-13-blocked-precondition-report.md | m40 | RETAIN_CURRENT_LOCATION | blocked-state trace | none_found | no | DO_NOT_TOUCH | keep discoverable for boundary audit |
| reports/m40-13-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-13-full-honest-pass-closure-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-5-dogfooding-evidence-inventory.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-dogfooding-gap-classification.md | m40 | ACTIVE_GAP_SOURCE | known gaps/deferred source | none_found | no | KEEP_LINKED | gap source for forward milestones |
| reports/m40-5-first-user-friction-map.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-honest-pass-readiness.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-6-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md;reports/m40-7-honest-pass-checkers-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-6-honest-pass-architecture-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-7-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-8-runner-proof-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-7-honest-pass-checkers-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-8-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-9-strict-mode-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-8-runner-proof-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-9-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-9-strict-mode-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-final-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md;reports/m40-5-first-user-friction-map.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-command-paths-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-dotfiles-portability-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-help-semantics-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-installer-mvp-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-first-user-friction-map.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-single-role-execution-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md | yes | KEEP_LINKED | referenced by closure or validation context |

## M41 Reports
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m41-1-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-2-unified-integrity-cli-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-1-post-m40-artifact-inventory.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-result-token-alignment-map.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-unified-integrity-command-plan.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-user-facing-gap-map.md | m41 | ACTIVE_GAP_SOURCE | known gaps/deferred source | none_found | no | KEEP_LINKED | gap source for forward milestones |
| reports/m41-2-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-3-integrity-fixture-registry-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-2-unified-integrity-cli-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-3-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-4-integrity-result-ux-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-3-integrity-fixture-registry-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-4-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-5-all-strict-integrity-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-4-integrity-result-ux-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-5-all-strict-integrity-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-5-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-6-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-6-blocked-precondition-report.md | m41 | RETAIN_CURRENT_LOCATION | blocked-state trace | none_found | no | DO_NOT_TOUCH | keep discoverable for boundary audit |
| reports/m41-6-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-6-unified-integrity-closure-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | yes | KEEP_LINKED | referenced by closure or validation context |

## M42 Reports
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m42-1-authority-boundary-regression-map.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-command-contract-map.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-2-integrity-regression-runner-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-1-regression-fixture-plan.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-unified-integrity-regression-baseline.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-2-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-3-integrity-regression-fixtures-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-2-integrity-regression-runner-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-3-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-4-integrity-regression-cli-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-3-integrity-regression-fixtures-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-4-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-5-blocked-precondition-report.md;reports/m42-5-known-gaps-and-regressions.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-4-integrity-regression-cli-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-5-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-5-blocked-precondition-report.md | m42 | RETAIN_CURRENT_LOCATION | blocked-state trace | none_found | no | DO_NOT_TOUCH | keep discoverable for boundary audit |
| reports/m42-5-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-5-integrity-regression-evidence-consolidation.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-6-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-5-known-gaps-and-regressions.md | m42 | ACTIVE_GAP_SOURCE | known gaps/deferred source | reports/m42-6-blocked-precondition-report.md;reports/m42-6-final-gaps-and-deferred-items.md | no | KEEP_LINKED | gap source for forward milestones |
| reports/m42-5-regression-gate-readiness-review.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-6-blocked-precondition-report.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-6-blocked-precondition-report.md | m42 | RETAIN_CURRENT_LOCATION | blocked-state trace | none_found | no | DO_NOT_TOUCH | keep discoverable for boundary audit |
| reports/m42-6-completion-review.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-final-capability-matrix.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-final-gaps-and-deferred-items.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-honest-pass-integrity-final-closure-report.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-hk1-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | none_found | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-hk1-housekeeping-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |

## M43.1 Reports
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m43-1-completion-review.md | m43 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | none_found | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m43-1-footprint-consolidation-plan.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m43-1-honest-pass-artifact-inventory.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m43-1-risk-and-retention-map.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |

## Active Closure References
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m42-6-completion-review.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-final-capability-matrix.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-final-gaps-and-deferred-items.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m42-6-honest-pass-integrity-final-closure-report.md | m42 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | no | KEEP_ACTIVE | used by current closure/precondition flow |
| reports/m43-1-completion-review.md | m43 | ACTIVE_CLOSURE_REFERENCE | closure/precondition reference | none_found | no | KEEP_ACTIVE | used by current closure/precondition flow |

## Historical Evidence
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m40-10-runtime-bypass-smoke-report.md | m40 | HISTORICAL_EVIDENCE | milestone evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | ARCHIVE_LATER | historical chain evidence |

## Archive Candidates
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m40-10-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md;reports/m40-11-validator-authority-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-10-runtime-bypass-smoke-report.md | m40 | HISTORICAL_EVIDENCE | milestone evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | ARCHIVE_LATER | historical chain evidence |
| reports/m40-11-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-12-evidence-immutability-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-11-validator-authority-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-12-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-13-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-12-evidence-immutability-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-13-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-13-full-honest-pass-closure-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-5-dogfooding-evidence-inventory.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-first-user-friction-map.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-5-honest-pass-readiness.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-6-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md;reports/m40-7-honest-pass-checkers-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-6-honest-pass-architecture-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-7-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-8-runner-proof-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-7-honest-pass-checkers-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-8-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-9-strict-mode-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-8-runner-proof-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-9-completion-review.md | m40 | FINAL_SUMMARY | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m40-9-strict-mode-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m40-single-role-execution-evidence-report.md | m40 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-2-unified-integrity-cli-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-1-post-m40-artifact-inventory.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-result-token-alignment-map.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-1-unified-integrity-command-plan.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-2-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-3-integrity-fixture-registry-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-2-unified-integrity-cli-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-3-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-4-integrity-result-ux-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-3-integrity-fixture-registry-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-4-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-5-all-strict-integrity-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-4-integrity-result-ux-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-5-all-strict-integrity-evidence-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m41-5-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m41-6-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-6-completion-review.md | m41 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m41-6-unified-integrity-closure-report.md | m41 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-authority-boundary-regression-map.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-command-contract-map.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-2-integrity-regression-runner-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-1-regression-fixture-plan.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-1-unified-integrity-regression-baseline.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-2-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-3-integrity-regression-fixtures-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-2-integrity-regression-runner-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-3-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-4-integrity-regression-cli-evidence-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-3-integrity-regression-fixtures-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-4-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-5-blocked-precondition-report.md;reports/m42-5-known-gaps-and-regressions.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-4-integrity-regression-cli-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-5-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-5-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | reports/m42-6-blocked-precondition-report.md | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-5-integrity-regression-evidence-consolidation.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-6-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-5-regression-gate-readiness-review.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m42-6-blocked-precondition-report.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m42-hk1-completion-review.md | m42 | FINAL_SUMMARY | milestone completion decision | none_found | yes | SUMMARIZE_LATER | can be summarized if closure links preserved |
| reports/m42-hk1-housekeeping-evidence-report.md | m42 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | none_found | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m43-1-footprint-consolidation-plan.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m43-1-honest-pass-artifact-inventory.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |
| reports/m43-1-risk-and-retention-map.md | m43 | ACTIVE_VALIDATION_EVIDENCE | validation and decision evidence | reports/m43-1-completion-review.md | yes | KEEP_LINKED | referenced by closure or validation context |

## Unknown / Needs Review
Report Path | Milestone | Classification | Current Role | Referenced By | Archive Candidate | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | --- | ---
| reports/m40-final-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md;reports/m40-5-first-user-friction-map.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-command-paths-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-dotfiles-portability-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-fixup-help-semantics-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | unknown | REVIEW_LATER | active dependency not verified safely |
| reports/m40-installer-mvp-report.md | m40 | UNKNOWN_NEEDS_REVIEW | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-first-user-friction-map.md | unknown | REVIEW_LATER | active dependency not verified safely |

