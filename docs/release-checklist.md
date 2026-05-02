# Release Checklist

## Purpose
Define a minimal, versioned release checklist for AgentOS MVP readiness evaluation.

## Version Source
- `VERSION` is the source of the release version.
- Expected value for this task: `0.2.0`.

## Release Scope
This checklist defines evidence collection and gate checks only.
It does not implement release automation and does not decide M20 completion by itself.

## Required Release Artifacts
- VERSION exists — status: PASS
- CHANGELOG.md exists — status: PASS
- docs/STABLE-MVP-RELEASE-READINESS.md exists — status: PASS
- docs/release-checklist.md exists — status: PASS
- templates/release-notes.md exists — status: PASS

## Required Readiness Gates
- DOCUMENTATION_GATE
- VALIDATION_GATE
- POLICY_GATE
- APPROVAL_GATE
- APPLY_PIPELINE_GATE
- REGRESSION_GATE
- AUDIT_GATE
- SMOKE_GATE
- EVIDENCE_GATE
- COMPLETION_REVIEW_GATE

## Required Validation Commands
- validate-task.py passed or explicitly marked NOT_APPLICABLE with reason — status: NOT_APPLICABLE
  - reason: validator not part of this release artifact task scope.
- validate-verification.py passed or explicitly marked NOT_APPLICABLE with reason — status: NOT_APPLICABLE
  - reason: validator not part of this release artifact task scope.
- run-all.sh passed or explicitly marked NOT_APPLICABLE with reason — status: NOT_APPLICABLE
  - reason: release automation runner is out of scope for this task.
- M19 gate audit passed or explicitly marked NOT_RUN — status: NOT_RUN
- M19 unified gate smoke passed or explicitly marked NOT_RUN — status: NOT_RUN

## Required Evidence
- reports/milestone-19-evidence-report.md — status: PASS
- reports/milestone-19-completion-review.md — status: PASS
- Gate outputs and marker compatibility from M19 artifacts — status: PASS

## Checklist Status Vocabulary
Allowed status values:
- PASS
- FAIL
- NOT_RUN
- NOT_IMPLEMENTED
- NOT_APPLICABLE

Status meanings:
- PASS: required item exists or required check passed with observable evidence.
- FAIL: required item missing/invalid or check failed.
- NOT_RUN: implementation exists but was not executed in this task/session.
- NOT_IMPLEMENTED: item does not exist yet, so it cannot be run.
- NOT_APPLICABLE: explicitly out of scope for this MVP version, with written reason.

Rules:
- NOT_RUN is not PASS.
- NOT_IMPLEMENTED is not PASS.
- NOT_APPLICABLE requires a written reason.
- PASS without evidence is invalid.
- FAIL cannot be converted to PASS by release notes, changelog entries, or future intent.
- An agent must not upgrade NOT_IMPLEMENTED to NOT_RUN or downgrade NOT_RUN to NOT_IMPLEMENTED without written justification.
- FAIL must not be hidden behind NOT_APPLICABLE.

## Blocking Conditions
- Any required safety gate result is FAIL.
- Any required safety gate marked NOT_RUN and treated as PASS.
- Any required gate ERROR treated as PASS.
- Any generic traceback or usage error treated as enforcement PASS.
- Missing required release artifacts.

## MVP Readiness Label Handling
Possible future outcomes only:
- MVP_READY
- MVP_READY_WITH_WARNINGS
- MVP_NOT_READY
- NEEDS_REVIEW

This checklist does not assign a final label by itself.

## Release Decision Boundary
- A release checklist cannot override failed safety gates.
- A release checklist cannot mark AgentOS as MVP-ready by itself.
- Final readiness decision must come from Milestone 20 evidence and completion review.

## Non-Goals
- Do not implement release automation.
- Do not create install scripts.
- Do not create smoke scripts.
- Do not create package publishing flow.
- Do not create CI release jobs.
- Do not create GitHub release.
- Do not tag the repository.
- Do not decide M20 completion.

## Planned but Not Implemented Items
- install smoke-test — status: NOT_IMPLEMENTED
- example project smoke-test — status: NOT_IMPLEMENTED
- GitHub Actions workflow exists — status: NOT_IMPLEMENTED
- PR Quality Gate exists — status: NOT_IMPLEMENTED
- minimal template exists — status: NOT_IMPLEMENTED
- full template exists — status: NOT_IMPLEMENTED
- quickstart exists — status: NOT_IMPLEMENTED
- usage docs exist — status: NOT_IMPLEMENTED
- known limitations documented — status: NOT_IMPLEMENTED
