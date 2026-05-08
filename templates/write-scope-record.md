---
type: template
module: m26-pre-merge-corridor
status: active
authority: supporting
version: 1.0.0
created: 2026-05-04
task_id: 26.4.1
milestone: M26
---

# Write Scope Record

## Purpose

Record a write scope decision for an agent operating within the M26
pre-merge execution corridor.

This template records a write scope decision for audit and traceability.
It does not by itself grant approval.
It does not authorize merge.
It does not authorize push.
It does not satisfy M25 override requirements.

---

## Write Scope Record Fields

```yaml
write_scope_record_id:      # Format: WS-{task_id}-{YYYYMMDD}-{sequence}
                            # Example: WS-26.4.1-20260504-001

task_id:                    # ID of the active task anchoring this write scope
created_at:                 # ISO 8601 timestamp of this record
reviewer:                   # Human reviewer name or identifier; must not be agent or CI
agent:                      # Agent identifier or model used
branch:                     # Branch on which writes occur

declared_scope:             # Full declared scope for the active task
  - path/to/allowed/directory/
  - path/to/allowed/file.md

allowed_write_paths:        # Paths explicitly allowed for this task execution
  - (none)                  # List all paths; (none) only if no writes are planned

conditional_write_paths:    # Paths requiring approval; list with approval reference
  - path: (none)
    approval: (none)

forbidden_write_paths:      # Confirmation that no normal agent writes occurred to forbidden paths
  confirmed_no_normal_agent_writes: yes

protected_zones:            # Confirmation that protected zones were not modified by normal agent writes
  confirmed_no_normal_agent_writes: yes
  owner_controlled_exception: no
  owner_approval: (none)

requested_write_paths:      # All paths the agent requests or has written to
  - (none)

expected_generated_artifacts:  # Generated output files from task execution
  - (none)                     # May persist after task completion if task-scoped

expected_temp_artifacts:    # Temporary/cache/test artifacts from command execution
  - (none)                  # Must not be committed; cleaned up after task unless unsafe/not required

deletions_requested:        # Files the agent requests to delete
  - (none)                  # Deletion requires explicit task contract authorization

risk_level:                 # LOW / MEDIUM / HIGH / CRITICAL

approval_required:          # yes / no - fill required; do not substitute default for review

approval_record:            # Reference to human approval if approval_required: yes
  - (none)                  # Path to approval file or explicit N/A with reason

conditions:                 # Any conditions attached to this write scope approval
  - (none)                  # List conditions explicitly; (none) only if truly unconditional

expiration:                 # When this write scope approval expires
                            # Format: ISO 8601 datetime, or TASK_COMPLETION
                            # Default: TASK_COMPLETION
                            # Write scope approvals are valid for the task duration by default

violations_open:            # Open violations at time of this decision
  - (none)                  # If populated, CONDITIONAL and PROTECTED_ZONE writes are blocked

decision:                   # WRITE_SCOPE_APPROVED / WRITE_SCOPE_APPROVED_WITH_CONDITIONS /
                            # NEEDS_HUMAN_REVIEW / WRITE_SCOPE_DENIED / WRITE_SCOPE_BLOCKED

notes:                      # Additional reviewer observations
```

---

## Allowed Write Category Values

| Value | Meaning |
|---|---|
| `ALLOWED_WRITE_PATH` | Path explicitly allowed within declared scope |
| `CONDITIONAL_WRITE_PATH` | Path requiring additional approval before write |
| `FORBIDDEN_WRITE_PATH` | Path blocked for normal agent execution |
| `PROTECTED_ZONE` | High-risk system path; owner-controlled exception required |
| `EVIDENCE_ARTIFACT` | Evidence/audit file; append-only if in progress, read-only if completed |
| `GENERATED_ARTIFACT` | Intended task output; may persist if task-scoped and documented |
| `TEMP_ARTIFACT` | Incidental command output; must not be committed; cleanup policy-dependent |

---

## Allowed Decision Values

