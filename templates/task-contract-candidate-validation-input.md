# Task Contract Candidate Validation Input Template (M52 MVP)

```yaml
candidate_validation_input:
  input_id: m52-input-001
  source_generated_artifact: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md
  source_candidate_path: conversion_package.candidate_output.task_contract_candidate
  source_conversion_package: conversion_package
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
    m51_generator_evidence: m51-generated-artifact-evidence-ref
  required_carry_forward:
    accepted_limitations:
      - review scope excludes runtime implementation and code execution
    open_questions:
      - should reviewer severity buckets be fixed or configurable in M51
    downstream_limits:
      - placement review required before any queue or active-task lifecycle operation
    non_authority_boundary:
      - conversion does not authorize execution
  downstream_target: M53_PLACEMENT_REVIEW
  m51_origin:
    required: true
    source_generator_evidence: m51-generator-evidence-ref
    source_generator_completion_review: m51-generator-completion-review-ref
    source_generator_integration_report: m51-generator-integration-report-ref
  boundaries:
    validation_only: true
    queue_write_allowed: false
    active_task_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
    placement_authorized: false
```

source_validator path is reserved for Task 52.5 and may not exist until the validator CLI is implemented.

This candidate validation input is not approval.
This candidate validation input does not authorize execution.
This candidate validation input does not authorize queue placement.
This candidate validation input does not authorize active-task replacement.
This candidate validation input does not authorize M53 placement.
