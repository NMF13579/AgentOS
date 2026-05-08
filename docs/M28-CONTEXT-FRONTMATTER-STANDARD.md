# M28 Context Frontmatter Standard

## 1. Purpose

M28 frontmatter exists to help AgentOS answer:
- what should the agent read?
- why is this file relevant?
- when should this file be selected?
- what authority does this file have?
- what role does this file play in context selection?

Frontmatter enables context selection.
Frontmatter does not grant approval.
Frontmatter does not replace file content.
Frontmatter is metadata over Markdown/YAML source files.

## 2. Source-of-Truth Rule

Markdown/YAML = Semantic Source of Truth.
Frontmatter is part of the source file.
Generated JSON is derived from frontmatter and file metadata.
SQLite is derived from generated JSON/source files.

Generated artifacts may accelerate lookup, but they must remain subordinate to source files.
Frontmatter metadata must not be used to bypass M27.
Frontmatter metadata must not grant approval.

## 3. Compatibility Boundary

M28 context frontmatter extends the general AgentOS frontmatter convention.
It does not replace existing frontmatter rules.
It must not introduce a second authority model.
It must remain compatible with existing AgentOS metadata conventions.

M28 context frontmatter extends AgentOS general frontmatter conventions.

## 4. Eligibility Rule

A file is eligible for automatic context selection only if it has valid M28 context frontmatter.

Files without valid frontmatter may still be used manually, but `select-context.py` should treat them as:
- not indexed
- needs review
- fallback/manual context only

No valid context frontmatter -> no automatic context selection eligibility.

## 5. Required Fields

Required frontmatter fields:

```yaml
---
type: policy
module: runtime-boundary
status: canonical
authority: canonical
created: 2026-05-07
last_validated: 2026-05-07
tags: [m27, runtime, guard, no-direct-execution]
context_role: required_when_relevant
summary: "Defines runtime no-direct-execution boundary."
---
```

Required fields:
- type
- module
- status
- authority
- created
- last_validated
- tags
- context_role
- summary

## 6. Optional Ranking Hints

Optional fields:
- applies_to
- excludes
- owner
- version
- related_tasks
- related_lessons

Example:

```yaml
applies_to:
  - "scripts/runtime/**"
  - "docs/M27-*"

excludes:
  - ".github/workflows/**"
  - "reports/milestone-*"
```

Rules:
- optional ranking hints help context selection
- optional ranking hints are not semantic authority
- missing optional ranking hints must not invalidate otherwise valid frontmatter
- applies_to may improve rank when task affected paths match
- excludes may reduce rank or require review when task affected paths conflict
- optional ranking hints must not grant approval

Missing optional ranking hints must not invalidate otherwise valid frontmatter.

## 7. Allowed Values

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

## 8. Field Meanings

- type: classifies the file kind.
- module: identifies the project area or subsystem.
- status: defines lifecycle state.
- authority: defines how strongly the file should influence context selection.
- created: date when the file was created or introduced into AgentOS.
- last_validated: date when the file content was reviewed for correctness and current relevance. It should not be updated merely because the file was touched or formatting changed.
- tags: machine-readable relevance hints.
- context_role: defines default selection behavior.
- summary: short human-readable explanation used in context selection records.
- applies_to: optional path/module hints that describe where the file is likely relevant.
- excludes: optional path/module hints that describe where the file should not normally apply.
- owner: optional human or team responsible for maintaining the file.
- version: optional version string for stable/canonical documents.
- related_tasks: optional list of related task IDs.
- related_lessons: optional list of related lesson IDs.

## 9. Selection Semantics

Rules:
- canonical authority should rank above supporting authority
- supporting authority should rank above context authority
- deprecated files should not be selected unless explicitly needed
- archived files should not be selected by default
- exclude_by_default files require explicit match or manual review
- exclude_by_default does not mean the file is forbidden to read
- required_when_relevant files should be selected when task tags/module/scope match
- canonical authority + exclude_by_default means the file is not selected automatically, but if explicitly selected or requested for review, it retains canonical authority
- exclude_by_default affects default selection behavior, not file authority
- if a deprecated file is referenced by related_tasks or related_lessons, the reference is informational only and must not automatically restore selection eligibility
- applies_to should increase relevance when task affected paths match
- excludes should reduce relevance or require review when task affected paths conflict
- summary must help explain why the file was selected

exclude_by_default means not selected automatically unless the task explicitly matches or human/manual review requests it. It does not mean the file is forbidden to read.

## 10. Minimal and Explainable Context Rule

Context Pack must be minimal and explainable, not exhaustive.
Frontmatter must help reduce context noise.
Frontmatter must not encourage selecting all files.
If too many files match, selection must prefer fewer high-authority relevant files.

## 11. Integrity Boundary

`source_hash` and `repo_commit_hash` are not manually written by humans in frontmatter.

Future index builders may compute:
- source_hash
- repo_commit_hash
- generated_at
- generator_version

But these belong to generated artifacts, not hand-authored semantic frontmatter.

source_hash is generated metadata.
repo_commit_hash is generated metadata.
generated_at is generated metadata.
generator_version is generated metadata.
Generated integrity metadata must not be manually authored as semantic truth.

## 12. Non-Authorization Warning

Frontmatter is not approval.
Frontmatter does not authorize commit, push, merge, release, deployment, or protected changes.
Fresh metadata does not grant permission.
Valid metadata does not grant permission.
Optional ranking hints do not grant permission.

## Rules

- Keep Markdown/YAML as Semantic Source of Truth.
- M28 frontmatter extends existing AgentOS frontmatter conventions.
- Do not define JSON schema in this task.
- Do not implement `build-context-index.py` in this task.
- Do not implement `select-context.py` in this task.
- Do not create `data/context-index.json` in this task.
- Do not create SQLite files in this task.
- Do not make frontmatter an approval mechanism.
- Do not put generated integrity metadata into hand-authored frontmatter.
- Do not require embeddings, vector DB, backend, or remote database.
- Keep the standard simple and Git-native.

## Non-Goals

Do not create:
- `schemas/context-index.schema.json`
- `scripts/build-context-index.py`
- `scripts/select-context.py`
- `scripts/check-context-compliance.py`
- `scripts/build-context-cache.py`
- `data/context-index.json`
- `.agentos/cache/context.sqlite`

Those belong to later M28 tasks.
