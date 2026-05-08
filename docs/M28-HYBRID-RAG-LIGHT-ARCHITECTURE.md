# M28 Hybrid RAG-Light Architecture

## 1. Purpose

M28 exists to prevent the agent from:
- reading the whole repository by default
- working from memory
- ignoring relevant lessons
- ignoring project rules
- checking only tests while ignoring project policies
- repeating known mistakes
- drifting out of scope

M28 creates a required context step before planning and verification.

## 2. M27 vs M28 Boundary

M27 = runtime enforcement
M28 = context control

- M27 blocks forbidden actions.
- M28 selects required context.
- M28 creates context obligation.
- M28 verifies alignment with selected context.
- M28 does not grant authority.
- M28 does not replace human approval.
- M28 does not bypass M27.
- M28 findings may inform runtime decisions, but do not approve them.

M28 may validate context compliance.
M28 must not become runtime authority.

## 3. Source-of-Truth Model

Markdown/YAML = Semantic Source of Truth.
Generated JSON = Derived Git-tracked Operational Artifact.
SQLite = Derived Runtime Index / Ephemeral Cache.
M27 Runtime = Enforcement Authority.
Human Gate = Approval Authority.

Rules:
- Markdown/YAML stores canonical meaning.
- Generated JSON supports navigation and selection.
- Generated JSON is subordinate to source files.
- JSON must be generated, not manually edited by the agent.
- SQLite is optional and rebuildable.
- SQLite must never become source of truth.
- Integrity checks prove freshness and alignment.
- Integrity checks do not approve execution.

Generated artifacts may accelerate lookup, but they must remain subordinate to source files.
Integrity check is not approval.
Freshness check is not approval.

## 4. General Index vs Context Index

data/index.json
= general repository navigation index

data/context-index.json
= generated M28 task-context selection artifact

Rules:
- neither index is semantic source of truth
- neither index grants approval
- neither index replaces Markdown/YAML source files
- context-index.json must not compete with data/index.json as an authority layer
- context-index.json may be derived from Markdown/YAML frontmatter directly
- context-index.json may also use data/index.json as an input if documented

## 5. Indexing and Integrity

Future generated context indexes must preserve source integrity metadata:
- repo_commit_hash or index_built_from_commit
- source_hash per indexed source file
- generated_at
- generator_version if available

Future SQLite cache implementations must preserve:
- source_path
- source_hash
- indexed_at
- index_commit_hash or repo_commit_hash

Freshness rules:
- if repo_commit_hash is stale, index/cache must be invalid
- if source_hash does not match current source file, record must be invalid
- if critical context is stale, Context Pack must be invalid or NEEDS_REVIEW
- stale cache must not be used for critical context decisions without source verification
- invalid or stale derived context must never be silently upgraded into trusted context

Freshness proves alignment with source.
Freshness does not grant approval.
Stale context must fail closed or require review.
Invalid or stale derived context must never be silently upgraded into trusted context.

## 6. M28 Pipeline

Task Contract
↓
Task Contract Lint
↓
Context Index
↓
Candidate Context Search
↓
Pre-flight Context Pruning
↓
Context Pack
↓
Context-Aware Plan
↓
Context Compliance Check
↓
Execution with Context
↓
Context-Aware Verification
↓
Lesson Candidate if needed
↓
Evidence Report

## 7. Context Pack Definition

Context Pack is a task-specific working context bundle.

It must contain:
- task_id
- goal
- risk_level
- affected_paths if available
- selected context files
- reason for each selected file
- must_follow rules
- relevant lessons
- relevant policies
- out-of-scope context
- context risks
- source integrity metadata if available
- non-authorization warning

Context Pack must be minimal and explainable, not exhaustive.
Context Pack is not approval.
Context Pack does not authorize commit, push, merge, release, deployment, or protected changes.

## 8. M28 Internal Phases

M28A — Context Pack MVP
Goal: generate a small explained Context Pack for a task.

M28B — Context Compliance
Goal: check that plan and verification align with Context Pack.

M28C — Context Layer Hardening
Goal: add freshness checks, negative fixtures, audit, evidence, and completion review.

M28D — Optional SQLite Cache
Goal: speed up local context selection without becoming source of truth.

## 9. Advisory vs Enforcement Boundary

M28 may report:
- Context Pack missing
- Context Pack invalid
- Context Pack stale
- selected context does not match task
- plan contradicts selected rule
- verification does not prove context alignment
- repeated lesson was ignored

M28 must not:
- approve execution
- approve commit
- approve push
- approve merge
- approve release
- approve protected changes
- replace human gate
- bypass M27
- create automatic approval
- treat cache freshness as permission
- silently upgrade stale derived context into trusted context

## 10. Non-Goals

- full RAG platform
- vector DB
- embeddings in first version
- LangGraph
- CrewAI
- backend service
- remote database
- autonomous execution
- memory backend
- automatic approval
- runtime bypass testing
- task state machine
- dry-run-first enforcement
- role separation enforcement
- tutor / human decision cards
- STATUS.md UX
- shadow branches
- git checkpoints

## 11. Success Criteria

M28 is conceptually successful when AgentOS can:
- receive a task
- validate that the task has enough structure for context selection
- select a small relevant Context Pack
- explain why each item was selected
- preserve source integrity metadata
- detect stale context
- plan against selected context
- verify against selected context
- propose a lesson candidate when repeated errors are found

## Rules

- Markdown/YAML remains Semantic Source of Truth.
- Generated JSON is a derived operational artifact, not semantic authority.
- Generated artifacts must remain subordinate to source files.
- SQLite is strictly optional and rebuildable.
- SQLite must be gitignored.
- M28 must not provide a way to bypass M27.
- M28 must not grant approval.
- Integrity check is not approval.
- Freshness check is not approval.
- Invalid or stale derived context must never be silently upgraded into trusted context.
- Context Pack must be minimal and explainable, not exhaustive.
- Keep the architecture simple, Git-native, and zero-config.
- Do not implement scripts in this task.
- Do not create index files in this task.
- Do not create .db files in this task.
- Do not modify M27 runtime enforcement files unless only adding a non-invasive roadmap reference is clearly necessary.
