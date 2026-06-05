# M60 Documentation Pruning Plan

## Purpose

Подготовить безопасный план будущего pruning документации M56–M60 без изменения текущих артефактов.

## Scope

Только планирование. Никакого pruning, consolidation, deprecation или archive в 60.9.

## Preconditions Checked

Все предусловия 60.9 пройдены, включая успешный запуск reusable chain checker и проверку M61/M62 с legacy-исключениями.

## Planning Method

- read-only анализ документации и отчетов M56–M60
- запуск `python3 scripts/check-execution-verification-chain.py --json`
- классификация документов по плановым категориям
- проверка требований canonical replacement

## Planning Boundaries

60.9 не изменяет документы и не выполняет pruning.

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
- reports/m60-validator-consolidation-plan.md
- scripts/check-execution-verification-chain.py
- docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md

## Reusable Chain Checker Result

Command: `python3 scripts/check-execution-verification-chain.py --json`
Result: `EXECUTION_VERIFICATION_CHAIN_VALID_WITH_WARNINGS`

## Pruning Categories

- keep-as-canonical
- keep-as-supporting
- merge-into-canonical-later
- mark-deprecated-later
- archive-later
- do-not-touch
- manual-review-required

## Safety-Boundary Preservation Rule

Any removal or shortening of safety-boundary text must include a canonical replacement reference.
No safety-boundary text may be removed if the replacement source is missing, non-canonical, stale, or unvalidated.
No non-authority boundary text may be removed unless the replacement source is canonical, current, and validated.
Documentation pruning must not change policy decisions, exit code mappings, final statuses, approval semantics, execution boundaries, or result verification semantics.

## No-Pruning Rule

No documentation pruning happens in 60.9.
60.9 only plans safe pruning.
No artifact is deleted, renamed, moved, archived, deprecated, edited, or consolidated by 60.9.

## Repetition Rule

Not all repetition is bad.
Human-facing explanatory duplication may remain when it preserves local readability and does not create policy drift.
Safety-critical boundary repetition may remain intentionally.

Safety-critical repeated text that should generally remain locally visible:
- PASS is not approval
- Evidence is not approval
- Completion review is not approval
- does not replace human review
- does not authorize merge, push, or release
- does not mutate lifecycle state
- does not start the next milestone automatically

## Do-Not-Touch Documents

do-not-touch in 60.9 is a planning classification.
It does not modify files.
It does not create file locks.
It does not create approval.

Do-not-touch classes:
- policy documents
- contract documents
- schema files
- CLI behavior documents
- completion reviews
- action reviews
- evidence reports
- fixture oracle files
- runner result contracts
- M56–M59 final reports
- M60 intake / architecture / inventory / classification / drift audit / registry contract / registry docs / validator plan / reusable checks docs

## Keep as Canonical

- docs/TASK-EXECUTION-READINESS-POLICY.md
- docs/TASK-EXECUTION-AUTHORIZATION-POLICY.md
- docs/CONTROLLED-EXECUTION-SESSION-POLICY.md
- docs/EXECUTION-RESULT-VERIFICATION-POLICY.md
- docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
- schemas/execution-verification-registry.schema.json

## Keep as Supporting

- reports/m60-artifact-inventory.md
- reports/m60-duplication-drift-audit.md
- docs/EXECUTION-VERIFICATION-REGISTRY.md
- docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md

## Merge into Canonical Later

- candidate_path: docs/EXECUTION-VERIFICATION-REGISTRY.md
  planning_category: merge-into-canonical-later
  canonical_replacement: docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
  replacement_exists: true
  replacement_is_canonical: true
  replacement_validated: true
  safety_semantics_changed: false
  non_authority_boundary_preserved: true
  requires_manual_review: false
  reason: Potentially move duplicated contract-level phrasing into canonical contract references while preserving visibility.

## Mark Deprecated Later

- candidate_path: docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md
  planning_category: mark-deprecated-later
  canonical_replacement: docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
  replacement_exists: true
  replacement_is_canonical: true
  replacement_validated: false
  safety_semantics_changed: false
  non_authority_boundary_preserved: true
  requires_manual_review: true
  reason: Possible future simplification candidate; validation incomplete, not eligible now.

