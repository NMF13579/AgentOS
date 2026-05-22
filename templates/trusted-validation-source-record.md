# Trusted Validation Source Record Template

Purpose: define trusted validation source registry entries.

Allowed types:
- CI runner
- AgentOS runner
- approved validation entrypoint
- trusted validation wrapper

Forbidden types:
- execution agent-created wrapper
- execution agent-modified validator
- unknown source
- self-declared authority

Unknown validation source -> HONEST_PASS_NEEDS_REVIEW.
Agent-created validation source -> HONEST_PASS_VIOLATION.
Agent-modified trusted wrapper -> HONEST_PASS_NEEDS_REVIEW or HONEST_PASS_VIOLATION.
Trusted validation source registry is not approval.

```json
{
  "trusted_validation_sources": [
    {
      "source_id": "agentos-runner",
      "source_type": "AgentOS runner",
      "allowed_commands": [
        "python3 scripts/agentos-validate.py all --json"
      ],
      "authority_scope": [
        "validation-output",
        "process-trace",
        "evidence-binding"
      ],
      "created_by": "human-or-repo-maintainer",
      "modifiable_by_execution_agent": false
    }
  ]
}
```
