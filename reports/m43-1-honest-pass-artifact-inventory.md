## Executive Summary
M42.6 precondition status found: `M42_6_HONEST_PASS_INTEGRITY_COMPLETE_WITH_GAPS`.

M43.1 does not delete, move, archive, or rewrite artifacts.
Historical evidence is not runtime authority.
Active source of truth must not be removed during footprint optimization.

Classification honesty rule:
- Only classify an artifact as ACTIVE_ if active use is verifiable from code references, CLI entrypoints, registries, schema/template links, or explicit completion-review references.
- If active use is not verifiable, classify as `UNKNOWN_NEEDS_REVIEW`.
- Do not invent references.

## Inventory Scope
Read-only audit scope:
- `docs/`
- `schemas/`
- `templates/`
- `scripts/`
- `tests/fixtures/`
- `reports/m40-*`, `reports/m41-*`, `reports/m42-*`
- `README.md`

Excluded from modification:
- scripts, docs, schemas, templates, fixtures, old reports

## Docs Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`docs/HONEST-PASS-HARDENING.md` | doc | ACTIVE_SOURCE_OF_TRUTH | branch hardening policy context | `README.md` | KEEP_AND_LINK | canonical context doc
`docs/HONEST-PASS-RESULT-CONTRACT.md` | doc | ACTIVE_SOURCE_OF_TRUTH | result token meaning | `README.md` | KEEP_AND_LINK | protects wording consistency
`docs/VALIDATOR-AUTHORITY-BOUNDARY.md` | doc | ACTIVE_SOURCE_OF_TRUTH | validator authority boundary | `README.md`, `reports/m42-1-authority-boundary-regression-map.md` | KEEP | safety-critical boundary
`docs/ROLE-SEPARATION-FOR-VALIDATION.md` | doc | ACTIVE_SOURCE_OF_TRUTH | role split rules | `README.md` | KEEP | linked with M40.11
`docs/EVIDENCE-IMMUTABILITY-POLICY.md` | doc | ACTIVE_SOURCE_OF_TRUTH | immutability guard policy | `README.md` | KEEP | linked with M40.12
`docs/INTEGRITY-REGRESSION-CLI-INTEGRATION.md` | doc | ACTIVE_RUNTIME_ENTRYPOINT | explains active CLI route | `reports/m42-4-integrity-regression-cli-evidence-report.md` | KEEP | tied to active regression flow
`docs/INTEGRITY-FIXTURE-REGISTRY.md` | doc | ACTIVE_VALIDATION_CHECK | fixture registry contract | `reports/m41-3-integrity-fixture-registry-evidence-report.md` | KEEP | registry wiring documented
`docs/INTEGRITY-RESULT-UX.md` | doc | DUPLICATE_OR_OVERLAPPING | user output guide overlaps result contract docs | none_found | MERGE_LATER | merge candidate with result-contract docs
`docs/ALL-STRICT-INTEGRITY-INTEGRATION.md` | doc | DUPLICATE_OR_OVERLAPPING | overlaps CLI integration docs | none_found | MERGE_LATER | keep until M43.4
`docs/M40-RUNTIME-BYPASS-SMOKE.md` | doc | HISTORICAL_EVIDENCE | smoke evidence context | `reports/m40-10-runtime-bypass-smoke-report.md` | ARCHIVE_LATER | historical, still useful for traceability
`docs/CANARY-FILES-POLICY.md` | doc | ACTIVE_VALIDATION_CHECK | canary checker policy | `scripts/agentos-validate.py` | KEEP | tied to checker behavior
`docs/TRUSTED-VALIDATION-SOURCES.md` | doc | ACTIVE_SOURCE_OF_TRUTH | trusted source definition | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | KEEP | authority clarity

