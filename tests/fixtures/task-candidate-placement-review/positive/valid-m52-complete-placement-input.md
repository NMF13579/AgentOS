---
type: fixture
scope: positive
name: valid-m52-complete-placement-input
---

This positive fixture proves eligibility without granting placement authority.

```json
{
  "placement_review_input": {
    "input_id": "fixture-valid-m52-complete-placement-input",
    "source_candidate_id": "agent-action-review-candidate",
    "source_m52_completion_review": "reports/m52-completion-review.md",
    "source_m52_evidence_report": "tests/fixtures/task-candidate-placement-review/sources/baseline-m52-evidence-report.md",
    "source_m52_integration_report": "tests/fixtures/task-candidate-placement-review/sources/baseline-m52-integration-report.md",
    "source_m52_validation_result": "tests/fixtures/task-candidate-placement-review/sources/baseline-m52-validation-result.json",
    "source_generated_artifact": "tests/fixtures/task-candidate-placement-review/sources/baseline-generated-conversion-package.md",
    "source_candidate_origin": "M52_VALIDATED_CANDIDATE_RESULT",
    "placement_review_mode": "QUEUE_CANDIDATE_ELIGIBILITY_REVIEW",
    "expected_candidate_shape": "QUEUE_MATERIALIZATION_INPUT_CANDIDATE",
    "m52_reports_dir": "reports/",
    "required_traceability": {
      "source_proposal": "reports/m50-agent-action-review-proposal.md",
      "source_authorization": "reports/m50-agent-action-review-authorization.md",
      "source_conversion_package": "reports/m50-agent-action-review-conversion-package.md",
      "source_generated_artifact": "tests/fixtures/task-candidate-placement-review/sources/baseline-generated-conversion-package.md",
      "m50_traceability": "M50_TRACEABILITY_PRESERVED",
      "m51_generator_evidence": "M51_GENERATOR_EVIDENCE_PRESERVED",
      "m52_validation_evidence": "M52_VALIDATION_EVIDENCE_PRESERVED"
    },
    "required_carry_forward": {
      "accepted_limitations": [],
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

This fixture is not approval.
This fixture does not authorize execution.
This fixture does not authorize queue placement.
This fixture does not authorize active-task replacement.
This fixture does not authorize lifecycle mutation.
This fixture does not authorize M54 materialization.
