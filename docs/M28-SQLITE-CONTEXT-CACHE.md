# M28 Optional SQLite Context Cache

## Purpose

M28 adds an optional local SQLite cache to speed up lookup.

- Markdown/YAML keeps meaning.
- `data/context-index.json` remains the generated Git-tracked context-selection index.
- SQLite is speed only.

SQLite is not source of truth.
SQLite is optional and rebuildable.
Git stores meaning.
SQLite accelerates lookup.
Cache freshness is not approval.
Cache validity is not approval.
SQLite does not authorize protected actions.
SQLite does not replace M27 runtime enforcement.
SQLite does not replace Human Gate approval.

## Cache Path

Default cache file:

- `.agentos/cache/context.sqlite`

Optional output path:

- `--output <path>` is allowed only inside `.agentos/cache/`

if --output resolves outside .agentos/cache/, the script must return `CONTEXT_CACHE_NEEDS_REVIEW` and must not write.

## Input Source

Primary source:

- `data/context-index.json`

This task reads only the generated index. It does not scan Markdown/YAML directly.

## Result Values and Exit Semantics

- `CONTEXT_CACHE_BUILT` => exit 0
- `CONTEXT_CACHE_OK` => exit 0
- `CONTEXT_CACHE_INVALID` => exit 1
- `CONTEXT_CACHE_STALE` => exit 1
- `CONTEXT_CACHE_SKIPPED` => exit 0
- `CONTEXT_CACHE_NEEDS_REVIEW` => exit 1

`CONTEXT_CACHE_SKIPPED` is valid when the source index is missing or cache usage is intentionally skipped.

## Build Mode

`python3 scripts/build-context-cache.py`

- creates or rebuilds SQLite at `.agentos/cache/context.sqlite`
- source hash uses `sha256:hexdigest`
- stores only repository-relative paths
- rejects absolute paths and `..` path escape

## --check Behavior

`python3 scripts/build-context-cache.py --check`

- read-only validation
- must not create, modify, or repair cache
- validates metadata, tables, hash freshness, counts, and path safety

default `--check`:

- checks `.agentos/cache/context.sqlite`
- missing cache => `CONTEXT_CACHE_INVALID`

If `data/context-index.json` is missing, return `CONTEXT_CACHE_SKIPPED`.

## --check --output Behavior

`python3 scripts/build-context-cache.py --check --output .agentos/cache/context.sqlite`

- checks provided cache path
- still enforces `.agentos/cache/` boundary
- missing explicit cache file => `CONTEXT_CACHE_INVALID`
- outside boundary => `CONTEXT_CACHE_NEEDS_REVIEW`

## --json Behavior

`python3 scripts/build-context-cache.py --json`

returns JSON fields:

- `result`
- `cache_path`
- `source_context_index_path`
- `source_context_index_hash`
- `entry_count`
- `warnings`
- `errors`
- `findings`

## SQLite Schema

Tables:

- `metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL)`
- `context_entries(path TEXT PRIMARY KEY, type TEXT, module TEXT, status TEXT, authority TEXT, context_role TEXT, tags_json TEXT, summary TEXT, source_hash TEXT, indexed_at TEXT)`

Recommended indexes:

- `idx_context_entries_type`
- `idx_context_entries_module`
- `idx_context_entries_status`
- `idx_context_entries_authority`
- `idx_context_entries_context_role`

Required metadata keys:

- `cache_schema_version`
- `source_context_index_path`
- `source_context_index_hash`
- `repo_commit_hash`
- `built_at`
- `generator`
- `sqlite_is_not_source_of_truth`

## Freshness and Hash Rules

Hash format is `sha256:hexdigest`.

`--check` validates:

- cache exists and opens
- required tables exist
- metadata exists
- metadata `source_context_index_hash` equals current index hash
- metadata `repo_commit_hash` equals index `repo_commit_hash`
- entry count equals index entry count
- no absolute or escaping paths stored

Mismatch behavior:

- hash or commit mismatch => `CONTEXT_CACHE_STALE`
- missing metadata/table => `CONTEXT_CACHE_INVALID`

## Zero-Entry Index Behavior

entries: [] is schema-valid but operationally suspicious
entries: \$begin:math:display$\\$end:math:display$ is schema-valid but operationally suspicious

- build may return `CONTEXT_CACHE_BUILT` with warning
- check may return `CONTEXT_CACHE_OK` with warning
- zero-entry cache is never authority

## Absolute Path Behavior

if data/context-index.json contains an entry with an absolute path, build must return `CONTEXT_CACHE_INVALID`.

Also invalid:

- Windows absolute path (`C:\...` / `C:/...`)
- any stored path with `..` that escapes root

## .gitignore Behavior

SQLite cache must be ignored.

Required entries:

- `.agentos/cache/`
- `*.sqlite`
- `*.sqlite3`
- `*.db`

## Authority and Non-Authorization Boundary

SQLite is not source of truth.
SQLite is optional and rebuildable.
SQLite does not grant approval.
SQLite does not authorize commit, push, merge, release, deployment, or protected changes.
SQLite does not replace Markdown/YAML.
SQLite does not replace data/context-index.json.
SQLite does not replace Context Pack.
SQLite does not replace M27 runtime enforcement.
SQLite does not replace Human Gate approval.

## What SQLite Does Not Do

- does not update Markdown/YAML
- does not update `data/context-index.json`
- does not select context by itself in this task
- does not provide approval
- does not require vector DB, embeddings, backend, or remote database
