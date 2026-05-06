---
type: template
module: m23
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Scope Gate Verification Template

## Purpose
This template records scope gate verification evidence for task review. Scope gate verification is evidence, not approval.

## Usage
Use this template after running scope compliance and related checks. Fill all fields from actual command outputs and observed git state.

## Scope Gate Verification Block
Scope Gate Verification

Task:
Date:
Reviewer:
Result: PASS | FAIL | WARN | NOT_RUN | ERROR | INCOMPLETE

Human Summary:
Reason:
Changed files count:
Violations count:
Warnings count:
Human action required: YES | NO
Next step:

Scope Compliance Evidence:
command:
exit_code:
result:
output_summary:

Changed Files Evidence:
tracked_changes:
staged_changes:
untracked_files:

Violations:
- NONE

Warnings:
- NONE

Validation Evidence:
- command:
  exit_code:
  result:
  output_summary:

Human Review:
required: YES | NO
reason:
override_applied: YES | NO
override_reason:
review_decision: PENDING | ACCEPTED | REJECTED | NEEDS_REVIEW

Field definitions:
- Task: reviewed task identifier.
- Date: verification date.
- Reviewer: person performing review.
- Result: final scope gate status.
- Human Summary: short human-readable summary line.
- Reason: short explanation for result.
- Changed files count: number of changed files.
- Violations count: number of scope violations.
- Warnings count: number of warnings.
- Human action required: whether manual review action is required.
- Next step: recommended follow-up action.
- command: exact executed command.
- exit_code: command exit code.
- result: command result state.
- output_summary: short command output summary.
- tracked_changes: tracked file changes evidence.
- staged_changes: staged file changes evidence.
- untracked_files: untracked file evidence.
- Violations: listed scope violations.
- Warnings: listed warnings.
- Validation Evidence: command evidence list with result metadata.
- Human Review: human decision block.
- override_applied: whether override was used.
- override_reason: explicit reason for override.
- review_decision: human decision state.

## Human Summary
Human summary is a short review interface for current scope status and required action.

## Scope Summary
Result semantics:
- PASS means no detected scope violation.
- FAIL means at least one scope violation was detected.
- WARN means review is recommended.
- NOT_RUN means no scope compliance evidence was produced.
- ERROR means the scope compliance check could not complete reliably.
- INCOMPLETE means required verification evidence is missing.

## Changed Files
Changed files evidence must include:
- tracked changes
- staged changes
- untracked files

Required evidence sources:
- git diff --name-status
- git diff --name-status --cached
- git ls-files --others --exclude-standard

## Scope Compliance
A scope gate verification without scope compliance result is incomplete.
A scope gate verification without command evidence is incomplete.
A scope gate verification without changed files evidence is incomplete.
NOT_RUN is not PASS.
INCOMPLETE is not PASS.

## Violations
FAIL requires human review.
Scope violation requires human review.

## Warnings
WARN requires human review or documented acceptance.

## Validation Evidence
Validation evidence entries must include command, exit code, result, and output summary.

## Human Review Required
Missing evidence requires human review.
ERROR requires human review.
Human override must be explicit and documented.
Human approval cannot be inferred from validator PASS.
Review decision must remain PENDING until a human decision is recorded.
PASS does not prove implementation correctness.

## Final Review Boundary
Scope gate verification supports review and does not approve task completion.

## Non-Authority Boundaries
Unsafe claims that are rejected:
- scope gate verification approves task completion
- scope gate verification proves correctness
- PASS means implementation is correct
- PASS means human review is unnecessary
- validator output replaces human review
- missing evidence can be ignored
- scope violation can be auto-approved
- human approval can be inferred from evidence
