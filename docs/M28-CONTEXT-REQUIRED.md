# M28 Context Required Check

## Purpose

This check validates Context Pack availability and structure.
This check does not validate whether a plan follows the Context Pack.
Context compliance belongs to a later task.

No valid Context Pack → No Context-Compliant Execution.

## Result Values and Exit Semantics

- CONTEXT_REQUIRED_OK -> exit 0
- CONTEXT_REQUIRED_MISSING -> exit 1
- CONTEXT_REQUIRED_INVALID -> exit 1
- CONTEXT_REQUIRED_NEEDS_REVIEW -> exit 1

## What This Script Checks

- Context Pack file exists and is readable.
- Required frontmatter fields and allowed status values.
- Task linkage by task_id extraction and matching.
- Required body section presence.
- Selected context reason and path safety checks.
- Source integrity checks for hashes and referenced files.
- Non-authorization block presence and order.
- Verification checklist concept coverage.
- Optional selection record consistency checks.

## What This Script Does Not Check

- It does not check plan-to-context compliance.
- It does not validate execution behavior.
- It does not regenerate Context Pack.
- It does not call select-context.py.

## Missing Artifact Behavior

- Missing task file -> CONTEXT_REQUIRED_MISSING
- Missing Context Pack -> CONTEXT_REQUIRED_MISSING
- Missing selection record when --selection is provided -> CONTEXT_REQUIRED_MISSING

No valid Context Pack → No Context-Compliant Execution.

## Invalid / Stale / Needs Review Behavior

- status=stale -> CONTEXT_REQUIRED_NEEDS_REVIEW
- status=invalid -> CONTEXT_REQUIRED_INVALID
- status=needs_review -> CONTEXT_REQUIRED_NEEDS_REVIEW
- missing required structure -> CONTEXT_REQUIRED_INVALID
- unverifiable freshness (for example git unavailable) -> CONTEXT_REQUIRED_NEEDS_REVIEW

Freshness proves alignment with source.
Freshness does not grant approval.
Integrity check is not approval.
Invalid or stale derived context must never be silently upgraded into trusted context.

## Non-Authorization Boundary

Context Pack is not approval.
Context Selection Record is not approval.
Valid Context Pack is not approval.

## No-Write Rule

- The script only validates existing artifacts.
- The script does not modify files.
- The script does not regenerate Context Pack.

## Task ID Extraction Behavior

Extraction order:
1. frontmatter field task_id
2. frontmatter field task.id
3. markdown line Task ID:
4. allowed heading patterns:
- Task <task_id>
- <task_id> —
- <task_id> -

If extraction fails: warning "task_id could not be extracted" and CONTEXT_REQUIRED_NEEDS_REVIEW.

## Non-Authorization Block Matching Behavior

The non-authorization block must be present as continuous text.
The six required sentences must appear in order.
At most two blank lines may exist between required sentences.
More than two blank lines between required sentences must fail the block check.

## Verification Checklist Matching Behavior

Verification Checklist checks may be validated by required concept presence.
Required concepts:
- selected rules
- selected policies
- selected lessons
- out-of-scope
- approval
- M27 or runtime enforcement
- stale or missing context / NEEDS_REVIEW

## Source Integrity Classification Behavior

- if a selected source file exists but its source_hash does not match -> CONTEXT_REQUIRED_NEEDS_REVIEW
- if a selected source file is missing at the recorded path -> CONTEXT_REQUIRED_INVALID
- if context_index_path target is missing -> CONTEXT_REQUIRED_INVALID
- if context_index_hash mismatches current index file -> CONTEXT_REQUIRED_NEEDS_REVIEW
- if git is unavailable for repo_commit_hash freshness check -> CONTEXT_REQUIRED_NEEDS_REVIEW
- source_hash without sha256: prefix is invalid

## Absolute Path Rejection Behavior

Absolute path detection must reject both POSIX and Windows-style absolute paths.
Examples:
- /home/user/repo/docs/file.md
- C:\repo\docs\file.md
- C:/repo/docs/file.md

## --root Path Resolution Behavior

--root sets the base repository path for resolving relative artifact paths.
Relative --task, --context, and --selection are resolved from root.
Absolute stored selected paths are still rejected.

## Section Matching Rule

Section presence must be checked by exact Markdown heading match.

## Selection Record Optional Behavior

- If --selection is omitted, selection record is not checked.
- If --selection is provided, failures affect final result.
- CONTEXT_SELECTED_WITH_WARNINGS must return CONTEXT_REQUIRED_NEEDS_REVIEW.

## Additional Rules

- No reason → invalid Context Pack.
- Do not modify existing readiness, validation, or enforcement scripts.
