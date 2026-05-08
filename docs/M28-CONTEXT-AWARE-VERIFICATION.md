# M28 Context-Aware Verification

## 1. Purpose

Context-aware verification answers:
- Were selected rules followed?
- Were selected policies respected?
- Were selected lessons not repeated as mistakes?
- Was out-of-scope context avoided?
- Did the result avoid treating Context Pack as approval?
- Did M27 remain the enforcement authority?
- Was test/command evidence recorded?
- Were context risks resolved or marked NEEDS_REVIEW?

- Context-aware verification checks alignment with selected context.
- Context-aware verification does not replace tests.
- Context-aware verification does not replace M27 runtime enforcement.
- Context-aware verification does not replace Human Gate approval.
- Context-aware verification is not approval.

## 2. Source-of-Truth Boundary

- Markdown/YAML source files remain Semantic Source of Truth.
- data/context-index.json is generated context-selection index.
- reports/context-pack.md is generated task-specific working context.
- reports/verification.md is generated/filled verification evidence.
- Verification must remain subordinate to source files and Context Pack.
- Verification must not override source files.
- Verification must not grant permission.

- Verification evidence does not grant approval.
- Passing verification does not authorize protected actions.
- Freshness check is not approval.
- Integrity check is not approval.

## 3. Verification Record Frontmatter

Required fields:
- type
- task_id
- status
- generated_by
- generated_at
- context_pack_path
- context_pack_hash
- repo_commit_hash

Optional fields:
- plan_path
- changed_files_path
- verification_commands_path

`verification_commands_path`: optional path to a file listing verification commands, command results, and evidence summaries if command evidence is recorded separately.

Allowed status values:
- pass
- pass_with_warnings
- fail
- needs_review

Rules:
- type must be context-verification-record
- status is a verification result, not approval
- generated_at is generated metadata
- context_pack_hash must use sha256:hexdigest
- context_pack_hash is generated metadata
- repo_commit_hash must be non-empty
- generated metadata must not be hand-authored as semantic truth

Frontmatter status must reflect Final Verification Result final_status.

Mapping:
- status: pass ↔ CONTEXT_VERIFICATION_PASS
- status: pass_with_warnings ↔ CONTEXT_VERIFICATION_PASS_WITH_WARNINGS
- status: fail ↔ CONTEXT_VERIFICATION_FAIL
- status: needs_review ↔ CONTEXT_VERIFICATION_NEEDS_REVIEW

If frontmatter status and final_status conflict, the verification record must be treated as needs_review.

## 4. Body Structure

Required sections:
- # Context-Aware Verification Record
- ## Task Summary
- ## Context Pack Reference
- ## Selected Context Coverage
- ## Rules Verification
- ## Policies Verification
- ## Lessons Verification
- ## Out-of-Scope Verification
- ## Changed Files Review
- ## Test and Command Evidence
- ## Context Risks Resolution
- ## Non-Authorization Verification
- ## Findings
- ## Final Verification Result

## 5. Task Summary

Must include:
- task_id
- goal
- risk_level if available
- source task path
- plan path if available
- context pack path
- changed files path if available

Rules:
- risk_level belongs to task contract and verification record, not context-index entries.
- risk_level in verification record refers to task risk from the task contract.
- It must not be confused with document-level metadata or future context-index metadata.

## 6. Context Pack Reference

Must include:
- context_pack_path
- context_pack_hash
- repo_commit_hash
- Context Pack status if available
- selected_count if available
- context risks if available

Rules:
- missing Context Pack reference -> needs_review
- stale Context Pack reference -> needs_review
- invalid Context Pack reference -> fail or needs_review depending on certainty
- Context Pack reference is not approval
- if context_pack_hash does not match the current sha256 hash of context_pack_path at verification time, status must be fail
- confirmed context_pack_hash mismatch -> fail
- if context_pack_path does not resolve to an existing file, status must be needs_review
- Context Pack hash mismatch must not be silently treated as pass

## 7. Selected Context Coverage

Each selected item should include:
- path
- authority
- context_role
- reason selected
- verification status
- evidence or finding

Allowed verification status:
- followed
- not_followed
- not_applicable
- needs_review

Rules:
- every selected required context item must be addressed
- silence about selected required context is not verification
- missing coverage for selected required context -> needs_review
- direct contradiction -> fail
- not_applicable requires explicit justification
- a selected required context item must not be marked not_applicable without explaining why it does not apply to this task result
- unjustified not_applicable -> needs_review

## 8. Rules Verification

Each rule item must include:
- rule summary
- source path
- verification status
- evidence
- finding if any

Rules:
- selected rules must be acknowledged
- selected rules must not be contradicted
- pass requires evidence
- no evidence -> needs_review
- contradiction -> fail

## 9. Policies Verification

Each policy item must include:
- policy summary
- source path
- verification status
- evidence
- finding if any

Rules:
- selected policies must be acknowledged
- selected policies must not be contradicted
- pass requires evidence
- no evidence -> needs_review
- contradiction -> fail

## 10. Lessons Verification

Each lesson item must include:
- lesson summary
- source path
- repeated-error risk
- required behavior
- verification status
- evidence

