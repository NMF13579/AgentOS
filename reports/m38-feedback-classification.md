# M38 Feedback Classification

## Purpose

This report classifies pilot feedback collected in:

- reports/m38-pilot-feedback-intake.md

This report does not fix issues and does not approve scope changes.

## Classification Rules

- Classify only real feedback items.
- Do not classify empty template placeholders as real feedback.
- Do not mark any item as resolved.
- Do not convert feedback into implementation scope.
- Do not hide P0 or P1 issues as known limitations.
- Fix planning happens in Task 38.3.1.

## Severity Model

### P0 — Critical Blocker

Pilot must stop or cannot safely continue.

### P1 — Pilot Blocker

Pilot can continue only after this issue is addressed.

### P2 — Usability Issue

Pilot can continue, but user friction is high.

### P3 — Backlog / Improvement

Useful, but not required for M38 hardening.

### UNKNOWN

Not enough evidence to classify safely.

## Issue Type Taxonomy

Allowed issue types:

- onboarding gap
- documentation gap
- validation gap
- safety/non-claims gap
- pilot-pack gap
- command mismatch
- user confusion
- known limitation candidate
- future feature request
- unknown

## Classification Table

| Feedback ID | Severity | Issue Type | Pilot Impact | Recommended Handling | Evidence Source |
|---|---|---|---|---|---|
| M38-FB-001 | P1 | validation gap | Blocker for new tasks | FIXED in 40.1.0; Add to troubleshooting | reports/m38-pilot-feedback-intake.md |
| M38-FB-002 | P2 | known limitation | Friction/Confusion | Record as Known Limitation | reports/m38-pilot-feedback-intake.md |

**Status:** `FEEDBACK_CLASSIFIED`

## Severity Summary

- P0 items: 0
- P1 items: 1
- P2 items: 1
- P3 items: 0
- UNKNOWN items: 0
- Empty placeholders ignored: 0

## Pilot Blocker Summary

### Must Fix Before M38 Completion

- P0: 0
- P1: 1 (Fixed)

### May Fix If Cheap

- P2: 1 (Documented)

### Defer / Backlog

- P3: 0

### Needs More Evidence

- UNKNOWN: 0

## Known Limitation Candidates

Items listed here are not accepted as known limitations yet.

## Next Step

Task 38.3.1 must create a P0/P1 fix scope plan based on this classification.
