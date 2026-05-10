# M36 README / First-User Entry Hardening

**Task ID:** task-m36-readme-first-user-entry-hardening
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-external-user-journey-inspection.md` exists and is complete: PASS
- `README.md` exists: PASS
- Inspection did not block hardening (`NO_EXACT_HARDENING_PATH_IDENTIFIED` not found): PASS

## Files Modified
- `README.md`

## Findings From 36.2.0 Addressed
- **P1_FIRST_RUN_CONFUSION (Landing Page):** The original README was dense with technical terms. It has been simplified to directly explain what AgentOS is and who it is for.
- **P2_DOCS_POLISH (Product Definition):** Re-worded to "programmable guardrail layer" to set clear expectations.
- **P1_FIRST_RUN_CONFUSION (First Validation):** Added a "First Safe Commands" block with direct, copy-pasteable execution paths.
- **P1_FIRST_RUN_CONFUSION (Failure Interpretation):** Added an "Understanding Validation Results" section explaining PASS, WARN, BLOCKED, etc., and how to safely respond to a failure.
- **P1_FIRST_RUN_CONFUSION (Example Project):** Added a clear section pointing to `examples/simple-project/` and how to run its smoke test.

## Hardening Applied
- Replaced the technical introduction with a first-user-focused definition.
- Added a "Who is AgentOS for?" section.
- Added a "What AgentOS is not" section, explicitly excluding web UIs, cloud platforms, vector DBs, and autonomous orchestration.
- Added a "First Safe Commands" code block showing `validate-task.py`, `run-all.sh`, `agentos-validate.py all`, and `audit-mvp-readiness.py`.
- Added an "Understanding Validation Results" section.
- Linked directly to the example project and getting started guides.

## First-User Path Added or Improved
- **Definition:** "AgentOS is a programmable guardrail layer for AI-assisted coding workflows."
- **First Commands:** The README now presents a clear 4-step command sequence to verify the repository state immediately upon cloning.

## Result Explanation Added or Improved
- The README now explicitly defines `PASS`, `PASS_WITH_WARNINGS`, `BLOCKED`, `NOT_READY`, and `INCONCLUSIVE`.
- It provides a 6-step checklist for what to do if validation fails (e.g., "Do not treat failure as success", "fix only the scoped blocker").

## Remaining Gaps
- **P0_EXTERNAL_USER_BLOCKER:** Missing `docs/installation.md`.
- **P0_EXTERNAL_USER_BLOCKER:** Russian language barriers in `docs/limitations.md` and `docs/troubleshooting.md`.
- **P1_FIRST_RUN_CONFUSION:** Quickstart assumptions about cloned repositories.

## Deferred Findings
- All remaining gaps are deferred to subsequent M36 inspection and hardening tasks (36.3.0, 36.4.0, 36.5.0) as they involve files outside the allowed scope of this specific task.

## Non-Claims
- This hardening does not make AgentOS externally usable by itself.
- This hardening does not run install smoke.
- This hardening does not run example smoke.
- This hardening does not approve release publication.
- This hardening does not authorize web UI, cloud/server, vector DB, or M37 feature work.
- This hardening does not replace M36 completion review.

## Final Status
`M36_README_FIRST_USER_ENTRY_HARDENING_COMPLETE_WITH_GAPS`
