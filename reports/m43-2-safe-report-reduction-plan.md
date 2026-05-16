## Purpose
Define safe report reduction paths after M43.2 planning, without changing files now.

## Reduction Strategy
1. Keep active closure and gap sources discoverable.
2. Reduce duplication through index + summary first.
3. Archive only after human review and link validation.

## Conservative Reduction Path
Conservative report reduction target: 20–30%.
- Prioritize indexing repetitive evidence reports.
- Keep completion reviews in current location until summary quality is approved.

## Balanced Reduction Path
Balanced report reduction target: 30–45%.
- Add consolidated milestone summaries for M40/M41/M42 evidence packs.
- Archive older evidence reports after links are verified.

## Aggressive Reduction Path
Aggressive report reduction target: 45–60%, requires extra review.
- Requires strict human review of traceability and gap coverage before archive action.

## Archive Index Proposal
Proposed future layout (proposal only):
- `reports/archive/m40/`
- `reports/archive/m41/`
- `reports/archive/m42/`
- `reports/archive/m43-1/`
- `reports/archive/index.md`
M43.2 proposes archive layout only; it does not create archive directories.

## Summary Report Proposal
A report may be summarized later only if the summary preserves: milestone/task id, final status, decision rationale, validation evidence, known gaps, deferred items, authority boundary disclaimers, and source report path.
A summary must preserve decision traceability to the original report.

## Human Review Gates
- Gate 1: verify closure and gap references are still resolvable.
- Gate 2: verify archive index links before moving any report.
- Gate 3: verify summaries preserve decision context.
- Gate 4: verify unresolved P1/P2 references are not hidden.

## Proposed M43.3 Action
Prepare fixture consolidation plan with explicit failure-class coverage map, while keeping report links from M43.2 intact.

Report reduction must preserve auditability and decision traceability.
Do not reduce reports by deleting evidence required to explain completion decisions.
