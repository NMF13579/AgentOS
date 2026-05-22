# M41.2 Unified Integrity CLI Evidence Report

## M41.1 Status Inspected
- Source: `reports/m41-1-completion-review.md`
- Status: `M41_1_CONSOLIDATION_MAP_COMPLETE_WITH_GAPS`

## honest-pass precondition result
- Command: `python3 scripts/agentos-validate.py honest-pass --help`
- Result: PASS (subcommand exists and usable)

## required fixture path precondition result
All required fixture paths exist:
- `tests/fixtures/validator-authority/positive/trusted-runner-authority/`
- `tests/fixtures/role-separation/positive/high-risk-independent-verifier/`
- `tests/fixtures/evidence-immutability/positive/completed-evidence-unchanged/`
- `tests/fixtures/evidence-amendments/positive/valid-amendment-record/`

## Blocked dependency summary
No blocking dependency detected.

## CLI Changes Made
- Modified: `scripts/agentos-validate.py`
- Added command surfaces:
  - `runtime-bypass-smoke`
  - `validator-authority`
  - `role-separation`
  - `evidence-immutability`
  - `evidence-amendments`
  - `integrity`
- Added `--input` support for domain subcommands.
- Extended `all --strict` to append `integrity --strict --fixtures` stage.

## Source Token Mapping Summary
Implemented mappings from source token families to unified navigation tokens:
- `HONEST_PASS_*` and `HONEST_PASS_FIXTURES_*`
- `BYPASS_TEST_*`
- `VALIDATOR_AUTHORITY_*`
- `ROLE_SEPARATION_*`
- `EVIDENCE_IMMUTABILITY_*`
- `EVIDENCE_AMENDMENT_*`

Unknown source token -> `INTEGRITY_NEEDS_REVIEW`.
Invalid wrapped JSON -> `INTEGRITY_BLOCKED`.

## Aggregate Token Behavior
Implemented aggregate priority:
`INTEGRITY_VIOLATION > INTEGRITY_BLOCKED > INTEGRITY_NEEDS_REVIEW > INTEGRITY_WARNING > INTEGRITY_OK`

## JSON Output Behavior
New unified outputs include:
- `suite`
- `result`
- `source_result`
- `source_failure_class`
- `exit_code`
- `generated_at`
- `details`
- `source_output` for wrapped checks

## Command Results
- `runtime-bypass-smoke --json`: source `BYPASS_TEST_PASS_WITH_WARNINGS`, unified `INTEGRITY_WARNING`
- `validator-authority --input ... --json`: `INTEGRITY_OK`
- `role-separation --input ... --json`: `INTEGRITY_OK`
- `evidence-immutability --input ... --json`: `INTEGRITY_OK`
- `evidence-amendments --input ... --json`: `INTEGRITY_OK`
- `integrity --fixtures --json`: `INTEGRITY_WARNING`
- `integrity --strict --fixtures --json`: `INTEGRITY_WARNING` (exit 0)

Missing-input checks:
- `validator-authority --json` -> `INTEGRITY_NEEDS_REVIEW`, message `validator-authority requires --input`
- `role-separation --json` -> `INTEGRITY_NEEDS_REVIEW`, message `role-separation requires --input`
- `evidence-immutability --json` -> `INTEGRITY_NEEDS_REVIEW`, message `evidence-immutability requires --input`
- `evidence-amendments --json` -> `INTEGRITY_NEEDS_REVIEW`, message `evidence-amendments requires --input`

## all --strict result
- Command runs with integrity stage included.
- Overall result remains FAIL due existing unrelated baseline checks.
- No new all-strict integration blocker observed.

## Validation Commands Run
- All dependency checks and help checks listed in task
- Individual JSON checks for all new subcommands
- Aggregate JSON checks for `integrity` and `integrity --strict`
- Missing-input negative checks
- `all --strict`

## Validation Gaps
- Existing unrelated global validation failures still affect `all --strict` overall result.

## Known Limitations
- Unified status is navigation metadata, not replacement for source token.
- INTEGRITY_WARNING is not clean PASS.
- Hardcoded fixture paths in integrity --fixtures are an M41.2 MVP limitation.

## Recommended M41.3 Action
- Replace hardcoded fixture paths with deterministic fixture registry/manifest.
- Add structured `next_safe_action` guidance per subcheck in unified output.
- Improve top-level `all --strict` explainability for unrelated baseline failures.

## Required Explicit Statements
M41.2 integrates existing integrity checks into the unified CLI.
M41.2 does not create new validators.
M41.2 does not create new policy.
M41.2 does not modify M40 checkers or fixtures.
Unified status is navigation metadata, not replacement for source token.
INTEGRITY_WARNING is not clean PASS.
Hardcoded fixture paths in integrity --fixtures are an M41.2 MVP limitation.
