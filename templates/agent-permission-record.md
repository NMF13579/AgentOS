---
type: template
module: m26-pre-merge-corridor
status: active
authority: supporting
version: 1.0.0
created: 2026-05-03
task_id: 26.2.1
milestone: M26
---

# Agent Permission Record

## Purpose

Record a permission change for an agent operating within the M26 pre-merge corridor.

This template records a permission decision for audit and traceability.
It does not grant approval.
It does not authorize merge.
It does not authorize push.

---

## Permission Record Fields

```yaml
permission_record_id:  # Format: PR-{task_id}-{YYYYMMDD}-{sequence}
                       # Example: PR-26.2.1-20260503-001

task_id:               # ID of the active task anchoring this permission
created_at:            # ISO 8601 timestamp of this record
reviewer:              # Human reviewer name or identifier; must not be agent or CI
agent:                 # Agent identifier or model used
branch:                # Branch on which execution occurs

current_permission:    # Current permission value before this decision
                       # READ_ONLY / PATCH_PROPOSE / LOCAL_EDIT / LOCAL_TEST /
                       # COMMIT_REQUEST / PUSH_REQUEST / BLOCKED

requested_permission:  # Permission value being requested or assigned
                       # READ_ONLY / PATCH_PROPOSE / LOCAL_EDIT / LOCAL_TEST /
                       # COMMIT_REQUEST / PUSH_REQUEST / BLOCKED

reason:                # Why this permission change is being requested or applied

declared_scope:        # Scope active at time of this permission decision
  - path/to/allowed/directory/
  - path/to/allowed/file.md

risk_level:            # LOW / MEDIUM / HIGH / CRITICAL

approval_required:     # yes / no — fill required; do not substitute default for review

approval_record:       # Reference to human approval record if approval_required: yes
  - (none)             # Path to approval file or explicit N/A with reason

conditions:            # Any conditions attached to this permission grant
  - (none)             # List conditions explicitly; (none) only if truly unconditional

expiration:            # When this permission expires
                       # Format: ISO 8601 datetime, or TASK_COMPLETION, or EXPLICIT_REVOCATION
                       # Default: TASK_COMPLETION
                       # Permission expires when the active task closes unless stated otherwise

violations_open:       # Open violations at time of this decision
  - (none)             # If populated, escalation to COMMIT_REQUEST or PUSH_REQUEST is blocked

decision:              # PERMISSION_GRANTED / PERMISSION_GRANTED_WITH_CONDITIONS /
                       # NEEDS_HUMAN_REVIEW / PERMISSION_DENIED / PERMISSION_REDUCED / BLOCKED

notes:                 # Additional reviewer observations
```

---

## Allowed Permission Values

| Value | Meaning |
|---|---|
| `READ_ONLY` | Inspect and summarize only; no writes |
| `PATCH_PROPOSE` | Propose patch text; no direct file writes |
| `LOCAL_EDIT` | Edit allowed files within declared scope |
| `LOCAL_TEST` | Run safe validation and test commands |
| `COMMIT_REQUEST` | Prepare commit proposal for human review; not commit by default |
| `PUSH_REQUEST` | Request push approval from human or runner; not push by default |
| `BLOCKED` | Execution stopped; human review required before any action |

---

## Allowed Decision Values

| Decision | Meaning |
|---|---|
| `PERMISSION_GRANTED` | Permission value assigned. This is not approval. Conditions may apply. |
| `PERMISSION_GRANTED_WITH_CONDITIONS` | Permission value assigned subject to explicit conditions listed in `conditions` field. This is not approval. |
| `NEEDS_HUMAN_REVIEW` | Decision deferred. Human review required before permission changes. |
| `PERMISSION_DENIED` | Permission change denied. Agent remains at current permission value. |
| `PERMISSION_REDUCED` | Permission reduced, typically following a violation. New value in `requested_permission`. |
| `BLOCKED` | Agent is blocked. Execution stopped until human exit decision. |

---

## Risk Level Reference

| Risk Level | Typical Trigger |
|---|---|
| `LOW` | READ_ONLY, PATCH_PROPOSE, LOCAL_TEST grants |
| `MEDIUM` | LOCAL_EDIT grant; first edit in new scope |
| `HIGH` | COMMIT_REQUEST or PUSH_REQUEST grant; post-violation escalation |
| `CRITICAL` | Any escalation while violations are open; protected zone write request |

---

## Important Reminders

### This Record Is Not Approval

- This permission record is not approval
- `PERMISSION_GRANTED` is not approval
- Permission record does not authorize merge
- Permission record does not authorize push
- Permission value does not bypass M25 enforcement
- Permission value does not expand declared scope
- Permission record does not satisfy M25 override requirements

### Human Approval Cannot Be Simulated

- Agent cannot fill the `reviewer` field
- Human approval cannot be simulated, implied, or derived from permission value
- Human approval cannot be granted by the agent
- Human approval cannot be automatic

### Violation Rules

- If `violations_open` is populated, escalation to `COMMIT_REQUEST` or `PUSH_REQUEST` is blocked
- Any decision to escalate while violations are open requires explicit human review
- `BLOCKED` state may only be exited by explicit human decision recorded in a new permission record

### Expiration Rules

- Permission expires at `TASK_COMPLETION` by default
- Expired permissions must be re-evaluated for the next task
- Expiration does not automatically reduce to `BLOCKED`; it resets to task default
- Explicit expiration datetime overrides `TASK_COMPLETION` default

---

## Usage Notes

- Create one permission record per permission change
- Store records in `reports/permissions/` or another documented evidence directory
- Link records from the task completion report
- Reference records in the M26 evidence report
- Reference records in pre-merge execution reviews when relevant
- Preserve records for audit trail

**This template does not grant approval. It records permission decisions for review.**
