# Example Task Contract Candidate Generator Input — Agent Action Review

## Purpose
Показать пример входа для M51-генератора на базе уже валидированного M50 conversion package.

## Example Boundary
Example artifact is not approval.
Example artifact does not authorize execution.
Example artifact does not authorize queue placement.
Example artifact does not authorize active-task replacement.
Example artifact does not authorize implementation.
Example artifact does not create active task state.
Example artifact does not create queue entry.
M51 example artifacts are documentation only.
M51 example artifacts must not be copied into tasks/active-task.md.
M51 example artifacts must not be placed into tasks/queue/.
M51 example artifacts require later M52 validation and M53 placement review before lifecycle movement.

## Source Artifacts
- examples/proposal-to-task-conversion-agent-action-review.md
- examples/task-contract-proposal-agent-action-review.md
- templates/generated-task-contract-candidate-record.md
- docs/TASK-CONTRACT-CANDIDATE-GENERATOR-POLICY.md
- scripts/validate-proposal-to-task-conversion.py

## Generator Input
```yaml
generator_input:
  input_id: agent-action-review
  generator_input_status: GENERATOR_INPUT_READY
  source_conversion_package: examples/proposal-to-task-conversion-agent-action-review.md
  source_task_contract_proposal: examples/task-contract-proposal-agent-action-review.md
  source_authorization: examples/proposal-to-task-conversion-agent-action-review.md
  source_candidate_template: templates/generated-task-contract-candidate-record.md
  source_conversion_policy: docs/TASK-CONTRACT-CANDIDATE-GENERATOR-POLICY.md
  source_validator: scripts/validate-proposal-to-task-conversion.py
  generation_mode: dry_run
  output_target: generated/task-contract-candidates/
  primary_output_format: generated_conversion_package_with_embedded_candidate
  primary_validator_target: null
  carry_forward:
    accepted_limitations: preserved from M50 example conversion package
    open_questions: preserved from M50 example conversion package
    downstream_limits: preserved from M50 example conversion package
    non_authority_boundary: preserved from M50 example conversion package
  boundaries:
    dry_run_required: true
    write_to_staging_only: true
    active_task_write_allowed: false
    queue_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
```

## Carry-Forward Fields
- accepted_limitations: preserved from M50 example conversion package
- open_questions: preserved from M50 example conversion package
- downstream_limits: preserved from M50 example conversion package
- non_authority_boundary: preserved from M50 example conversion package

## Authorization Traceability Note
Note: source_authorization references the M50 example conversion package because the scoped human authorization record is embedded within that conversion package for this example.

This does not mean generic conversion package existence is sufficient authorization.

The authorization must remain traceable inside the M50 conversion package.

## Boundary Flags
- dry_run_required: true
- write_to_staging_only: true
- active_task_write_allowed: false
- queue_write_allowed: false
- execution_authorized: false
- approval_record_creation_allowed: false

## Expected Dry-Run Behavior
- Dry-run по умолчанию.
- would_write_to будет предсказан.
- output_path останется null.
- primary_validator_target останется null.
- generated_candidate_path останется null.
- Файлы в generated/ не создаются.

## Non-Authority Rules
This example generator input is not approval.
This example generator input does not authorize execution.
This example generator input does not authorize queue placement.
This example generator input does not authorize active-task replacement.
This example generator input does not authorize implementation.
This example generator input does not create generated artifacts.

## Explicit Non-Goals
Task 51.7 does not do:
- create real generated artifacts
- write to generated/task-contract-candidates/
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create fixtures
- modify generator CLI
- create evidence reports
- create lessons entries
- create completion reviews
- commit
- push
- merge
- deploy
- release
