---
type: template
module: m26-pre-merge-corridor
status: active
authority: supporting
version: 1.0.0
created: 2026-05-04
task_id: 26.9.1
milestone: M26
---

# Retry Attempt Record

> M26 Template — Task 26.9.1
>
> This retry record is not approval.
> This retry record does not authorize commit.
> This retry record does not authorize push.
> This retry record does not authorize merge.
> This retry record does not bypass M25.
> Agent cannot set retry_allowed after violation.
> Agent cannot reset retry count.
> Agent cannot close its own retry record after violation.
> Human review cannot be simulated.

---

## Identity

```yaml
retry_record_id:  # Format: RA-{task_id}-{YYYYMMDD}-{sequence}
                  # Example: RA-26.9.1-20260504-001
task_id:          # Active task ID
created_at:       # ISO 8601 timestamp
reviewer:         # MUST be filled by human for post-violation records
                  # Agent must use PENDING_HUMAN_ASSIGNMENT if retry follows violation
                  # Agent must not fill with own identifier after violation
agent:            # Agent identifier or model used
branch:           # Branch on which retry is attempted
```

---

## Retry Context

```yaml
retry_context:
  trigger:                    # What caused this retry
  related_violation_record:   # AV-{...} reference, or NONE
                              # Required if retry follows a violation
  related_checker_result:     # 26.7.1 output that triggered this retry, or NONE
  previous_attempt_count:     # Total retry attempts for this task_id before this record
                              # Determined by counting prior retry-attempt-record files
                              # Agent cannot self-report 0 when prior records exist
  same_failure_count:         # Number of times the same failure type has occurred
  retry_reason:               # Human-readable reason why retry is being attempted
```

---

## Retry Decision

```yaml
retry_decision:
  decision:               # RETRY_ALLOWED / RETRY_ALLOWED_WITH_CONDITIONS /
                          # NEEDS_HUMAN_REVIEW / RETRY_BLOCKED / RETRY_EXHAUSTED
                          #
                          # Agent may set RETRY_ALLOWED only when all Retry Allowed
                          # Conditions are satisfied and no human-only condition applies.
                          # Agent must set NEEDS_HUMAN_REVIEW if any human-only condition applies.
  conditions:             # Conditions that must be met if RETRY_ALLOWED_WITH_CONDITIONS
                          # NONE if not applicable
  max_attempts_allowed:   # Policy limit that applies: 3 / 2 / 1 / 0
  permission_for_retry:   # READ_ONLY / PATCH_PROPOSE / LOCAL_EDIT / LOCAL_TEST /
                          # COMMIT_REQUEST / PUSH_REQUEST
                          #
                          # BLOCKED is not a valid permission_for_retry value.
                          # If permission would be BLOCKED, decision must be RETRY_BLOCKED.
                          # COMMIT_REQUEST and PUSH_REQUEST are forbidden after violation
                          # without explicit human restoration.
  human_review_required:  # yes / no
  owner_review_required:  # yes / no
```

---

## Retry Plan

```yaml
retry_plan:
  intended_actions:
    - description of action
  declared_scope:
    - path/to/file
  commands_planned:
    - command
  write_paths_planned:
    - path/to/file
  forbidden_paths_confirmed: # yes / no
  m25_validation_required:  # yes / no
                            # Must be yes if retry produces new commit or change
```

---

## Retry Result

```yaml
retry_result:
  outcome:                  # RETRY_SUCCESS / RETRY_FAILED / RETRY_BLOCKED /
                            # RETRY_ABORTED / NEEDS_REVIEW
  files_changed:
    - path/to/file
  commands_run:
    - command
  validation_result:        # M25 validation result after retry, or NOT_RUN
  scope_check_result:       # 26.5.1 result after retry, or NOT_RUN
  commit_push_check_result: # 26.7.1 result after retry, or NOT_RUN
  new_violation_created:    # yes / no
                            # If yes, reference violation record in related_records
```

---

## Post-Retry State

```yaml
post_retry_state:
  permission_after_retry:    # READ_ONLY / PATCH_PROPOSE / LOCAL_EDIT / LOCAL_TEST /
                             # COMMIT_REQUEST / PUSH_REQUEST / BLOCKED
  task_status_after_retry:   # TASK_CONTINUES / TASK_REDUCED / TASK_BLOCKED /
                             # TASK_RESET_REQUIRED / OWNER_REVIEW_REQUIRED
  retry_count_after_attempt: # Total retry attempts for this task_id including this record
  stop_required:             # yes / no
  next_required_action:      # HUMAN_REVIEW_REQUIRED / OWNER_REVIEW_REQUIRED /
                             # CONTINUE_TASK / TASK_BLOCKED / NONE
```

---

## Evidence

```yaml
evidence_artifacts:
  - reports/...
related_records:
  - AV-...
  - RA-...
```

---

## Notes

```yaml
notes:  # Reviewer notes or agent factual description of what occurred.
        # Agent may add factual description of retry trigger and actions taken.
        # Agent must not add self-exonerating language.
        # Agent must not claim retry was successful without evidence.
```

---

## Required Validation Rules

```text
[ ] retry_record_id is unique
[ ] task_id matches active task
[ ] previous_attempt_count matches count of prior retry-attempt-record files for task_id
[ ] same_failure_count is accurate
[ ] decision is from the defined list
[ ] permission_for_retry is not BLOCKED
[ ] if permission would be BLOCKED, decision is RETRY_BLOCKED
[ ] if retry follows violation, related_violation_record is not NONE
[ ] if retry follows violation, reviewer is PENDING_HUMAN_ASSIGNMENT or filled by human
[ ] if retry follows violation, agent does not set RETRY_ALLOWED without human authorization
[ ] forbidden_paths_confirmed: yes
[ ] m25_validation_required: yes if retry produces new commit or change
[ ] outcome is from the defined list
[ ] if new_violation_created: yes, reference is in related_records
[ ] stop_required: yes if outcome is RETRY_BLOCKED, RETRY_FAILED beyond limit, or NEEDS_REVIEW
[ ] retry_count_after_attempt equals previous_attempt_count + 1
```

---

## Important Reminders

### This Record Is Not Approval

- This retry record is not approval.
- This retry record does not authorize commit.
- This retry record does not authorize push.
- This retry record does not authorize merge.
- `RETRY_SUCCESS` does not satisfy the Pre-Merge Execution Corridor.
- `RETRY_SUCCESS` does not authorize merge.
- `RETRY_SUCCESS` does not bypass M25.

### Agent Cannot Self-Authorize

- Agent cannot set `retry_allowed: yes` after violation.
- Agent cannot reset `previous_attempt_count` to zero when prior records exist.
- Agent cannot set `decision` to `RETRY_ALLOWED` when a human-only condition applies.
- Agent cannot close its own retry record after violation.
- Agent cannot mark outcome as `RETRY_SUCCESS` without evidence.

### Stop When Required

- Agent must stop when `stop_required: yes`.
- Agent must not re-interpret `stop_required: yes` as a different state.
- Agent must not attempt alternative paths after stop.
- Agent must not create a new retry record to continue past an exhausted retry limit.

---

## Usage Notes

- Create one retry attempt record per retry attempt.
- Store records in `reports/retry-attempts/` or another documented evidence directory.
- Reference records from violation records and pre-merge execution reviews.
- Retain records for audit trail.
- Retry attempt records must not be modified or deleted by the agent.
