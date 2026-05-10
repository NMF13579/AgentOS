# M36 External Usability Smoke Test

**Task ID:** task-m36-external-usability-smoke-test
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- M36 README, Installation, Onboarding, Troubleshooting, and First-User Pack hardening reports exist and show complete: PASS

## Smoke Test Method
The smoke test was performed by simulating a first external user journey. Documentation presence and content were verified via automated greps against safety/usability standards. Core installation, validation, and project smoke scripts were executed to confirm the operational green path.

## Documentation Presence Checks
- `README.md`: PASS
- `docs/first-user-guide.md`: PASS
- `docs/installation.md`: PASS
- `docs/quickstart.md`: PASS
- `docs/troubleshooting.md`: PASS
- `prompts/first-user-agent.md`: PASS

## Content Checks
- **Landing (README):** Definition, Non-Claims, and Result Semantics are present and clear.
- **Guide (docs/first-user-guide.md):** First safe path and Safety boundaries are explicitly documented.
- **Quickstart (docs/quickstart.md):** Verification steps and result interpretation are present.
- **Troubleshooting (docs/troubleshooting.md):** Result meanings and failure handling are hardened and in English.
- **Agent Prompt (prompts/first-user-agent.md):** Scope rules and validation honesty instructions are correctly framed for AI agents.

## Command Smoke Tests
- `python3 scripts/validate-task.py tasks/active-task.md`: 0 (PASS)
- `bash scripts/run-all.sh`: 0 (PASS)
- `python3 scripts/agentos-validate.py all`: 0 (PASS)
- `python3 scripts/audit-mvp-readiness.py`: 0 (PASS_WITH_WARNINGS)
- `bash scripts/test-install.sh`: 0 (PASS)
- `bash scripts/test-example-project.sh`: 0 (PASS)

## Smoke Matrix
| Area | Check / Command | Exit Code | Result | Classification | Evidence |
|---|---|---:|---|---|---|
| Repository Landing | Content Grep (README) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | All required strings found. |
| First-User Guide | Content Grep (Guide) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | Path and rules documented. |
| Installation Guidance | Content Grep (Install) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | prerequisites and templates explained. |
| Quickstart Guidance | Content Grep (Quickstart) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | First validation visible. |
| Troubleshooting Guidance | Content Grep (Troubleshoot) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | Result meanings explained. |
| First-User Agent Prompt | Content Grep (Prompt) | 0 | `PASS` | `M36_USABILITY_P0_PASS` | Honesty rules present. |
| Active Task Validation | `scripts/validate-task.py` | 0 | `PASS` | `M36_USABILITY_P0_PASS` | task validation passed. |
| Run-All Validation | `scripts/run-all.sh` | 0 | `PASS` | `M36_USABILITY_P0_PASS` | task & verification passed. |
| Unified AgentOS Validation | `scripts/agentos-validate.py all` | 0 | `PASS` | `M36_USABILITY_P0_PASS` | All checks green. |
| Install Smoke | `scripts/test-install.sh` | 0 | `PASS` | `M36_USABILITY_P0_PASS` | install smoke test passed. |
| Example Project Smoke | `scripts/test-example-project.sh` | 0 | `PASS` | `M36_USABILITY_P0_PASS` | example project validation passed. |
| MVP Readiness Audit | `scripts/audit-mvp-readiness.py` | 0 | `PASS_WITH_WARNINGS` | `M36_USABILITY_P1_WARNING` | future milestone checks skipped. |

## Required P0 Summary
- README clarity: PASS
- First-User Guide safe path: PASS
- Quickstart/Installation docs: PASS
- Troubleshooting result meanings: PASS
- Agent prompt honesty: PASS
- Command Green Path (Unified/Audit/Smoke): PASS

## Remaining Gaps
- **audit-mvp-readiness warnings** (`P1_FIRST_USER_WARNING`): Users see warnings for skipped future milestones. This is honest but may cause slight confusion for absolute beginners.
- **M33 inherited gaps** (`DEFER_TO_M37`): Context pipeline fail-closed details are deferred.

## Overall External Usability Smoke Classification
`M36_EXTERNAL_USABILITY_SMOKE_PASS_WITH_WARNINGS`

**Reason:** All primary P0 usability blockers are resolved. AgentOS is installable and verifiable. Warnings exist for future milestones but do not block external MVP trial.

## Non-Claims
- This smoke test does not repair failures.
- This smoke test does not update documentation.
- This smoke test does not approve release publication.
- This smoke test does not approve production deployment.
- This smoke test does not authorize web UI, cloud/server, hosted diagnostics, IDE plugin, vector DB, or M37 feature work.
- This smoke test does not replace M36 evidence report.
- This smoke test does not replace M36 completion review.

## Final Status
`M36_EXTERNAL_USABILITY_SMOKE_TEST_COMPLETE`
