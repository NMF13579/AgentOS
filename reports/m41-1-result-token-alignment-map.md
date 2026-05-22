# M41.1 Result Token Alignment Map

Token alignment must not erase domain-specific meaning.
Unified status is navigation metadata, not replacement for source token.

## Token Families

| Family | Success | Violation/Failure | Needs-Review | Warning | Exit Semantics | Unified Mapping | Ambiguity | Recommended Standardization |
|---|---|---|---|---|---|---|---|---|
| HONEST_PASS_* | HONEST_PASS_OK | HONEST_PASS_VIOLATION | HONEST_PASS_NEEDS_REVIEW | none | OK->0, others->1 | clean | low | keep as primary proof-domain tokens |
| HONEST_PASS_FIXTURES_* | HONEST_PASS_FIXTURES_OK | HONEST_PASS_FIXTURES_FAILED | HONEST_PASS_FIXTURES_NEEDS_REVIEW | none | OK->0, others->1 | clean | medium (fixture-scope only) | map to HONEST_PASS_* in wrappers but keep source token |
| BYPASS_TEST_* | BYPASS_TEST_PASS | BYPASS_TEST_FAIL | BYPASS_TEST_NEEDS_REVIEW | BYPASS_TEST_PASS_WITH_WARNINGS | PASS/WARN->0, FAIL/REVIEW->1 | partial | medium (warning semantics) | normalize warning -> unified WARNING, keep source token |
| VALIDATOR_AUTHORITY_* | VALIDATOR_AUTHORITY_OK | VALIDATOR_AUTHORITY_VIOLATION | VALIDATOR_AUTHORITY_NEEDS_REVIEW | none | OK->0, others->1 | clean | low | map directly to OK/VIOLATION/NEEDS_REVIEW |
| ROLE_SEPARATION_* | ROLE_SEPARATION_OK | ROLE_SEPARATION_VIOLATION | ROLE_SEPARATION_NEEDS_REVIEW | none | OK->0, others->1 | clean | low | map directly to OK/VIOLATION/NEEDS_REVIEW |
| EVIDENCE_IMMUTABILITY_* | EVIDENCE_IMMUTABILITY_OK | EVIDENCE_IMMUTABILITY_VIOLATION | EVIDENCE_IMMUTABILITY_NEEDS_REVIEW | none | OK->0, others->1 | clean | medium (LEGACY path) | preserve LEGACY-driven NEEDS_REVIEW rationale |
| EVIDENCE_AMENDMENT_* | EVIDENCE_AMENDMENT_OK | EVIDENCE_AMENDMENT_VIOLATION | EVIDENCE_AMENDMENT_NEEDS_REVIEW | none | OK->0, others->1 | clean | medium (authority ambiguity) | keep first failure class + detail list |

## Proposed Unified Navigation Status
- `OK`
- `VIOLATION`
- `NEEDS_REVIEW`
- `WARNING`
- `BLOCKED`

## Mapping Notes
- `BYPASS_TEST_PASS_WITH_WARNINGS` -> unified `WARNING`
- any `*_NEEDS_REVIEW` -> unified `NEEDS_REVIEW`
- source token is always preserved in output payload

## M41.2 Recommendation
Define a standard envelope:
- `source_token`
- `unified_status`
- `failure_class`
- `blocking`
- `next_safe_action`
without rewriting domain semantics.
