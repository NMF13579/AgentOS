# M36 External MVP Usability Evidence Report

**Task ID:** task-m36-external-mvp-usability-evidence-report
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- M36 intake and all hardening reports exist: PASS
- M36 usability smoke test report exists and shows complete: PASS

## Evidence Sources Checked
- `reports/m35-completion-review.md`
- `reports/m36-external-mvp-usability-intake.md`
- `reports/m36-external-user-journey-inspection.md`
- `reports/m36-readme-first-user-entry-hardening.md`
- `reports/m36-installation-quickstart-inspection.md`
- `reports/m36-installation-quickstart-hardening.md`
- `reports/m36-first-project-onboarding-inspection.md`
- `reports/m36-first-project-onboarding-scenario.md`
- `reports/m36-troubleshooting-error-message-inspection.md`
- `reports/m36-troubleshooting-result-explanation-hardening.md`
- `reports/m36-first-user-prompt-guide-pack.md`
- `reports/m36-external-usability-smoke-test.md`

## M36 Purpose
The goal of M36 is to make AgentOS understandable, installable, and usable by a first external user without the author nearby, effectively proving "First User Readiness".

## Evidence Summary Table
| Area | Source Report / File | Evidence Classification | Key Result | Remaining Gap |
|---|---|---|---|---|
| M35 Readiness Input | `reports/m35-completion-review.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `M35_MVP_READY_WITH_GAPS` | Future milestone audit skips |
| M36 Intake | `reports/m36-external-mvp-usability-intake.md` | `EVIDENCE_PASS` | `M36_USABILITY_INTAKE_COMPLETE` | None |
| External User Journey | `reports/m36-external-user-journey-inspection.md` | `EVIDENCE_PASS` | `M36_EXTERNAL_USER_JOURNEY_INSPECTION_COMPLETE` | None |
| README / First-User Entry | `reports/m36-readme-first-user-entry-hardening.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `README_HARDENING_COMPLETE` | Documentation gaps (installation/RU) |
| Installation / Quickstart | `reports/m36-installation-quickstart-hardening.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `INSTALLATION_HARDENING_COMPLETE` | First task creation guidance |
| First Project Onboarding | `reports/m36-first-project-onboarding-scenario.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `ONBOARDING_SCENARIO_COMPLETE` | RU language in troubleshooting |
| Troubleshooting / Result Explanation | `reports/m36-troubleshooting-result-explanation-hardening.md` | `EVIDENCE_PASS` | `TROUBLESHOOTING_HARDENING_COMPLETE` | None |
| First-User Guide | `docs/first-user-guide.md` | `EVIDENCE_PASS` | File exists and follows rules. | None |
| First-User Agent Prompt | `prompts/first-user-agent.md` | `EVIDENCE_PASS` | File exists and follows rules. | None |
| External Usability Smoke Test | `reports/m36-external-usability-smoke-test.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `M36_EXTERNAL_USABILITY_SMOKE_PASS_WITH_WARNINGS` | Future milestones warnings |
| Remaining Gaps | `reports/m36-external-usability-smoke-test.md` | `EVIDENCE_PASS_WITH_WARNINGS` | `P1_FIRST_USER_WARNING` | See Gaps section |

## First-User Readiness Summary
- **Can a first external user understand what AgentOS is?** YES
- **Can a first external user understand what AgentOS is not?** YES
- **Can a first external user find installation / quickstart guidance?** YES
- **Can a first external user find the first-user guide?** YES
- **Can a first external user find the first-user agent prompt?** YES
- **Can a first external user run the first validation path?** YES
- **Can a first external user inspect an example or onboarding scenario?** YES
- **Can a first external user understand failed / blocked validation?** YES
- **Can a first external user know the next safe action?** YES

## External Usability Smoke Summary
`M36_EXTERNAL_USABILITY_SMOKE_PASS_WITH_WARNINGS`

## Remaining Gaps
- **Gap: `audit-mvp-readiness` warnings** (`P1_FIRST_USER_WARNING`): Users see warnings for skipped future milestones. This is honest but may cause slight confusion for absolute beginners.
- **Gap: M33 inherited gaps** (`DEFER_TO_M37`): Detailed context pipeline fail-closed documentation is deferred.
- **Gap: `failed-verification.md` scenario** (`P2_DOCS_POLISH`): The legacy scenario for verification failure is still technical/partially Russian.

## Completion Review Readiness
`READY_FOR_M36_COMPLETION_REVIEW_WITH_WARNINGS`

**Reason:** All required evidence exists, and the usability smoke test confirmed that the primary P0 blockers (installation docs, Russian troubleshooting language, README clarity) are resolved. The system is verifiable and usable by an external party, with non-blocking warnings remaining for future development stages.

## Non-Claims
- This evidence report does not repair failures.
- This evidence report does not update documentation.
- This evidence report does not approve release publication.
- This evidence report does not approve production deployment.
- This evidence report does not make AgentOS externally usable by itself.
- This evidence report does not authorize web UI, cloud/server, hosted diagnostics, IDE plugin, vector DB, or M37 feature work.
- This evidence report does not replace M36 completion review.
- This evidence report does not reinterpret failed smoke results as usability.

## Final Status
`M36_EXTERNAL_MVP_USABILITY_EVIDENCE_COMPLETE`