| Decision | Meaning |
|---|---|
| `WRITE_SCOPE_APPROVED` | Explicit human decision approving the write scope. Not merge approval. |
| `WRITE_SCOPE_APPROVED_WITH_CONDITIONS` | Explicit human decision approving subject to listed conditions. Not merge approval. |
| `NEEDS_HUMAN_REVIEW` | Decision deferred. Human review required before writes occur. |
| `WRITE_SCOPE_DENIED` | Write scope denied. Writes must not proceed. |
| `WRITE_SCOPE_BLOCKED` | Write scope blocked. Corridor violation may be recorded. |

---

## Risk Level Reference

| Risk Level | Typical Trigger |
|---|---|
| `LOW` | Writes to declared ALLOWED_WRITE_PATH only; no deletions |
| `MEDIUM` | Writes to CONDITIONAL_WRITE_PATH; first write in new scope area |
| `HIGH` | Deletions; writes near protected zones; any write while violations exist |
| `CRITICAL` | Any protected-zone exception; evidence correction; writes with open violations |

---

## Expiration Reference

| Expiration | Meaning |
|---|---|
| `TASK_COMPLETION` | Write scope is valid for the duration of the active task (default) |
| ISO 8601 datetime | Write scope expires at the specified time |

Write scope approvals default to `TASK_COMPLETION` because scope boundaries
are task-level constructs, not single-operation constructs.

---

## GENERATED_ARTIFACT vs TEMP_ARTIFACT

| Property | GENERATED_ARTIFACT | TEMP_ARTIFACT |
|---|---|---|
| Purpose | Intended task output | Incidental command output |
| May persist after task | Yes, if task-scoped | No, unless cleanup unsafe/not required |
| May be committed | Yes, if intended task output and explicitly scoped | Never |
| Cleanup required | No, unless task policy requires | Yes, when safe and required |
| Must be documented | Yes, in expected_generated_artifacts | Yes, in expected_temp_artifacts |
| May overwrite evidence | Never | Never |
| May be in protected zone | Never | Never |

---

## Important Reminders

### This Record Is Not Approval By Itself

- This write scope record alone is not approval
- Only an explicit human decision inside the record may approve an approvable write scope
- `WRITE_SCOPE_APPROVED` is not merge approval
- `WRITE_SCOPE_APPROVED` is not push authorization
- Write scope record does not authorize merge
- Write scope record does not authorize push
- Write scope record does not satisfy M25 override requirements
- Write path category does not bypass M25 enforcement
- Write path category does not expand declared scope

### Human Approval Cannot Be Simulated

- Agent cannot fill the `reviewer` field
- Human approval cannot be simulated, implied, or derived from write category
- Human approval cannot be granted by the agent
- Human approval cannot be granted by CI
- Human approval cannot be automatic

### Violation Rules

- If `violations_open` is populated, conditional and protected-zone writes are blocked
- Any normal agent write to a FORBIDDEN_WRITE_PATH is always a violation
- Any unauthorized modification to a completed EVIDENCE_ARTIFACT is always a violation
- Decision `WRITE_SCOPE_BLOCKED` must escalate to human owner
- Deletion without explicit task authorization is always a violation
- Owner-controlled protected-zone exceptions must be explicit and documented

### Expiration Rules

- Write scope approvals default to `TASK_COMPLETION`
- Expired write scope must be re-evaluated for the next task
- Expiration does not block already-written files; it constrains future writes
- Explicit datetime expiration overrides `TASK_COMPLETION` default

---

## Usage Notes

- Create one write scope record per task execution where non-trivial writes occur
- Always create a write scope record when deletions are requested
- Always create a write scope record when conditional write paths are accessed
- Always create a write scope record for protected-zone exceptions
- Store records in `reports/write-scope/` or another documented directory
- Link records from the task completion report
- Reference records in the pre-merge execution review
- Reference records in the M26 evidence report when relevant
- Preserve records for audit trail

**This template does not by itself grant approval. It records write scope decisions for review.**
