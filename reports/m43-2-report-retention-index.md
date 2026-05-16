## Purpose
Set planned retention decisions for historical reports without performing archive actions.
Retention index is a planning artifact, not an archive action.
Human review is required before archiving or deleting historical evidence.

## Retention Categories
- `KEEP_ACTIVE`
- `KEEP_LINKED`
- `ARCHIVE_LATER`
- `SUMMARIZE_LATER`
- `REVIEW_LATER`
- `DO_NOT_TOUCH`

## Keep Active
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m42-6-completion-review.md | KEEP_ACTIVE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_ACTIVE | no |
| reports/m42-6-final-capability-matrix.md | KEEP_ACTIVE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_ACTIVE | no |
| reports/m42-6-final-gaps-and-deferred-items.md | KEEP_ACTIVE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_ACTIVE | no |
| reports/m42-6-honest-pass-integrity-final-closure-report.md | KEEP_ACTIVE | closure/precondition reference | reports/m43-1-completion-review.md;reports/m43-1-footprint-consolidation-plan.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_ACTIVE | no |
| reports/m43-1-completion-review.md | KEEP_ACTIVE | closure/precondition reference | UNKNOWN_NEEDS_REVIEW | KEEP_ACTIVE | no |

## Keep Linked
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m40-11-validator-authority-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m40-12-evidence-immutability-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m40-13-full-honest-pass-closure-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m40-5-dogfooding-evidence-inventory.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-5-dogfooding-gap-classification.md | KEEP_LINKED | known gaps/deferred source | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-5-first-user-friction-map.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-5-honest-pass-readiness.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-6-honest-pass-architecture-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-7-honest-pass-checkers-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-8-runner-proof-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m40-9-strict-mode-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m40-single-role-execution-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md | KEEP_LINKED | no |
| reports/m41-1-post-m40-artifact-inventory.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-1-result-token-alignment-map.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-1-unified-integrity-command-plan.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-1-user-facing-gap-map.md | KEEP_LINKED | known gaps/deferred source | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-2-unified-integrity-cli-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-3-integrity-fixture-registry-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m41-4-integrity-result-ux-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m41-5-all-strict-integrity-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m41-6-unified-integrity-closure-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | KEEP_LINKED | no |
| reports/m42-1-authority-boundary-regression-map.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md;scripts/__pycache__/test-integrity-regression.cpython-314.pyc;scripts/test-integrity-regression.py | KEEP_LINKED | no |
| reports/m42-1-command-contract-map.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m42-1-regression-fixture-plan.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m42-1-unified-integrity-regression-baseline.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m42-2-integrity-regression-runner-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m42-3-integrity-regression-fixtures-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m42-4-integrity-regression-cli-evidence-report.md | KEEP_LINKED | validation and decision evidence | reports/m42-5-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m42-5-integrity-regression-evidence-consolidation.md | KEEP_LINKED | validation and decision evidence | reports/m42-6-blocked-precondition-report.md;reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | no |
| reports/m42-5-known-gaps-and-regressions.md | KEEP_LINKED | known gaps/deferred source | reports/m42-6-blocked-precondition-report.md;reports/m42-6-final-gaps-and-deferred-items.md | KEEP_LINKED | no |
| reports/m42-5-regression-gate-readiness-review.md | KEEP_LINKED | validation and decision evidence | reports/m42-6-blocked-precondition-report.md | KEEP_LINKED | no |
| reports/m42-hk1-housekeeping-evidence-report.md | KEEP_LINKED | validation and decision evidence | UNKNOWN_NEEDS_REVIEW | KEEP_LINKED | no |
| reports/m43-1-footprint-consolidation-plan.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-completion-review.md | KEEP_LINKED | no |
| reports/m43-1-honest-pass-artifact-inventory.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-completion-review.md | KEEP_LINKED | no |
| reports/m43-1-risk-and-retention-map.md | KEEP_LINKED | validation and decision evidence | reports/m43-1-completion-review.md | KEEP_LINKED | no |

## Archive Later
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m40-10-runtime-bypass-smoke-report.md | ARCHIVE_LATER | milestone evidence | reports/m43-1-honest-pass-artifact-inventory.md | ARCHIVE_LATER | yes |

