# M36 First Project Onboarding Scenario Inspection

**Task ID:** task-m36-first-project-onboarding-inspection
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- `reports/m36-readme-first-user-entry-hardening.md` exists and is complete: PASS
- `reports/m36-installation-quickstart-hardening.md` exists and is complete: PASS

## Inspection Method
The inspection was performed from the perspective of a first external user who has successfully installed AgentOS and run the initial validation commands. The focus was on identifying clear, actionable instructions for structuring and executing their very first real task or example scenario.

## First External User Assumption
A developer who understands the concept of "Markdown-first guardrails" from the README but needs practical guidance on *how* to fill out `tasks/active-task.md` for the first time, what files they are allowed to edit, and how to verify their work.

## First Project Path Findings
- **Status:** FAIL
- **Starting Point:** `docs/quickstart.md` tells the user to "Open tasks/active-task.md" and "Define a small, scoped goal". However, it provides no structural example of what a valid M35/M36 task contract looks like (e.g., the `scope_control` block).
- **GETTING-STARTED:** `docs/GETTING-STARTED.md` describes a complex 7-step flow (Initialization -> Specification -> Validation -> Review -> Contract -> Approval -> Activation) that is currently out of sync with the simpler M35 minimal contract approach. This will severely confuse a first-time user.
- **Root Cause:** Lack of a clear "Your First Task" tutorial or copy-pasteable minimal contract in the quickstart or onboarding docs.

## Example Project Path Findings
- **Status:** PARTIAL / CONFUSING
- **Starting Point:** `examples/simple-project/` exists and runs, but the primary `examples/README.md` lists scenarios (`scenario-01-new-feature.md`, `scenario-02-bugfix.md`, etc.) that do not actually exist under those names. They exist in `examples/scenarios/` under different names (e.g., `simple-docs-change.md`), and the content of these files is heavily technical and partially in Russian.

## Surface Check Summary
| Surface | Status | Classification |
|---|---|---|
| `README` first-project guidance | `AVAILABLE_PARTIAL` | `P2_DOCS_POLISH` |
| `docs/quickstart.md` first project section | `AVAILABLE_PARTIAL` | `P0_ONBOARDING_BLOCKER` |
| `docs/installation.md` post-install next step | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` (Links to quickstart) |
| `docs/mvp-checklist.md` first project checklist | `NOT_AVAILABLE` | `OUT_OF_SCOPE_FOR_M36` |
| `docs/GETTING-STARTED.md` | `AVAILABLE_CONFUSING` | `P0_ONBOARDING_BLOCKER` |
| `examples/` entrypoint | `AVAILABLE_CONFUSING` | `P1_FIRST_PROJECT_CONFUSION` |
| `examples/scenarios/` entrypoint | `AVAILABLE_CONFUSING` | `P1_FIRST_PROJECT_CONFUSION` |
| `examples/simple-project` | `AVAILABLE_CLEAR` | `P2_DOCS_POLISH` |
| `templates/agentos-minimal` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |
| `templates/agentos-full` | `AVAILABLE_CLEAR` | `NOT_APPLICABLE` |
| `prompts/` entrypoint | `AVAILABLE_PARTIAL` | `P3_FOLLOWUP` (Deferred to 36.6.1) |

## First Project Gap Table
| Area | Current Surface | Current State | Finding | Classification | Suggested Fix Area |
|---|---|---|---|---|---|
| Quickstart Task | `docs/quickstart.md` | `AVAILABLE_PARTIAL` | No concrete example of how to fill out `active-task.md`. | `P0_ONBOARDING_BLOCKER` | `DOCS_QUICKSTART_FIRST_PROJECT` |
| Getting Started | `docs/GETTING-STARTED.md` | `AVAILABLE_CONFUSING` | Documents a complex 7-step flow that contradicts the M35 minimal approach. | `P0_ONBOARDING_BLOCKER` | `README_FIRST_PROJECT_PATH` |
| Example Scenarios | `examples/README.md` | `AVAILABLE_CONFUSING` | Lists non-existent files; existing scenarios are too complex/RU-heavy. | `P1_FIRST_PROJECT_CONFUSION` | `EXAMPLES_ENTRYPOINT` |

## Blocker Classification Summary
- **P0 Blockers:** First users lack a concrete, copy-pasteable example of an `active-task.md` contract to start their work. Existing conceptual docs (`GETTING-STARTED.md`) contradict the current minimal workflow.
- **P1 Confusions:** Example scenarios are mislinked and poorly targeted for first external use.

## Files Allowed for 36.4.1
- `docs/quickstart.md`
- `docs/GETTING-STARTED.md`
- `examples/README.md`

## Deferred Findings
- **36.5.0 — Troubleshooting and Error Message Inspection:** Translate and harden the troubleshooting documentation.
- **36.6.1 — First-User Prompt and Guide Pack:** Creation of `prompts/README.md` to guide AI tools.

## Non-Claims
- This inspection does not create onboarding scenarios.
- This inspection does not update examples.
- This inspection does not update templates.
- This inspection does not update documentation.
- This inspection does not run example smoke.
- This inspection does not make AgentOS externally usable by itself.
- This inspection does not approve release publication.
- This inspection does not authorize web UI, cloud/server, hosted onboarding, IDE plugin, vector DB, or M37 feature work.
- This inspection does not replace M36 completion review.

## Final Status
`M36_FIRST_PROJECT_ONBOARDING_INSPECTION_COMPLETE_WITH_GAPS`
