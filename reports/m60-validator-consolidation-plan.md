# M60 Validator Consolidation Plan

## Purpose

Определить, какие повторяющиеся проверки можно безопасно вынести в 60.8 без изменения семантики M56–M59.

## Scope

Только планирование консолидации валидаторов. Без реализации скриптов.

## Preconditions Checked

Все предусловия 60.7 пройдены, включая наличие артефактов 60.6 и валидный результат checker реестра.

## Planning Method

- read-only просмотр M56–M60 артефактов
- запуск `python3 scripts/check-execution-verification-registry.py --json`
- группировка повторяющихся проверок по семействам
- классификация по категориям консолидации

## Planning Boundaries

60.7 планирует, но не реализует валидаторы и не меняет существующие артефакты.

## Source Artifacts Checked

- reports/m60-m59-completion-intake.md
- docs/REPOSITORY-CLEANUP-CONSOLIDATION-ARCHITECTURE.md
- reports/m60-artifact-inventory.md
- docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md
- reports/m60-duplication-drift-audit.md
- docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
- schemas/execution-verification-registry.schema.json
- data/execution-verification-registry.json
- scripts/build-execution-verification-registry.py
- scripts/check-execution-verification-registry.py
- docs/EXECUTION-VERIFICATION-REGISTRY.md

## Registry Checker Result

Command: `python3 scripts/check-execution-verification-registry.py --json`
Result: `EXECUTION_VERIFICATION_REGISTRY_VALID`
registry_warning_count: 0

## Consolidation Categories

- consolidate-now
- leave-local
- unsafe-to-consolidate
- future-candidate
- manual-review-required

## Semantics Preservation Rules

Reusable checks must preserve existing pass/fail semantics.
No reusable check may silently downgrade BLOCKED to WARNING.
No reusable check may convert UNKNOWN, NOT_RUN, malformed, missing, or contradictory input into PASS.
No reusable check may turn PASS into approval.
No reusable check may replace human review.
No reusable check may authorize merge, push, release, lifecycle mutation, M61, or M62.

## Validator Scope Boundary for 60.8

60.8 may implement only checks classified as consolidate-now.
60.8 must not implement checks classified as leave-local.
60.8 must not implement checks classified as unsafe-to-consolidate.
60.8 must not implement checks classified as future-candidate.
60.8 must not implement checks classified as manual-review-required.

## Candidate Check Families Evaluated

- final_status checks
- policy_version checks
- non-authority statement checks
- fixture expected.json / oracle checks
- runner JSON checks
- protected path checks
- no downstream artifact checks
- no M60/M61/M62 premature artifact checks
- source artifact existence checks
- registry consistency checks
- schema JSON validity checks
- CLI help checks
- CLI JSON-only output checks
- path containment checks
- exit code mapping checks
- planning gate / may-proceed consistency checks
- warnings/blockers consistency checks
- action review performed_actions checks
- evidence report correlation checks
- completion review correlation checks

## Final Status Checks

Category: consolidate-now
Reason: deterministic and repeated across milestones.

## Policy Version Checks

Category: consolidate-now
Reason: repeated presence check with stable semantics.

## Non-Authority Statement Checks

Category: consolidate-now
Reason: repeated, deterministic phrase checks with fail-closed behavior.

## Fixture Oracle Checks

Category: future-candidate
Reason: reusable core exists, but oracle semantics vary by milestone context.

## Runner JSON Checks

Category: future-candidate
Reason: common structure exists, but field-level expectations still differ.

## Protected Path Checks

Category: leave-local
Reason: tied to task-local protected zone intent and review context.

## Downstream Artifact Checks

Category: consolidate-now
Reason: repeated denylist logic can be centralized safely.

## M60 / M61 / M62 Premature Artifact Checks

Category: consolidate-now
Reason: already standardized and deterministic with approved legacy exclusions.

## Source Artifact Existence Checks

Category: consolidate-now
Reason: stable file existence checks with explicit required paths.

## Registry Consistency Checks

