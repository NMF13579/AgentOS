# Positive Fixture

Expected M52 Result:
- expected_result: TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS

```yaml
conversion_package:
  source_candidate_origin: M51_GENERATED_STAGING_ARTIFACT
  source_proposal: baseline-source-proposal
  source_authorization: baseline-source-authorization
  source_conversion_package: baseline-source-conversion-package
  source_generated_artifact: generated/task-contract-candidates/agent-action-review.generated-conversion-package.md
  m50_traceability: baseline-m50-traceability
  m51_generator_evidence: baseline-m51-generator-evidence
  source_generator_evidence: baseline-m51-generator-evidence
  source_generator_completion_review: baseline-m51-completion-review
  source_generator_integration_report: baseline-m51-integration-report
  candidate_output:
    task_contract_candidate:
      task_id: fixture-positive
      mode: EXECUTION_SHAPE
      goal:
        - keep validation bounded
      scope:
        - validate candidate only
      allowed_changes:
        - create review artifact only
      forbidden_changes:
        - no queue placement
        - no active-task replacement
        - no execution permission
        - no approval creation
      validation:
        - verify required sections
      expected_final_report:
        - findings
        - warnings
        - blockers
      accepted_limitations:
        - limitation retained
      open_questions:
        - open question retained
      downstream_limits:
        - requires M53 review
      non_authority_boundary:
        - validation is not approval
      boundaries:
        validation_only: true
        placement_authorized: false
        execution_authorized: false
        queue_write_allowed: false
        active_task_write_allowed: false
        approval_record_creation_allowed: false
```
