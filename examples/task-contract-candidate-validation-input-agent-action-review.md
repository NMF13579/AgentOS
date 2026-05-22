# Example M52 Candidate Validation Input — Agent Action Review

This example shows how M51 generated staging artifact becomes M52 validation input.

```yaml
candidate_validation_input:
  input_id: m52-example-input-agent-action-review-001
  source_generated_artifact: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md
  source_candidate_path: conversion_package.candidate_output.task_contract_candidate
  source_conversion_package: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md#conversion_package
  source_candidate_origin: M51_GENERATED_STAGING_ARTIFACT
  source_validator: scripts/validate-task-contract-candidate.py
  validation_mode: M52_CANDIDATE_READINESS_VALIDATION
  expected_candidate_shape: generated_conversion_package_with_embedded_candidate
  required_traceability:
    source_proposal: m49-agent-action-review-proposal-v1
    source_authorization: example-human-auth-ref-agent-action-review-001
    source_conversion_package: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md#conversion_package
    source_generated_artifact: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md
    source_candidate_origin: M51_GENERATED_STAGING_ARTIFACT
    m50_traceability: conversion_id:m50-example-conv-agent-action-review-001
    m51_generator_evidence: reports/m51-task-contract-candidate-generator-evidence-report.md
  required_carry_forward:
    accepted_limitations:
      - review scope excludes runtime implementation and code execution
    open_questions:
      - should reviewer severity buckets be fixed or configurable in M51
    downstream_limits:
      - placement review required before any queue or active-task lifecycle operation
    non_authority_boundary:
      - conversion does not authorize execution
      - conversion does not authorize queue placement
      - conversion does not authorize active-task replacement
  downstream_target: M53_PLACEMENT_REVIEW
  m51_origin:
    required: true
    source_generator_evidence: reports/m51-task-contract-candidate-generator-evidence-report.md
    source_generator_completion_review: reports/m51-completion-review.md
    source_generator_integration_report: reports/m51-generator-integration-validation.md
  boundaries:
    validation_only: true
    queue_write_allowed: false
    active_task_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
    placement_authorized: false
```

m51_origin is required because source_candidate_origin is M51_GENERATED_STAGING_ARTIFACT.
M51-origin evidence is provenance evidence only.
M51-origin evidence is not approval.
M51-origin evidence is not execution authorization.
M51-origin evidence is not placement authorization.

source_authorization means provenance authorization for source conversion or candidate generation only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.

source_conversion_package appears both as a top-level input reference and inside required_traceability.
The top-level source_conversion_package identifies the package used by this validation input.
The required_traceability.source_conversion_package field preserves provenance traceability for downstream validation and M53 review.

accepted_limitations, open_questions, downstream_limits, and non_authority_boundary must be carried forward from the source conversion package without deletion.
Existing carry-forward items must not be removed, softened, renamed into weaker meaning, converted into resolved state, converted into approved state, or hidden from M53 review.

Example candidate validation input is not approval.
Example candidate validation input does not authorize execution.
Example candidate validation input does not authorize queue placement.
Example candidate validation input does not authorize active-task replacement.
Example candidate validation input does not authorize M53 placement.
Example candidate validation input does not create lifecycle state.
