## Purpose
Preserve source-of-truth semantics during future docs consolidation.

## Source-of-Truth Preservation Principles
Docs consolidation must preserve source-of-truth clarity, authority boundaries, and validation semantics.
A merged doc must not blur the difference between policy, evidence, validation, and approval.
Human approval remains above every PASS.
Evidence is not approval.
Regression evidence is validation evidence, not approval.

## Authority Boundary Rules
- Keep policy docs separate from evidence/history docs.
- Keep approval boundary statements explicit and unchanged in meaning.
- Keep PASS/NOT_RUN/WARNING semantics visible to operators.

## Policy Semantics That Must Not Be Lost
- Markdown/YAML as source of truth: found
- JSON as generated/index/navigation data: found
- SQLite/cache as optional runtime cache: not_found
- PASS as validation signal, not approval: found
- evidence report as claim/evidence, not authority: found
- human gate / approval boundary: found
- scope boundary: found
- no lower gate overrides higher safety gate: found
- NOT_RUN is not PASS: found
- WARNING is not clean PASS: found
- fixture registry is navigation metadata, not policy authority: found
- renderer/UX explains status but does not change authority: found
- regression runner detects drift but does not grant approval: found

## Docs Dependency Map
- `README.md` -> user routes and canonical docs links.
- `docs/VALIDATION.md` -> command semantics and validator flow.
- `docs/SAFETY-BOUNDARIES.md` -> boundary rules and human checkpoint meaning.
- Integrity policy docs -> M40–M43 reports and scripts references.

## Merge Risk Matrix
Candidate Doc(s) | Shared Topic | Authority Boundary Risk | Source-of-Truth Risk | Merge Recommendation | Reason
--- | --- | --- | --- | --- | ---
| `docs/INTEGRITY-RESULT-UX.md` + `docs/HONEST-PASS-RESULT-CONTRACT.md` | integrity result semantics | medium | medium | MERGE_LATER_WITH_REVIEW | topics overlap but authority wording must stay precise |
| `docs/ALL-STRICT-INTEGRITY-INTEGRATION.md` + `docs/INTEGRITY-REGRESSION-CLI-INTEGRATION.md` | strict/integration flow | low | low | MERGE_LATER_SAFE | same audience and adjacent runtime guidance |
| `docs/VALIDATOR-AUTHORITY-BOUNDARY.md` + `docs/ROLE-SEPARATION-FOR-VALIDATION.md` | authority controls | high | high | KEEP_SEPARATE | distinct boundary axes; merge may blur accountability model |
| `docs/GETTING-STARTED.md` + `docs/quickstart.md` | onboarding | low | low | LINK_ONLY | improve navigation without collapsing content scope |
| policy docs + milestone evidence reports | policy + evidence | high | high | KEEP_SEPARATE | policy must remain separate from historical evidence |

## Link-Only Candidates
- `docs/GETTING-STARTED.md` <-> `docs/quickstart.md`
- `README.md` <-> `docs/VALIDATION.md`
- `docs/HONEST-PASS-HARDENING.md` <-> `docs/TRUSTED-VALIDATION-SOURCES.md`

## Preservation Gaps
- SQLite/cache optional runtime cache concept: not_found in current docs scan.
- Some docs remain `UNKNOWN_NEEDS_REVIEW` due weak explicit reference signal.
