# Context Selection Record

- task_id: task-m22-gate-contract-artifacts
- task_path: tasks/active-task.md
- context_index_path: data/context-index.json
- context_index_hash: sha256:0b9135ce4b7dc002c561a06880b7a0e5daac83aa9f85544fb19f57a2c099bea8
- repo_commit_hash: 837e97e8978be93420e436e946b5f311cb388abf
- candidate_count: 1
- selected_count: 0
- excluded_count: 1
- result: CONTEXT_NEEDS_REVIEW

Allowed result values:
- CONTEXT_SELECTED
- CONTEXT_SELECTED_WITH_WARNINGS
- CONTEXT_NEEDS_REVIEW
- CONTEXT_INVALID

## selected_items

- none

## excluded_items

- path: templates/context-frontmatter-example.md
  reason: canonical authority; required_when_relevant context role; conflict with out_of_scope/excludes; no direct task relevance signal. Final score=1.
  status: canonical
  authority: canonical
  context_role: required_when_relevant

## warnings

- matched_signals are explainability metadata, not authority
- score is optional and score is not authority

- matched_signals are explainability metadata, not authority.
- score is optional and score is not authority.
