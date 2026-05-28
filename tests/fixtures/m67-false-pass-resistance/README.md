# M67 False PASS Resistance Fixtures

## 1. Purpose
M67 fixtures are not approval.
M67 fixtures do not complete tasks.
M67 fixtures do not mutate lifecycle state.
M67 fixtures do not start M68.
Human review remains required.

## 2. Fixture Categories
This suite uses five categories:
- positive
- warning
- not-enough
- negative
- malformed

## 3. Positive Fixtures
Positive fixtures prove safe non-authority validation PASS language is accepted.

## 4. Warning Fixtures
Warning fixtures prove non-blocking warnings remain visible and do not become clean PASS.

## 5. Not-Enough Fixtures
Not-enough fixtures prove inconclusive false PASS safety does not pass as clean validation.

## 6. Negative Fixtures
Negative fixtures prove fake approval, fake completion, fake gate pass, human review waiver, lifecycle mutation, production readiness, and M68 auto-start claims block.

## 7. Malformed Fixtures
Malformed fixtures cover more than one malformed scenario.
Malformed coverage is not limited to one invalid JSON file.

## 8. Safe Context Boundary
Fixture names may contain forbidden terms because they describe test cases.
Documentation examples may contain forbidden terms if clearly marked as examples.
Fixture content is still evaluated according to expected result.

## 9. Non-Authority Boundary
Fixture PASS is not approval.
Fixture PASS does not complete tasks.
Fixture PASS does not mutate lifecycle state.
Fixture PASS does not start M68.
Human review remains required.

## 10. Expected Results Manifest
`expected-results.json` lists every fixture, its expected result, and its expected exit code.

## 11. How To Run
Use:
`python3 scripts/check-false-pass-resistance.py --input <fixture-path> --json`

Optional strict mode:
`python3 scripts/check-false-pass-resistance.py --input <fixture-path> --json --strict`

## 12. Final Status
FINAL_STATUS: M67_FALSE_PASS_FIXTURES_COMPLETE_WITH_WARNINGS
