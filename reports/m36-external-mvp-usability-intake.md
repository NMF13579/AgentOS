# M36 External MVP Usability Intake

**Task ID:** task-m36-external-mvp-usability-intake
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Preconditions
- M35 Completion Review exists and confirms readiness: PASS
- tasks/active-task.md correctly activated: PASS

## M35 Readiness Input
- Status: `M35_MVP_READY_WITH_GAPS`
- Evidence: M35 repairs successfully resolved P0 structural blockers; pipeline is green.

## M36 Purpose
Make AgentOS understandable, installable, and usable by a first external user without the author nearby.

## First External User Definition
A user who did not build AgentOS, opens the repository for the first time, and wants to install or copy AgentOS into another project using only repository documentation and scripts.

## External User Journey
1. Understand what AgentOS is
2. Understand what AgentOS is not
3. Install or copy AgentOS into a project
4. Run the first validation command
5. Run or inspect the example project
6. Understand PASS / WARNING / BLOCKED / NOT_READY results
7. Know the next safe action after failure
8. Know where not to go next

## Current Usability Surface
| Item | Status | Notes |
|---|---|---|
| README | PRESENT | Main entry point; needs clarity check. |
| docs/installation | NOT_AVAILABLE | Critical gap for external users. |
| docs/quickstart | PRESENT | Initial onboarding; needs hardening. |
| docs/limitations | PRESENT | Non-claims and boundaries. |
| docs/troubleshooting | PRESENT | Recovery paths. |
| docs/mvp-checklist | PRESENT | Readiness tracking. |
| templates | PRESENT | Core structural artifacts. |
| examples | PRESENT | Reference projects. |
| prompts | PRESENT | Prompt packs. |
| install script | PRESENT | `install.sh` in root. |
| test-install script | PRESENT | `scripts/test-install.sh`. |
| test-example-project script | PRESENT | `scripts/test-example-project.sh`. |
| audit-mvp-readiness entrypoint | PRESENT | `scripts/audit-mvp-readiness.py`. |
| agentos-validate entrypoint | PRESENT | `scripts/agentos-validate.py`. |

## First-User Blocker Classification
- `P0_EXTERNAL_USER_BLOCKER`: Missing `docs/installation`. External user cannot reliably install into a new project without specific instructions.
- `P1_FIRST_RUN_CONFUSION`: `README` and `Quickstart` clarity. Existing content is mostly author-centric and technical.
- `P1_FIRST_RUN_CONFUSION`: User-facing explanation of audit/validation results. Current output is technical/audit-focused.
- `P2_DOCS_POLISH`: Formatting and cross-referencing between docs.

## M36 Allowed Scope
- README first-user clarity
- installation instructions
- quickstart
- limitations / non-claims
- troubleshooting
- MVP checklist
- first-project onboarding scenario
- example scenario clarity
- prompt pack usage instructions
- user-facing explanation of audit/validation results
- first-user smoke test documentation

## Explicit Non-Scope
M36 must not implement:
- web UI
- cloud/server
- dashboard
- marketplace
- tutor layer as product feature
- new RAG features
- vector DB
- LangGraph
- CrewAI
- self-heal platform
- multi-agent orchestration
- shadow branching
- Git checkpoints
- pip/npm packaging
- M37 features

## Proposed M36 Task Sequence
- 36.2.0 — External User Journey Inspection
- 36.2.1 — README / First-User Entry Hardening
- 36.3.0 — Installation and Quickstart Inspection
- 36.3.1 — Installation / Quickstart Hardening
- 36.4.0 — First Project Onboarding Scenario Inspection
- 36.4.1 — First Project Onboarding Scenario
- 36.5.0 — Troubleshooting and Error Message Inspection
- 36.5.1 — Troubleshooting / Result Explanation Hardening
- 36.6.1 — First-User Prompt and Guide Pack
- 36.7.1 — External Usability Smoke Test
- 36.8.1 — M36 Evidence Report
- 36.9.1 — M36 Completion Review

## Success Criteria
A first external user can understand what AgentOS is, install or copy it, run first validation, inspect an example, understand failures, and know the next safe action without the author nearby.

Target completion states:
- `M36_EXTERNAL_MVP_USABLE`
- `M36_EXTERNAL_MVP_USABLE_WITH_GAPS`
- `M36_EXTERNAL_MVP_NOT_USABLE`
- `M36_BLOCKED`

## Non-Claims
- This intake does not update documentation.
- This intake does not run install smoke.
- This intake does not run example smoke.
- This intake does not make AgentOS externally usable by itself.
- This intake does not approve release publication.
- This intake does not authorize web UI, cloud/server, vector DB, or M37 feature work.
- This intake does not replace M36 completion review.

## Final Status
`M36_USABILITY_INTAKE_COMPLETE`
