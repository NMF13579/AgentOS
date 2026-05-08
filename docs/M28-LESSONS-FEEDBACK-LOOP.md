# M28 Lessons Feedback Loop

## 1. Purpose

This feedback loop answers:
- What repeated issue was found?
- Which Context Pack, plan, compliance check, or verification record exposed it?
- Is it a one-off mistake or a recurring pattern?
- What lesson candidate should be proposed?
- What source files or rules might need human review?
- What must not be auto-updated?

- Agent may propose lesson.
- Agent must not auto-update canonical rules.
- Lesson Candidate requires human review.
- Lesson Candidate is not approval.
- Lesson Candidate does not authorize protected actions.

## 2. Source-of-Truth Boundary

- Markdown/YAML source files remain Semantic Source of Truth.
- Existing canonical lessons remain source of truth until changed by human review.
- Lesson Candidate is proposed evidence, not canonical truth.
- Lesson Candidate must remain subordinate to source files.
- Lesson Candidate must not override policies, rules, or architecture documents.

- Proposed lesson is not canonical.
- Proposed lesson does not update context-index by itself.
- Proposed lesson does not update Context Pack by itself.
- Proposed lesson does not grant approval.
- Human review is required before promotion.

## 3. When to Propose a Lesson Candidate

A lesson candidate may be proposed when context compliance or verification identifies:
- repeated mistake pattern
- missing selected rule acknowledgement
- repeated lesson violation
- recurring out-of-scope touch
- stale or missing context recurring across tasks
- ambiguous context selection that caused wrong execution
- recurring policy contradiction
- repeated non-authorization confusion
- repeated command/test evidence omission
- repeated mismatch between plan and verification

Rules:
- one-off errors may be recorded as findings without lesson candidate
- repeated or systemic patterns may become lesson candidates
- uncertain pattern -> needs_review
- lesson candidate must include evidence
- no evidence -> no promotion
- One lesson candidate should cover one distinct issue pattern.
- Do not batch multiple unrelated issues into one candidate.
- If multiple unrelated repeated patterns are found, propose separate candidates or record only the highest-priority candidate and mark the rest as needs_review.
- Secondary repeated patterns not covered in this candidate must be recorded in the milestone evidence report or task evidence report as pending_lesson_candidates.
- Pending lesson candidates are not canonical lessons.
- Pending lesson candidates require future review before promotion or conversion into lesson-candidate records.

## 4. When Not to Propose

Do not propose a lesson candidate for:
- a one-time typo
- a task-specific exception
- a problem already covered by an existing canonical lesson
- a problem already covered by a selected canonical rule
- missing evidence
- speculative improvement without observed failure
- disagreement with M27 runtime enforcement
- request to bypass Human Gate
- request to bypass protected change rules

Mandatory rule:
- Do not create duplicate lessons for already-covered canonical rules.
- Do not create duplicate lessons.

## 5. Lesson Candidate Frontmatter

Required fields:
- type
- task_id
- status
- created_by
- created_at
- review_required
- repo_commit_hash

Optional fields:
- source_context_pack
- source_compliance_report
- source_verification_record
- related_rule
- related_policy
- related_lesson
- affected_module
- affected_paths

Allowed status values:
- proposed
- needs_review
- accepted_by_human
- rejected_by_human
- superseded
- archived

Rules:
- status proposed is the default for agent-created candidates
- agent-created candidates may use only proposed or needs_review
- agent must not set accepted_by_human
- agent must not set rejected_by_human
- agent must not set superseded
- agent must not set archived
- accepted_by_human, rejected_by_human, superseded, and archived require explicit human action
- agent must not promote candidate to canonical lesson
- review_required must be true for agent-created candidates
- repo_commit_hash must be non-empty
- created_at is generated metadata
- generated metadata is not approval

## 6. Body Structure

Required sections:
- # Lesson Candidate Record
- ## Summary
- ## Trigger
- ## Evidence
- ## Repeated Pattern Assessment
- ## Existing Context Check
- ## Proposed Lesson
- ## Required Behavior
- ## Non-Goals
- ## Human Review Checklist
- ## Promotion Requirements
- ## Non-Authorization Warning
- ## Final Recommendation

## 7. Summary

Must include:
- task_id
- short candidate title
- affected module if known
- affected paths if known
- severity
- confidence
- review_required

Allowed severity values:
- low
- medium
- high
- critical

Allowed confidence values:
- low
- medium
- high
- needs_review

Rules:
- confidence high requires concrete evidence
- confidence low or needs_review must not be promoted without human review
- severity is not approval authority

## 8. Trigger

Allowed trigger types:
- context_compliance_violation
- context_compliance_needs_review
- context_verification_fail
- context_verification_needs_review
- repeated_lesson_violation
- out_of_scope_touch
- non_authorization_confusion
- stale_context_recurrence
- missing_context_recurrence
- manual_observation

Each trigger must include:
- source artifact path
- observed issue
- result value if available
- finding category if available

Rules:
- One Lesson Candidate Record should contain exactly one primary trigger.
- If multiple triggers point to the same issue pattern, list one primary trigger and mention supporting triggers in Evidence.
- Do not mix unrelated triggers in one candidate.

## 9. Evidence

Evidence may include:
- Context Pack
- Context Selection Record
- Context Required Check
- Context Compliance Check
- Context-Aware Verification Record
- changed-files evidence
- test/command evidence
- human review note

Each evidence item must include:
- source
- excerpt or summary
- why it supports the lesson candidate
- confidence

