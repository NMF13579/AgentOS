# Context Selection Record

- task_id: task-example
- task_path: tasks/active-task.md
- context_index_path: data/context-index.json
- context_index_hash: sha256:example
- repo_commit_hash: example-commit-hash
- candidate_count: 10
- selected_count: 3
- excluded_count: 7
- result: CONTEXT_SELECTED

Allowed result values:
- CONTEXT_SELECTED
- CONTEXT_SELECTED_WITH_WARNINGS
- CONTEXT_NEEDS_REVIEW
- CONTEXT_INVALID

## selected_items

- path: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
  score: 0.95
  matched_signals:
    - tags
    - module
    - authority
    - context_role
    - task keywords
  reason: Directly defines M28 boundary rules required by this task.
  authority: canonical
  context_role: required_when_relevant
  source_hash: sha256:example

- path: docs/M28-CONTEXT-FRONTMATTER-STANDARD.md
  matched_signals:
    - tags
    - applies_to
  reason: Defines frontmatter constraints used by context metadata.
  authority: canonical
  context_role: supporting
  source_hash: sha256:example

## excluded_items

- path: docs/legacy-archive.md
  reason: archived source, not required for current task
  status: archived
  authority: context
  context_role: exclude_by_default

- path: docs/unrelated-module.md
  reason: unrelated module
  status: active
  authority: supporting
  context_role: optional

## warnings

- score is optional for M28A; unranked selection is valid if every selected item has a human-readable reason.
- matched_signals are explainability metadata, not authority.
- score is generated metadata and is not authority.
