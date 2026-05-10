# M36 Troubleshooting and Error Message Inspection

**Task ID:** task-m36-troubleshooting-inspection
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-readme-first-user-entry-hardening.md` exists: PASS
- `reports/m36-installation-quickstart-hardening.md` exists: PASS
- `reports/m36-first-project-onboarding-scenario.md` exists: PASS (Renamed from `m36-first-project-onboarding-report.md`)

## Inspection Method
The inspection was performed from the perspective of an English-speaking external user encountering a failure. I evaluated the readability of troubleshooting docs, the clarity of result tokens in scripts, and the availability of error scenarios.

## First External User Assumption
A user who encounters a `FAIL` or `BLOCKED` result during their first 10 minutes and needs to know exactly which report to read and what the next safe action is, without needing a translator or maintainer.

## Result Meaning Findings
- **PASS/FAIL/WARN:** Clearly visible in script outputs (e.g., `agentos-validate.py`).
- **BLOCKED/NOT_READY:** These terms exist in the codebase but are not consistently explained in the primary documentation for an external user.
- **Language Barrier:** `docs/troubleshooting.md` and `docs/limitations.md` are almost entirely in Russian. This is a critical blocker for the "understandable without the author nearby" goal.

## Command-to-Report Mapping Findings
- **validate-task.py:** Output is terminal-only. No persistent report.
- **run-all.sh:** Aggregates task and verification validation. Next safe action is unclear if verification fails.
- **agentos-validate.py:** Provides a summary, but the link between a failure (e.g., scope violation) and the specific report (e.g., `reports/changed-files.txt`) is not prominent.
- **audit-mvp-readiness.py:** Results are clear, but instructions on how to resolve "skipped future milestones" are missing.

## Surface Check Summary
| Surface | Status | Classification |
|---|---|---|
| README troubleshooting section | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` (Hardened in 36.2.1) |
| `docs/troubleshooting.md` | `AVAILABLE_CONFUSING` | `P0_TROUBLESHOOTING_BLOCKER` (Russian only) |
| `docs/quickstart.md` results | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` (Hardened in 36.3.1) |
| `docs/installation.md` failure | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` (Created in 36.3.1) |
| `docs/mvp-checklist.md` | `AVAILABLE_CONFUSING` | `P2_DOCS_POLISH` (Russian only) |
| `docs/limitations.md` | `AVAILABLE_CONFUSING` | `P0_TROUBLESHOOTING_BLOCKER` (Russian only) |
| `examples/scenarios/failed-verification.md` | `AVAILABLE_PARTIAL` | `P1_RESULT_CONFUSION` (Highly technical/technical jargon) |
| `agentos-validate.py` tokens | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |
| `audit-mvp-readiness.py` tokens | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |

## Troubleshooting Gap Table
| Area | Current Surface | Current State | Finding | Classification | Suggested Fix Area |
|---|---|---|---|---|---|
| Troubleshooting | `docs/troubleshooting.md` | `AVAILABLE_CONFUSING` | Content is in Russian. Critical recovery paths are unreadable. | `P0_TROUBLESHOOTING_BLOCKER` | `DOCS_TROUBLESHOOTING` |
| Boundaries | `docs/limitations.md` | `AVAILABLE_CONFUSING` | Content is in Russian. Product non-claims are unreadable. | `P0_TROUBLESHOOTING_BLOCKER` | `DOCS_LIMITATIONS` |
| Status Matrix | `docs/mvp-checklist.md` | `AVAILABLE_CONFUSING` | Content is in Russian. | `P2_DOCS_POLISH` | `DOCS_MVP_CHECKLIST` |
| Scenarios | `examples/scenarios/` | `AVAILABLE_PARTIAL` | Scenarios like `failed-verification.md` use RU headings or technical jargon. | `P1_RESULT_CONFUSION` | `EXAMPLE_FAILED_VALIDATION` |

## Blocker Classification Summary
- **P0 Blockers:** Critical troubleshooting and boundary documentation (`troubleshooting.md`, `limitations.md`) is in Russian. This prevents external users from safely self-diagnosing or understanding the project's limits.
- **P1 Confusions:** Scenario files are inconsistent and use technical internal terms.

## Files Allowed for 36.5.1
- `docs/troubleshooting.md`
- `docs/limitations.md`
- `docs/mvp-checklist.md`
- `examples/scenarios/failed-verification.md`
- `examples/scenarios/failed-validation.md` (CREATE_ALLOWED)

## Deferred Findings
- **36.6.1 — First-User Prompt and Guide Pack:** Guidance on how AI tools should handle specific AgentOS error messages.
- **36.7.1 — External Usability Smoke Test:** Verification that translated documents actually help a user fix a real blocker.

## Non-Claims
- This inspection does not update troubleshooting docs.
- This inspection does not update error messages.
- This inspection does not modify scripts.
- This inspection does not run install smoke.
- This inspection does not run example smoke.
- This inspection does not make AgentOS externally usable by itself.
- This inspection does not approve release publication.
- This inspection does not authorize UI dashboard, hosted diagnostics, IDE plugin, cloud/server, or M37 feature work.
- This inspection does not replace M36 completion review.

## Final Status
`M36_TROUBLESHOOTING_INSPECTION_COMPLETE`