Category: consolidate-now
Reason: checker already enforces deterministic rules and schema alignment.

## Schema JSON Validity Checks

Category: consolidate-now
Reason: deterministic JSON/schema structural validation.

## CLI Help Checks

Category: manual-review-required
Reason: help-output wording may vary and can create brittle checks.

## CLI JSON Output Checks

Category: consolidate-now
Reason: strict machine-readable output checks are deterministic.

## Path Containment Checks

Category: consolidate-now
Reason: deterministic security-style boundary checks.

## Exit Code Mapping Checks

Category: unsafe-to-consolidate
Reason: accidental remapping risk could change fail semantics.

## Planning Gate / May-Proceed Checks

Category: leave-local
Reason: gate wording and transitions are milestone-specific.

## Warnings / Blockers Consistency Checks

Category: future-candidate
Reason: partially reusable, but some context remains report-specific.

## Action Review Performed Actions Checks

Category: leave-local
Reason: tied to task-specific action traces.

## Evidence Report Correlation Checks

Category: leave-local
Reason: depends on local evidence source and task context.

## Completion Review Correlation Checks

Category: leave-local
Reason: milestone closure semantics need local explicitness.

## Consolidate Now

- final_status checks
- policy_version checks
- non-authority statement checks
- no downstream artifact checks
- no M60/M61/M62 premature artifact checks
- source artifact existence checks
- registry consistency checks
- schema JSON validity checks
- CLI JSON-only output checks
- path containment checks

## Leave Local

- protected path checks
- planning gate / may-proceed consistency checks
- action review performed_actions checks
- evidence report correlation checks
- completion review correlation checks

## Unsafe to Consolidate

- exit code mapping checks

## Future Candidates

- fixture expected.json / oracle checks
- runner JSON checks
- warnings/blockers consistency checks

## Manual Review Required

- CLI help checks

## Recommended 60.8 Minimal Implementation Set

- registry
- non-authority
- source-artifact-existence
- no-premature-downstream-artifacts
- schema-json-validity
- policy-version-presence
- final-status-presence

## Scripts Recommended for 60.8

- `scripts/check-execution-verification-chain.py`
- `scripts/check-non-authority-boundaries.py`
- `scripts/check-protected-paths.py` (only generic deterministic subset)

Recommended rationale: separate scripts are safer at 60.8 because they preserve explicit boundaries and reduce risk of hidden authority coupling.

## Scripts Deferred from 60.8

- `scripts/agentos-validate.py`
- `scripts/check-fixture-oracles.py`

Deferred rationale: unified entrypoint is deferred to avoid premature coupling of milestone-specific checks; oracle checks need additional manual boundary review.

## Risks

- Over-consolidation can hide local safety context.
- Exit-code mapping consolidation can alter fail-closed behavior.
- Premature unification can create implicit authority layer.

## Warnings

- Several families are intentionally left local.
- Some families require manual review before consolidation.

## Blockers

- None.

## Non-Authority Boundary

M60 validator consolidation plan is not approval.
M60 validator consolidation plan does not start cleanup execution.
M60 validator consolidation plan does not mutate lifecycle state.
M60 validator consolidation plan does not authorize merge, push, or release.
M60 validator consolidation plan does not change M56–M59 safety semantics.
M60 validator consolidation plan does not implement validators.
M60 validator consolidation plan does not create registry, regression runner, evidence report, or completion review.
M60 validator consolidation plan does not delete, rename, move, archive, deprecate, edit, or consolidate artifacts.
M60 validator consolidation plan does not authorize starting 60.8 automatically.

## Final Plan Status

approximate_count: true
consolidate_now_count: 10
leave_local_count: 5
unsafe_to_consolidate_count: 1
future_candidate_count: 3
manual_review_required_count: 1
candidate_check_family_count: 20
recommended_60_8_script_count: 3
deferred_script_count: 2
registry_warning_count: 0
blocker_count: 0

FINAL_STATUS: M60_VALIDATOR_CONSOLIDATION_PLAN_COMPLETE_WITH_WARNINGS
