---
type: canonical
module: m23
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Scope Summary Standard

## Purpose
Scope summary provides a short human-readable view of scope compliance results so a user can understand risk quickly without reading full validator logs.

## Relationship to Scope Compliance
Scope summary is derived from scope compliance validator output. It is an evidence layer that reports result, reason, counts, and required human action.

## Relationship to Human-Readable Summaries
This document is specific to scope compliance outcomes and can align with broader human-readable summary standards when both are present.

## Required Scope Summary Fields
Scope Summary

Result: PASS | FAIL | WARN | NOT_RUN | ERROR
Reason:
Changed files:
Violations:
Warnings:
Human action required: YES | NO
Next step:
Evidence:

Field definitions:
- Result: final scope status.
- Reason: short explanation for the status.
- Changed files: count or explicit scope file evidence.
- Violations: count of detected violations.
- Warnings: count of warning conditions.
- Human action required: whether manual review is needed.
- Next step: recommended next action.
- Evidence: command output reference or report location.

## Result Meanings
PASS means no detected scope violation.
FAIL means at least one scope violation was detected.
WARN means review is recommended.
NOT_RUN means no scope compliance evidence was produced.
ERROR means the scope compliance check could not complete reliably.

## Human Action Rules
FAIL requires human review.
WARN requires human review or documented acceptance.
ERROR requires human review.
NOT_RUN is not PASS.
PASS does not prove implementation correctness.

## Evidence Requirements
A valid scope summary should reference:
- scope compliance command
- exit code
- validator result
- changed files count
- violations count
- warnings count
- scope evidence source

A scope summary without command evidence is incomplete.
A scope summary without changed files evidence is incomplete.

## PASS Example
Scope Summary

Result: PASS
Reason: no detected scope violations
Changed files: 1
Violations: 0
Warnings: 0
Human action required: NO
Next step: continue review
Evidence: python3 scripts/check-scope-compliance.py --task tasks/active-task.md; exit code 0

## FAIL Example
Scope Summary

Result: FAIL
Reason: changed file outside allowed scope
Changed files: 2
Violations: 1
Warnings: 0
Human action required: YES
Next step: review and correct scope mismatch
Evidence: python3 scripts/check-scope-compliance.py --task tasks/active-task.md; exit code 1

## WARN Example
Scope Summary

Result: WARN
Reason: sensitive path changed
Changed files: 1
Violations: 0
Warnings: 1
Human action required: YES
Next step: perform human review for sensitive path
Evidence: python3 scripts/check-scope-compliance.py --task tasks/active-task.md; exit code 2

## NOT_RUN Example
Scope Summary

Result: NOT_RUN
Reason: scope compliance validator was not executed
Changed files: NOT_CHECKED
Violations: NOT_CHECKED
Warnings: NOT_CHECKED
Human action required: YES
Next step: run scope compliance validator
Evidence: no command output captured

## ERROR Example
Scope Summary

Result: ERROR
Reason: scope compliance check could not complete reliably
Changed files: NOT_CHECKED
Violations: NOT_CHECKED
Warnings: NOT_CHECKED
Human action required: YES
Next step: investigate validator execution failure
Evidence: python3 scripts/check-scope-compliance.py --task tasks/active-task.md; exit code 3

## Non-Authority Boundaries
Unsafe claims that are rejected:
- scope summary approves task completion
- scope summary proves correctness
- PASS means implementation is correct
- PASS means human approval is not needed
- summary replaces full evidence
- summary replaces scope validator output
- summary can override scope violations

Scope summary is evidence only and does not replace validator output or human decisions.
