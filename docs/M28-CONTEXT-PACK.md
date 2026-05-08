# M28 Context Pack

## 1. Purpose

Context Pack exists to answer:
- what context was selected for this task?
- why was each item selected?
- what rules must the agent follow?
- what lessons are relevant?
- what context is explicitly out of scope?
- what risks or conflicts were found?
- what must be verified after execution?

- Context Pack is task-specific.
- Context Pack must be minimal and explainable, not exhaustive.
- Context Pack is generated from source-aligned context metadata.
- Context Pack does not replace source files.
- Context Pack is not approval.

## 2. Source-of-Truth Boundary

- Markdown/YAML = Semantic Source of Truth.
- data/context-index.json = generated M28 context-selection index.
- Context Pack = generated task-specific working context.
- Context Pack is subordinate to source files.
- Context Pack may quote or summarize source context, but source files remain authoritative.

- Context Pack must remain subordinate to source files.
- Context Pack freshness does not grant approval.
- Context Pack validity does not grant approval.
- Context Pack must not override M27 runtime enforcement.

## 3. Context Pack Frontmatter

Required frontmatter fields:
- type
- task_id
- status
- generated_by
- generated_at
- context_index_path
- context_index_hash
- repo_commit_hash

Allowed status values:
- generated
- stale
- invalid
- needs_review

Rules:
- generated_at is generated metadata
- context_index_hash is generated metadata
- repo_commit_hash is generated metadata
- generated metadata must not be hand-authored as semantic truth
- context_index_hash must use the same hash format as source_hash in data/context-index.json: sha256:hexdigest

Status immutability:
- Context Pack status must not be updated by the agent during execution.
- Status transitions are performed only by context management scripts or human review.
- The Context Pack must not silently rewrite itself from generated to stale, invalid, or needs_review during task execution.

## 4. Context Pack Body Structure

`templates/context-pack.md` includes:
- # Context Pack
- ## Task Summary
- ## Selected Context
- ## Required Context
- ## Supporting Context
- ## Relevant Rules
- ## Relevant Lessons
- ## Relevant Policies
- ## Out-of-Scope Context
- ## Context Risks
- ## Source Integrity
- ## Non-Authorization Warning
- ## Verification Checklist

## 5. Task Summary

Must include:
- task_id
- goal
- risk_level if available from task contract
- affected_paths if available
- source task path
- task lint status if available

Rule:
- risk_level belongs to task contract and Context Pack, not context-index entries.

## 6. Selected Context

Selected context files must include:
- path
- type
- module
- authority
- context_role
- status
- reason
- must_follow
- source_hash if available
- warnings if any

Mandatory rule:
- Every selected context item must have a reason.
- No reason -> invalid Context Pack.

## 7. Required Context vs Supporting Context

Definitions:
- Required Context: files the agent must consider before planning or verification.
- Supporting Context: files that may help but do not define hard task-relevant obligations.

Rules:
- canonical + required_when_relevant should usually become Required Context when matched
- supporting authority usually becomes Supporting Context unless task relevance is strong
- context authority should not override canonical or supporting authority
- deprecated files should not be selected unless explicitly justified
- exclude_by_default files require explicit reason or review

## 8. Relevant Rules

Each relevant rule must include:
- rule
- source path
- why it matters for this task

Mandatory statement:
- Relevant Rules must be traceable to selected source files.

## 9. Relevant Lessons

Each lesson should include:
- lesson summary
- source path
- repeated-error risk
- required behavior

Rules:
- lessons may inform execution and verification
- lessons do not automatically update canonical rules
- lesson candidates require human review

## 10. Out-of-Scope Context

Should list excluded context with:
- path or category
- reason excluded
- whether manual review is needed

Examples:
- deprecated source
- archived source
- exclude_by_default without explicit task match
- too broad for current task
- unrelated module

## 11. Context Risks

Possible risks:
- no canonical context found
- too many matching candidates
- stale context index
- deprecated context referenced
- selected context has warnings
- task lacks affected_paths
- task scope too broad for confident context selection

## 12. Source Integrity

Must include:
- context_index_path
- context_index_hash
- repo_commit_hash
- selected source_hash values if available
- stale or missing integrity warnings

Mandatory statements:
- Freshness proves alignment with source.
- Freshness does not grant approval.
- Invalid or stale derived context must never be silently upgraded into trusted context.

## 13. Non-Authorization Warning

Context Pack is not approval.
Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.
Context Pack does not replace M27 runtime enforcement.
Context Pack does not replace Human Gate approval.
Freshness check is not approval.
Integrity check is not approval.

## 14. Verification Checklist

- [ ] Selected rules were acknowledged in the plan.
- [ ] Selected policies were not contradicted.
- [ ] Selected lessons were not repeated as mistakes.
- [ ] Out-of-scope context was not touched.
- [ ] Context Pack did not grant approval.
- [ ] Runtime enforcement remained under M27.
- [ ] Any stale or missing context was handled as NEEDS_REVIEW.

## 15. Context Selection Record

`templates/context-selection-record.md` defines a lower-level record with:
- task_id
- task_path
- context_index_path
- context_index_hash
- repo_commit_hash
- candidate_count
- selected_count
- excluded_count
- selected_items
- excluded_items
- warnings
- result

Allowed result values:
- CONTEXT_SELECTED
- CONTEXT_SELECTED_WITH_WARNINGS
- CONTEXT_NEEDS_REVIEW
- CONTEXT_INVALID

Selected item fields:
- path
- score if available
- matched_signals
- reason
- authority
- context_role
- source_hash

Excluded item fields:
- path
- reason
- status
- authority
- context_role

`matched_signals` are matched frontmatter/task signals.
Examples:
- tags
- module
- authority
- context_role
- affected_paths
- applies_to
- excludes
- task keywords

Rules:
- selection records may include score
- score is generated metadata
- score is not authority
- selected reason is required
- selected reason must be human-readable
- matched_signals must be explainable
- matched_signals must not become authority
- score is optional

Unranked selection is valid for M28A if every selected item has a human-readable reason.

## 16. Minimal and Explainable Rule

- Context Pack must prefer fewer high-relevance files.
- Context Pack must not become a mini repository dump.
- If too many files match, selection should return NEEDS_REVIEW rather than silently expanding context.
- Default target size should be 3-5 high-value context items.
- Larger packs require justification.

## 17. Non-Goals

This task does not implement:
- select-context.py
- context ranking algorithm
- Context Pack generation
- context compliance checker
- SQLite cache
- runtime enforcement
- automatic approval
- tutor UX
- state machine
- bypass testing

## Rules

- Keep Markdown/YAML as Semantic Source of Truth.
- Context Pack is generated working context, not semantic authority.
- Context Pack must remain subordinate to source files.
- Context Pack must be minimal and explainable, not exhaustive.
- Every selected context item must have a reason.
- Context Pack status must not be updated by the agent during execution.
- Status transitions are performed only by context management scripts or human review.
- context_index_hash must use sha256:hexdigest format.
- score is optional and must not become authority.
- matched_signals are explainability metadata, not authority.
- Do not implement select-context.py in this task.
- Do not create reports/context-pack.md in this task.
- Do not create SQLite cache in this task.
- Do not modify M27 runtime enforcement logic.
- Do not make Context Pack an approval mechanism.
- No vector DB.
- No embeddings.
- No backend.

## Non-Goals

Do not create:
- scripts/select-context.py
- scripts/check-context-compliance.py
- scripts/build-context-cache.py
- reports/context-pack.md
- .agentos/cache/context.sqlite
- runtime bypass harness
- tutor cards
- state machine validators

Those belong to later M28 tasks or later milestones.
