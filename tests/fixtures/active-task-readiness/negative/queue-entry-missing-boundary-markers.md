# Queue Entry Missing Boundary Markers

expected_result: ACTIVE_TASK_READINESS_NOT_CONFIRMED
expected_exit_code: 1
expected_blocker: QUEUE_ENTRY_BOUNDARY_MARKERS_MISSING

This queue entry intentionally omits one required boundary marker.
Queue entry is not active task.
Queue entry does not authorize active-task replacement.
Queue entry does not authorize execution.

active_task_replacement_authorized: false
active_task_file_created: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
