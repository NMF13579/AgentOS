# Role Separation For Validation

Producer cannot be final verifier for high-risk work.
Implementor cannot be final verifier for high-risk work.
Verifier must not patch the same artifact it verifies.
Human approver must remain separate from execution agent.
Role separation result is not approval.

Risk levels requiring separation: HIGH, CRITICAL.
LOW and MEDIUM work may use same-agent validation only if explicitly recorded as allowed by policy and not used as human approval.
