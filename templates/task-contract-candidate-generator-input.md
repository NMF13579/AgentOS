generator_input:
  input_id: {{input_id}}
  generator_input_status: {{generator_input_status}}
  source_conversion_package: {{source_conversion_package}}
  source_task_contract_proposal: {{source_task_contract_proposal}}
  source_authorization: {{source_authorization}}
  source_candidate_template: {{source_candidate_template}}
  source_conversion_policy: {{source_conversion_policy}}
  source_validator: scripts/validate-proposal-to-task-conversion.py
  generation_mode: {{generation_mode}}
  output_target: {{output_target}}
  primary_output_format: generated_conversion_package_with_embedded_candidate
  primary_validator_target: {{primary_validator_target}}
  carry_forward:
    accepted_limitations: {{accepted_limitations}}
    open_questions: {{open_questions}}
    downstream_limits: {{downstream_limits}}
    non_authority_boundary: {{non_authority_boundary}}
  boundaries:
    dry_run_required: true
    write_to_staging_only: true
    active_task_write_allowed: false
    queue_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false

This generator input template is not a generated artifact.
This generator input template does not authorize execution.
This generator input template does not authorize queue placement.
This generator input template does not authorize active-task replacement.
This generator input template does not authorize implementation.
