---
type: template
module: m26-pre-merge-corridor
status: active
authority: supporting
version: 1.0.0
created: 2026-05-04
task_id: 26.8.1
milestone: M26
---

# Agent Violation Record

> M26 Template — Task 26.8.1
>
> This violation record is not approval.
> This violation record does not clear a violation.
> Agent cannot fill the reviewer field.
> Agent cannot close its own violation.
> Agent cannot set `retry_allowed: yes` on its own violation record.
> Human review cannot be simulated.
> `FALSE_POSITIVE` requires human reviewer decision.

---

## Identity

```yaml
violation_record_id: # Format: AV-{task_id}-{YYYYMMDD}-{sequence}
                     # Example: AV-26.8.1-20260504-001
task_id:             # Active task ID
created_at:          # ISO 8601 timestamp
reviewer:            # MUST be filled by human — agent must use PENDING_HUMAN_ASSIGNMENT
                     # Agent must not fill with own identifier
agent:               # Agent identifier or model used
branch:              # Branch on which violation occurred
```

---

## Source Event

```yaml
source_event:        # What triggered this record: checker output path, command log,
                     # human observation, or brief description
detected_by:         # CHECKER / HUMAN / BOTH
```

---

## Violation Classification

```yaml
violation_category:  # One of the defined violation categories (see policy)
severity:            # LOW / MEDIUM / HIGH / CRITICAL
                     # Must not be set below minimum for category.
                     # Agent must not self-reduce severity.
description:         # Human-readable description of what occurred
```

---

## Affected Artifacts

```yaml
affected_files:      # List of files involved, or NONE
  - path/to/file
commands_involved:   # List of commands involved, or NONE
  - git push origin main
push_target:         # Remote branch targeted, or NONE
```

---

## Corridor State at Violation

```yaml
m25_validation_result:        # PASS / FAIL / WARN / ERROR / NOT_RUN / INCOMPLETE / UNKNOWN
scope_check_result:           # SCOPE_OK / SCOPE_WARNING / SCOPE_VIOLATION / NEEDS_REVIEW / NOT_RUN / UNKNOWN
commit_push_check_result:     # COMMIT_ALLOWED / PUSH_ALLOWED / NEEDS_APPROVAL /
                              # BLOCKED / NEEDS_REVIEW / NOT_RUN / UNKNOWN
open_violations_before:       # Number of open violations before this one, or 0
```

---

## Sanctions

```yaml
sanctions_required:  # List of sanctions required per policy for this violation category
  - REQUIRE_HUMAN_REVIEW
sanctions_applied:   # List of sanctions actually applied (filled by human reviewer)
  - PENDING_HUMAN_REVIEW
```

---

## Post-Violation State

```yaml
permission_after_violation:       # READ_ONLY / PATCH_PROPOSE / LOCAL_EDIT / LOCAL_TEST /
                                  # COMMIT_REQUEST / PUSH_REQUEST / BLOCKED
task_status_after_violation:      # TASK_CONTINUES / TASK_REDUCED / TASK_BLOCKED /
                                  # TASK_RESET_REQUIRED / OWNER_REVIEW_REQUIRED
human_review_required:            # yes / no
owner_escalation_required:        # yes / no
```

---

## Retry

```yaml
retry_allowed:       # yes / no
                     # May be set to yes ONLY by human reviewer or authorized owner.
                     # Agent cannot set retry_allowed: yes on its own violation record.
                     # Retry conditions are defined in 26.9.1 Bounded Retry Loop Policy.
retry_conditions:    # Conditions under which retry is permitted, or NONE
                     # Filled by human reviewer.
```

---

## Reset

```yaml
reset_required:      # yes / no
                     # If yes, task state must be restored before continuation.
                     # Agent cannot initiate or confirm reset.
reset_reference:     # Reference to reset authorization record, or NONE
```

---

## Evidence

```yaml
evidence_artifacts:  # Paths to related evidence artifacts
  - reports/...
related_records:     # Prior violation records if REPEATED_FAILURE applies
  - AV-...
```

---

## Decision

```yaml
decision:    # One of:
             # VIOLATION_CONFIRMED
             # VIOLATION_CONFIRMED_WITH_CONDITIONS
             # NEEDS_HUMAN_REVIEW
             # FALSE_POSITIVE               — requires human reviewer; agent cannot set
             # ESCALATED_TO_OWNER
             # TASK_BLOCKED
             # AGENT_BLOCKED
             #
             # Agent may only set: NEEDS_HUMAN_REVIEW
             # All other values require human reviewer.

notes:       # Reviewer notes, conditions, links to related records
             # Agent may add factual description of event.
             # Agent must not add self-exonerating language.
```

---

## Required Validation Rules

- [ ] violation_record_id is unique
- [ ] task_id matches active task
- [ ] violation_category is from the defined list
- [ ] severity is not below minimum for category
- [ ] reviewer is `PENDING_HUMAN_ASSIGNMENT` if created by agent
- [ ] reviewer is NOT agent identifier
- [ ] decision is `NEEDS_HUMAN_REVIEW` if created by agent
- [ ] sanctions_required matches policy for violation_category
- [ ] retry_allowed: no if created by agent
- [ ] reset_required reflects actual reset need
- [ ] related_records references prior record if `REPEATED_FAILURE`
- [ ] open_violations_before count is accurate

---

## Important Reminders

This Record Is Not Approval

- This violation record is not approval.
- This violation record does not clear the violation.
- `VIOLATION_CONFIRMED` does not authorize merge.
- `VIOLATION_CONFIRMED` does not authorize push.
- `VIOLATION_CONFIRMED` does not bypass M25.
- Sanctions do not convert M25 `FAIL` to `PASS`.

Human Review Cannot Be Simulated

- Agent cannot fill the reviewer field with own identifier.
- Agent cannot set decision to any value other than `NEEDS_HUMAN_REVIEW`.
- Agent cannot set `retry_allowed: yes`.
- Agent cannot mark violation as `FALSE_POSITIVE`.
- Human review cannot be automated or simulated.
- Human review must be explicit and traceable.

Agent Cannot Self-Clear

- Agent cannot clear its own violation.
- Agent cannot reduce severity below policy minimum.
- Agent cannot resume from `BLOCKED` without human decision.
- Agent cannot initiate or confirm `RESET_TO_LAST_SAFE_STATE`.

---

## Usage Notes

- Create one violation record per detected violation.
- Store records in `reports/violations/` or another documented evidence
  directory.
- Link records from the pre-merge execution review.
- Reference records in M26 evidence report when relevant.
- Preserve records for audit trail.
- Violation records must not be modified or deleted by the agent.
