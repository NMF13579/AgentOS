---
type: template
milestone: M55
template_for: task-candidate-active-task-readiness-input
status: draft
authority: template
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---
This template describes M55 active-task readiness input only; it does not replace active-task.md.

```json
{
  "active_task_readiness_input": {
    "input_id": "M55_ACTIVE_TASK_READINESS_INPUT_ID",
    "source_m54_completion_review": "reports/m54-completion-review.md",
    "source_m54_materialization_result": "reports/m54-placement-materialization-result-agent-action-review.json",
    "source_queue_entry": "tasks/queue/agent-action-review-task-candidate.md",
    "source_m53_placement_result": "reports/m53-placement-review-result-agent-action-review.json",
    "source_m52_validation_result": "reports/m52-candidate-validation-result-agent-action-review.json",
    "checked_queue_entry_id": "QUEUE_ENTRY_ID",
    "target_active_task_path": "tasks/active-task.md",
    "readiness_mode": "ACTIVE_TASK_READINESS_REVIEW",
    "required_traceability": {
      "source_proposal": "SOURCE_PROPOSAL_REFERENCE",
      "source_authorization": "SOURCE_AUTHORIZATION_REFERENCE",
      "source_conversion_package": "SOURCE_CONVERSION_PACKAGE_REFERENCE",
      "source_generated_artifact": "SOURCE_GENERATED_ARTIFACT_REFERENCE",
      "m50_traceability": "M50_TRACEABILITY_REFERENCE",
      "m51_generator_evidence": "M51_GENERATOR_EVIDENCE_REFERENCE",
      "m52_validation_evidence": "M52_VALIDATION_EVIDENCE_REFERENCE",
      "m53_placement_review_evidence": "M53_PLACEMENT_REVIEW_EVIDENCE_REFERENCE",
      "m54_materialization_evidence": "M54_MATERIALIZATION_EVIDENCE_REFERENCE",
      "queue_entry_evidence": "QUEUE_ENTRY_EVIDENCE_REFERENCE"
    },
    "carry_forward": {
      "accepted_limitations": [],
      "warnings": [],
      "open_questions": [],
      "downstream_limits": [],
      "known_gaps": [],
      "non_authority_boundary": [
        "M55 input is not approval.",
        "M55 input does not authorize execution.",
        "M55 input does not authorize active-task replacement.",
        "M55 input does not create approval records.",
        "M55 input does not authorize M56.",
        "M55 input does not start M56."
      ]
    },
    "boundary_flags": {
      "active_task_readiness_only": true,
      "active_task_replacement_authorized": false,
      "execution_authorized": false,
      "approval_created": false,
      "lifecycle_mutation_authorized": false,
      "m56_authorized": false,
      "m56_started": false
    },
    "non_authority_markers": [
      "M55 input is not approval.",
      "M55 input does not authorize execution.",
      "M55 input does not authorize active-task replacement.",
      "M55 input does not create approval records.",
      "M55 input does not authorize M56.",
      "M55 input does not start M56."
    ]
  }
}
```
