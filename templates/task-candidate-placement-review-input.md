---
type: template
milestone: M53
task: 53.2
title: Task Candidate Placement Review Input Template
status: draft
authority: supporting
schema: schemas/task-candidate-placement-review-input.schema.json
---

```yaml
placement_review_input:
  input_id: ""
  source_candidate_id: ""
  source_m52_completion_review: reports/m52-completion-review.md
  source_m52_evidence_report: ""
  source_m52_integration_report: ""
  source_m52_validation_result: ""
  source_generated_artifact: ""
  source_candidate_origin: M52_VALIDATED_CANDIDATE_RESULT
  placement_review_mode: REVIEW_ONLY
  expected_candidate_shape: TASK_CONTRACT_CANDIDATE
  m52_reports_dir: reports/
  required_traceability:
    source_proposal: ""
    source_authorization: ""
    source_conversion_package: ""
    source_generated_artifact: ""
    m50_traceability: ""
    m51_generator_evidence: ""
    m52_validation_evidence: ""
  required_carry_forward:
    accepted_limitations: []
    warnings: []
    open_questions: []
    downstream_limits: []
    known_gaps: []
    non_authority_boundary:
      - M53 placement review input is not approval.
      - M53 placement review input does not authorize execution.
      - M53 placement review input does not authorize queue placement.
      - M53 placement review input does not authorize active-task replacement.
      - M53 placement review input does not authorize lifecycle mutation.
      - M53 placement review input does not authorize M54 materialization.
  placement_target:
    queue_candidate_allowed_for_review: false
    active_task_candidate_allowed_for_review: false
  boundaries:
    review_only: true
    queue_write_allowed: false
    active_task_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
    lifecycle_mutation_allowed: false
    m54_materialization_authorized: false
```

This template is not approval.
This template does not authorize queue placement.
This template does not authorize active-task replacement.
This template does not authorize execution.
This template does not authorize M54 materialization.
