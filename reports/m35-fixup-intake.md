# M35 MVP Fixup Intake

**Task ID:** task-m35-fixup-intake
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## M34 Evidence Checked
- `reports/m34-completion-review.md`
- `reports/m34-release-readiness-evidence-report.md`
- `reports/m34-mvp-readiness-audit.md`
- `reports/m34-install-smoke-report.md`
- `reports/m34-template-integrity-report.md`
- `reports/m34-release-readiness-intake.md`
- `tasks/active-task.md`

## M34 Final Decision
- `M34_MVP_NOT_READY`
- `M34_COMPLETION_REVIEW_COMPLETE`

## M34 Next Step
- `PROCEED_TO_M34_FIXUP` (M35)

## M35 Purpose
Fix M34-proven MVP release-readiness blockers only. Do not add new features. Do not start M36.

## Confirmed M34 Blockers
- `bash scripts/run-all.sh` fails due to schema mismatch in `tasks/active-task.md` (additionalProperties error).
- `python3 scripts/agentos-validate.py all` fails.
- `bash scripts/test-example-project.sh` fails due to YAML verification parsing error in `reports/verification.md` within the example.
- `scripts/audit-mvp-readiness.py` standalone entrypoint is missing.

## Blocker Classification
| Item | Classification |
|---|---|
| `run-all` failure (active-task schema mismatch) | `P0_FIXUP_REQUIRED` |
| `agentos-validate all` failure | `P0_FIXUP_REQUIRED` |
| `example-project` smoke failure (verification YAML error) | `P0_FIXUP_REQUIRED` |
| missing standalone MVP audit entrypoint | `P1_FIXUP_RECOMMENDED` |
| M33 inherited gaps (blocked pipeline, negative fixtures wiring) | `NEEDS_HUMAN_REVIEW` |
| M34 documentation gaps (non-blocking) | `OUT_OF_SCOPE_FOR_M35` |

## Fixup Scope
1. Repair `active-task.md` schema mismatch causing `run-all` failure.
2. Fix validation path failures causing `agentos-validate.py all` failure.
3. Repair example project smoke YAML/verification parsing error.
4. Create `scripts/audit-mvp-readiness.py` as a standalone entrypoint wrapper.
5. Perform evidence and completion review after revalidation.

## Explicit Non-Scope
M35 must not implement:
- web UI
- cloud/server
- tutor layer
- new RAG features
- vector DB
- LangGraph
- CrewAI
- self-heal platform
- multi-agent orchestration
- shadow branching
- Git checkpoints
- pip/npm packaging
- M36 features

## Proposed M35 Task Sequence
- 35.2.0 — Validation Failure Inspection
- 35.2.1 — Active Task Schema / run-all Repair
- 35.3.0 — Example Project Smoke Failure Inspection
- 35.3.1 — Example Project Verification YAML Repair
- 35.4.0 — Unified Validation Failure Inspection
- 35.4.1 — Unified Validation Green Path Repair
- 35.5.1 — MVP Audit Entrypoint Wrapper
- 35.6.1 — M35 Full Revalidation Matrix
- 35.7.1 — M35 Evidence Report
- 35.8.1 — M35 Completion Review

## Validation Commands To Re-run Later
- `bash scripts/run-all.sh`
- `python3 scripts/agentos-validate.py all`
- `bash scripts/test-example-project.sh`
- `python3 scripts/audit-mvp-readiness.py`

## Release Readiness Target
M35 target is to move from M34_MVP_NOT_READY to one of:
- `M35_MVP_READY`
- `M35_MVP_READY_WITH_GAPS`

## Non-Claims
- This intake does not make AgentOS MVP-ready.
- This intake does not repair any blocker.
- This intake does not rerun full validation.
- This intake does not rerun install smoke.
- This intake does not rerun example smoke.
- This intake does not approve a release.
- This intake does not authorize M36.
- This intake does not replace M35 completion review.

## Final Status
`M35_FIXUP_INTAKE_COMPLETE`
