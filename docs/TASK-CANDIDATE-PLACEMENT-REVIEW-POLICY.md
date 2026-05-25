---
type: policy
milestone: M53
task: 53.4
title: Task Candidate Placement Review Policy
status: draft
authority: canonical
created_for: M53
depends_on:
  - reports/m52-completion-review.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-ARCHITECTURE.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-INPUT-CONTRACT.md
  - docs/TASK-CANDIDATE-PLACEMENT-REVIEW-OUTPUT-CONTRACT.md
input_schema:
  - schemas/task-candidate-placement-review-input.schema.json
result_schema:
  - schemas/task-candidate-placement-review-result.schema.json
---

## 1. Metadata

This policy defines canonical decision rules for M53 task 53.4.

## 2. Purpose

The placement review policy defines how M53 decides whether an M52-validated candidate is eligible for future controlled placement consideration.

- M53 policy governs placement eligibility review only
- M53 policy does not perform placement
- M53 policy does not approve execution
- M53 policy does not authorize queue creation
- M53 policy does not authorize active-task replacement
- M53 policy does not authorize M54 materialization

## 3. Non-Authority Boundary

M53 placement review policy is not approval.
M53 placement review policy does not authorize execution.
M53 placement review policy does not authorize queue placement.
M53 placement review policy does not authorize active-task replacement.
M53 placement review policy does not authorize lifecycle mutation.
M53 placement review policy does not authorize M54 materialization.

## 4. Acceptable M53 Source Artifacts

```yaml
acceptable_source_artifacts:
  canonical_m52_completion_review:
    path: reports/m52-completion-review.md
    required: true
  m52_candidate_validation_result:
    required: true
  m52_evidence_report:
    required: true
  m52_integration_report:
    required: true
  generated_candidate_artifact:
    required: true
  placement_review_input:
    required_for_input_mode: true
```

- source artifacts must exist before eligibility can be claimed
- source artifacts must be reported, not inferred
- missing required source artifacts block review
- non-canonical M52 completion review paths are invalid
- legacy M52 reports cannot replace reports/m52-completion-review.md

## 5. Canonical M52 Completion Dependency

M53 canonical M52 completion dependency is reports/m52-completion-review.md.

```yaml
source_m52_completion_review: reports/m52-completion-review.md
```

- M53 may proceed only if reports/m52-completion-review.md exists
- M53 may proceed only if m53_handoff_ready is true
- M53 may proceed only if M52 final_status allows handoff
- M53 must stop if M52 is incomplete or blocked
- M53 must carry forward M52 limitations if M52 completed with limitations

## 6. Acceptable M52 Completion Statuses

```yaml
acceptable_m52_final_status:
  - M52_CANDIDATE_VALIDATION_LAYER_COMPLETE
  - M52_CANDIDATE_VALIDATION_LAYER_COMPLETE_WITH_LIMITATIONS

blocking_m52_final_status:
  - M52_INCOMPLETE
  - M52_BLOCKED
```

Rules:
- If final_status is M52_CANDIDATE_VALIDATION_LAYER_COMPLETE:
  - M53 may review eligibility
  - M53 must still preserve non-authority boundaries
- If final_status is M52_CANDIDATE_VALIDATION_LAYER_COMPLETE_WITH_LIMITATIONS:
  - M53 may review eligibility only with limitations carried forward
  - M53 result may be PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS
- If final_status is M52_INCOMPLETE:
  - M53 review must be PLACEMENT_REVIEW_BLOCKED
- If final_status is M52_BLOCKED:
  - M53 review must be PLACEMENT_REVIEW_BLOCKED

## 7. Acceptable M52 Evidence Statuses

Evidence is acceptable only if it confirms candidate validation without authority escalation.

Required evidence properties:
- M52 candidate validation result exists
- M52 evidence report exists
- M52 integration report exists
- generated candidate artifact exists
- validation outcome is preserved
- candidate source is preserved
- limitations are preserved
- non-authority boundaries are preserved

M52 evidence may support M53 eligibility review, but M52 evidence does not authorize placement.

## 8. Placement Eligibility Criteria

A candidate may be considered placement-eligible only if all of these are true:
- canonical M52 completion review exists
- m53_handoff_ready is true
- M52 final_status is acceptable
- M52 candidate validation result exists
- M52 evidence report exists
- M52 integration report exists
- generated candidate artifact exists
- source candidate id is present
- source candidate origin is known
- M50/M51/M52 traceability is preserved
- required carry-forward fields are preserved
- boundary flags are safe
- no queue placement has occurred
- no active-task replacement has occurred
- no approval record has been created by M53
- no execution authorization is claimed
- no lifecycle mutation is claimed
- no M54 materialization authorization is claimed
- forbidden changes are not weakened
- allowed changes are not expanded

