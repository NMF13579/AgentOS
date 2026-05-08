# Fixture
- scenario: exit-zero-without-pass-result
- expected mode: both
- expected result: CONTEXT_COMPLIANCE_INCOMPLETE
- what makes the fixture pass/warning/missing/invalid/violation/incomplete/blocked/needs_review: synthetic marker
- safety notes: inert fixture
- non-authorization statement: fixture is not approval

- This fixture documents a downstream gate responsibility.
- The checker itself may not be able to simulate its own inconsistent process exit.
- Required callers must validate both conditions:
  - process exit code is 0
  - explicit result value is CONTEXT_COMPLIANCE_PASS
- If either condition is missing, malformed, or inconsistent, downstream gates must treat the result as CONTEXT_COMPLIANCE_INCOMPLETE.
