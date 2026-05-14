# M40.5 Dogfooding Gap Classification

## Overview
Classification of gaps identified in M40 dogfooding evidence, specifically focusing on the transition to Honest PASS.

## Gap Classification

| Gap ID | Evidence Source | Severity | Category | Affected Layer | Recommended Action | Owner Milestone | Blocks M40.6 | Blocks Strict Mode |
|---|---|---|---|---|---|---|---|---|
| GAP-001 | `m40-final-report.md` | P0 | agent-written-claim | reporting | Enforce machine-readable evidence binding in final reports. | M40.8 | YES | YES |
| GAP-002 | `m40-single-role-execution-evidence-report.md` | P1 | weak-proof | validation | Redirect test output to persistent evidence artifacts. | M40.7 | NO | YES |
| GAP-003 | `pre-m40-install-agentos-script-report.md` | P1 | checklist-gaming | reporting | Require runner trace for each checklist PASS item. | M40.10 | NO | YES |
| GAP-004 | `m40-final-report.md` | P1 | fake-pass | validation | "PASS with gaps" must block overall PASS until gaps are P3. | M40.6 | NO | YES |
| GAP-005 | `reports/ci/` | P2 | missing-evidence-binding | ci | Bind CI JSON results to human approval records. | M40.12 | NO | NO |
| GAP-006 | `reports/execution/` | P2 | validation-gap | runner | Add verification step hashes to execution sessions. | M40.8 | NO | NO |
| GAP-007 | `scripts/` | P1 | future-bypass-hardening | security | Implement static bypass resistance checker for scripts. | M40.10 | NO | YES |
| GAP-008 | `docs/quickstart.md` | P2 | first-user-friction | documentation | Clarify `cp -an` behavior and state directory requirements. | M40.13 | NO | NO |
| GAP-009 | `scripts/agentos-validate.py` | P1 | validation-gap | validation | Fix idle-state bypass to return PASS when no active task exists. | M40.6 | YES | YES |

## Severity Summary
* **P0:** 1 (Reporting authority gap)
* **P1:** 5 (Proof/Bypass/Validation rigor/Idle-bypass)
* **P2:** 3 (Usability/Clarity)
* **P3:** 0

## Blocking Status
* **Blocks M40.6:** YES (GAP-001, GAP-009 require immediate attention to enable clean CI).
* **Blocks Strict Mode:** YES (Multiple P0/P1 gaps regarding evidence rigor).
