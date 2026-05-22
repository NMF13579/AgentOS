# Task Contract Candidate Template

This task contract candidate template is not an active task.
This task contract candidate template does not authorize execution.
This task contract candidate template does not authorize queue placement.
This task contract candidate template does not authorize active-task replacement.
This task contract candidate template does not authorize implementation.

M50 uses EXECUTION_SHAPE, not EXECUTION.
EXECUTION_SHAPE means the candidate has the structure of an executable task contract.
EXECUTION_SHAPE does not mean execution is authorized.
EXECUTION_SHAPE does not allow queue placement.
EXECUTION_SHAPE does not allow active-task replacement.
EXECUTION_SHAPE does not allow implementation.
mode must be EXECUTION_SHAPE.
mode must not be EXECUTION.

Task contract candidate is not active task state.
Task contract candidate is not queue entry.
Task contract candidate must not be copied into tasks/active-task.md by M50.
Task contract candidate must not be placed into tasks/queue/ by M50.

Task contract candidate:

task_contract_candidate:
  task_id: {{task_id}}
  source_proposal: {{source_proposal}}
  source_authorization: {{source_authorization}}
  mode: EXECUTION_SHAPE
  goal: {{goal}}
  scope: {{scope}}
  allowed_changes:
    - {{allowed_changes}}
  forbidden_changes:
    - {{forbidden_changes}}
  validation:
    - {{validation}}
  expected_final_report:
    - {{expected_final_report}}
  carry_forward:
    accepted_limitations:
      - {{accepted_limitations}}
    open_questions:
      - {{open_questions}}
    downstream_limits:
      - {{downstream_limits}}
    non_authority_boundary:
      - {{non_authority_boundary}}
  boundaries:
    conversion_validated: true
    executable_contract_shape: true
    candidate_ready_for_placement_review: true
    placement_review_required: true
    execution_authorized: false
    execution_permission_granted: false
    active_task_allowed: false
    task_queue_allowed: false

Carry-forward rules:
- Accepted limitations must be carried forward.
- Open questions must be carried forward.
- Downstream limits must be carried forward.
- Non-authority boundary must be carried forward.
- Source traceability must be preserved.
