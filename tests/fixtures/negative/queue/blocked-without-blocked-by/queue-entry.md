# Queue Entry — Blocked Without Blocked By
## Metadata
    task_id: task-negative-queue-blocked-without-blocked-by
    status: blocked
    priority: normal
    blocked_by: []
## Expected Failure
Blocked queue entry should include at least one blocked_by reference.
## Notes
blocked_by field is present but empty ([]). Future validator should check that
blocked_by contains at least one entry when status is blocked.
