---
type: canonical
module: m23
status: draft
authority: canonical
created: 2026-05-06
last_validated: unknown
---

# Required Evidence Policy

## Purpose
This policy defines the minimum evidence required before accepting task execution results for review. Evidence supports review decisions and does not approve completion.

## Relationship to Scope Compliance
Scope compliance output is a required evidence source for execution review. The policy defines how command results and git-state evidence must be recorded.

## Relationship to Validation Summaries
Validation summaries provide quick human-readable status. This policy defines the minimum mandatory evidence fields that summaries and reports must include.

## Minimum Evidence Block
Evidence

command:
exit_code:
result:
output_summary:
changed_files:
violations:
warnings:
human_action_required:

Field definitions:
- command: the exact command executed.
- exit_code: command exit code.
- result: PASS, FAIL, WARN, NOT_RUN, ERROR, or INCOMPLETE.
- output_summary: short result summary.
- changed_files: changed files evidence details.
- violations: listed violations.
- warnings: listed warnings.
- human_action_required: YES or NO for required human action.

## Evidence Result Semantics
PASS means the command completed and no violation was detected.
FAIL means the command completed and at least one violation was detected.
WARN means the command completed and review is recommended.
NOT_RUN means the command was not executed.
ERROR means the command could not complete reliably.
INCOMPLETE means evidence is missing required fields.

## Command Evidence Requirements
Every required validation must include the command that was run.
Every required validation must include the exit code.
Every required validation must include the result.
A command without an exit code is incomplete evidence.
A result without command evidence is incomplete evidence.

## Changed Files Evidence Requirements
Changed files evidence is required for execution review.
Changed files evidence must include tracked changes.
Changed files evidence must include staged changes when present.
Changed files evidence must include untracked files when present.
A report without changed files evidence is incomplete.

Required evidence sources:
- git diff --name-status
- git diff --name-status --cached
- git ls-files --others --exclude-standard

## Violation Evidence Requirements
Violations must be listed when result is FAIL.
Warnings must be listed when result is WARN.
FAIL blocks acceptance unless a human explicitly overrides.
ERROR requires human review.
NOT_RUN is not PASS.
INCOMPLETE is not PASS.

## Human Review Requirements
Scope violation requires human review.
Missing evidence requires human review.
ERROR requires human review.
NOT_RUN requires human review or documented justification.
WARN requires human review or documented acceptance.
PASS does not prove implementation correctness.

## Incomplete Evidence Handling
Evidence missing required fields must be marked INCOMPLETE.
INCOMPLETE evidence must be treated as review-blocking until gaps are resolved or explicitly reviewed.
Missing evidence must be visible as NOT_RUN, ERROR, or INCOMPLETE.

## Non-Authority Boundaries
Unsafe claims that are rejected:
- evidence approves task completion
- evidence proves correctness
- PASS means implementation is correct
- NOT_RUN can be treated as PASS
- missing evidence can be ignored
- human approval can be inferred from evidence
- validator output replaces human review

Evidence informs review and does not replace human approval.
