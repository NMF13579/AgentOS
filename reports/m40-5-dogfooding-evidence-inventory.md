# M40.5 Dogfooding Evidence Inventory

## Purpose
This report inventories evidence from M40 dogfooding to distinguish between agent claims and runner-generated proof.

## Inspected Artifacts
* `reports/m40-final-report.md`
* `reports/m40-fixup-command-paths-report.md`
* `reports/m40-fixup-dotfiles-portability-report.md`
* `reports/m40-fixup-help-semantics-report.md`
* `reports/m40-installer-mvp-report.md`
* `reports/m40-single-role-execution-evidence-report.md`
* `reports/pre-m40-clean-full-template-assembly-report.md`
* `reports/pre-m40-install-agentos-script-report.md`
* `reports/pre-m40-use-template-readiness-report.md`
* `reports/ci/agentos-validate.json`
* `reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023.md`

## Claim vs Proof Classification

| Artifact | Classification | Notes |
|---|---|---|
| `reports/m40-final-report.md` | AGENT_CLAIM | High-level summary without direct runner output or hashes. |
| `reports/m40-fixup-command-paths-report.md` | AGENT_CLAIM | Describes fixes and claims PASS without verifiable trace. |
| `reports/m40-fixup-dotfiles-portability-report.md` | AGENT_CLAIM | Claims VERIFIED but lacks runner output. |
| `reports/m40-fixup-help-semantics-report.md` | AGENT_CLAIM | Claims VERIFIED but lacks runner output. |
| `reports/m40-installer-mvp-report.md` | AGENT_CLAIM | Summarizes installer testing without linking to logs. |
| `reports/m40-single-role-execution-evidence-report.md` | AGENT_CLAIM | Mentions successful fixture tests but doesn't include raw output. |
| `reports/pre-m40-clean-full-template-assembly-report.md` | AGENT_CLAIM | Process description without runner-verified artifacts. |
| `reports/pre-m40-install-agentos-script-report.md` | AGENT_CLAIM | Detailed table of PASS results but all are agent-written. |
| `reports/pre-m40-use-template-readiness-report.md` | AGENT_CLAIM | Checklist-based claims without runner proof. |
| `reports/ci/agentos-validate.json` | VALIDATION_OUTPUT | Machine-generated JSON with command outputs and exit codes. |
| `reports/execution/exec-task-20260426-brief-readiness-check-20260429-075023.md` | RUNNER_PROOF | Machine-generated session report with readiness output. |

## Evidence Summary
* **M40 artifacts found:** 9+ reports, 1 CI artifact, 1 execution record.
* **M40 validation commands found or referenced:** `python3 scripts/agentos-validate.py`, `python3 scripts/test-single-role-execution-fixtures.py`, `python3 -m py_compile`.
* **M40 validation outputs found or missing:** Mostly found inside `reports/ci/agentos-validate.json` (partial) and `reports/execution/`. Missing raw logs for specific M40 fixup tasks.
* **Commits referenced:** None in reports.
* **Push performed:** Manual (per README/GEMINI.md rules).
* **Missing evidence:** Raw terminal traces for M40 installer smoke tests; full log for `test-single-role-execution-fixtures.py`.
* **Ambiguous evidence:** "PASS with gaps" in `m40-final-report.md` without gap details.
* **Legacy limitations:** Pre-Honest-PASS reports rely almost entirely on `AGENT_CLAIM` (Markdown tables written by the agent).
