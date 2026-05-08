---
type: canonical
module: m23
status: draft
authority: canonical
created: 2026-05-06
last_validated: unknown
---

# Scope Compliance Model

## Purpose
Scope compliance defines how AgentOS checks whether actual file changes match the allowed task scope. The check is evidence for review, not approval.

Task scope is not trusted by words.
Task scope is verified against git state.

## Relationship to M22 Guardrails
M22 introduced deterministic validators for document and metadata rules. M23 adds execution control by checking what files were actually changed against declared scope.

## Task Scope Fields
Required scope fields for future contracts:
- `allowed_paths`: path patterns where changes are allowed.
- `forbidden_paths`: path patterns where changes are not allowed.
- `allow_new_files`: boolean permission to create new files.
- `allowed_new_files`: allowed path patterns for new files.
- `forbidden_new_files`: forbidden path patterns for new files.
- `allow_modify_existing`: boolean permission to modify existing files.
- `allow_deletes`: boolean permission to delete files.
- `allow_renames`: boolean permission to rename files.
- `sensitive_paths`: paths that require stricter review.

Definitions:
- `scope violation`: any git-detected change that conflicts with declared scope fields.
- `changed files evidence`: machine-observed file status from git commands.
- `untracked files`: new files not tracked by git.
- `deleted files`: files removed from git tracking.
- `renamed files`: files whose paths changed in git.
- `out-of-scope change`: any added, modified, deleted, or renamed file outside permitted scope.

## Git State Evidence
Future scope checks must compare task contract fields against git evidence:
- `git diff --name-status`
- `git ls-files --others --exclude-standard`

Evidence model must include:
- deleted files
- renamed files
- new files
- modified files

## Changed File Categories
Changed files must be grouped into categories:
- new tracked files
- modified tracked files
- deleted tracked files
- renamed tracked files
- untracked files

Each category is checked against task scope fields.

## Violation Categories
Violation categories:
- path violation (file outside `allowed_paths`)
- forbidden path violation (matches `forbidden_paths`)
- new file violation (`allow_new_files` is false, or file outside `allowed_new_files`, or file in `forbidden_new_files`)
- modify violation (`allow_modify_existing` is false)
- delete violation (`allow_deletes` is false)
- rename violation (`allow_renames` is false)
- sensitive path violation (change touches `sensitive_paths` without explicit allowance)

## Sensitive Paths
`sensitive_paths` lists high-risk locations where extra human review is required. Sensitive path matches should produce at least `WARN`, and may produce `FAIL` if scope explicitly forbids them.

## Human Review Rules
Scope violation requires human review.
FAIL blocks acceptance unless a human explicitly overrides.
NOT_RUN is not PASS.
ERROR requires review.

Result semantics:
- `PASS`: no detected scope violation.
- `FAIL`: at least one scope violation was detected.
- `WARN`: review is recommended but not necessarily blocking.
- `NOT_RUN`: no scope evidence was produced.
- `ERROR`: the check could not complete reliably.

## Allowed vs Forbidden Operations
Allowed operations depend on declared scope fields. Forbidden operations are any operations not explicitly allowed by scope fields.

Examples:
- creating files when `allow_new_files` is false is forbidden.
- creating files outside `allowed_new_files` is forbidden.
- creating files inside `forbidden_new_files` is forbidden.
- modifying existing files when `allow_modify_existing` is false is forbidden.
- deletes when `allow_deletes` is false are forbidden.
- renames when `allow_renames` is false are forbidden.

## Expected Future Validator Behavior
Future scope validator behavior should:
- read task scope fields;
- read git state evidence;
- classify each change by category;
- compare each change to scope rules;
- report `PASS`, `FAIL`, `WARN`, `NOT_RUN`, or `ERROR`;
- print clear file-level reasons.

It must detect violations and provide evidence, but must not approve completion or correctness.

## Non-Authority Boundaries
Unsafe claims that must be rejected:
- scope check approves task completion
- scope check proves correctness
- no violations means implementation is correct
- script can approve out-of-scope changes
- human approval can be inferred from PASS

This model is non-authoritative:
- it does not approve tasks;
- it does not prove correctness;
- it does not decide release readiness;
- it does not replace human review.
