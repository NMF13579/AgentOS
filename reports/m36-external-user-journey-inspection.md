# M36 External User Journey Inspection

**Task ID:** task-m36-external-user-journey-inspection
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-external-mvp-usability-intake.md` exists and is complete: PASS
- `README.md` exists: PASS

## Inspection Method
The inspection was performed from the perspective of a first external user with no prior AgentOS knowledge. Every link, command, and explanation was evaluated for clarity, accessibility (language), and navigability.

## First External User Assumption
A technical user who wants to add guardrails to their AI-assisted project. They understand basic Git, Python, and Markdown, but they have never seen AgentOS internal "canonical modules" or "gate contracts".

## Journey Step Findings
| Journey Step | Current Surface | Current State | Finding | Classification | Suggested Fix Area |
|---|---|---|---|---|---|
| 1. Landing Page | `README.md` | `AVAILABLE_PARTIAL` | Dense with technical terms (canonical modules) early on. | `P1_FIRST_RUN_CONFUSION` | `README_FIRST_USER_ENTRY` |
| 2. Product Definition | `README.md` | `AVAILABLE_CLEAR` | Well-defined as a "Markdown-first guardrail framework". | `P2_DOCS_POLISH` | `README_FIRST_USER_ENTRY` |
| 3. Limitations | `docs/limitations.md` | `AVAILABLE_CONFUSING` | Document is primarily in Russian. Unreadable for most external users. | `P0_EXTERNAL_USER_BLOCKER` | `DOCS_LIMITATIONS` |
| 4. Installation | `install.sh` / `docs/quickstart.md` | `NOT_AVAILABLE` | No dedicated `docs/installation.md`. Quickstart assumes repo is already cloned. | `P0_EXTERNAL_USER_BLOCKER` | `DOCS_INSTALLATION` |
| 5. First Validation | `scripts/agentos-validate.py` | `AVAILABLE_PARTIAL` | Command is listed, but dependency requirements are thin. | `P1_FIRST_RUN_CONFUSION` | `DOCS_QUICKSTART` |
| 6. Example Project | `examples/simple-project/` | `AVAILABLE_PARTIAL` | Exists, but not prominently linked from root README. | `P1_FIRST_RUN_CONFUSION` | `EXAMPLES_ENTRYPOINT` |
| 7. MVP Audit | `scripts/audit-mvp-readiness.py` | `AVAILABLE_PARTIAL` | Script exists but isn't mentioned in the primary onboarding flow. | `P2_DOCS_POLISH` | `DOCS_QUICKSTART` |
| 8. Failure Interpretation | `docs/troubleshooting.md` | `AVAILABLE_CONFUSING` | Document is primarily in Russian. Blocks autonomous diagnosis. | `P0_EXTERNAL_USER_BLOCKER` | `DOCS_TROUBLESHOOTING` |
| 9. Next Safe Action | `scripts/agentos-explain.py` | `AVAILABLE_PARTIAL` | The tool exists but is not marketed as the primary recovery step in docs. | `P1_FIRST_RUN_CONFUSION` | `AUDIT_RESULT_EXPLANATION` |
| 10. Boundary | `docs/safety-boundaries.md` | `AVAILABLE_CLEAR` | Good English documentation of what not to do. | `P2_DOCS_POLISH` | `OUT_OF_SCOPE` |

## Surface Check Summary
| Surface | Status | Classification |
|---|---|---|
| `README.md` | `AVAILABLE_PARTIAL` | `P1_FIRST_RUN_CONFUSION` |
| `docs/installation.md` | `NOT_AVAILABLE` | `P0_EXTERNAL_USER_BLOCKER` |
| `docs/quickstart.md` | `AVAILABLE_CLEAR` | `P1_FIRST_RUN_CONFUSION` |
| `docs/limitations.md` | `AVAILABLE_CONFUSING` | `P0_EXTERNAL_USER_BLOCKER` (RU content) |
| `docs/troubleshooting.md` | `AVAILABLE_CONFUSING` | `P0_EXTERNAL_USER_BLOCKER` (RU content) |
| `docs/mvp-checklist.md` | `AVAILABLE_CONFUSING` | `P2_DOCS_POLISH` (RU content) |
| `examples/` | `AVAILABLE_PARTIAL` | `P1_FIRST_RUN_CONFUSION` |
| `prompts/` | `AVAILABLE_PARTIAL` | `P2_DOCS_POLISH` (Missing README) |
| `install.sh` | `AVAILABLE_CLEAR` | `P1_FIRST_RUN_CONFUSION` (Needs doc link) |
| `agentos-validate.py` | `AVAILABLE_CLEAR` | `P1_FIRST_RUN_CONFUSION` |
| `audit-mvp-readiness.py` | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` |

## Blocker Classification Summary
- **P0 Blockers:** Language barrier in `limitations` and `troubleshooting`; missing `installation` documentation.
- **P1 Confusions:** README complexity; Quickstart assumptions; visibility of example projects and recovery tools.

## Files Allowed for 36.2.1
- `README.md`
- `docs/quickstart.md`
- `docs/GETTING-STARTED.md`

## Deferred Findings
- **36.3.0 — Installation and Quickstart Inspection:** Detailed review of missing `docs/installation.md` and installation scripts.
- **36.5.0 — Troubleshooting and Error Message Inspection:** Translation and hardening of `docs/troubleshooting.md` and `docs/limitations.md`.
- **36.6.1 — First-User Prompt and Guide Pack:** Creation of `prompts/README.md`.

## Non-Claims
- This inspection does not update README.
- This inspection does not update documentation.
- This inspection does not create guides.
- This inspection does not run install smoke.
- This inspection does not run example smoke.
- This inspection does not make AgentOS externally usable by itself.
- This inspection does not approve release publication.
- This inspection does not authorize web UI, cloud/server, vector DB, or M37 feature work.
- This inspection does not replace M36 completion review.

## Final Status
`M36_EXTERNAL_USER_JOURNEY_INSPECTION_COMPLETE`
