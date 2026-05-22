fixture_name: authorization-expired
fixture_type: negative
expected_result: PROPOSAL_TO_TASK_CONVERSION_VALIDATION_BLOCKED

conversion_package:
  conversion_id: conv-neg
  conversion_input_status: CONVERSION_INPUT_READY
  source_task_contract_proposal: proposal-neg
  proposal_validation_result: TASK_CONTRACT_PROPOSAL_VALIDATED
  source_ux_contract: ux-neg
  source_readiness_report: readiness-neg
  source_boundary_policy: boundary-neg
  source_sections:
    - section-a
  accepted_limitations:
    - limitation-a
  open_questions:
    - question-a
  downstream_limits:
    - downstream-a
  non_authority_boundary:
    - non-auth-a
  human_authorization_record: auth-neg
  conversion_scope: scope-neg
  candidate_output: candidate-neg

human_authorization:
  authorization_id: auth-neg
  authorization_type: proposal_to_task_contract_candidate_conversion
  source_proposal: proposal-neg
  authorized_scope: conversion-only
  not_authorized:
    - execution
  authorized_by: owner_team
  authorization_status: AUTHORIZATION_VALID
  expires_at: 2000-01-01T00:00:00Z

task_contract_candidate:
  task_id: task-neg
  source_proposal: proposal-neg
  source_authorization: auth-neg
  mode: EXECUTION_SHAPE
  goal:
    - goal-a
  scope:
    - scope-a
  allowed_changes:
    - file-a
  forbidden_changes:
    - no-queue
  validation:
    - check-a
  expected_final_report:
    - report-a
  carry_forward:
    accepted_limitations:
      - limitation-a
    open_questions:
      - question-a
    downstream_limits:
      - downstream-a
    non_authority_boundary:
      - non-auth-a
  boundaries:
    conversion_validated: true
    executable_contract_shape: true
    candidate_ready_for_placement_review: true
    placement_review_required: true
    execution_authorized: false
    execution_permission_granted: false
    active_task_allowed: false
    task_queue_allowed: false