## Schemas Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`schemas/private-evaluator-checklist.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | checklist structure contract | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | used as structure contract
`schemas/process-trace.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | trace structure contract | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | paired with checker
`schemas/evidence-binding.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | binding structure contract | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | paired with checker
`schemas/validator-authority.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | authority record structure | `reports/m40-11-validator-authority-evidence-report.md` | KEEP | linked to M40.11
`schemas/role-separation.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | role separation structure | `reports/m40-11-validator-authority-evidence-report.md` | KEEP | linked to M40.11
`schemas/evidence-immutability.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | immutability structure | `reports/m40-12-evidence-immutability-report.md` | KEEP | linked to M40.12
`schemas/integrity-fixture-registry.schema.json` | schema | UNKNOWN_NEEDS_REVIEW | registry schema relation unclear from active calls | unknown_needs_review | REVIEW_LATER | verify direct runtime validation usage
`schemas/integrity-regression-fixture.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | regression fixture format | `reports/m42-3-integrity-regression-fixtures-evidence-report.md` | KEEP | verified in M42.3
`schemas/integrity-result-summary.schema.json` | schema | ACTIVE_SCHEMA_OR_TEMPLATE | result-summary format | `reports/m41-4-integrity-result-ux-evidence-report.md` | KEEP | verified by json.tool in evidence