## Archive Later

- candidate_path: reports/m60-artifact-inventory.md
  planning_category: archive-later
  canonical_replacement: docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md
  replacement_exists: true
  replacement_is_canonical: false
  replacement_validated: false
  safety_semantics_changed: false
  non_authority_boundary_preserved: true
  requires_manual_review: true
  reason: Historical report may be archivable later, but replacement is not canonical.

## Manual Review Required

- candidate_path: docs/EXECUTION-VERIFICATION-REGISTRY.md
  planning_category: manual-review-required
  canonical_replacement: docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
  replacement_exists: true
  replacement_is_canonical: true
  replacement_validated: false
  safety_semantics_changed: false
  non_authority_boundary_preserved: true
  requires_manual_review: true
  reason: Need explicit human review on local readability impact.

## Canonical Replacement Requirements

For merge-into-canonical-later, mark-deprecated-later, archive-later candidates, all fields are required:
- candidate_path:
- planning_category:
- canonical_replacement:
- replacement_exists: true|false
- replacement_is_canonical: true|false
- replacement_validated: true|false
- safety_semantics_changed: false
- non_authority_boundary_preserved: true|false
- requires_manual_review: true|false
- reason:

If canonical_replacement is missing or not validated, the candidate is not eligible for 60.10.

## Candidates Eligible for 60.10

- docs/EXECUTION-VERIFICATION-REGISTRY.md (merge-into-canonical-later; validated canonical replacement present)

## Candidates Not Eligible for 60.10

- docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md (replacement_validated: false)
- reports/m60-artifact-inventory.md (replacement_is_canonical: false)
- manual-review-required candidates

## 60.10 Scope Boundary

60.10 may act only on candidates explicitly classified as merge-into-canonical-later, mark-deprecated-later, or archive-later with validated canonical replacement and safety_semantics_changed: false.
60.10 must not modify do-not-touch items.
60.10 must not modify manual-review-required items.
60.10 must not modify keep-as-canonical items.
60.10 must not modify keep-as-supporting items unless the plan explicitly marks a safe supporting-doc update with validated canonical replacement.

## Documentation Risk Assessment

- Risk of accidental safety-boundary loss during over-aggressive pruning.
- Risk of removing local non-authority visibility from supporting docs.
- Risk of drift if replacements are not canonical+validated.

## Plan Counts

approximate_count: true
keep_as_canonical_count: 6
keep_as_supporting_count: 4
merge_into_canonical_later_count: 1
mark_deprecated_later_count: 1
archive_later_count: 1
do_not_touch_count: 20
manual_review_required_count: 1
eligible_for_60_10_count: 1
not_eligible_for_60_10_count: 3
validated_canonical_replacement_count: 1
missing_canonical_replacement_count: 0
safety_boundary_preservation_issue_count: 0
non_authority_boundary_preservation_issue_count: 0
warning_count: 3
blocker_count: 0

## Warnings

- Есть manual-review-required кандидаты.
- Есть кандидаты с replacement_validated: false.
- Часть replacement источников supporting/non-canonical.

## Blockers

- Нет.

## Non-Authority Boundary

M60 documentation pruning plan is not approval.
M60 documentation pruning plan does not start cleanup execution.
M60 documentation pruning plan does not mutate lifecycle state.
M60 documentation pruning plan does not authorize merge, push, or release.
M60 documentation pruning plan does not change M56–M59 safety semantics.
M60 documentation pruning plan does not prune documentation.
M60 documentation pruning plan does not delete, rename, move, archive, deprecate, edit, or consolidate artifacts.
M60 documentation pruning plan does not create regression runner, evidence report, or completion review.
M60 documentation pruning plan does not authorize starting 60.10 automatically.

## Final Plan Status

FINAL_STATUS: M60_DOCUMENTATION_PRUNING_PLAN_COMPLETE_WITH_WARNINGS
