# Positive Markdown Input

This fixture contains exactly one fenced JSON block.

```json
{
  "queue_placement_input": {
    "input_id": "M54_POSITIVE_MARKDOWN_FENCED_JSON_INPUT",
    "source_candidate_id": "CANDIDATE_FOR_VALIDATION",
    "placement_kind": "queue_materialization",
    "queue_materialization_requested": true,
    "active_task_replacement_requested": false,
    "approval_requested": false,
    "execution_requested": false,
    "m55_requested": false,
    "boundary_flags": {
      "queue_materialization_authorized_by_input": false,
      "active_task_replacement_authorized": false,
      "execution_authorized": false,
      "approval_created": false,
      "m55_authorized": false
    },
    "source_traceability": {
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
        "Queue placement input is not approval.",
        "Queue placement input is not execution.",
        "Queue placement input is not active-task replacement.",
        "Queue placement input is not M55 authorization."
      ]
    }
  }
}
```
