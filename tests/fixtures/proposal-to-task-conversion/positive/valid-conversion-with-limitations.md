fixture_name: valid-conversion-with-limitations
fixture_type: positive
expected_result: PROPOSAL_TO_TASK_CONVERSION_VALIDATION_OK

conversion_package:
  conversion_id: conv-002
  conversion_input_status: CONVERSION_INPUT_READY_WITH_LIMITATIONS
  source_task_contract_proposal: proposal-002
  proposal_validation_result: TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS
  source_ux_contract: ux-002
  source_readiness_report: readiness-002
  source_boundary_policy: boundary-002
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
  human_authorization_record: auth-002
  conversion_scope: scope-002
  candidate_output: candidate-ref-002

human_authorization:
  authorization_id: auth-002
  authorization_type: proposal_to_task_contract_candidate_conversion
  source_proposal: proposal-002
  authorized_scope: conversion-only
  not_authorized:
    - execution
  authorized_by: owner_team
  authorization_status: AUTHORIZATION_VALID
  expires_at: 2099-12-31T23:59:59Z

task_contract_candidate:
  task_id: task-002
  source_proposal: proposal-002
  source_authorization: auth-002
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