Placement eligibility is a classification, not a materialization action.

## 9. Queue Materialization Input Eligibility Criteria

```yaml
eligible_as_m54_queue_materialization_input: true | false
```

A candidate may be marked eligible as an M54 queue materialization input only if:
- placement eligibility criteria are satisfied
- placement target allows queue candidate review
- candidate shape is compatible with queue materialization input
- no queue entry currently exists as an M53 output
- M53 result preserves M54 independent validation boundary

eligible_as_m54_queue_materialization_input: true does not authorize queue placement.

- M54 must independently validate queue materialization
- M53 cannot create tasks/queue/*.md
- M53 cannot trigger M54 automatically

## 10. Active-Task Proposal Input Eligibility Criteria

```yaml
eligible_as_m54_active_task_proposal_input: true | false
```

A candidate may be marked eligible as an M54 active-task proposal input only if:
- placement eligibility criteria are satisfied
- placement target allows active-task proposal review
- candidate shape is compatible with active-task proposal input
- no active-task replacement occurred
- M53 result preserves M54 independent validation boundary

eligible_as_m54_active_task_proposal_input: true does not authorize active-task replacement.

- M54 must independently validate active-task proposal materialization
- M53 cannot replace tasks/active-task.md
- M53 cannot trigger M54 automatically

## 11. Result Decision Rules

```yaml
PLACEMENT_REVIEW_ELIGIBLE:
  exit_code: 0
  meaning: eligible as future M54 input candidate without blocking limitations

PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS:
  exit_code: 0
  meaning: eligible as future M54 input candidate only with limitations preserved

PLACEMENT_REVIEW_NOT_ELIGIBLE:
  exit_code: 1
  meaning: reviewed but not eligible for downstream placement consideration

PLACEMENT_REVIEW_BLOCKED:
  exit_code: 2
  meaning: review could not safely complete
```

- PLACEMENT_REVIEW_ELIGIBLE may be used only when no carry-forward limitation affects eligibility
- PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS must be used when eligibility exists but M52 limitations, warnings, open questions, downstream limits, or known gaps remain relevant
- PLACEMENT_REVIEW_NOT_ELIGIBLE must be used when review completes and the candidate fails eligibility criteria
- PLACEMENT_REVIEW_BLOCKED must be used when required source artifacts, traceability, boundaries, or dependencies are missing or unsafe

Exit code 0 does not authorize queue placement, active-task replacement, execution, lifecycle mutation, or M54 materialization.

## 12. Blocking Conditions

- M52 completion review missing
- M52 completion review not at reports/m52-completion-review.md
- M52 completion review does not set m53_handoff_ready: true
- M52 final_status is M52_INCOMPLETE
- M52 final_status is M52_BLOCKED
- M52 final_status is unknown
- M52 validation result missing
- M52 evidence report missing
- M52 integration report missing
- generated candidate artifact missing
- placement review input missing when input mode is used
- source_candidate_id missing
- source_candidate_origin unknown
- required_traceability missing
- required_carry_forward missing
- boundary flags missing
- review_only not true
- queue_write_allowed not false
- active_task_write_allowed not false
- execution_authorized not false
- approval_record_creation_allowed not false
- lifecycle_mutation_allowed not false
- m54_materialization_authorized not false
- M53 input claims execution authorization
- M53 input claims queue placement already performed
- M53 input claims active-task replacement already performed
- M53 input claims approval already created
- M53 input claims M54 materialization authorization
- M53 input drops accepted limitations
- M53 input drops warnings
- M53 input drops open questions
- M53 input drops downstream limits
- M53 input drops known gaps
- M53 input weakens forbidden changes
- M53 input expands allowed changes

Any blocking condition must produce PLACEMENT_REVIEW_BLOCKED.

## 13. Not-Eligible Conditions

- candidate shape incompatible with requested placement target
- source candidate is valid but not suitable for queue materialization input
- source candidate is valid but not suitable for active-task proposal input
- traceability exists but indicates wrong candidate lineage
- candidate is already superseded by a newer valid candidate
- candidate does not satisfy placement target criteria
- dual target requested without explicit dual eligibility review
- candidate cannot preserve required downstream limits
- candidate would require expanding allowed changes
- candidate would require weakening forbidden changes

PLACEMENT_REVIEW_NOT_ELIGIBLE means the review completed; it does not authorize any corrective action.

## 14. Limitations Conditions

Conditions that require PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS instead of PLACEMENT_REVIEW_ELIGIBLE:
- M52 final_status is M52_CANDIDATE_VALIDATION_LAYER_COMPLETE_WITH_LIMITATIONS
- accepted limitations are present
- warnings are present
- open questions are present
- downstream limits are present
- known gaps are present
- eligibility depends on preserving specific non-authority boundaries
- M54 must receive explicit carry-forward notes

Limitations must be carried forward; they must not be converted into clean eligibility.

## 15. Traceability Requirements

M53 policy must require traceability to:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- m50_traceability
- m51_generator_evidence
- m52_validation_evidence

M53 policy must not allow placement eligibility with broken M50/M51/M52 provenance.

## 16. Carry-Forward Requirements

M53 policy must require carry-forward of:
- accepted_limitations
- warnings
- open_questions
- downstream_limits
- known_gaps
- non_authority_boundary

M53 policy must not allow silent loss of accepted limitations, warnings, open questions, downstream limits, or known gaps.

## 17. Forbidden Authority Claims

Forbidden claims:
- M53 approved the candidate
- M53 authorized execution
- M53 created a queue entry
- M53 replaced active-task.md
- M53 created approval record
- M53 authorized lifecycle mutation
- M53 authorized M54 materialization
- M53 started M54
- M53 result is sufficient for queue placement
- M53 result is sufficient for active-task replacement
- M53 result is sufficient for execution
- M53 result is sufficient for commit
- M53 result is sufficient for push
- M53 result is sufficient for merge
- M53 result is sufficient for release

Any forbidden authority claim invalidates the placement review result.

## 18. M52 Reports Directory Lookup Policy

```yaml
m52_reports_dir:
  default: reports/
  scope: M52 supporting reports only
  arbitrary_discovery_allowed: false
  recursive_lookup_allowed: false
```

Rules:
- CLI may use --m52-reports-dir to locate M52 supporting reports
- default --m52-reports-dir must be reports/
- CLI must not search outside --m52-reports-dir for M52 supporting reports
- CLI must not silently discover M52 reports from arbitrary paths
- CLI must not recursively follow references
- CLI must not replace reports/m52-completion-review.md with a file from m52_reports_dir
- canonical completion review path remains reports/m52-completion-review.md

m52_reports_dir may locate supporting M52 reports, but it cannot replace the canonical M52 completion dependency.

## 19. Repository State Read Boundary

This section is forward-looking policy for future M53 CLI implementation.

The following read boundary defines policy for future M53 CLI implementation, not for this task (53.4). Task 53.4 must not read tasks/queue/, tasks/active-task.md, or approvals/.

```yaml
repo_state_read_boundary:
  applies_to: future_m53_cli_only
  applies_to_current_task_53_4: false
  allowed_read_only_paths:
    - tasks/queue/
    - tasks/active-task.md
    - approvals/
  purpose:
    - detect candidate already queued
    - detect candidate already active
    - detect approval already created by M53
  write_allowed: false
```

Rules:
- this read boundary applies to future M53 CLI only
- this read boundary does not authorize Task 53.4 to inspect tasks/queue/
- this read boundary does not authorize Task 53.4 to inspect tasks/active-task.md
- this read boundary does not authorize Task 53.4 to inspect approvals/
- future CLI may inspect canonical repository state only for placement-conflict detection
- future CLI must not write to tasks/queue/
- future CLI must not write to tasks/active-task.md
- future CLI must not write to approvals/
- future CLI must not search arbitrary repository paths
- future CLI must not use repository state reads to infer missing M52 evidence

Repository state checks are read-only conflict checks; they are not placement actions.

## 20. M54 Handoff Boundary

```yaml
m54_independent_validation_required: true
m54_may_not_start_without_own_gate: true
m54_materialization_authorized: false
```

M53 may identify a candidate for future M54 consideration.
M53 does not authorize M54 to run.
M53 does not authorize queue materialization.
M53 does not authorize active-task proposal materialization.
M54 must independently validate materialization.

## 21. Policy Summary

M53 policy permits only controlled placement eligibility review.

A placement-eligible candidate is still:
not queued,
not active,
not approved,
not executable,
not materialized,
and still waiting for M54 controlled placement materialization.
