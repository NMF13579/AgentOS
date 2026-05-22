fixture:
  fixture_type: negative
  expected_result: TASK_CONTRACT_CANDIDATE_GENERATION_BLOCKED
  expected_exit_code: 2

generator_input:
  input_id: source-does-not-exist
  generator_input_status: GENERATOR_INPUT_READY
  source_conversion_package: tests/fixtures/task-contract-candidate-generator/sources/missing-conversion-package.md
  source_task_contract_proposal: /tmp/proposal.md
  source_authorization: /tmp/auth.md
  source_candidate_template: templates/generated-task-contract-candidate-record.md
  source_conversion_policy: docs/TASK-CONTRACT-CANDIDATE-GENERATOR-POLICY.md
  source_validator: scripts/validate-proposal-to-task-conversion.py
  generation_mode: dry_run
  output_target: generated/task-contract-candidates/
  primary_output_format: generated_conversion_package_with_embedded_candidate
  primary_validator_target: null
  carry_forward:
    accepted_limitations: present
    open_questions: present
    downstream_limits: present
    non_authority_boundary: present
  boundaries:
    dry_run_required: true
    write_to_staging_only: true
    active_task_write_allowed: false
    queue_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
