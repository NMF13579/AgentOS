---
type: context-pack
task_id: task-fixture
status: generated
generated_by: select-context.py
generated_at: 2026-05-08T13:55:17Z
context_index_path: data/context-index.json
context_index_hash: sha256:0a636b4ee50b64fbc41cc41427300ba54795928384491d129bcfba312169a288
repo_commit_hash: 40f70c83a4fad1f2b24e4ec32b98b7dd787860ae
---

# Context Pack

## Task Summary

- task_id: task-fixture
- goal: Fixture goal
- risk_level: LOW
- affected_paths:
  - tests/fixtures/context-required/bad-source-hash-format/source.md
- source_task_path: tests/fixtures/context-required/valid-context-pack/example-task.md
- task_lint_status: PASS

## Selected Context

| Path | Type | Authority | Context Role | Reason | Must Follow |
|---|---|---|---|---|---|
| tests/fixtures/context-required/bad-source-hash-format/source.md | policy | canonical | required_when_relevant | Matches fixture task signals. | Follow fixture policy. |

## Required Context

- tests/fixtures/context-required/bad-source-hash-format/source.md

## Supporting Context

- none

## Relevant Rules

- rule: Follow fixture rule
  source: tests/fixtures/context-required/bad-source-hash-format/source.md
  why: Needed for fixture

## Relevant Lessons

- none

## Relevant Policies

- none

## Out-of-Scope Context

- path_or_category: archive
  reason_excluded: unrelated
  manual_review_needed: false

## Context Risks

- none

## Source Integrity

- context_index_path: data/context-index.json
- context_index_hash: sha256:0a636b4ee50b64fbc41cc41427300ba54795928384491d129bcfba312169a288
- repo_commit_hash: 40f70c83a4fad1f2b24e4ec32b98b7dd787860ae
- selected_source_hashes:
  - tests/fixtures/context-required/bad-source-hash-format/source.md: abc123
- integrity_warnings: []

Freshness proves alignment with source.
Freshness does not grant approval.
Invalid or stale derived context must never be silently upgraded into trusted context.

## Non-Authorization Warning

Context Pack is not approval.
Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.
Context Pack does not replace M27 runtime enforcement.
Context Pack does not replace Human Gate approval.
Freshness check is not approval.
Integrity check is not approval.

## Verification Checklist

- [ ] Selected rules were acknowledged in the plan.
- [ ] Selected policies were not contradicted.
- [ ] Selected lessons were not repeated as mistakes.
- [ ] Out-of-scope context was not touched.
- [ ] Context Pack did not grant approval.
- [ ] Runtime enforcement remained under M27.
- [ ] Any stale or missing context was handled as NEEDS_REVIEW.
