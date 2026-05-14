# Validator Authority Boundary

Execution agent must not create trusted validation authority.
Execution agent must not modify trusted validation authority during execution.
Execution agent must not modify trusted wrapper during execution.
Unknown validation authority must produce NEEDS_REVIEW.
Validator authority PASS is not human approval.

Validator weakening is any change that reduces validation strictness, removes failure detection, downgrades BLOCKED/VIOLATION/NEEDS_REVIEW, or allows clean PASS without required proof.

## Non-Goals
M40.11 does not implement production sandboxing.
M40.11 does not implement evidence immutability.
M40.11 does not replace human approval.
M40.11 does not prove cryptographic validator integrity.
