# M38 Pilot Fix Scope Plan

## Purpose

This report defines the M38 fix scope based on pilot feedback classification.

This report does not apply fixes. It only defines what later M38 tasks are allowed to update.

## Source Reports

- reports/m38-pilot-feedback-intake.md
- reports/m38-feedback-classification.md
- reports/m37-completion-review.md
- reports/m37-pilot-readiness-evidence-report.md

## Fix Scope Rules

- P0 items must be fixed before M38 completion.
- P1 pilot blockers must be fixed before M38 completion.
- P2 items may be fixed only if they are low-cost and do not expand milestone scope.
- P3 items must be deferred to backlog or future milestones.
- UNKNOWN items must not be silently downgraded.
- Known limitations cannot hide unresolved P0/P1 issues.
- No new product features are allowed in M38.
- M38 is pilot hardening, not architecture expansion.

## Classification Summary

- P0 items: 0
- P1 items: 0
- P2 items: 0
- P3 items: 0
- UNKNOWN items: 0
- No real feedback recorded: YES

**Status:** `NO_REAL_FEEDBACK_RECORDED`

## Must Fix Before M38 Completion

### P0 Fix Scope

| Feedback ID | Issue | Required Fix Area | Allowed Later Task | Notes |
|---|---|---|---|---|
| NONE | | | | |

### P1 Fix Scope

| Feedback ID | Issue | Required Fix Area | Allowed Later Task | Notes |
|---|---|---|---|---|
| NONE | | | | |

## May Fix If Cheap

### P2 Fix Candidates

| Feedback ID | Issue | Proposed Low-Cost Fix | Allowed Later Task | Defer If |
|---|---|---|---|---|
| NONE | | | | |

## Deferred Items

### P3 / Backlog

| Feedback ID | Issue | Reason Deferred | Suggested Future Milestone |
|---|---|---|---|
| NONE | | | |

## Needs More Evidence

### UNKNOWN Items

| Feedback ID | Missing Evidence | Required Follow-up | Risk If Ignored |
|---|---|---|---|
| NONE | | | |

## Allowed Later M38 Fix Areas

Later M38 tasks may update only the following areas if justified by this scope plan:

- README.md
- docs/quickstart.md
- docs/first-user-guide.md
- docs/troubleshooting.md
- docs/pilot-scope.md
- docs/pilot-safety-boundaries.md
- docs/pilot-onboarding.md
- templates/pilot-feedback.md
- templates/pilot-issue-report.md
- templates/pilot-validation-failure-report.md
- docs/known-limitations.md
- examples/pilot-scenarios/

## Explicitly Out of Scope for M38

The following are not allowed in M38:

- new runtime enforcement layer
- TUI implementation
- SaaS implementation
- MAD / multi-agent debate
- model routing
- vector database / full RAG
- major task pipeline redesign
- autonomous approval
- raw git automation
- release candidate freeze

## No Real Feedback Case

Since no real pilot feedback exists yet, M38 may proceed only as a structural dry run.

## Next Step

Task 38.4.1 may update quickstart and first-user documentation only if this report identifies relevant P0/P1/P2 documentation or onboarding issues.
