# Proposal-to-Task Conversion Package Template

This conversion package template is not an approval record.
This conversion package template does not authorize execution.
This conversion package template does not authorize queue placement.
This conversion package template does not authorize active-task replacement.

conversion_package:
  conversion_id: {{conversion_id}}
  conversion_input_status: {{conversion_input_status}}
  source_task_contract_proposal: {{source_task_contract_proposal}}
  proposal_validation_result: {{proposal_validation_result}}
  source_ux_contract: {{source_ux_contract}}
  source_readiness_report: {{source_readiness_report}}
  source_boundary_policy: {{source_boundary_policy}}
  source_sections:
    - {{source_section_1}}
  accepted_limitations:
    - {{accepted_limitation_1}}
  open_questions:
    - {{open_question_1}}
  downstream_limits:
    - {{downstream_limit_1}}
  non_authority_boundary:
    - {{non_authority_boundary_1}}
  human_authorization_record: {{human_authorization_record}}
  conversion_scope:
    summary: {{conversion_scope}}
  candidate_output: {{candidate_output}}
  boundaries:
    conversion_input_ready_is_execution_permission: false
    conversion_input_ready_is_queue_permission: false
    conversion_input_ready_is_active_task_permission: false
    approval_record_creation_allowed: false
    execution_authorization_granted: false

Carry-forward rules:
- Accepted limitations must be carried forward.
- Open questions must be carried forward.
- Downstream limits must be carried forward.
- Non-authority boundary must be carried forward.
- Source traceability must be preserved.

Human authorization boundary:
- Human authorization record is required for conversion readiness.
- Human authorization record in this package is a reference, not a newly created approval record.
- Task 50.2 must not create approval records.
- Missing human authorization must result in CONVERSION_INPUT_NEEDS_HUMAN_AUTHORIZATION or CONVERSION_INPUT_BLOCKED.
- Human authorization for conversion is not execution approval.
- Human authorization for conversion is not queue placement approval.
- Human authorization for conversion is not active-task replacement approval.

Candidate output boundary:
- candidate_output in Task 50.2 is a bounded output reference or placeholder.
- Task 50.2 does not create a task contract candidate.
- Task 50.2 does not define the final task contract candidate model.
- Task 50.4 defines the task contract candidate model.
- candidate_output must not grant execution permission.
- candidate_output must not grant queue permission.
- candidate_output must not grant active-task permission.
