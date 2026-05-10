# MVP Readiness Checklist

This document defines the core requirements for the External MVP milestone (M36).

## Required Artifacts

- `docs/installation.md`
- `docs/quickstart.md`
- `docs/troubleshooting.md`
- `docs/limitations.md`
- `docs/first-project-onboarding.md`
- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `scripts/check-template-integrity.py`
- `scripts/agentos-validate.py`
- `scripts/audit-mvp-readiness.py`

## Validation Result Guidance

| Status | Interpretation | External User Action |
|---|---|---|
| **MVP_READY** | All P0 blockers resolved. | Project is safe for external trial. |
| **MVP_READY_WITH_GAPS** | P0 blockers resolved, but non-critical P1 issues remain. | Use with caution, read warning reports. |
| **MVP_NOT_READY** | Critical P0 blockers remain. | Do not use for real tasks. |
| **NEEDS_REVIEW** | Evidence is incomplete or contradictory. | Stop and perform manual review. |

## Blocking Conditions for External MVP

- **Failed Safety Gate:** Any P0 validator returning FAIL or BLOCKED.
- **Missing Required Artifact:** Any file listed in "Required Artifacts" is missing.
- **Language Barrier:** Primary troubleshooting documentation is not in English.
- **Technical Debt:** Any "vibe-coding" result (ERROR treated as PASS).

## Decision Boundary

- This checklist does **not** mark AgentOS as MVP-ready automatically.
- Final readiness must be confirmed by the Milestone completion review.
- Template integrity PASS does not equal overall project readiness.
- No lower-level check can override a higher-level safety gate.

## Non-Goals

- Do not claim M36 is finished without a verified evidence report.
- Do not bypass human review through automated metrics.