## Summarize Later
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m40-10-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md;reports/m40-11-validator-authority-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m40-11-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-12-evidence-immutability-report.md | SUMMARIZE_LATER | yes |
| reports/m40-12-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-13-blocked-precondition-report.md | SUMMARIZE_LATER | yes |
| reports/m40-13-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | SUMMARIZE_LATER | yes |
| reports/m40-5-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m40-6-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-6-honest-pass-architecture-evidence-report.md;reports/m40-7-honest-pass-checkers-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m40-7-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-8-runner-proof-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m40-8-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-9-strict-mode-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m40-9-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m40-10-runtime-bypass-smoke-report.md | SUMMARIZE_LATER | yes |
| reports/m41-1-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m41-2-unified-integrity-cli-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m41-2-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m41-3-integrity-fixture-registry-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m41-3-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m41-4-integrity-result-ux-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m41-4-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m41-5-all-strict-integrity-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m41-5-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m41-6-blocked-precondition-report.md | SUMMARIZE_LATER | yes |
| reports/m41-6-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-6-completion-review.md;reports/m42-6-honest-pass-integrity-final-closure-report.md;reports/m43-1-honest-pass-artifact-inventory.md | SUMMARIZE_LATER | yes |
| reports/m42-1-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-2-integrity-regression-runner-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | SUMMARIZE_LATER | yes |
| reports/m42-2-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-3-integrity-regression-fixtures-evidence-report.md;reports/m42-5-known-gaps-and-regressions.md;reports/m42-6-final-gaps-and-deferred-items.md | SUMMARIZE_LATER | yes |
| reports/m42-3-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-4-integrity-regression-cli-evidence-report.md | SUMMARIZE_LATER | yes |
| reports/m42-4-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-5-blocked-precondition-report.md;reports/m42-5-known-gaps-and-regressions.md | SUMMARIZE_LATER | yes |
| reports/m42-5-completion-review.md | SUMMARIZE_LATER | milestone completion decision | reports/m42-6-blocked-precondition-report.md | SUMMARIZE_LATER | yes |
| reports/m42-hk1-completion-review.md | SUMMARIZE_LATER | milestone completion decision | UNKNOWN_NEEDS_REVIEW | SUMMARIZE_LATER | yes |

## Review Later
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m40-final-report.md | REVIEW_LATER | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-dogfooding-gap-classification.md;reports/m40-5-first-user-friction-map.md | REVIEW_LATER | yes |
| reports/m40-fixup-command-paths-report.md | REVIEW_LATER | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | REVIEW_LATER | yes |
| reports/m40-fixup-dotfiles-portability-report.md | REVIEW_LATER | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | REVIEW_LATER | yes |
| reports/m40-fixup-help-semantics-report.md | REVIEW_LATER | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md | REVIEW_LATER | yes |
| reports/m40-installer-mvp-report.md | REVIEW_LATER | legacy or side-track report | reports/m40-5-dogfooding-evidence-inventory.md;reports/m40-5-first-user-friction-map.md | REVIEW_LATER | yes |

## Do Not Touch
Report Path | Retention Category | Reason | Source Evidence | Next Action | Human Review Required
--- | --- | --- | --- | --- | ---
| reports/m40-13-blocked-precondition-report.md | DO_NOT_TOUCH | blocked-state trace | UNKNOWN_NEEDS_REVIEW | DO_NOT_TOUCH | yes |
| reports/m41-6-blocked-precondition-report.md | DO_NOT_TOUCH | blocked-state trace | UNKNOWN_NEEDS_REVIEW | DO_NOT_TOUCH | yes |
| reports/m42-5-blocked-precondition-report.md | DO_NOT_TOUCH | blocked-state trace | UNKNOWN_NEEDS_REVIEW | DO_NOT_TOUCH | yes |
| reports/m42-6-blocked-precondition-report.md | DO_NOT_TOUCH | blocked-state trace | UNKNOWN_NEEDS_REVIEW | DO_NOT_TOUCH | yes |

## Retention Decision Rules
- Final closure reports should usually be `KEEP_ACTIVE` or `KEEP_LINKED`.
- Gap/deferred reports remain discoverable as `KEEP_LINKED` when still referenced.
- Evidence reports may be `ARCHIVE_LATER` only when closure context is preserved by summary/index links.
- Reports with unresolved P0/P1 references require human review before archive actions.
- Reports used by current preconditions remain `KEEP_ACTIVE`/`DO_NOT_TOUCH`.
