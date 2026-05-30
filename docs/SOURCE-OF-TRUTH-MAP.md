# Source-of-Truth Map
## M68.1 Boundary
This map is an M68.1 planning and review artifact.
This map does not authorize cleanup, deletion, compression, consolidation, or docs-to-code conversion.
This map does not create approval.
This map does not create lifecycle mutation.
This map does not complete M68.
Human review remains required before M68.2.

## Active Task Record
- active_task_id: task-68.1

## Inputs Used
- tasks/active-task.md
- reports/m68-inventory.json
- reports/m68-docs-to-code-drift.json
- reports/m68-duplicates.json
- reports/m68-repo-raw-inventory.md

## Classification Model
- canonical candidate
- supporting doc
- derived artifact
- report artifact
- template artifact
- schema artifact
- checker doc
- historical artifact
- needs review
- possible duplicate
- possible deprecated

## Canonical Candidates
- `llms.txt`
- `core-rules/MAIN.md`
- `state/MAIN.md`
- `workflow/MAIN.md`
- `quality/MAIN.md`
- `security/MAIN.md`
- `tasks/active-task.md` (active task binding record)

## Supporting Documents
- Operational docs under `docs/` that explain boundaries and usage.
- Milestone review docs in `reports/` for context.

## Derived Artifacts
- Scanner outputs in `reports/m68-*.json` and `reports/m68-*.txt`.
- Derived from current tree snapshot, not primary authority.

## Report Artifacts
- `reports/m68-repo-raw-inventory.md`
- `reports/m68-scan.rev.txt`
- `reports/m68-pre-scan-status.txt`

## Template Artifacts
- Files under `templates/` used as structure/input helpers.

## Schema Artifacts
- Files under `schemas/` (contract model surface).

## Checker Documentation
- Checker-oriented docs and script usage references in `docs/` and `scripts/`.

## Historical Artifacts
- Prior milestone reports (for example M63–M67 completion reviews).

## Needs Review
- Files with repeated readiness/final status wording (from drift candidates).
- Areas with high policy repetition likely requiring deterministic checks.

## Possible Duplicate Candidates
- Filename-based signals from M68.0 duplicates report (794 total signals).
- Same-stem candidate clusters: 371.

## Possible Deprecated Candidates
- Numbered/copy/backup-name variants flagged by scan.
- Legacy text variants with overlapping boundary statements.
M68.1 does not finally mark documents as deprecated.
M68.1 only proposes possible deprecated candidates for later M69 review.

## Source-of-Truth Risks
- High repetition may blur which document is primary.
- Boundary text appears across many files; review is needed to reduce ambiguity.
- Reports can be mistaken for authority unless explicitly labeled as derived.

## Explicit Non-Authority Boundary
- This map provides candidate classification only.
- It does not override repository content or mark final deprecation/canonical state.

## Final Status
FINAL_STATUS: M68_SOURCE_OF_TRUTH_MAP_COMPLETE_WITH_WARNINGS