Rules:
- if Relevant Lessons section is non-empty, lessons must be acknowledged
- lesson repeated as mistake -> fail
- lesson not addressed -> needs_review
- lessons do not automatically update canonical rules
- lesson candidates require human review

## 11. Out-of-Scope Verification

Must include:
- listed out-of-scope paths or categories
- changed files reviewed
- conflicts found
- verification status

Rules:
- changed files must be repository-relative
- POSIX absolute paths are invalid
- Windows absolute paths are invalid
- paths must not escape repo root using ..
- out-of-scope touched -> fail
- unclear changed-files evidence -> needs_review

## 12. Changed Files Review

Allowed states:
- changed_files_reviewed
- no_changes_claimed
- changed_files_missing
- needs_review

Rules:
- if plan or verification claims changes were made, changed files should be listed
- empty changed-files is allowed only if no changes were made
- if changes are claimed but changed-files is empty or missing -> needs_review
- changed-files review does not authorize commit or push

## 13. Test and Command Evidence

Each command evidence item must include:
- command
- purpose
- result
- evidence summary
- skipped reason if not run

Allowed result values:
- pass
- fail
- skipped
- needs_review

Rules:
- skipped commands must explain why
- failing commands must make final status fail or needs_review
- command success does not override context violation
- tests do not replace context-aware verification
- context-aware verification does not replace tests

## 14. Context Risks Resolution

Each risk item must include:
- risk
- source
- resolution
- status

Allowed risk status:
- resolved
- accepted_for_review
- unresolved
- needs_review

Rules:
- unresolved critical context risk -> needs_review or fail
- stale context risk -> needs_review
- missing canonical context risk -> needs_review
- risk silently ignored -> needs_review

## 15. Non-Authorization Verification

Required exact block:

Context-aware verification is not approval.
Context-aware verification does not authorize commit, push, merge, release, deployment, or protected changes.
Context-aware verification does not replace M27 runtime enforcement.
Context-aware verification does not replace Human Gate approval.
Passing verification does not authorize protected actions.
Test success does not authorize protected actions.

Rules:
- this block must not be removed
- this block must not be weakened
- verification must not claim approval
- verification must not claim commit/push/merge/release/deploy authorization

## 16. Findings

Each finding should include:
- severity
- category
- message
- source
- affected_path if applicable
- result impact

Allowed severity:
- info
- warning
- violation
- needs_review

Suggested categories:
- selected_rule_followed
- selected_rule_missing
- selected_rule_contradicted
- selected_policy_followed
- selected_policy_missing
- selected_policy_contradicted
- lesson_acknowledged
- lesson_repeated
- out_of_scope_clean
- out_of_scope_touched
- command_failed
- command_skipped
- stale_context
- missing_context
- context_pack_integrity_failure
- non_authorization_verified
- non_authorization_violation

## 17. Final Verification Result

Must include:
- final_status
- summary
- blocking_findings
- warnings
- evidence_summary
- next_required_action

Allowed final_status values:
- CONTEXT_VERIFICATION_PASS
- CONTEXT_VERIFICATION_PASS_WITH_WARNINGS
- CONTEXT_VERIFICATION_FAIL
- CONTEXT_VERIFICATION_NEEDS_REVIEW

Rules:
- PASS requires selected context coverage and evidence
- PASS_WITH_WARNINGS requires no violations but unresolved warnings
- FAIL requires explicit contradiction, out-of-scope touch, repeated prohibited lesson, confirmed context_pack_hash mismatch, or failed mandatory verification
- NEEDS_REVIEW is required when evidence is incomplete or parsing is uncertain
- verification must prefer NEEDS_REVIEW over false PASS
- verification must not infer compliance from silence
- frontmatter status must reflect final_status
- if frontmatter status and final_status conflict, the record must be treated as needs_review

Status mapping:
- status: pass ↔ CONTEXT_VERIFICATION_PASS
- status: pass_with_warnings ↔ CONTEXT_VERIFICATION_PASS_WITH_WARNINGS
- status: fail ↔ CONTEXT_VERIFICATION_FAIL
- status: needs_review ↔ CONTEXT_VERIFICATION_NEEDS_REVIEW

## 18. Non-Goals

This task does not implement:
- verification checker script
- compliance checker changes
- SQLite cache
- runtime enforcement
- automatic approval
- CI enforcement
- tutor UX
- state machine
- bypass testing

This task does not implement runtime or approval authority changes.

## Rules

- Keep Markdown/YAML as Semantic Source of Truth.
- Context-aware verification is evidence, not authority.
- Verification status is not approval.
- Passing verification does not authorize protected actions.
- Do not implement a new script in this task.
- Do not modify check-context-compliance.py in this task.
- Do not run tests in this task.
- Do not create reports/verification.md in this task unless explicitly needed as a demo artifact.
- Do not modify M27 runtime enforcement logic.
- Do not integrate this template into existing check scripts in this task.
- No vector DB.
- No embeddings.
- No backend.

## Non-Goals

Do not create:
- scripts/check-context-verification.py
- scripts/build-context-cache.py
- .agentos/cache/context.sqlite
- runtime bypass harness
- tutor cards
- state machine validators

Those belong to later M28 tasks or later milestones.
