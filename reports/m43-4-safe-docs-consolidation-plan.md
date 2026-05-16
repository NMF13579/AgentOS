## Purpose
Plan safe docs/spec consolidation without changing docs in M43.4.

## Consolidation Strategy
1. Keep source-of-truth and policy-boundary docs intact.
2. Merge only overlapping guidance docs after wording review.
3. Prefer link maps where authority boundaries may blur.

## Conservative Docs Reduction Path
Conservative docs reduction target: 10–20%.
- Apply link-map cleanup only.

## Balanced Docs Reduction Path
Balanced docs reduction target: 20–35%.
- Merge select overlapping guide docs with explicit traceability notes.

## Aggressive Docs Reduction Path
Aggressive docs reduction target: 35–45%, requires extra review.
- Requires dedicated authority-boundary review before merge actions.

## Proposed Source-of-Truth Layout
- `docs/HONEST-PASS-INTEGRITY-SPEC.md`
- `docs/UNIFIED-INTEGRITY-SPEC.md`
- `docs/REGRESSION-HARDENING-SPEC.md`
- `docs/USER-GUIDE.md`
- `docs/OPERATOR-GUIDE.md`
M43.4 proposes docs consolidation only; it does not modify docs.

## Proposed Link Map
- Keep authority docs separate, add cross-links.
- Keep policy vs evidence split explicit in headings and links.

## Do-Not-Touch Docs
- `docs/VALIDATION.md`
- `docs/SAFETY-BOUNDARIES.md`
- `docs/VALIDATOR-AUTHORITY-BOUNDARY.md`
- `docs/ROLE-SEPARATION-FOR-VALIDATION.md`
- `docs/EVIDENCE-IMMUTABILITY-POLICY.md`
- `docs/TRUSTED-VALIDATION-SOURCES.md`

## Human Review Gates
- Gate 1: authority-boundary equivalence check.
- Gate 2: policy semantics preservation check.
- Gate 3: validation semantics preservation check.
- Gate 4: source doc traceability check.

## Proposed M43.5 Action
Prepare script entrypoint simplification plan, using M43.4 link map as reference.

Docs consolidation must preserve source-of-truth clarity.
Do not merge docs if authority boundaries become ambiguous.
Do not merge policy docs with historical evidence reports.
A merged doc must preserve traceability to every original doc.
