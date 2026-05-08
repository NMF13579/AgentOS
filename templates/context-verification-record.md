---
type: context-verification-record
task_id: task-example
status: needs_review
generated_by: agent-or-human
generated_at: 2026-05-07T00:00:00Z
context_pack_path: reports/context-pack.md
context_pack_hash: sha256:example
plan_path: reports/plan.md
changed_files_path: reports/changed-files.txt
verification_commands_path: reports/verification-commands.md
repo_commit_hash: example-commit-hash
---

# Context-Aware Verification Record

## Task Summary

- task_id: task-example
- goal: Example goal.
- risk_level: MEDIUM
- source_task_path: tasks/active-task.md
- plan_path: reports/plan.md
- context_pack_path: reports/context-pack.md
- changed_files_path: reports/changed-files.txt

## Context Pack Reference

- context_pack_path: reports/context-pack.md
- context_pack_hash: sha256:example
- repo_commit_hash: example-commit-hash
- context_pack_status: generated
- selected_count: 3
- context_risks:
  - stale context index

## Selected Context Coverage

- path: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
  authority: canonical
  context_role: required_when_relevant
  reason_selected: Matches task module and tags.
  verification_status: followed
  evidence_or_finding: Rule acknowledged in plan and verified in evidence.

## Rules Verification

- rule_summary: M28 must not become runtime authority.
  source_path: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
  verification_status: followed
  evidence: Plan and verification both confirm M27 remained enforcement authority.
  finding: none

## Policies Verification

- policy_summary: No direct push without required controls.
  source_path: docs/NO-DIRECT-PUSH-POLICY.md
  verification_status: followed
  evidence: Changed files review shows no protected push path touched.
  finding: none

## Lessons Verification

- lesson_summary: Avoid scope drift during implementation.
  source_path: lessons/lessons.md
  repeated_error_risk: medium
  required_behavior: Keep changes inside approved scope.
  verification_status: followed
  evidence: Changed files match planned scope.

## Out-of-Scope Verification

- out_of_scope_items:
  - .github/
  - schemas/
- changed_files_reviewed: reports/changed-files.txt
- conflicts_found: []
- verification_status: followed

## Changed Files Review

- state: changed_files_reviewed
- files:
  - reports/context-pack.md
  - reports/context-selection-record.md
- notes: all paths are repository-relative

## Test and Command Evidence

- command: python3 scripts/check-context-compliance.py --context reports/context-pack.md --plan reports/plan.md
  purpose: Verify context alignment after execution.
  result: pass
  evidence_summary: Output indicates context alignment or explicit review status.
  skipped_reason: none

## Context Risks Resolution

- risk: stale context index
  source: Context Pack
  resolution: escalated to review
  status: accepted_for_review

## Non-Authorization Verification

Context-aware verification is not approval.
Context-aware verification does not authorize commit, push, merge, release, deployment, or protected changes.
Context-aware verification does not replace M27 runtime enforcement.
Context-aware verification does not replace Human Gate approval.
Passing verification does not authorize protected actions.
Test success does not authorize protected actions.

## Findings

- severity: info
  category: selected_rule_followed
  message: Selected rule acknowledged and verified.
  source: reports/plan.md
  affected_path: docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md
  result_impact: CONTEXT_VERIFICATION_PASS

- severity: warning
  category: context_pack_integrity_failure
  message: Context pack hash must be revalidated in final run.
  source: reports/context-pack.md
  affected_path: reports/context-pack.md
  result_impact: CONTEXT_VERIFICATION_NEEDS_REVIEW

## Final Verification Result

- final_status: CONTEXT_VERIFICATION_NEEDS_REVIEW
- summary: Core selected context appears followed, but integrity revalidation is pending.
- blocking_findings:
  - context_pack_integrity_failure
- warnings:
  - stale context risk accepted for review
- evidence_summary: Rule, policy, lesson, and out-of-scope checks recorded.
- next_required_action: Re-run with fresh Context Pack hash and final evidence before closure.
