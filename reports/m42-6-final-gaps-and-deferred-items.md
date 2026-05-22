## Remaining Gaps
Gap | Source | Severity | Blocks Final Closure | Assigned Next Area | Recommended Action
--- | --- | --- | --- | --- | ---
`summary-json-conflict` failure in regression runner | `reports/m42-2-completion-review.md`, `reports/m42-5-known-gaps-and-regressions.md` | P1 | no | M42.7+ regression contract hardening | Align summary/json conflict behavior checks and rerun baseline
`warning-not-clean-pass` needs-review in runner | `reports/m42-2-completion-review.md`, `reports/m42-5-known-gaps-and-regressions.md` | P2 | no | M42.7+ diagnostics cleanup | Improve warning phrase extraction/placement consistency
`all --strict` aggregate remains non-zero due baseline failures | `reports/m42-1-completion-review.md`, `reports/m42-5-known-gaps-and-regressions.md` | P1 | no | broader repo strict remediation | Resolve failing strict checks outside Honest PASS branch logic

## Deferred Non-Goals
- production-grade sandboxing
- full behavioural telemetry
- cryptographic timestamp authority
- semantic correctness without human/domain review
- SaaS evaluator
- human approval replacement

## Items Assigned Beyond Honest PASS
- onboarding / installation hardening
- TUI / tutor UX polish
- pilot readiness
- portability / template update flow
- broader repository release readiness
- SaaS architecture later

Deferred items beyond Honest PASS must not be counted as Honest PASS failure if they are explicit non-goals.

## P0/P1/P2/P3 Classification
- P0: blocks final closure (false approval/authorization claim, recursion ambiguity, hidden regression, broken core runner)
- P1: does not automatically block closure when documented and assigned forward
- P2: non-blocking completeness/diagnostic limitation
- P3: minor documentation polish

Current unresolved count:
- P0: 0
- P1: 2
- P2: 1
- P3: 0

## Final Risk Statement
Residual risk is manageable with explicit tracking. No unresolved P0 remains. Remaining P1/P2 items are documented and assigned forward.
