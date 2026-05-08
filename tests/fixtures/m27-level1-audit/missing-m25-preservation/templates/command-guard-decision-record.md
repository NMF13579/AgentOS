# command-guard-decision-record.md


Guards are mandatory boundaries, not optional helper scripts.
Agent may request actions.
Agent may not directly execute risky actions.
Agent must not bypass runtime guards.
Agent cannot self-approve.
Agent cannot impersonate human reviewer.
Agent cannot use admin token.
Agent cannot clear its own violation.
Agent cannot reset retry count.
Audit records are not approval.
Human gate request is not approval.
COMMAND_ALLOWED does not authorize push, merge, or release.
WRITE_ALLOWED does not authorize commit, push, merge, or release.
GIT_ALLOWED does not authorize push to dev/main, merge, or release.
ENFORCE_ALLOWED is not approval.

M27 preserves M26 corridor boundaries.
Level 2 disabled does not fail Level 1.
SKIPPED_LEVEL_2_NOT_ENABLED
PERMISSION_OK COMMAND_ALLOWED WRITE_ALLOWED GIT_ALLOWED AUDIT_OK HUMAN_GATE_APPROVED SANCTION_REQUIRED RETRY_ALLOWED ENFORCE_ALLOWED PERMISSION_BLOCKED COMMAND_BLOCKED WRITE_BLOCKED GIT_POLICY_VIOLATION AUDIT_TAMPERED HUMAN_GATE_SIMULATED TASK_BLOCKED RETRY_BLOCKED ENFORCE_BLOCKED

