---
type: cli-doc
milestone: M53
task: 53.5
title: Task Candidate Placement Review CLI
status: draft
authority: supporting
created_for: M53
depends_on:
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-INPUT-CONTRACT.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-OUTPUT-CONTRACT.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-POLICY.md
script:
  - scripts/review-task-candidate-placement.py
---

## 1. Purpose

The placement review CLI performs read-only M53 placement eligibility review.

## 2. Non-Authority Boundary

The placement review CLI is not approval.
The placement review CLI does not authorize execution.
The placement review CLI does not authorize queue placement.
The placement review CLI does not authorize active-task replacement.
The placement review CLI does not authorize lifecycle mutation.
The placement review CLI does not authorize M54 materialization.

## 3. CLI Usage

```bash
python3 scripts/review-task-candidate-placement.py --explain
python3 scripts/review-task-candidate-placement.py --input <path>
python3 scripts/review-task-candidate-placement.py --candidate-result <path>
python3 scripts/review-task-candidate-placement.py --candidate-result <path> --m52-reports-dir reports --json
python3 scripts/review-task-candidate-placement.py --fixtures
```

## 4. Mode Exclusivity

Exactly one of --input, --candidate-result, --fixtures, or --explain must be provided.

- using more than one review input mode blocks the review
- using none blocks the review
- --json is an output mode, not a review input mode
- --json combined with --fixtures returns PLACEMENT_REVIEW_BLOCKED with exit code 2
- --json combined with --explain returns PLACEMENT_REVIEW_BLOCKED with exit code 2
- conflicting modes with --json write blocked JSON to stdout and diagnostics to stderr
- blocked mode combinations are not PLACEMENT_REVIEW_NOT_ELIGIBLE
- mode validation failures happen before M52 dependency checks

## 5. --fixtures Behavior

In 53.5, --fixtures runs built-in self-checks only and does not use repository fixture directories.

- --fixtures exits 0 if built-in self-checks pass
- --fixtures exits 2 if built-in self-checks fail
- --fixtures writes human-readable self-check output to stderr
- --fixtures writes nothing to stdout
- --fixtures does not create reports
- --fixtures does not inspect tasks/queue/
- --fixtures does not inspect tasks/active-task.md
- --fixtures does not inspect approvals/
- --fixtures --json returns PLACEMENT_REVIEW_BLOCKED with exit code 2

## 6. Result Tokens and Exit Codes

- PLACEMENT_REVIEW_ELIGIBLE: 0
- PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS: 0
- PLACEMENT_REVIEW_NOT_ELIGIBLE: 1
- PLACEMENT_REVIEW_BLOCKED: 2

Exit code 0 does not authorize queue placement, active-task replacement, execution, lifecycle mutation, or M54 materialization.

## 7. JSON Output Contract

- --json writes result JSON to stdout only
- stdout must contain no prose when --json is used
- diagnostics may go to stderr
- conflicting modes with --json still produce blocked JSON on stdout
- the result follows schemas/task-candidate-placement-review-result.schema.json
- no top-level execution_authorized field is allowed
- execution_authorized exists only under boundary_flags

## 8. Input Format Boundary

The CLI supports JSON input and Markdown fenced JSON input only.

- fenced YAML is not supported in 53.5
- YAML frontmatter is not a machine-readable input package
- unsupported YAML input returns PLACEMENT_REVIEW_BLOCKED
- PyYAML is forbidden
- ad-hoc YAML parsing is forbidden

## 9. Carry-Forward Extraction

carry_forward fields are the union of values found in reports/m52-completion-review.md and the provided input/candidate-result.

- if a carry-forward field is missing from both sources, output []
- non_authority_boundary must never be empty
- M52 limitations must not be dropped because candidate-result omits them
- COMPLETE_WITH_LIMITATIONS forces PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS unless blocked or not eligible

## 10. Read-Only Boundary

The placement review CLI is read-only.

Forbidden writes:
- tasks/queue/
- tasks/active-task.md
- reports/
- approvals/
- generated/
- docs/
- schemas/
- templates/
- tests/
- examples/
- memory-bank/

## 11. M52 Dependency

The CLI always requires reports/m52-completion-review.md as the canonical M52 completion dependency.

- --m52-reports-dir may locate supporting M52 reports only
- --m52-reports-dir cannot replace reports/m52-completion-review.md
- non-canonical completion review paths are invalid

## 12. M54 Boundary

The placement review CLI may identify a candidate for future M54 consideration.
The placement review CLI does not authorize M54 to run.
The placement review CLI does not authorize queue materialization.
The placement review CLI does not authorize active-task proposal materialization.
M54 must independently validate materialization.

## 13. Summary

The M53 placement review CLI may produce a placement eligibility result.

That result is still:
not queued,
not active,
not approved,
not executable,
not materialized,
and still waiting for M54 controlled placement materialization.