Rules:
- evidence must be traceable
- evidence must not be invented
- missing evidence means partial evidence exists but is incomplete
- no evidence means no traceable artifact supports the candidate
- missing evidence -> needs_review
- no evidence -> candidate must not be promoted

## 10. Repeated Pattern Assessment

Must answer:
- Is this a repeated issue?
- Has it appeared in previous tasks?
- Is it already covered by selected context?
- Is it likely to recur?
- Is a new lesson justified?

Allowed assessment values:
- one_off
- repeated
- systemic
- unclear

Rules:
- one_off usually should not become canonical lesson
- unclear requires human review
- repeated or systemic may justify candidate
- assessment must include reason

## 11. Existing Context Check

Check coverage by:
- selected rules
- selected policies
- selected lessons
- architecture docs
- existing canonical lessons

Rules:
- if existing canonical context already covers the issue, propose improving selection or acknowledgement, not duplicate lesson
- if the issue is already covered by a selected canonical lesson and the agent ignored it, the lesson candidate should be about selection failure or acknowledgement failure, not about creating a new rule
- selection failure or acknowledgement failure should be explicitly recorded in this case
- duplicate candidate -> needs_review or rejected_by_human
- missing selected context may justify context selection improvement
- missing canonical lesson may justify new lesson candidate

## 12. Proposed Lesson

Must include:
- lesson statement
- short explanation
- scope
- affected module
- when to apply
- when not to apply
- examples if useful

Rules:
- lesson must be narrow and actionable
- lesson must not restate broad philosophy
- lesson must be directly traceable to evidence in the Trigger and Evidence sections
- if the proposed lesson cannot be traced to evidence, final recommendation must be needs_more_evidence
- lesson must not conflict with existing canonical rules
- lesson must not authorize protected actions
- lesson must not bypass M27

## 13. Required Behavior

Include:
- required behavior
- forbidden behavior
- validation cue
- related context tags if useful

Rules:
- required behavior must be testable or reviewable
- forbidden behavior must be specific
- vague lesson -> needs_review

## 14. Non-Goals

Mandatory non-goals:
- does not update canonical rules automatically
- does not modify existing policies automatically
- does not approve execution
- does not authorize commit, push, merge, release, deployment, or protected changes
- does not bypass Human Gate
- does not bypass M27 runtime enforcement

## 15. Human Review Checklist

- [ ] Evidence is sufficient.
- [ ] This is not a duplicate of an existing canonical lesson.
- [ ] Repeated Pattern Assessment confirms pattern is not one_off.
- [ ] Proposed lesson is narrow and actionable.
- [ ] Proposed lesson does not conflict with existing policy.
- [ ] Proposed lesson does not grant approval.
- [ ] Promotion target is identified if accepted.
- [ ] Rejection reason is recorded if rejected.

## 16. Promotion Requirements

Promotion may include:
- converting candidate into canonical lesson file
- updating lesson index/frontmatter
- rebuilding context index
- rerunning context selection if needed
- recording evidence in milestone report

Rules:
- agent must not promote lesson automatically
- accepted_by_human status requires explicit human action
- canonical lesson updates must be reviewed through normal Git flow
- context-index must be regenerated after canonical lesson change
- SQLite cache, if present later, must be rebuilt after source changes

## 17. Non-Authorization Warning

Required exact block:

Lesson Candidate is not approval.
Lesson Candidate does not authorize commit, push, merge, release, deployment, or protected changes.
Lesson Candidate does not update canonical rules automatically.
Lesson Candidate does not replace Human Gate approval.
Lesson Candidate does not replace M27 runtime enforcement.
Human review is required before promotion.

Rules:
- this block must not be removed
- this block must not be weakened
- lesson candidate must not claim approval
- lesson candidate must not claim automatic promotion

## 18. Final Recommendation

Must include:
- recommendation
- reason
- proposed next action
- reviewer needed
- final candidate status

Allowed recommendation values:
- propose_for_review
- do_not_promote
- merge_with_existing_lesson
- needs_more_evidence

Rules:
- propose_for_review requires evidence
- do_not_promote must explain why
- merge_with_existing_lesson requires a referenced existing lesson
- if the existing lesson is unknown or not identified, use needs_more_evidence instead of merge_with_existing_lesson
- merge_with_existing_lesson must reference existing lesson if known
- needs_more_evidence must specify missing evidence
- if confidence is low, final recommendation must be needs_more_evidence or do_not_promote
- If confidence is low, do not promote automatically.
- if confidence is needs_review, final recommendation must be needs_more_evidence unless a human reviewer explicitly chooses another outcome

## Rules

- Keep Markdown/YAML as Semantic Source of Truth.
- Lesson Candidate is evidence, not authority.
- Agent may propose lesson.
- Agent must not auto-update canonical rules.
- Agent must not promote lessons automatically.
- Agent must not set accepted_by_human.
- Agent must not set rejected_by_human.
- Agent must not set superseded.
- Agent must not set archived.
- Human review is required before promotion.
- Do not implement scripts in this task.
- Do not modify canonical lesson files in this task.
- Do not modify existing policies, rules, or architecture docs in this task.
- Do not modify check-context-compliance.py in this task.
- Do not modify check-context-required.py in this task.
- Do not create SQLite cache in this task.
- Do not modify M27 runtime enforcement logic.
- No vector DB.
- No embeddings.
- No backend.

## Non-Goals

Do not create:
- scripts/update-lessons.py
- scripts/promote-lesson.py
- scripts/check-lesson-candidates.py
- scripts/build-context-cache.py
- .agentos/cache/context.sqlite
- canonical lesson files
- runtime bypass harness
- tutor cards
- state machine validators

Those belong to later M28 tasks or later milestones.
