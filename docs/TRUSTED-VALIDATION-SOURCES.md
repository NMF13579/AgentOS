# Trusted Validation Sources

## Definition
Trusted validation source is a known authority that produced or verified validation artifacts.

## Allowed Source Types
- CI runner
- AgentOS runner
- approved validation entrypoint
- trusted validation wrapper

## Forbidden Source Types
- execution agent-created wrapper
- execution agent-modified validator
- unknown source
- self-declared authority

## Required Rules
Unknown validation source -> HONEST_PASS_NEEDS_REVIEW.
Agent-created validation source -> HONEST_PASS_VIOLATION.
Agent-modified trusted wrapper -> HONEST_PASS_NEEDS_REVIEW or HONEST_PASS_VIOLATION.

## Source Record Fields
- source_id
- source_type
- allowed_commands
- authority_scope
- created_by
- modifiable_by_execution_agent

## Authority Limitation
Trusted validation source registry is not approval.
Trusted validation source registry does not authorize state transition, commit, push, merge, or release.
