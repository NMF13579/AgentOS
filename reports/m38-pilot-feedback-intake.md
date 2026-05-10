# M38 Pilot Feedback Intake

## Purpose

This report captures raw pilot feedback collected after M37.

Feedback recorded here is not yet classified, prioritized, or resolved.

## Source Milestone

- Previous milestone: M37
- Required source evidence:
  - reports/m37-completion-review.md
  - reports/m37-pilot-readiness-evidence-report.md

## Intake Rules

- Record observed feedback before proposing fixes.
- Do not classify severity in this report as final.
- Do not mark feedback as resolved here.
- Do not hide pilot blockers as known limitations.
- Do not convert feedback directly into scope changes.
- Classification happens in Task 38.2.1.

## Feedback Entry Template

### Feedback Item: M38-FB-001

- Date: 2026-05-10
- Pilot user/session: Implementor (Task 40.x)
- Pilot scenario: Scope Enforcement Setup
- User goal: Define a task with empty sensitive_paths or forbidden_new_files.
- Step where issue appeared: Validation (agentos-validate all)
- Observed behavior: FAIL: scope block parse failed.
- Expected behavior: Successful parsing of empty YAML/JSON lists.
- User confusion / blocker: BLOCKER. The parser cannot handle standard YAML '[]' syntax for empty lists.
- Command output or evidence: scripts/check-scope-compliance.py exit code 3.
- Initial severity candidate: P1
- Initial issue type candidate: validation gap
- Notes: Fixed during Task 40.1.0 by removing brackets.

### Feedback Item: M38-FB-002

- Date: 2026-05-10
- Pilot user/session: Project Audit
- Pilot scenario: TUI Status Check
- User goal: Monitor repository health via TUI.
- Step where issue appeared: TUI launch
- Observed behavior: Status shows STATUS_SOURCE_DAMAGED.
- Expected behavior: Operational status display.
- User confusion / blocker: Usability issue. Metadata sync is broken.
- Initial severity candidate: P2
- Initial issue type candidate: known limitation candidate
- Notes: TUI repair was intentionally deferred.

## Current Intake Summary

- Total feedback items recorded: 2
- P0 candidates: 0
- P1 candidates: 1
- P2 candidates: 1
- P3 candidates: 0
- UNKNOWN candidates: 0

## Open Questions

- Which feedback items need classification in 38.2.1?
- Which items may be pilot blockers?
- Which items may be only documentation gaps?
- Which items may be known limitations?

## Next Step

Task 38.2.1 must classify this feedback by severity and issue type.
