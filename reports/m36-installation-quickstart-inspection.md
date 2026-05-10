# M36 Installation and Quickstart Inspection

**Task ID:** task-m36-installation-quickstart-inspection
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-readme-first-user-entry-hardening.md` exists and is complete: PASS
- `README.md` exists: PASS

## Inspection Method
The inspection was performed from the perspective of a first external user who wants to integrate AgentOS into their own project. The focus was on identifying clear instructions for prerequisites, installation/copy methods, template selection, and initial validation, without relying on internal project knowledge.

## First External User Assumption
A developer looking to add AgentOS guardrails to a pre-existing project. They need to know *how* to extract the necessary files from the AgentOS repository and place them into their own workspace, and then how to verify the setup.

## Installation Path Findings
- **Status:** FAIL
- **Prerequisites:** Not clearly defined in a dedicated installation guide.
- **Install/Copy Method:** The `install.sh` script exists and allows installing to a `TARGET_DIR` (current working directory), but there is no `docs/installation.md` explaining this process step-by-step for a new user integrating into an external repo.
- **Template Selection:** `install.sh` supports `--minimal` and `--full`, but the criteria for choosing between them are not detailed in a dedicated installation guide.
- **Root Cause:** Missing dedicated `docs/installation.md` and insufficient installation guidance in the README.

## Quickstart Path Findings
- **Status:** PARTIAL
- **Path:** `docs/quickstart.md` exists.
- **Clarity:** It lists commands but assumes the user knows they need to run `install.sh` from the AgentOS repository targeting their own project directory. The explanation of *what* is being installed is brief.
- **Validation:** Includes validation commands (`agentos-validate.py all`), but lacks the detailed explanation of result meanings (PASS, WARN, BLOCKED) that was just added to the README.
- **Next Actions:** Does not clearly outline the safe next actions after a success or failure specifically in the context of a fresh installation.

## Surface Check Summary
| Surface | Status | Classification |
|---|---|---|
| `README.md` install section | `AVAILABLE_PARTIAL` | `P1_FIRST_RUN_CONFUSION` |
| `README.md` quickstart section | `AVAILABLE_PARTIAL` | `P1_FIRST_RUN_CONFUSION` |
| `docs/installation.md` | `NOT_AVAILABLE` | `P0_INSTALL_BLOCKER` |
| `docs/quickstart.md` | `AVAILABLE_PARTIAL` | `P0_QUICKSTART_BLOCKER` |
| `docs/mvp-checklist.md` | `AVAILABLE_CONFUSING` | `OUT_OF_SCOPE_FOR_M36` (RU text, not primary quickstart path) |
| `docs/limitations.md` | `AVAILABLE_CONFUSING` | `OUT_OF_SCOPE_FOR_M36` (RU text, handled in 36.5.0) |
| `docs/troubleshooting.md` | `AVAILABLE_CONFUSING` | `OUT_OF_SCOPE_FOR_M36` (RU text, handled in 36.5.0) |
| `install.sh` | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` |
| `scripts/test-install.sh` | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` |
| `scripts/run-all.sh` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` (No change needed) |
| `scripts/agentos-validate.py` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` (No change needed) |
| `scripts/audit-mvp-readiness.py` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` (No change needed) |
| `templates/agentos-minimal` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |
| `templates/agentos-full` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |
| `examples/` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |

## Installation / Quickstart Gap Table
| Area | Current Surface | Current State | Finding | Classification | Suggested Fix Area |
|---|---|---|---|---|---|
| Installation | `docs/installation.md` | `NOT_AVAILABLE` | No dedicated step-by-step guide for integrating AgentOS into a new project. | `P0_INSTALL_BLOCKER` | `DOCS_INSTALLATION` |
| Quickstart | `docs/quickstart.md` | `AVAILABLE_PARTIAL` | Lacks context on template selection and clear next steps post-validation. | `P0_QUICKSTART_BLOCKER` | `DOCS_QUICKSTART` |
| README | `README.md` | `AVAILABLE_PARTIAL` | Setup section only points to hooks, not the actual `install.sh` usage. | `P1_FIRST_RUN_CONFUSION` | `README_INSTALL_SECTION` |

## Blocker Classification Summary
- **P0 Blockers:** Missing `docs/installation.md` prevents users from understanding the copy/install mechanism. `docs/quickstart.md` lacks necessary context for a smooth first run.
- **P1 Confusions:** README lacks a clear, high-level installation snippet pointing to the new docs.

## Files Allowed for 36.3.1
- `README.md`
- `docs/quickstart.md`
- `docs/installation.md` (CREATE_ALLOWED)

## Deferred Findings
- **36.4.0 — First Project Onboarding Scenario Inspection:** Ensure the user knows how to create their first task after installation.
- **36.5.0 — Troubleshooting and Error Message Inspection:** Address the Russian language barrier in `troubleshooting.md` and `limitations.md`.

## Non-Claims
- This inspection does not update installation docs.
- This inspection does not update quickstart.
- This inspection does not modify install scripts.
- This inspection does not run install smoke.
- This inspection does not run example smoke.
- This inspection does not make AgentOS externally usable by itself.
- This inspection does not approve release publication.
- This inspection does not authorize pip/npm packaging, web UI, cloud/server, vector DB, or M37 feature work.
- This inspection does not replace M36 completion review.

## Final Status
`M36_INSTALLATION_QUICKSTART_INSPECTION_COMPLETE_WITH_GAPS`
