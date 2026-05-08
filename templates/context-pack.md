---
type: context-pack
task_id: task-example
status: generated
generated_by: select-context.py
generated_at: 2026-05-07T00:00:00Z
context_index_path: data/context-index.json
context_index_hash: sha256:example
repo_commit_hash: example-commit-hash
---

# Context Pack

## Task Summary

- task_id: task-example
- goal: Example goal.
- risk_level: MEDIUM
- affected_paths:
  - docs/M28-*
- source_task_path: tasks/active-task.md
- task_lint_status: PASS

## Selected Context

| Path | Type | Authority | Context Role | Reason | Must Follow |
|---|---|---|---|---|---|
| docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md | architecture | canonical | required_when_relevant | Matches m28/context-control task. | M28 must not become runtime authority. |

## Required Context

- docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md

## Supporting Context

- docs/M28-CONTEXT-FRONTMATTER-STANDARD.md

## Relevant Rules

- rule: M28 may validate context compliance and must not become runtime authority.
  source: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
  why: Prevents authority drift during execution.

## Relevant Lessons

- lesson_summary: Prevent scope drift by constraining implementation to approved files.
  source: lessons/lessons.md
  repeated_error_risk: Medium
  required_behavior: Stop when scope expands without approval.

## Relevant Policies

- docs/NO-DIRECT-PUSH-POLICY.md

## Out-of-Scope Context

- path_or_category: archived docs
  reason_excluded: Not required for current task.
  manual_review_needed: false

## Context Risks

- selected context has warnings in one source file

## Source Integrity

- context_index_path: data/context-index.json
- context_index_hash: sha256:example
- repo_commit_hash: example-commit-hash
- selected_source_hashes:
  - docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md: sha256:example
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
