---
type: template
milestone: M53
task: 53.3
title: Task Candidate Placement Review Result Template
status: draft
authority: supporting
schema: schemas/task-candidate-placement-review-result.schema.json
---

```yaml
placement_review_result:
  result: PLACEMENT_REVIEW_BLOCKED
  exit_code: 2
  reviewed: false
  eligible_for_downstream_placement: false
  eligible_as_m54_queue_materialization_input: false
  eligible_as_m54_active_task_proposal_input: false
  checked_candidate_id: ""
  source_m52_completion_review: reports/m52-completion-review.md
  source_m52_validation_result: ""
  source_generated_artifact: ""
  source_traceability:
    source_proposal: ""
    source_authorization: ""
    source_conversion_package: ""
    source_generated_artifact: ""
    m50_traceability: ""
    m51_generator_evidence: ""
    m52_validation_evidence: ""
  carry_forward:
    accepted_limitations: []
    warnings: []
    open_questions: []
    downstream_limits: []
    known_gaps: []
    non_authority_boundary:
      - M53 placement review result is not approval.
      - M53 placement review result does not authorize execution.
      - M53 placement review result does not authorize queue placement.
      - M53 placement review result does not authorize active-task replacement.
      - M53 placement review result does not authorize lifecycle mutation.
      - M53 placement review result does not authorize M54 materialization.
  placement_findings: []
  warnings: []
  blockers: []
  boundary_flags:
    review_only: true
    queue_write_allowed: false
    active_task_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
    lifecycle_mutation_allowed: false
    m54_materialization_authorized: false
  non_authority_markers:
    - M53 placement review result is not approval.
    - M53 placement review result does not authorize execution.
    - M53 placement review result does not authorize queue placement.
    - M53 placement review result does not authorize active-task replacement.
    - M53 placement review result does not authorize lifecycle mutation.
    - M53 placement review result does not authorize M54 materialization.
  m54_independent_validation_required: true
  m54_may_not_start_without_own_gate: true
  m54_materialization_authorized: false
  queue_placement_performed: false
  active_task_replacement_performed: false
  approval_created: false
```

This template is not approval.
This template does not authorize queue placement.
This template does not authorize active-task replacement.
This template does not authorize execution.
This template does not authorize M54 materialization.
