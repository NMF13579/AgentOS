# M41.1 User-Facing Gap Map

PASS is a validation signal, not authorization.
Checker PASS is validation signal, not approval.
Human approval remains above every PASS.
Runtime bypass smoke is not production-grade sandboxing.
Evidence immutability is metadata/hash consistency checking, not cryptographic timestamp authority.

## Operator Gaps After M40
- Users still need one discoverable command map across standalone checkers.
- Token families are understandable per checker, but cross-check navigation is fragmented.
- Strict mode boundaries and "smoke vs enforcement" must be repeated in user-facing outputs.

## Command / Area Guide
Command / Area | Possible Result | Meaning | Next Safe Action | Human Approval Required | Limitation
---|---|---|---|---|---
honest-pass | HONEST_PASS_OK / HONEST_PASS_VIOLATION / HONEST_PASS_NEEDS_REVIEW | proof/trace/binding integrity status | review details and fix proof gaps before completion | yes | does not grant authorization
runtime-bypass-smoke | BYPASS_TEST_PASS / BYPASS_TEST_PASS_WITH_WARNINGS / BYPASS_TEST_FAIL / BYPASS_TEST_NEEDS_REVIEW | controlled bypass simulation outcome | treat warnings/findings as hardening input, not production guarantees | yes | smoke simulation only
validator-authority | VALIDATOR_AUTHORITY_OK / VALIDATOR_AUTHORITY_VIOLATION / VALIDATOR_AUTHORITY_NEEDS_REVIEW | validator trust boundary status | resolve authority ambiguity or mutation risk | yes | metadata-based trust checks
role-separation | ROLE_SEPARATION_OK / ROLE_SEPARATION_VIOLATION / ROLE_SEPARATION_NEEDS_REVIEW | actor separation for risk level | assign independent verifier/approver when required | yes | LOW/MEDIUM exceptions can confuse operators
evidence-immutability | EVIDENCE_IMMUTABILITY_OK / EVIDENCE_IMMUTABILITY_VIOLATION / EVIDENCE_IMMUTABILITY_NEEDS_REVIEW | rewrite/amendment integrity status | preserve failed evidence and attach amendment record | yes | no external timestamp authority
evidence-amendments | EVIDENCE_AMENDMENT_OK / EVIDENCE_AMENDMENT_VIOLATION / EVIDENCE_AMENDMENT_NEEDS_REVIEW | amendment quality and authority status | fix reason/hash/scope/authority fields | yes | authority ambiguity may require manual review
all --strict | PASS/FAIL with strict-integrity stage details | global validation plus strict checks | inspect failed check family and resolve by domain | yes | known unrelated baseline failures may remain

## Recommended M41.2 UX Action
- Add explicit subcommand help for each integrity area.
- Add `next_safe_action` field in machine output for each token family.
- Keep warnings about non-authorization and human approval in all top-level summaries.
