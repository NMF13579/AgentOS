---
type: template
module: m26-pre-merge-corridor
status: active
authority: supporting
version: 1.0.0
created: 2026-05-04
task_id: 26.6.1
milestone: M26
---

# Push Request Record

## Purpose

Record a push request decision for an agent operating within the M26
pre-merge execution corridor.

This record is not approval by itself.
Only an explicit human decision inside the record may approve an approvable push.

This record is not merge approval.
This record is not release approval.
`PUSH_APPROVED` is not merge approval.
`PUSH_APPROVED` does not bypass M25.
`PUSH_APPROVED` does not convert M25 `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` to `PASS`.

Agent cannot fill the `reviewer` field.
Human approval cannot be simulated.

## Push Request Record Fields

```yaml
push_request_id:       # Format: PUSH-{task_id}-{YYYYMMDD}-{sequence}
                       # Example: PUSH-26.6.1-20260504-001

task_id:               # ID of the active task anchoring this push request
created_at:            # ISO 8601 timestamp of this record
reviewer:              # Human reviewer name or identifier; must not be agent or CI
agent:                 # Agent identifier or model used
branch:                # Local branch being pushed

source_branch:         # Branch origin if created from another branch
target_remote:         # Remote name, e.g. origin
target_branch:         # Remote branch name

protected_branch_target:          # yes / no
remote_branch_exists:             # yes / no / unknown
remote_branch_creation_requested: # yes / no

push_type:             # FEATURE_BRANCH_PUSH / REMOTE_BRANCH_CREATE / TAG_PUSH /
                       # FORCE_PUSH / PROTECTED_BRANCH_PUSH /
                       # REMOTE_BRANCH_DELETE / UNKNOWN

scope_check_result:    # SCOPE_OK / SCOPE_WARNING / SCOPE_VIOLATION / NEEDS_REVIEW
scope_check_artifact:  # Path or reference to scope checker output

m25_validation_result:   # PASS / FAIL / WARN / ERROR / NOT_RUN / INCOMPLETE
m25_validation_artifact: # Path or reference to M25 validation output
m25_override_record:     # Path to override record, or NONE

commit_reference:        # Full git commit SHA; not branch name or tag
changed_files_summary:   # Brief description or count of changed files

risk_level:              # LOW / MEDIUM / HIGH / CRITICAL / PUSH_BLOCKED
approval_required:       # yes / no

approval_record:         # Reference to approval artifact, or NONE
conditions:              # Conditions attached to approval, or NONE
expiration:              # ISO 8601 expiration datetime, TASK_COMPLETION, ONE_TIME, or NONE

violations_open:         # yes / no — any open scope/push/corridor violation

decision:                # PUSH_APPROVED / PUSH_APPROVED_WITH_CONDITIONS /
                         # NEEDS_HUMAN_REVIEW / PUSH_DENIED / PUSH_BLOCKED

notes:                   # Reviewer notes, conditions, links to related records
```

## Allowed Push Type Values

| Value | Meaning |
|---|---|
| `FEATURE_BRANCH_PUSH` | Push to an existing non-protected remote branch. |
| `REMOTE_BRANCH_CREATE` | Create a new remote branch. |
| `TAG_PUSH` | Push a git tag. Requires explicit authorization. |
| `FORCE_PUSH` | Force push. Must result in `PUSH_BLOCKED`. |
| `PROTECTED_BRANCH_PUSH` | Direct push to dev, main, or another protected branch. Must result in `PUSH_BLOCKED`. |
| `REMOTE_BRANCH_DELETE` | Delete a remote branch. Must result in `PUSH_BLOCKED`. |
| `UNKNOWN` | Push type cannot be determined. Must result in `NEEDS_HUMAN_REVIEW`. |

## Allowed Decision Values

