## Purpose
Map fixture coverage constraints before any future consolidation.

## Coverage Preservation Principles
Fixture consolidation must preserve failure-class coverage, result-token coverage, and diagnostic clarity.
A merged fixture must not make failure diagnosis ambiguous.
Negative fixtures must remain capable of proving that bad cases fail.
Positive fixtures must remain capable of proving that valid cases pass.

## Failure Class Coverage
- COMMAND_CONTRACT_REGRESSION: found
- JSON_CONTRACT_REGRESSION: found
- JSON_FIELD_REGRESSION: found
- TOKEN_CONTRACT_REGRESSION: not_found
- SUMMARY_CONTRACT_REGRESSION: found
- UNKNOWN_TOKEN_REGRESSION: found
- ARGPARSE_ABBREVIATION_REGRESSION: found
- SUMMARY_JSON_CONFLICT_REGRESSION: found
- AUTHORITY_BOUNDARY_MISSING: found
- FALSE_AUTHORITY_CLAIM_REGRESSION: found
- SHELL_TRUE_REGRESSION: found
- FIXTURE_ROOT_MISSING: not_found

## Result Token Coverage
- NEGATIVE_EXPECT_FAIL: found
- POSITIVE_EXPECT_PASS: found
- NEEDS_REVIEW: found
- INTEGRITY_REGRESSION_TOKEN: found

## Negative Fixture Coverage
- Negative fixtures are present across integrity, authority, trace, binding, canary, and policy-oriented roots.

## Positive Fixture Coverage
- Positive fixtures are present and must remain separated from negative fixtures for clear diagnosis.

## Diagnostic Clarity Review
- Keep separate where positive/negative semantics differ.
- Keep separate where failure classes differ.
- Use merge-later only after explicit equivalence proof.

## Merge Safety Matrix
Candidate Fixture(s) | Shared Failure Class | Shared Result Token | Diagnostic Risk | Merge Recommendation | Reason
--- | --- | --- | --- | --- | ---
| `tests/fixtures/template-integrity/missing-fixtures-warning/*` + `tests/fixtures/template-integrity/missing-optional-report-warning/*` | partial overlap | mixed | medium | MERGE_LATER_WITH_REVIEW | overlap exists but diagnostic intent differs by warning type |
| `tests/fixtures/integrity-regression/unknown-token-exit-zero-fail/*` + `tests/fixtures/integrity-regression/unknown-integrity-token-fail/*` | UNKNOWN_TOKEN_REGRESSION | similar | medium | KEEP_SEPARATE | token contracts and payload shapes can differ |
| `tests/fixtures/integrity-regression/summary-json-conflict-exit-zero-fail/*` + `tests/fixtures/integrity-regression/summary-missing-human-approval-fail/*` | different | different | high | KEEP_SEPARATE | summary conflict vs approval omission are distinct failures |
| `tests/fixtures/canary-integrity/negative/*` variants | canary integrity failures | NEGATIVE_EXPECT_FAIL | low | MERGE_LATER_SAFE | only if merged case preserves per-variant diagnosis fields |
| `tests/fixtures/m27-*` legacy sets | unknown_needs_review | mixed | medium | UNKNOWN_NEEDS_REVIEW | active runtime dependency unclear in current scope |

## Coverage Gaps
- `TOKEN_CONTRACT_REGRESSION`: not_found in current direct fixture-name scan.
- `FIXTURE_ROOT_MISSING`: not_found as fixture file pattern; appears in command-level evidence text.
