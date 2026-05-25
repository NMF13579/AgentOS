# Queue Entry Authority Escalation

expected_result: ACTIVE_TASK_READINESS_BLOCKED
expected_exit_code: 2
expected_blocker: QUEUE_ENTRY_AUTHORITY_ESCALATION

Queue entry is not active task.
Queue entry does not authorize active-task replacement.
Queue entry does not authorize execution.
Queue entry does not authorize M56.

execution_authorized: true
active_task_replacement_authorized: false
active_task_file_created: false
active_task_write_allowed: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
