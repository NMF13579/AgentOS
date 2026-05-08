# M28 Context Layer Audit

## Purpose

M28 context layer audit checks structural readiness of the M28 context-control layer.

Context layer audit is not approval.
Context layer audit does not authorize commit, push, merge, release, deployment, or protected changes.
Context layer audit does not replace M27 runtime enforcement.
Context layer audit does not replace Human Gate approval.
Context layer audit does not run task execution.
Context layer audit does not regenerate context artifacts.
Context layer audit does not require SQLite.

## Audit Result Values and Exit Semantics

- `CONTEXT_LAYER_READY` => exit 0
- `CONTEXT_LAYER_READY_WITH_WARNINGS` => exit 1
- `CONTEXT_LAYER_NOT_READY` => exit 1
- `CONTEXT_LAYER_NEEDS_REVIEW` => exit 1

Detailed result distinction must be read from stdout or `--json` output.
In human-readable mode, the script must print the final result value as the last line of stdout.

## What The Audit Checks

- required M28 artifact list
- required artifact presence rules
- required docs/templates/schema/scripts/index presence
- required non-authorization boundaries
- required result values in contracts
- forbidden authority claim detection
- false-positive protection for negated non-authorization statements
- optional SQLite boundary
- no-write and no-new-files behavior
- JSON output behavior
- fixture behavior

## What The Audit Does Not Check

- It does not execute tasks.
- It does not run M28 scripts.
- It does not regenerate index/context artifacts.
- It does not run tests.
- It does not approve anything.

## Required M28 Artifact List

Required artifacts are considered valid only when each file exists and has non-zero size.

- `docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md`
- `docs/M28-CONTEXT-FRONTMATTER-STANDARD.md`
- `docs/M28-CONTEXT-INDEX-SCHEMA.md`
- `docs/M28-CONTEXT-PACK.md`
- `docs/M28-CONTEXT-REQUIRED.md`
- `docs/M28-CONTEXT-COMPLIANCE.md`
- `docs/M28-CONTEXT-AWARE-VERIFICATION.md`
- `docs/M28-LESSONS-FEEDBACK-LOOP.md`
- `schemas/context-index.schema.json`
- `templates/context-frontmatter-example.md`
- `templates/context-pack.md`
- `templates/context-selection-record.md`
- `templates/context-verification-record.md`
- `templates/lesson-candidate-record.md`
- `scripts/build-context-index.py`
- `scripts/select-context.py`
- `scripts/check-context-required.py`
- `scripts/check-context-compliance.py`
- `data/context-index.json`

## Core vs Non-Critical Architecture Boundary Checks

Core architecture boundary statements:

- `M28 = context control`
- `Markdown/YAML = Semantic Source of Truth`
- `Context Pack is not approval`
- `M28 does not replace M27`
- `Human Gate remains approval authority`

Missing core architecture boundary statements make the layer not ready.

Non-critical architecture boundary statements:

- `SQLite is optional and rebuildable`
- no Vector DB / embeddings / backend required

Missing non-critical explanatory statements produce warnings, not hard failure.

## Source and Authority Boundaries

Generated JSON is operational/index artifact, not semantic authority.
Context Pack is working context, not approval.
Lesson Candidate is proposal, not canonical truth.

## Frontmatter and Context Rules

The audit verifies that frontmatter docs/templates keep these fields visible:

- `type`
- `module`
- `status`
- `authority`
- `tags`
- `context_role`
- `summary`
- `last_validated`

It also verifies:

- no valid context frontmatter → no automatic context selection eligibility
- generated integrity metadata must not be hand-authored as semantic truth
- Context Pack must be minimal and explainable, not exhaustive

## Context Index Schema Checks

Draft-07 check method:

- parse `schemas/context-index.schema.json` as JSON
- check that top-level `$schema` field exists
- `$schema` must contain `draft-07` or `json-schema.org/draft-07`

If schema JSON cannot be parsed, the layer is not ready.

The audit checks for key integrity fields:

- `repo_commit_hash`
- `source_hash`
- `source_index_hash`
- `generated_at`
- `generator_version`
- `entries`

It also checks `additionalProperties: false` where required.

## Script Contract Coverage Checks

The audit checks both text-verifiable and documentation-verifiable requirements.

Text-verifiable checks are checked directly in script text when possible.
Documentation-verifiable checks may be satisfied by M28 docs when wording is not present in script comments/strings.

## Optional SQLite Boundary

SQLite is not source of truth.
SQLite is optional and rebuildable.
Audit must not create SQLite files.

Absence of SQLite cache files does not fail the audit.
Presence of `.sqlite`, `.sqlite3`, or `.db` outside optional cache locations raises review/not-ready findings.

## Forbidden Authority Claim Detection

The audit scans for forbidden authority claims such as:

- Context Pack approves execution
- Context Pack authorizes commit
- Context compliance approves execution
- verification approves protected actions
- M28 replaces M27
- SQLite is source of truth

This uses bounded phrase checks for forbidden authority claim detection.
The audit must not flag non-authorization statements as forbidden authority claims.
Negated safety statements like `does not authorize` must remain valid.

## No-Write Rule

The script is read-only.

- no file modifications
- no file creation
- no context artifact regeneration
- no script chaining into M28 mutating tools

No-write validation must confirm tracked file mtimes stay unchanged and no new files were created in watched directories.

## No-New-Files Rule

The audit must not create output files.
The audit must not create reports.
The audit must not create SQLite files.

## JSON Output Behavior

`--json` returns machine-readable JSON with findings and summary fields.
`--json` output must be valid JSON.

## Fixture Behavior

Each fixture directory must contain README.md or fixture-notes.md.
Each note should include:

- scenario name
- expected audit result
- what differs from ready-minimal

Expected fixture intent:

- ready-minimal => `CONTEXT_LAYER_READY` or `CONTEXT_LAYER_READY_WITH_WARNINGS`
- missing-required-doc => `CONTEXT_LAYER_NOT_READY`
- missing-non-authorization => `CONTEXT_LAYER_NOT_READY`
- forbidden-approval-claim => `CONTEXT_LAYER_NOT_READY`
- invalid-schema-json => `CONTEXT_LAYER_NOT_READY`
- sqlite-artifact-present => `CONTEXT_LAYER_NEEDS_REVIEW` or `CONTEXT_LAYER_NOT_READY`

## Pending Lesson Candidate Token

The audit checks for exact `pending_lesson_candidates` token in lessons feedback docs.
If equivalent wording exists without exact token, warning is acceptable.
If behavior is unclear, needs review is required.

## Known Limitations

- This is structural/document-level audit, not runtime behavior proof.
- Phrase-based checks can miss equivalent wording or flag phrasing drift.
- It does not validate business correctness of task execution.

Audit must not run M28 scripts.
