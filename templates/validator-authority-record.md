# Validator Authority Record Template

Validator authority record is integrity evidence, not approval.
trusted_wrapper.path is informational only in M40.11.
M40.11 does not require hashing live repository validator files.

```json
{
  "task_id": "task-smoke-001",
  "execution_agent_id": "developer-agent",
  "trusted_validation_sources": [
    {
      "source_id": "agentos-runner",
      "source_type": "AgentOS runner",
      "created_by": "human-or-repo-maintainer",
      "created_during_execution": false,
      "modified_by_execution_agent": false
    }
  ],
  "validator_artifacts": [
    {
      "path": "artifacts/check-process-trace-stub.py",
      "sha256_before": "sha256:...",
      "sha256_after": "sha256:...",
      "modified_during_execution": false,
      "modified_by": null,
      "strictness_reduced": false
    }
  ],
  "trusted_wrapper": {
    "path": "scripts/agentos-validate.py",
    "created_by": "human-or-repo-maintainer",
    "created_during_execution": false,
    "modified_during_execution": false,
    "modified_by_execution_agent": false
  },
  "failure_context": {
    "previous_result": "HONEST_PASS_VIOLATION",
    "validator_changed_after_failure": false
  }
}
```
