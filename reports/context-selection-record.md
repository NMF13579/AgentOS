# Context Selection Record

- task_id: task-m22-gate-contract-artifacts
- task_path: tasks/active-task.md
- context_index_path: data/context-index.json
- context_index_hash: sha256:0a636b4ee50b64fbc41cc41427300ba54795928384491d129bcfba312169a288
- repo_commit_hash: 40f70c83a4fad1f2b24e4ec32b98b7dd787860ae
- candidate_count: 1
- selected_count: 1
- excluded_count: 0
- result: CONTEXT_SELECTED

## selected_items

- path: templates/context-frontmatter-example.md
  score: 10
  matched_signals:
    - tags
    - authority
  reason: Matched required runtime/context signals.
  authority: canonical
  context_role: required_when_relevant
  source_hash: sha256:7e8b57a1367aa918ef168c6877efaa94abbf213c2879367f410e9274002a1988

## excluded_items

- none

## warnings

- matched_signals are explainability metadata, not authority.
- score is optional and score is not authority.