| Decision | Meaning |
|---|---|
| `PUSH_APPROVED` | Explicit human decision approving an approvable push after all preconditions are satisfied. |
| `PUSH_APPROVED_WITH_CONDITIONS` | Explicit human decision approving an approvable push subject to listed conditions. |
| `NEEDS_HUMAN_REVIEW` | Preconditions incomplete or ambiguous; human review required. |
| `PUSH_DENIED` | Push explicitly denied; new request required. |
| `PUSH_BLOCKED` | Push blocked; no approval path available under this policy. |

## Risk Level Reference

| Risk Level | Typical Trigger |
|---|---|
| `LOW` | Reserved for future low-risk remote operations. Not normally used for push. |
| `MEDIUM` | Existing feature branch push with `SCOPE_OK` and M25 `PASS`. |
| `HIGH` | Remote branch creation, tag push, or push after resolved `SCOPE_WARNING`. |
| `CRITICAL` | Push with valid M25 override. |
| `PUSH_BLOCKED` | Protected branch push, force push, remote branch deletion, or blocked precondition. |

## Required Validation Rules

- If `protected_branch_target: yes`, decision must be `PUSH_BLOCKED`.
- If `push_type: PROTECTED_BRANCH_PUSH`, decision must be `PUSH_BLOCKED`.
- If `push_type: FORCE_PUSH`, decision must be `PUSH_BLOCKED`.
- If `push_type: REMOTE_BRANCH_DELETE`, decision must be `PUSH_BLOCKED`.
- If `push_type: UNKNOWN`, decision must be `NEEDS_HUMAN_REVIEW`.
- If `remote_branch_creation_requested: yes`, risk level must be at least `HIGH`.
- If `scope_check_result: SCOPE_VIOLATION`, decision must be `PUSH_BLOCKED`.
- If unresolved `scope_check_result: NEEDS_REVIEW`, decision must be `NEEDS_HUMAN_REVIEW` or `PUSH_BLOCKED`.
- If M25 result is `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` without override, decision must be `PUSH_BLOCKED`.
- If `violations_open: yes`, decision must be `PUSH_BLOCKED` or `NEEDS_HUMAN_REVIEW`.

## Precondition Checklist

Complete before submitting for human review:

- scope_check_result is `SCOPE_OK` or `SCOPE_WARNING` with conditions documented.
- scope_check_result is not `SCOPE_VIOLATION`.
- scope_check_result is not unresolved `NEEDS_REVIEW`.
- m25_validation_result is `PASS` or `m25_override_record` is valid.
- m25_validation_result is not `FAIL`, `WARN`, `ERROR`, `NOT_RUN`, or `INCOMPLETE` without override.
- push_request_id is unique.
- commit_reference is a full SHA, not a branch name or tag.
- protected_branch_target is `no`.
- push_type is not `PROTECTED_BRANCH_PUSH`.
- push_type is not `FORCE_PUSH`.
- push_type is not `REMOTE_BRANCH_DELETE`.
- remote branch creation is explicitly authorized if requested.
- tag push is explicitly authorized if requested.
- violations_open is `no`.
- expiration is not in the past.
- reviewer field is not filled by agent.

## Important Reminders

This record is not merge approval.
This record is not release approval.
`PUSH_APPROVED` is not merge approval.
`PUSH_APPROVED` is not release approval.
`PUSH_APPROVED` does not bypass M25.
`PUSH_APPROVED` does not convert M25 result to `PASS`.

Human approval cannot be simulated.
Agent cannot fill the reviewer field.
Human approval cannot be granted by CI.
Human approval cannot be automatic.
Human approval must be explicit and traceable.

Blocked push rules:

- Protected branch push is blocked.
- Force push is blocked.
- Remote branch deletion is blocked.
- Push after `SCOPE_VIOLATION` is blocked.
- Push with unresolved M25 failure is blocked.
- Push after expired approval is blocked until renewed.

## Usage Notes

- Create one push request record per push request.
- Push approval is per branch, per commit, and time-limited.
- Store records in `reports/push-requests/` or another documented evidence directory.
- Link records from the pre-merge execution review.
- Reference records in M26 evidence report when relevant.
- Preserve records for audit trail.

This template does not by itself grant approval. It records push request decisions for review.
