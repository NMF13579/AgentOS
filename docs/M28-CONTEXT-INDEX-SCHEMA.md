# M28 Context Index Schema

## 1. Purpose

`data/context-index.json` exists to help AgentOS:
- find relevant context files
- filter by type, module, status, authority, tags, and context_role
- support Context Pack construction
- detect stale context
- provide audit coverage for context selection
- avoid reading the whole repository by default

- data/context-index.json is generated.
- data/context-index.json is not Semantic Source of Truth.
- data/context-index.json does not grant approval.
- data/context-index.json must remain subordinate to Markdown/YAML source files.
- Context Pack must be minimal and explainable, not exhaustive.

## 2. Source-of-Truth Boundary

- Markdown/YAML = Semantic Source of Truth.
- Generated JSON = Derived Git-tracked Operational Artifact.
- SQLite = Optional Derived Runtime Cache.

Rules:
- source files define meaning
- frontmatter defines hand-authored context metadata
- data/context-index.json stores generated navigation and integrity metadata
- generated index data must not override source files
- generated index freshness does not grant permission
- index validity does not authorize protected changes

- Generated artifacts may accelerate lookup, but they must remain subordinate to source files.
- Index validity is not approval.
- Freshness check is not approval.

## 3. Relationship to data/index.json

`data/index.json`
= general repository navigation index

`data/context-index.json`
= generated M28 context-selection index

Rules:
- data/context-index.json may be derived from Markdown/YAML frontmatter directly
- data/context-index.json may use data/index.json as an input if documented
- data/context-index.json must not compete with data/index.json as an authority layer
- neither index is Semantic Source of Truth
- neither index grants approval
- both indexes remain subordinate to Markdown/YAML source files

Canonical phrase:
data/context-index.json = generated M28 context-selection index

## 4. Top-Level Schema Fields

Top-level fields:
- schema_version
- generated_at
- generator
- generator_version
- repo_commit_hash
- source_index_path
- source_index_hash
- entries

Field meanings:
- schema_version: version of the context-index schema.
- generated_at: timestamp when the index was generated.
- generator: string name/path of the tool that generated the index. It is not restricted to one hardcoded value.
- generator_version: version of the generator if available.
- repo_commit_hash: Git commit hash the index was built from.
- source_index_path: optional path to source navigation index, usually `data/index.json`.
- source_index_hash: optional hash of `source_index_path` if used.
- entries: array of indexed context records.

## 5. Entry Schema Fields

Required entry fields:
- path
- type
- module
- status
- authority
- created
- last_validated
- tags
- context_role
- summary
- source_hash
- indexed_at

Optional entry fields:
- applies_to
- excludes
- owner
- version
- related_tasks
- related_lessons
- warnings

Clarification:
- risk_level belongs to the task contract and Context Pack, not to source file frontmatter or context-index entry fields.
- risk_level must not be required in data/context-index.json entries.

## 6. Allowed Values

type:
- policy
- spec
- lesson
- decision
- task
- report
- template
- doc
- guide
- architecture

status:
- draft
- active
- canonical
- archived
- deprecated

authority:
- canonical
- supporting
- context

context_role:
- required_when_relevant
- supporting
- optional
- exclude_by_default

## 7. Integrity Metadata

These fields are generated metadata:
- repo_commit_hash
- source_hash
- generated_at
- indexed_at
- generator_version
- source_index_hash

Rules:
- source_hash must represent the indexed source file content
- repo_commit_hash must represent the Git commit used to build the index
- indexed_at must represent when the entry was indexed
- generated_at must represent when the index file was generated
- generated integrity metadata must not be hand-authored as semantic truth
- source_hash and source_index_hash must use the same hash format

Hash format:
- hash values must use the format `algorithm:hexdigest`
- expected algorithm is `sha256`

Examples:
- `sha256:abc123...`
- `sha256:example`

- source_hash is generated metadata.
- repo_commit_hash is generated metadata.
- source_index_hash is generated metadata.
- Invalid or stale derived context must never be silently upgraded into trusted context.
- Stale context must fail closed or require review.

## 8. Freshness Semantics

