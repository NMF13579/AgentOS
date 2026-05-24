---
type: template
milestone: M54
template_for: task-queue-placement-artifact
status: draft
authority: template
queue_artifact_created: false
queue_materialization_authorized: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

This template describes a future queue artifact shape only; it does not create a queue artifact.

The template must not imply approval, execution, active-task replacement, lifecycle activation, or M55 authorization.

```json
{
  "queue_placement_artifact": {
    "task_id": "agent-action-review",
    "queue_status": "QUEUED_CANDIDATE",
    "source_candidate_id": "SOURCE_CANDIDATE_ID",
    "source_m53_completion_review": "reports/m53-completion-review.md",
    "source_m53_placement_result": "reports/m53-placement-review-result-agent-action-review.json",
    "source_m52_validation_result": "reports/m52-candidate-validation-result-agent-action-review.json",
    "source_generated_candidate": "generated/agent-action-review-task-candidate.md",
    "placement_created_by": "M54",
    "placement_created_at": "2026-01-01T00:00:00Z",
    "placement_authority": "QUEUE_PLACEMENT_ONLY",
    "approval_status": "NOT_APPROVED",
    "execution_status": "NOT_STARTED",
    "active_task_status": "NOT_ACTIVE",
    "required_traceability": {
      "source_proposal": "SOURCE_PROPOSAL_REFERENCE",
      "source_authorization": "SOURCE_AUTHORIZATION_REFERENCE",
      "source_conversion_package": "SOURCE_CONVERSION_PACKAGE_REFERENCE",
      "source_generated_artifact": "SOURCE_GENERATED_ARTIFACT_REFERENCE",
      "m50_traceability": "M50_TRACEABILITY_REFERENCE",
      "m51_generator_evidence": "M51_GENERATOR_EVIDENCE_REFERENCE",
      "m52_validation_evidence": "M52_VALIDATION_EVIDENCE_REFERENCE",
      "m53_placement_review_evidence": "M53_PLACEMENT_REVIEW_EVIDENCE_REFERENCE",
      "m54_materialization_evidence": "M54_MATERIALIZATION_EVIDENCE_REFERENCE"
    },
    "carry_forward": {
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
    "boundaries": {
      "queue_entry_created": true,
      "active_task_replacement_performed": false,
      "execution_authorized": false,
      "approval_created": false,
      "lifecycle_active_transition_performed": false,
      "m55_start_authorized": false
    }
  }
}
```
