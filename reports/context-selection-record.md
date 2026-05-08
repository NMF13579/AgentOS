# Context Selection Record

- task_id: task-m22-gate-contract-artifacts
- task_path: tasks/active-task.md
- context_index_path: data/context-index.json
- context_index_hash: sha256:1544a23c63d62b91665f24e5a68b0360a64d446489260ab1bf03c2156e16c716
- repo_commit_hash: cb176ae1b346999d28fad36ae61c9aa85d6375dc
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
  reason: canonical authority; required_when_relevant context role; no direct task relevance signal. Final score=6.
  status: canonical
  authority: canonical
  context_role: required_when_relevant

## warnings

- matched_signals are explainability metadata, not authority
- score is optional and score is not authority

- matched_signals are explainability metadata, not authority.
- score is optional and score is not authority.