## Templates Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`templates/private-evaluator-checklist.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | evaluator input template | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | core evidence authoring
`templates/process-trace-record.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | trace input template | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | core evidence authoring
`templates/evidence-binding-record.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | binding input template | `reports/m40-8-runner-proof-evidence-report.md` | KEEP | core evidence authoring
`templates/validator-authority-record.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | authority record template | `reports/m40-11-validator-authority-evidence-report.md` | KEEP | core for authority checks
`templates/role-separation-record.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | role record template | `reports/m40-11-validator-authority-evidence-report.md` | KEEP | core for role checks
`templates/evidence-immutability-record.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | immutability input template | `reports/m40-12-evidence-immutability-report.md` | KEEP | core for immutability checks
`templates/integrity-result-summary.md` | template | ACTIVE_SCHEMA_OR_TEMPLATE | summary output template | `reports/m41-4-integrity-result-ux-evidence-report.md` | KEEP | active UX artifact

## Scripts Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`scripts/agentos-validate.py` | script | ACTIVE_RUNTIME_ENTRYPOINT | unified validation CLI entrypoint | `README.md`, `reports/m41-6-unified-integrity-closure-report.md` | DO_NOT_TOUCH | runtime entrypoint
`scripts/test-honest-pass-fixtures.py` | script | ACTIVE_VALIDATION_CHECK | M40 fixture aggregator | `scripts/agentos-validate.py`, `reports/m40-13-full-honest-pass-closure-report.md` | KEEP | active checker flow
`scripts/check-private-evaluator-consistency.py` | script | ACTIVE_VALIDATION_CHECK | private/public rule consistency checker | `scripts/agentos-validate.py`, `scripts/test-honest-pass-fixtures.py` | KEEP | referenced by active CLI
`scripts/check-canary-integrity.py` | script | ACTIVE_VALIDATION_CHECK | canary integrity checker | `scripts/agentos-validate.py`, `scripts/test-honest-pass-fixtures.py` | KEEP | referenced by active CLI
`scripts/check-process-trace.py` | script | ACTIVE_VALIDATION_CHECK | trace integrity checker | `scripts/agentos-validate.py`, `scripts/test-honest-pass-fixtures.py` | KEEP | referenced by active CLI
`scripts/check-evidence-binding.py` | script | ACTIVE_VALIDATION_CHECK | evidence binding checker | `scripts/agentos-validate.py`, `scripts/test-honest-pass-fixtures.py` | KEEP | referenced by active CLI
`scripts/test-m40-runtime-bypass-smoke.py` | script | ACTIVE_VALIDATION_CHECK | runtime bypass smoke checker | `scripts/agentos-validate.py`, `reports/m40-10-runtime-bypass-smoke-report.md` | KEEP | safety smoke tool
`scripts/check-validator-authority-boundary.py` | script | ACTIVE_VALIDATION_CHECK | validator mutation boundary checker | `scripts/agentos-validate.py`, `reports/m40-11-validator-authority-evidence-report.md` | KEEP | core M40.11 checker
`scripts/check-role-separation.py` | script | ACTIVE_VALIDATION_CHECK | actor-role checker | `scripts/agentos-validate.py`, `reports/m40-11-validator-authority-evidence-report.md` | KEEP | core M40.11 checker
`scripts/check-evidence-immutability.py` | script | ACTIVE_VALIDATION_CHECK | immutability checker | `scripts/agentos-validate.py`, `reports/m40-12-evidence-immutability-report.md` | KEEP | core M40.12 checker
`scripts/test-integrity-regression.py` | script | ACTIVE_RUNTIME_ENTRYPOINT | integrity regression runner | `scripts/agentos-validate.py`, `docs/INTEGRITY-REGRESSION-CLI-INTEGRATION.md` | DO_NOT_TOUCH | active M42 runtime route
`scripts/test-gate-regression-fixtures.py` | script | DUPLICATE_OR_OVERLAPPING | regression helper overlaps newer regression runner scope | `scripts/audit-release-readiness.py`, `reports/m33-negative-fixture-coverage-inspection.md` | REVIEW_LATER | keep until M43.5 decision
`scripts/check-template-integrity.py` | script | UNKNOWN_NEEDS_REVIEW | template checker, relation to Honest PASS consolidation partial | unknown_needs_review | REVIEW_LATER | outside strict M40–M42 core
`scripts/test-template-integrity.py` | script | UNKNOWN_NEEDS_REVIEW | template fixture runner; unclear impact on Honest PASS branch | unknown_needs_review | REVIEW_LATER | verify operational dependency
`scripts/test-template-integrity-fixtures.py` | script | UNKNOWN_NEEDS_REVIEW | template fixture self-test helper | unknown_needs_review | REVIEW_LATER | verify active usage scope

## Fixtures Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`tests/fixtures/private-evaluator/` | fixture-set | ACTIVE_REGRESSION_INPUT | negative/positive private evaluator tests | `scripts/test-honest-pass-fixtures.py` | KEEP | active M40 fixture root
`tests/fixtures/canary-integrity/` | fixture-set | ACTIVE_REGRESSION_INPUT | canary tamper scenarios | `scripts/test-honest-pass-fixtures.py` | KEEP | active M40 fixture root
`tests/fixtures/process-trace/` | fixture-set | ACTIVE_REGRESSION_INPUT | trace validation scenarios | `scripts/test-honest-pass-fixtures.py` | KEEP | active M40 fixture root
`tests/fixtures/evidence-binding/` | fixture-set | ACTIVE_REGRESSION_INPUT | binding validation scenarios | `scripts/test-honest-pass-fixtures.py` | KEEP | active M40 fixture root
`tests/fixtures/validator-authority/` | fixture-set | ACTIVE_REGRESSION_INPUT | authority boundary scenarios | `scripts/agentos-validate.py` | KEEP | active via integrity path
`tests/fixtures/role-separation/` | fixture-set | ACTIVE_REGRESSION_INPUT | role split scenarios | `scripts/agentos-validate.py` | KEEP | active via integrity path
`tests/fixtures/evidence-immutability/` | fixture-set | ACTIVE_REGRESSION_INPUT | immutability scenarios | `scripts/agentos-validate.py` | KEEP | active via integrity path
`tests/fixtures/integrity-regression/` | fixture-set | ACTIVE_REGRESSION_INPUT | M42 regression fixtures | `scripts/test-integrity-regression.py` | DO_NOT_TOUCH | active regression input
`tests/fixtures/integrity-fixture-registry.json` | fixture-registry | ACTIVE_SOURCE_OF_TRUTH | registry map for integrity fixtures | `scripts/agentos-validate.py`, `scripts/test-integrity-regression.py` | DO_NOT_TOUCH | active registry
`tests/fixtures/template-integrity/` | fixture-set | DUPLICATE_OR_OVERLAPPING | template-integrity fixtures overlap separate quality domain | `scripts/test-template-integrity-fixtures.py` | MERGE_LATER | merge/split review in M43.3+

## Reports Inventory
Path | Type | Classification | Current Role | Referenced By | Recommended Action | Notes
--- | --- | --- | --- | --- | --- | ---
`reports/m40-13-completion-review.md` | report | ACTIVE_SOURCE_OF_TRUTH | final M40 status token source | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | KEEP_AND_LINK | status authority for M40
`reports/m41-6-completion-review.md` | report | ACTIVE_SOURCE_OF_TRUTH | final M41 status token source | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | KEEP_AND_LINK | status authority for M41
`reports/m42-6-completion-review.md` | report | ACTIVE_SOURCE_OF_TRUTH | final M42.6 branch closure status | precondition for M43.1 | DO_NOT_TOUCH | required precondition file
`reports/m42-6-honest-pass-integrity-final-closure-report.md` | report | ACTIVE_SOURCE_OF_TRUTH | final closure decision narrative | `reports/m42-6-completion-review.md` | KEEP_AND_LINK | closure rationale
`reports/m42-6-final-capability-matrix.md` | report | ACTIVE_SOURCE_OF_TRUTH | capability status matrix | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | KEEP_AND_LINK | consolidated capability map
`reports/m42-6-final-gaps-and-deferred-items.md` | report | ACTIVE_SOURCE_OF_TRUTH | known gaps/deferred items | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | KEEP_AND_LINK | explicit non-P0 carry-forward
`reports/m40-*.md` | report-set | HISTORICAL_EVIDENCE | implementation evidence history | `reports/m40-13-full-honest-pass-closure-report.md` | ARCHIVE_CANDIDATE | keep immutable history
`reports/m41-*.md` | report-set | HISTORICAL_EVIDENCE | consolidation evidence history | `reports/m41-6-unified-integrity-closure-report.md` | ARCHIVE_CANDIDATE | keep immutable history
`reports/m42-1-*.md` | report-set | HISTORICAL_EVIDENCE | regression baseline planning evidence | `reports/m42-5-integrity-regression-evidence-consolidation.md` | ARCHIVE_CANDIDATE | archive later with index links
`reports/m42-2-*.md` | report-set | HISTORICAL_EVIDENCE | regression runner evidence | `reports/m42-5-integrity-regression-evidence-consolidation.md` | ARCHIVE_CANDIDATE | archive later with index links
`reports/m42-3-*.md` | report-set | HISTORICAL_EVIDENCE | fixture evidence | `reports/m42-5-integrity-regression-evidence-consolidation.md` | ARCHIVE_CANDIDATE | archive later with index links
`reports/m42-4-*.md` | report-set | HISTORICAL_EVIDENCE | CLI integration evidence | `reports/m42-5-integrity-regression-evidence-consolidation.md` | ARCHIVE_CANDIDATE | archive later with index links
`reports/m42-5-*.md` | report-set | HISTORICAL_EVIDENCE | gate readiness and known gaps | `reports/m42-6-honest-pass-integrity-final-closure-report.md` | ARCHIVE_CANDIDATE | keep for audit trace
`reports/m42-hk1-*.md` | report-set | MERGEABLE_LATER | housekeeping evidence, partial overlap with M42 closure records | none_found | MERGE_LATER | evaluate for summary merge

## Active vs Historical Summary
- Active source-of-truth artifacts: final completion reviews and final closure matrix/gaps set.
- Active runtime entrypoints: `scripts/agentos-validate.py`, `scripts/test-integrity-regression.py`.
- Active validation checks: M40/M42 checker scripts and their fixture roots.
- Historical evidence: most milestone evidence reports (`m40-*`, `m41-*`, `m42-1..5-*`) should be retained now and only archived later.

## Unknown / Needs Review
Path | Open Question | Next Review Window
--- | --- | ---
`schemas/integrity-fixture-registry.schema.json` | direct runtime validation usage is not fully explicit in inspected calls | M43.2
`scripts/check-template-integrity.py` | consolidation impact to Honest PASS branch is unclear | M43.5
`scripts/test-template-integrity.py` | current operational role vs historical testing is unclear | M43.5
`scripts/test-template-integrity-fixtures.py` | current operational role vs historical testing is unclear | M43.5
