conversion_package:
  conversion_id: fixture-conversion-001
  conversion_input_status: CONVERSION_INPUT_READY_WITH_LIMITATIONS
  source_task_contract_proposal: fixture-proposal-001
  proposal_validation_result: TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS
  source_ux_contract: fixture-ux-contract
  source_readiness_report: fixture-readiness
  source_boundary_policy: fixture-boundary-policy
  source_sections: fixture-sections
  accepted_limitations:
    - bounded fixture limitations
  open_questions:
    - fixture open question
  downstream_limits:
    - fixture downstream limit
  non_authority_boundary:
    - fixture non-authority boundary
  human_authorization_record: fixture-auth-reference
  conversion_scope: fixture-scope
  candidate_output: fixture-candidate-output
  boundaries:
    conversion_input_ready_is_execution_permission: false
    conversion_input_ready_is_queue_permission: false
    conversion_input_ready_is_active_task_permission: false
    approval_record_creation_allowed: false
    execution_authorization_granted: false

task_contract_candidate:
  task_id: fixture-task-001
  source_proposal: fixture-proposal-001
  source_authorization: fixture-auth-reference
  mode: EXECUTION_SHAPE
  goal: fixture goal
  scope: fixture scope
  allowed_changes:
    - fixture allowed change
  forbidden_changes:
    - fixture forbidden change
  validation:
    - fixture validation
  expected_final_report: fixture report
  carry_forward:
    accepted_limitations:
      - bounded fixture limitations
    open_questions:
      - fixture open question
    downstream_limits:
      - fixture downstream limit
    non_authority_boundary:
      - fixture non-authority boundary
  boundaries:
    conversion_validated: true
    executable_contract_shape: true
    candidate_ready_for_placement_review: true
    placement_review_required: true
    execution_authorized: false
    execution_permission_granted: false
    active_task_allowed: false
    task_queue_allowed: false

Fixture source conversion package is not approval.
Fixture source conversion package does not authorize execution.
Fixture source conversion package does not authorize queue placement.
Fixture source conversion package does not authorize active-task replacement.
Fixture source conversion package does not authorize implementation.
