# Evidence Immutability Policy

Failed evidence must not be silently overwritten.
Completed evidence must not be silently rewritten.
Trace artifacts must not be silently rewritten after completion.
Binding artifacts must not be silently rewritten after PASS.
Completion reviews must not be silently rewritten after final status.
Evidence correction requires amendment record.
Evidence report is not approval.
Evidence Binding is not approval.

Checker validates metadata consistency only; it cannot detect rewrite of both artifact and immutability record simultaneously.

Legacy evidence without immutability metadata must be recorded as legacy limitation, not retroactively treated as tampering.

## Non-Goals
M40.12 does not implement cryptographic timestamp authority.
M40.12 does not implement production tamper-proof storage.
M40.12 does not replace human approval.
M40.12 does not prove legal or compliance-grade retention.
