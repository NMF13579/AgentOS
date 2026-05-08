---
type: lesson-candidate
task_id: task-example
status: proposed
created_by: agent-or-human
created_at: 2026-05-07T00:00:00Z
source_context_pack: reports/context-pack.md
source_compliance_report: reports/context-compliance.md
source_verification_record: reports/verification.md
repo_commit_hash: example-commit-hash
review_required: true
related_rule: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
related_policy: docs/NO-DIRECT-PUSH-POLICY.md
related_lesson: lesson-001
affected_module: context-control
affected_paths:
  - reports/context-pack.md
---

# Lesson Candidate Record

## Summary

- task_id: task-example
- title: Missing selected-rule acknowledgement pattern
- affected_module: context-control
- affected_paths:
  - reports/context-pack.md
- severity: medium
- confidence: needs_review
- review_required: true

## Trigger

- primary_trigger_type: context_compliance_needs_review
- source_artifact_path: reports/context-compliance.md
- observed_issue: selected rule acknowledgement repeatedly missing
- result_value: CONTEXT_NEEDS_REVIEW
- finding_category: selected_rule_missing

## Evidence

- source: reports/context-pack.md
  excerpt_or_summary: Selected rules exist but were not acknowledged in plan.
  support_reason: Shows traceable mismatch between selected context and execution planning.
  confidence: medium

- source: reports/verification.md
  excerpt_or_summary: Verification flagged missing context-aware acknowledgement.
  support_reason: Confirms issue recurrence across stages.
  confidence: medium

Note:
- missing evidence means partial evidence exists but is incomplete.
- no evidence means no traceable artifact supports the candidate.

## Repeated Pattern Assessment

- assessment: repeated
- reason: Same issue appeared in multiple task artifacts.
- appeared_in_previous_tasks: yes
- already_covered_by_selected_context: yes
- likely_to_recur: yes
- new_lesson_justified: needs_review

## Existing Context Check

- selected_rules_checked: yes
- selected_policies_checked: yes
- selected_lessons_checked: yes
- architecture_docs_checked: yes
- existing_canonical_lessons_checked: needs_review
- duplicate_candidate_risk: medium
- if_already_covered_action: improve selection failure or acknowledgement failure handling

## Proposed Lesson

- lesson_statement: Always acknowledge selected required rules in plan and verification artifacts.
- short_explanation: Prevent silent drift between selected context and execution behavior.
- scope: context-compliance and verification artifacts
- affected_module: context-control
- when_to_apply: when Context Pack contains required context items
- when_not_to_apply: one_off typo without repeated pattern
- examples:
  - include selected rule path in plan acknowledgement section

Requirement:
- lesson must be directly traceable to evidence.

## Required Behavior

- required_behavior: Explicitly acknowledge each selected required context item in plan and verification.
- forbidden_behavior: Ignoring selected required context while claiming compliance.
- validation_cue: selected_rule_missing finding should not appear in repeated tasks.
- related_context_tags:
  - context
  - compliance
  - verification

## Non-Goals

- does not update canonical rules automatically
- does not modify existing policies automatically
- does not approve execution
- does not authorize commit, push, merge, release, deployment, or protected changes
- does not bypass Human Gate
- does not bypass M27 runtime enforcement

## Human Review Checklist

- [ ] Evidence is sufficient.
- [ ] This is not a duplicate of an existing canonical lesson.
- [ ] Repeated Pattern Assessment confirms pattern is not one_off.
- [ ] Proposed lesson is narrow and actionable.
- [ ] Proposed lesson does not conflict with existing policy.
- [ ] Proposed lesson does not grant approval.
- [ ] Promotion target is identified if accepted.
- [ ] Rejection reason is recorded if rejected.

## Promotion Requirements

- human_review_required: true
- if_accepted:
  - convert candidate to canonical lesson through normal Git review flow
  - update lesson index/frontmatter
  - rebuild context index
  - record evidence in milestone report
- if_rejected:
  - keep status as rejected_by_human by explicit human action only

## Non-Authorization Warning

Lesson Candidate is not approval.
Lesson Candidate does not authorize commit, push, merge, release, deployment, or protected changes.
Lesson Candidate does not update canonical rules automatically.
Lesson Candidate does not replace Human Gate approval.
Lesson Candidate does not replace M27 runtime enforcement.
Human review is required before promotion.

## Final Recommendation

- recommendation: needs_more_evidence
- reason: repeated pattern is likely, but duplicate coverage check requires stronger evidence
- proposed_next_action: review existing canonical lessons and attach direct comparison evidence
- reviewer_needed: human-owner
- final_candidate_status: needs_review
