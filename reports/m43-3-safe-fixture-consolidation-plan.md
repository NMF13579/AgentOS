## Purpose
Define safe fixture consolidation planning boundaries without changing fixture files.

## Consolidation Strategy
1. Keep active regression and self-test fixtures intact.
2. Consolidate only overlapping warning/metadata fixture packs first.
3. Preserve positive/negative diagnostic separation.
4. Require human review before any physical fixture merge.

## Conservative Fixture Reduction Path
Conservative fixture reduction target: 10–20%.
- Focus only on clearly overlapping warning fixtures.

## Balanced Fixture Reduction Path
Balanced fixture reduction target: 20–35%.
- Consolidate repeated metadata/warning fixtures with explicit mapping tables.

## Aggressive Fixture Reduction Path
Aggressive fixture reduction target: 35–50%, requires extra review.
- Requires additional gate reviews for failure-class and token equivalence.

## Fixture Manifest Proposal
- `tests/fixtures/integrity-regression/cases.json`
- `tests/fixtures/integrity-regression/inputs/`
- `tests/fixtures/archive/`
M43.3 proposes fixture consolidation only; it does not modify fixture files.

## Do-Not-Touch Fixtures
- `tests/fixtures/integrity-regression/`
- `tests/fixtures/private-evaluator/`
- `tests/fixtures/canary-integrity/`
- `tests/fixtures/process-trace/`
- `tests/fixtures/evidence-binding/`
- `tests/fixtures/validator-authority/`
- `tests/fixtures/role-separation/`
- `tests/fixtures/evidence-immutability/`

## Human Review Gates
- Gate 1: verify shared failure class equivalence.
- Gate 2: verify shared expected result token equivalence.
- Gate 3: verify merged output keeps diagnosis clear.
- Gate 4: verify old-to-new path traceability map.

## Proposed M43.4 Action
Prepare docs/spec consolidation plan using M43.1 and M43.2 references without touching fixtures.

Fixture consolidation must preserve negative coverage.
Do not merge fixtures if failure diagnosis becomes ambiguous.
Do not merge fixtures with different failure classes or expected result tokens.
A merged fixture must preserve traceability to every original fixture.
