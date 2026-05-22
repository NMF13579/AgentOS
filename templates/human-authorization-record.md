# Human Authorization Record Template

This human authorization template is not an approval record.
This human authorization template does not authorize execution.
This human authorization template does not authorize queue placement.
This human authorization template does not authorize active-task replacement.
This human authorization template does not authorize implementation.

Human authorization in M50 authorizes conversion only.
Human authorization in M50 does not authorize execution.
Human authorization in M50 does not authorize queue placement.
Human authorization in M50 does not authorize active-task replacement.
Human authorization in M50 does not authorize implementation.

human_authorization:
  authorization_id: {{authorization_id}}
  authorization_type: proposal_to_task_contract_candidate_conversion
  source_proposal: {{source_proposal}}
  authorized_scope: {{authorized_scope}}
  not_authorized:
    - {{not_authorized}}
    - execution
    - queue placement
    - active-task replacement
    - implementation
    - commit
    - push
    - merge
    - deploy
    - release
    - approval record creation by agent or validator
  authorized_by: {{authorized_by}}
  authorized_at: {{authorized_at}}
  authorization_status: {{authorization_status}}
  expires_at: {{expires_at}}
  evidence_reference: {{evidence_reference}}
  boundaries:
    conversion_only: true
    execution_approval_granted: false
    queue_placement_approval_granted: false
    active_task_replacement_approval_granted: false
    implementation_approval_granted: false
    approval_record_creation_allowed: false
