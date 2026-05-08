---
type: context-pack
task_id: task-demo
status: generated
generated_by: select-context.py
generated_at: 2026-05-08T14:03:09Z
context_index_path: data/context-index.json
context_index_hash: sha256:0a636b4ee50b64fbc41cc41427300ba54795928384491d129bcfba312169a288
repo_commit_hash: 45eb4d19f2bb7faf684bdceed5da682c8f42ab10
---

# Context Pack

## Task Summary

- task_id: task-demo
- goal: demo

## Selected Context

| Path | Type | Authority | Context Role | Reason | Must Follow |
|---|---|---|---|---|---|
| docs/policy.md | policy | canonical | required_when_relevant | Required for task compliance. | Follow policy boundary. |

## Required Context

- docs/policy.md

## Supporting Context

- none

## Relevant Rules

- rule: Do not bypass M27 runtime enforcement.
  source: docs/policy.md
  why: safety boundary

## Relevant Lessons

- lesson_summary: avoid repeating forbidden approval claims

## Relevant Policies

- docs/policy.md

## Out-of-Scope Context

- path_or_category: secret/
  reason_excluded: out of task scope

## Context Risks

- stale context index

## Source Integrity

- context_index_path: data/context-index.json
- context_index_hash: sha256:0a636b4ee50b64fbc41cc41427300ba54795928384491d129bcfba312169a288
- repo_commit_hash: CURRENT_PLACEHOLDER
- selected_source_hashes:
  - docs/policy.md: sha256:abc

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

- [ ] selected rules checked
- [ ] selected policies checked
- [ ] selected lessons checked
- [ ] out-of-scope checked
- [ ] approval boundary checked
- [ ] M27 checked
- [ ] stale or missing context as NEEDS_REVIEW
