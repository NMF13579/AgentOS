## Purpose
Define a safe consolidation plan for Honest PASS / Unified Integrity artifacts without deleting, moving, or rewriting artifacts in M43.1.

## Consolidation Strategy
1. Separate active authority/runtime artifacts from historical evidence artifacts.
2. Consolidate links and indexes first, not raw evidence files.
3. Apply consolidation only in later milestones with explicit human review.
4. Keep branch traceability from M40 -> M41 -> M42.

Consolidation must preserve auditability, regression coverage, and source-of-truth clarity.

## Safe Consolidation Candidates
- Report groups with repetitive milestone evidence text (`reports/m40-*`, `reports/m41-*`, `reports/m42-1..5-*`) as archive-later candidates.
- Overlapping guidance docs (`INTEGRITY-RESULT-UX`, `ALL-STRICT-INTEGRITY-INTEGRATION`, `INTEGRITY-REGRESSION-CLI-INTEGRATION`) as merge-later docs.
- Template-integrity fixture packs as merge-later candidates only after failure-class map review.

## Report Archival Candidates
- `reports/m40-*.md` -> archive-later bundle with index links to final closure reports.
- `reports/m41-*.md` -> archive-later bundle with index links to M41.6 closure.
- `reports/m42-1-*.md`, `m42-2-*.md`, `m42-3-*.md`, `m42-4-*.md`, `m42-5-*.md` -> archive-later bundles preserving pointer links from M42.6 closure.

Recommended action class for these groups: `ARCHIVE_LATER`.

## Fixture Merge Candidates
Fixtures are mergeable only if the merged fixture preserves all failure classes, expected result tokens, and diagnostic clarity of the original fixtures.

Do not merge fixtures if:
- they test different failure classes
- their expected result tokens differ
- diagnosis would become ambiguous
- a negative fixture would become harder to understand
- regression coverage would be weakened

Fixture consolidation must preserve negative coverage.

Candidate sets:
- `tests/fixtures/template-integrity/*` packs with similar structure warnings.
- select M42 integrity-regression cases with same failure class and same expected token only.

## Docs Merge Candidates
- `docs/INTEGRITY-RESULT-UX.md` + `docs/HONEST-PASS-RESULT-CONTRACT.md` (single result-behavior guide).
- `docs/ALL-STRICT-INTEGRITY-INTEGRATION.md` + `docs/INTEGRITY-REGRESSION-CLI-INTEGRATION.md` (single integration guide).
- Keep policy docs separate when they define different boundaries (`VALIDATOR-AUTHORITY`, `ROLE-SEPARATION`, `EVIDENCE-IMMUTABILITY`).

## Schema / Template Simplification Candidates
- Keep all currently active schemas/templates unchanged in M43.1.
- Later simplification candidate: add a consolidated mapping doc linking each template to its schema/checker.
- No schema or template merge until runtime and fixture references are revalidated.

## Script Consolidation Candidates
- Keep runtime entrypoints unchanged: `scripts/agentos-validate.py`, `scripts/test-integrity-regression.py`.
- Review-later candidates: older helper paths that overlap newer flows (`scripts/test-gate-regression-fixtures.py` vs newer regression runner scope).
- For standalone checkers, prefer wrapper-level simplification later, not checker deletion.

## Do-Not-Touch List
- `reports/m42-6-completion-review.md`
- `reports/m42-6-honest-pass-integrity-final-closure-report.md`
- `reports/m42-6-final-capability-matrix.md`
- `reports/m42-6-final-gaps-and-deferred-items.md`
- `scripts/agentos-validate.py`
- `scripts/test-integrity-regression.py`
- `tests/fixtures/integrity-regression/`
- `tests/fixtures/integrity-fixture-registry.json`
- `docs/VALIDATOR-AUTHORITY-BOUNDARY.md`
- `docs/ROLE-SEPARATION-FOR-VALIDATION.md`
- `docs/EVIDENCE-IMMUTABILITY-POLICY.md`

## Proposed M43.2+ Task Sequence
- M43.2 — historical report archive plan
- M43.3 — fixture consolidation plan
- M43.4 — docs/spec consolidation plan
- M43.5 — script entrypoint simplification plan
- M43.6 — post-consolidation validation review

Target reduction bands:
- Conservative reduction target: 25–35%.
- Balanced reduction target: 35–50%.
- Aggressive reduction target: 50–60%, requires extra review.
