## Retention Principles
- Keep source-of-truth and runtime entrypoint artifacts intact.
- Keep enough historical evidence to explain milestone decisions.
- Separate runtime authority from historical narrative evidence.
- Retention decisions should be reversible until validation confirms safety.

## Deletion Risks
Do not remove evidence needed to explain past completion decisions.

Main risk:
- loss of chain-of-evidence across M40 -> M41 -> M42
- inability to explain why final closure status was set
- inability to reproduce historical checker outcomes

## Archive Risks
- broken references from final closure documents to detailed evidence
- hidden dependency on archived files in scripts/docs/tests
- mistaken archive of still-active source-of-truth documents

## Fixture Consolidation Risks
Do not merge fixtures if failure diagnosis becomes ambiguous.

Main risk:
- losing negative-path coverage for specific failure classes
- mixing fixtures with different expected result tokens
- reducing incident diagnosis quality during regressions

## Source-of-Truth Risks
- confusing final completion-review documents with ordinary historical reports
- accidentally treating historical evidence as active runtime authority
- accidental modification of precondition documents required for later audits

## Runtime Entrypoint Risks
Do not consolidate scripts if standalone checker behavior becomes harder to validate.

Main risk:
- wrapper simplification hides checker-level failures
- entrypoint overlap creates unclear ownership of validation output
- regression runner behavior changes without explicit evidence update

## Safe Retention Rules
- Keep all ACTIVE_SOURCE_OF_TRUTH artifacts unchanged during M43.1.
- Keep all ACTIVE_RUNTIME_ENTRYPOINT artifacts unchanged during M43.1.
- For historical reports: prefer index consolidation first, archive later with links.
- For fixtures: merge only after failure-class/token equivalence review.
- For scripts: review overlap first, consolidate wrappers later.

## Required Human Review Points
Human review is required before deleting or archiving Honest PASS artifacts.

Required checkpoints:
1. Before any archive batch operation.
2. Before any fixture merge operation.
3. Before any runtime entrypoint consolidation.
4. Before any source-of-truth document migration.
