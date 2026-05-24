---
type: template
milestone: M54
template_for: task-candidate-queue-placement-input
status: draft
authority: template
queue_materialization_authorized: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

The template must not imply that pre-materialization checks have passed.

```json
{
  "queue_placement_input": {
    "input_id": "M54_QUEUE_PLACEMENT_INPUT_ID",
    "source_candidate_id": "SOURCE_CANDIDATE_ID",
    "source_m53_completion_review": "reports/m53-completion-review.md",
    "source_m53_evidence_report": "reports/m53-task-candidate-placement-review-evidence-report.md",
    "source_m53_integration_report": "reports/m53-task-candidate-placement-review-integration.md",
    "source_m53_placement_result": "reports/m53-placement-review-result-agent-action-review.json",
    "source_m52_completion_review": "reports/m52-completion-review.md",
    "source_m52_validation_result": "reports/m52-candidate-validation-result-agent-action-review.json",
    "source_generated_candidate": "generated/agent-action-review-task-candidate.md",
    "source_candidate_origin": "M53_PLACEMENT_ELIGIBLE_CANDIDATE",
    "materialization_mode": "QUEUE_PLACEMENT_ONLY",
    "target_queue_dir": "tasks/queue/",
    "target_queue_file": "agent-action-review.md",
    "required_traceability": {
      "source_proposal": "SOURCE_PROPOSAL_REFERENCE",
      "source_authorization": "SOURCE_AUTHORIZATION_REFERENCE",
      "source_conversion_package": "SOURCE_CONVERSION_PACKAGE_REFERENCE",
      "source_generated_artifact": "SOURCE_GENERATED_ARTIFACT_REFERENCE",
      "m50_traceability": "M50_TRACEABILITY_REFERENCE",
      "m51_generator_evidence": "M51_GENERATOR_EVIDENCE_REFERENCE",
      "m52_validation_evidence": "M52_VALIDATION_EVIDENCE_REFERENCE",
      "m53_placement_review_evidence": "M53_PLACEMENT_REVIEW_EVIDENCE_REFERENCE"
    },
    "required_carry_forward": {
      "accepted_limitations": [],
      "warnings": [],
      "open_questions": [],
      "downstream_limits": [],
      "known_gaps": [],
      "non_authority_boundary": [
        "Queue placement is not approval.",
        "Queue placement is not execution.",
        "Queue placement is not active-task replacement.",
        "Queue placement is not M55 authorization."
      ]
    },
    "pre_materialization_checks": {
      "m53_completion_valid": false,
      "m53_input_review_ready": false,
      "m53_materialization_authorized_false": true,
      "candidate_not_already_queued": false,
      "candidate_not_active": false,
      "target_path_safe": false,
      "target_file_absent": false
    },
    "boundaries": {
      "queue_materialization_requested": true,
      "queue_write_allowed_only_by_m54_cli": true,
      "active_task_write_allowed": false,
      "execution_authorized": false,
      "approval_record_creation_allowed": false,
      "lifecycle_active_transition_allowed": false,
      "m55_start_authorized": false
    }
  }
}
```