The index is stale if:
- repo_commit_hash does not match the current repo commit
- any entry source_hash does not match the current source file
- source_index_hash does not match `data/index.json` when source_index_path is used
- required schema fields are missing
- an entry references a missing source file
- a source file is not found at the recorded path
- allowed values are violated
- the schema_version is unsupported

Required edge-case rule:
- If a source file is not found at the recorded path, the entry must be treated as stale regardless of whether a file with matching content exists elsewhere.

Required behavior for future tools:
- stale index must not be used for critical context decisions
- stale index must produce `CONTEXT_INDEX_STALE` or `CONTEXT_INDEX_INVALID`
- stale context must require regeneration or review
- stale context must fail closed or require review
- freshness does not grant approval

- Stale context must fail closed or require review.
- Freshness check is not approval.
- Invalid or stale derived context must never be silently upgraded into trusted context.

## 9. Minimal and Explainable Context Rule

The index must support minimal and explainable Context Pack construction.

Rules:
- index entries should contain enough metadata to explain why a file was selected
- summary must be preserved from source frontmatter
- tags, module, authority, context_role, applies_to, and excludes should support ranking
- the index must not encourage selecting all files
- Context Pack must be minimal and explainable, not exhaustive

## 10. Non-Authorization Warning

- data/context-index.json is not approval.
- A fresh context index is not approval.
- A valid context index is not approval.
- Index validity is not approval.
- Freshness check is not approval.
- The index does not authorize commit, push, merge, release, deployment, or protected changes.

## 11. JSON Schema Requirements

The schema file is:
- `schemas/context-index.schema.json`

The schema uses:
- JSON Schema draft-07
- `$schema: http://json-schema.org/draft-07/schema#`
- required top-level metadata fields
- required `entries` array
- required entry fields
- enforced allowed values for `type`, `status`, `authority`, `context_role`
- optional ranking hint fields
- `additionalProperties: false` on the top-level object
- `additionalProperties: false` on each entry object
- string arrays for `tags`, `applies_to`, `excludes`, `related_tasks`, `related_lessons`, `warnings`
- non-hardcoded `generator`
- no `risk_level` in entries

Unknown fields are rejected unless a future schema version explicitly adds them.
Future fields are added through schema version updates, not arbitrary `additionalProperties`.

## 12. Example Shape

```json
{
  "schema_version": "1.0.0",
  "generated_at": "2026-05-07T00:00:00Z",
  "generator": "scripts/build-context-index.py",
  "generator_version": "0.1.0",
  "repo_commit_hash": "example-commit-hash",
  "source_index_path": "data/index.json",
  "source_index_hash": "sha256:example",
  "entries": [
    {
      "path": "docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md",
      "type": "architecture",
      "module": "context-control",
      "status": "canonical",
      "authority": "canonical",
      "created": "2026-05-07",
      "last_validated": "2026-05-07",
      "tags": ["m28", "context", "architecture"],
      "context_role": "required_when_relevant",
      "summary": "Defines M28 context control architecture.",
      "applies_to": ["docs/M28-*"],
      "excludes": [],
      "source_hash": "sha256:example",
      "indexed_at": "2026-05-07T00:00:00Z"
    }
  ]
}
```

## Rules

- Keep Markdown/YAML as Semantic Source of Truth.
- Generated JSON is a derived operational artifact, not semantic authority.
- Use JSON Schema draft-07.
- Use additionalProperties: false at top-level and entry-level.
- Use sha256 hash format as algorithm:hexdigest.
- Do not implement build-context-index.py in this task.
- Do not implement select-context.py in this task.
- Do not create data/context-index.json in this task.
- Do not create SQLite files in this task.
- Do not make index validity an approval mechanism.
- Do not make freshness an approval mechanism.
- Do not require embeddings, vector DB, backend, or remote database.
- Keep the schema simple and Git-native.

## Non-Goals

Do not create:
- scripts/build-context-index.py
- scripts/select-context.py
- scripts/check-context-compliance.py
- scripts/build-context-cache.py
- data/context-index.json
- .agentos/cache/context.sqlite
- runtime bypass harness
- tutor cards
- state machine validators

Those belong to later M28 tasks or later milestones.
