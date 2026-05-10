# M36 Installation / Quickstart Hardening

**Task ID:** task-m36-installation-quickstart-hardening
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-installation-quickstart-inspection.md` exists and is complete: PASS
- Inspection did not block hardening: PASS

## Files Modified
- `docs/installation.md` (Created)
- `docs/quickstart.md` (Modified)
- `README.md` (Modified)

## Findings From 36.3.0 Addressed
- **P0_INSTALL_BLOCKER:** Missing dedicated installation guide. Created `docs/installation.md` to explain how to clone and copy AgentOS into an existing project.
- **P0_QUICKSTART_BLOCKER:** `docs/quickstart.md` assumed installation was done and lacked context. Updated it to focus on post-installation validation, explaining PASS/FAIL semantics and providing next steps.
- **P1_FIRST_RUN_CONFUSION:** README setup section was vague. Added a direct link to `docs/installation.md` under "Where to read more".

## Installation Guidance Added or Improved
- **Prerequisites:** Clearly listed (Git, Bash, Python 3.10+, pip) in `docs/installation.md`.
- **Template Selection Guidance:** Explained the difference between the minimal (learning/small projects) and full (complete guardrails) templates, advising users to start with minimal if unsure.
- **Install/Copy Method:** Provided exact bash commands to clone the repo, navigate to the target project, and run `install.sh` (including a dry-run step).

## Quickstart Guidance Added or Improved
- **First Validation Command:** Clear, copyable blocks for validating both minimal (`validate-task.py`, `run-all.sh`) and full (`agentos-validate.py`, `audit-mvp-readiness.py`) installations.
- **Result Explanation Added or Improved:** Explicitly defined PASS, PASS_WITH_WARNINGS, WARNING, BLOCKED, NOT_READY, and INCONCLUSIVE in both `installation.md` and `quickstart.md`.
- **Failure Guidance Added or Improved:** Added a 6-step checklist on what to do if validation fails (read output, check reports, fix scoped blocker, rerun).
- **Success Guidance:** Added clear next steps (open active-task, define a small goal, test example project).
- **Explicit Non-Goals:** Re-iterated that AgentOS does not provide web UIs, cloud hosting, vector DBs, or autonomous execution.

## Remaining Gaps
- **P0_EXTERNAL_USER_BLOCKER:** Russian language barriers in `docs/limitations.md` and `docs/troubleshooting.md`.
- **P1_FIRST_RUN_CONFUSION:** User needs an explicit scenario for creating their first actual task.

## Deferred Findings
- **36.4.0 — First Project Onboarding Scenario Inspection:** Address the gap in first-task creation guidance.
- **36.5.0 — Troubleshooting and Error Message Inspection:** Translate and harden the troubleshooting documentation.

## Non-Claims
- This hardening does not make AgentOS externally usable by itself.
- This hardening does not run install smoke.
- This hardening does not run example smoke.
- This hardening does not approve release publication.
- This hardening does not authorize pip/npm packaging, web UI, cloud/server, vector DB, or M37 feature work.
- This hardening does not replace M36 completion review.

## Final Status
`M36_INSTALLATION_QUICKSTART_HARDENING_COMPLETE_WITH_GAPS`
