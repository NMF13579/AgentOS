---
type: example
milestone: M53
task: 53.7
title: Example Placement Review Input — Agent Action Review
status: draft
authority: example
created_for: M53
example_kind: placement_review_input
source_m52_completion_review: reports/m52-completion-review.md
source_m52_validation_result: reports/m52-candidate-validation-result-agent-action-review.json
m54_materialization_authorized: false
---

This example demonstrates M53 placement review input without granting placement authority.

This example references production-style M52 artifacts for demonstration.
Those referenced artifacts may be absent in the current repository state.
If absent, the optional dry-run may block without invalidating this example document.

This example preserves M52 carry-forward material when reports/m52-completion-review.md contains limitations.
Empty carry-forward arrays are allowed only when M52 final_status is M52_CANDIDATE_VALIDATION_LAYER_COMPLETE.
Conservative limitation notes must be placed in limitation fields, not in non_authority_boundary.

```json
{
  "placement_review_input": {
    "input_id": "example-agent-action-review-placement-review-input",
    "source_candidate_id": "agent-action-review-candidate",
    "source_m52_completion_review": "reports/m52-completion-review.md",
    "source_m52_evidence_report": "reports/m52-task-candidate-validation-evidence-report.md",
    "source_m52_integration_report": "reports/m52-task-candidate-validation-integration.md",
    "source_m52_validation_result": "reports/m52-candidate-validation-result-agent-action-review.json",
    "source_generated_artifact": "generated/agent-action-review-task-candidate.md",
    "source_candidate_origin": "M52_VALIDATED_CANDIDATE_RESULT",
    "placement_review_mode": "QUEUE_CANDIDATE_ELIGIBILITY_REVIEW",
    "expected_candidate_shape": "QUEUE_MATERIALIZATION_INPUT_CANDIDATE",
    "m52_reports_dir": "reports/",
    "required_traceability": {
      "source_proposal": "reports/m50-agent-action-review-proposal.md",
      "source_authorization": "reports/m50-agent-action-review-authorization.md",
      "source_conversion_package": "reports/m50-agent-action-review-conversion-package.md",
      "source_generated_artifact": "generated/agent-action-review-task-candidate.md",
      "m50_traceability": "M50_TRACEABILITY_PRESERVED",
      "m51_generator_evidence": "M51_GENERATOR_EVIDENCE_PRESERVED",
      "m52_validation_evidence": "M52_VALIDATION_EVIDENCE_PRESERVED"
    },
    "required_carry_forward": {
      "accepted_limitations": [
        "M52 completion review indicates limitations; exact limitation text requires manual review before M54."
      ],
      "warnings": [],
      "open_questions": [],
      "downstream_limits": [],
      "known_gaps": [],
      "non_authority_boundary": [
        "M53 placement review input is not approval.",
        "M53 placement review input does not authorize execution.",
        "M53 placement review input does not authorize queue placement.",
        "M53 placement review input does not authorize active-task replacement.",
        "M53 placement review input does not authorize lifecycle mutation.",
        "M53 placement review input does not authorize M54 materialization."
      ]
    },
    "placement_target": {
      "queue_candidate_allowed_for_review": true,
      "active_task_candidate_allowed_for_review": false
    },
    "boundaries": {
      "review_only": true,
      "queue_write_allowed": false,
      "active_task_write_allowed": false,
      "execution_authorized": false,
      "approval_record_creation_allowed": false,
      "lifecycle_mutation_allowed": false,
      "m54_materialization_authorized": false
    }
  }
}
```

This example is not approval.
This example does not authorize execution.
This example does not authorize queue placement.
This example does not authorize active-task replacement.
This example does not authorize lifecycle mutation.
This example does not authorize M54 materialization.

M53 example input may identify a candidate for future M54 consideration.
M53 example input does not authorize M54 to run.
M53 example input does not authorize queue materialization.
M53 example input does not authorize active-task proposal materialization.
M54 must independently validate materialization.

This example input is:
not queued,
not active,
not approved,
not executable,
not materialized,
and still waiting for M54 controlled placement materialization.
