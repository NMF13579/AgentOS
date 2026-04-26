# Queue Entry — Invalid Status
## Metadata
    task_id: task-negative-queue-invalid-status
    status: invalid_state
    priority: normal
    blocked_by: []
## Expected Failure
Queue entry status must be one of: queued, blocked, in_progress, done, dropped.
