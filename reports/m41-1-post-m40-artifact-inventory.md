# M41.1 Post-M40 Artifact Inventory

## Policy Docs
- path: `docs/HONEST-PASS-HARDENING.md` | milestone: M40.6 | purpose: root Honest PASS architecture | status: REPORT_ONLY | limitation: policy-only | M41 action: keep canonical entry and cross-link in CLI help
- path: `docs/EVALUATOR-PRIVATE-CHECKLIST-POLICY.md` | milestone: M40.6 | purpose: hidden check boundary | status: REPORT_ONLY | limitation: no runtime enforcement by itself | M41 action: map to `validator-authority` command docs
- path: `docs/CANARY-FILES-POLICY.md` | milestone: M40.6 | purpose: canary integrity rules | status: REPORT_ONLY | limitation: no reliable canary read detection | M41 action: keep limitation visible in user output
- path: `docs/PROCESS-TRACE-POLICY.md` | milestone: M40.6 | purpose: trace trust boundary | status: REPORT_ONLY | limitation: proof verification depends on source metadata | M41 action: align with trace checker output
- path: `docs/EVIDENCE-BINDING-POLICY.md` | milestone: M40.6 | purpose: binding integrity rules | status: REPORT_ONLY | limitation: no cryptographic timestamp authority | M41 action: expose in strict guidance
- path: `docs/HONEST-PASS-RESULT-CONTRACT.md` | milestone: M40.6 | purpose: token/exit rules | status: REPORT_ONLY | limitation: multiple token families remain | M41 action: token alignment map
- path: `docs/TRUSTED-VALIDATION-SOURCES.md` | milestone: M40.6 | purpose: trusted source boundary | status: REPORT_ONLY | limitation: registry != approval | M41 action: include in user gap map
- path: `docs/HONEST-PASS-LEGACY-COMPATIBILITY.md` | milestone: M40.6 | purpose: legacy artifact handling | status: REPORT_ONLY | limitation: pre-M40.9 remains legacy-limited | M41 action: preserve strict scope messaging
- path: `docs/M40-RUNTIME-BYPASS-SMOKE.md` | milestone: M40.10 | purpose: smoke harness boundaries | status: REPORT_ONLY | limitation: not production isolation | M41 action: keep explicit warning in UX
- path: `docs/VALIDATOR-AUTHORITY-BOUNDARY.md` | milestone: M40.11 | purpose: validator boundary | status: REPORT_ONLY | limitation: no crypto integrity proof | M41 action: route through dedicated command
- path: `docs/ROLE-SEPARATION-FOR-VALIDATION.md` | milestone: M40.11 | purpose: actor separation rules | status: REPORT_ONLY | limitation: policy must be evidenced by records | M41 action: checker + UX guidance
- path: `docs/EVIDENCE-IMMUTABILITY-POLICY.md` | milestone: M40.12 | purpose: immutable evidence rules | status: REPORT_ONLY | limitation: metadata-level guarantees | M41 action: explicit needs-review path
- path: `docs/EVIDENCE-AMENDMENT-FLOW.md` | milestone: M40.12 | purpose: correction flow rules | status: REPORT_ONLY | limitation: amendment authority still procedural | M41 action: command-level next-action hints

## Templates
- path: `templates/private-evaluator-checklist.md` | milestone: M40.8 | purpose: private checklist record template | status: TEMPLATE_ONLY | limitation: no enforcement | M41 action: connect to checker docs
- path: `templates/process-trace-record.md` | milestone: M40.8 | purpose: trace record template | status: TEMPLATE_ONLY | limitation: user can misread claim/proof | M41 action: user-facing clarification
- path: `templates/evidence-binding-record.md` | milestone: M40.8 | purpose: binding record template | status: TEMPLATE_ONLY | limitation: structure != trust | M41 action: strict-mode guidance
- path: `templates/trusted-validation-source-record.md` | milestone: M40.8 | purpose: source registry template | status: TEMPLATE_ONLY | limitation: registry != approval | M41 action: command output note
- path: `templates/validator-authority-record.md` | milestone: M40.11 | purpose: authority record template | status: TEMPLATE_ONLY | limitation: metadata trust assumptions | M41 action: map to authority checker
- path: `templates/role-separation-record.md` | milestone: M40.11 | purpose: role separation record template | status: TEMPLATE_ONLY | limitation: high-risk interpretation complexity | M41 action: add examples in UX docs
- path: `templates/evidence-immutability-record.md` | milestone: M40.12 | purpose: immutability record template | status: TEMPLATE_ONLY | limitation: no external timestamp authority | M41 action: make limitation explicit in command help
- path: `templates/evidence-amendment-record.md` | milestone: M40.12 | purpose: amendment record template | status: TEMPLATE_ONLY | limitation: authority ambiguity may persist | M41 action: route to needs-review

## Schemas
- path: `schemas/private-evaluator-checklist.schema.json` | milestone: M40.8 | purpose: checklist structure | status: SCHEMA_ONLY | limitation: structure-only validation | M41 action: keep token mapping explicit
- path: `schemas/process-trace.schema.json` | milestone: M40.8 | purpose: trace structure | status: SCHEMA_ONLY | limitation: does not prove runner trust | M41 action: pair with checker result
- path: `schemas/evidence-binding.schema.json` | milestone: M40.8 | purpose: binding structure | status: SCHEMA_ONLY | limitation: agent-generated may be schema-valid | M41 action: preserve policy-based rejection
- path: `schemas/trusted-validation-source.schema.json` | milestone: M40.8 | purpose: source structure | status: SCHEMA_ONLY | limitation: authority still semantic | M41 action: map to NEEDS_REVIEW logic
- path: `schemas/validator-authority.schema.json` | milestone: M40.11 | purpose: authority record structure | status: SCHEMA_ONLY | limitation: no live file integrity proof | M41 action: keep as input contract only
- path: `schemas/role-separation.schema.json` | milestone: M40.11 | purpose: actor/risk structure | status: SCHEMA_ONLY | limitation: semantic conflicts unresolved by schema | M41 action: checker-first interpretation
- path: `schemas/evidence-immutability.schema.json` | milestone: M40.12 | purpose: immutability structure | status: SCHEMA_ONLY | limitation: cannot detect coordinated rewrite | M41 action: retain limitation warning
- path: `schemas/evidence-amendment.schema.json` | milestone: M40.12 | purpose: amendment structure | status: SCHEMA_ONLY | limitation: author trust not guaranteed by schema | M41 action: authority checker path

## Checkers
- path: `scripts/check-private-evaluator-consistency.py` | milestone: M40.7 | purpose: hidden requirement detection | status: STANDALONE_CHECKER | limitation: not directly in unified CLI | M41 action: expose as `validator-authority` or subcommand chain
- path: `scripts/check-canary-integrity.py` | milestone: M40.7 | purpose: canary tamper checks | status: STANDALONE_CHECKER | limitation: no reliable read detection | M41 action: integrate as integrity stage
- path: `scripts/check-process-trace.py` | milestone: M40.7 | purpose: runner trace proof checks | status: CLI_INTEGRATED | limitation: source trust ambiguity -> needs review | M41 action: preserve source token in aggregate output
- path: `scripts/check-evidence-binding.py` | milestone: M40.7 | purpose: reproducible binding checks | status: CLI_INTEGRATED | limitation: not timestamp authority | M41 action: keep strict non-approval wording
- path: `scripts/check-validator-authority-boundary.py` | milestone: M40.11 | purpose: authority mutation checks | status: STANDALONE_CHECKER | limitation: no unified CLI route yet | M41 action: add dedicated command
- path: `scripts/check-role-separation.py` | milestone: M40.11 | purpose: actor separation checks | status: STANDALONE_CHECKER | limitation: needs risk-context UX | M41 action: add dedicated command
- path: `scripts/check-evidence-immutability.py` | milestone: M40.12 | purpose: post-finalization rewrite checks | status: STANDALONE_CHECKER | limitation: coordinated rewrite blind spot | M41 action: add dedicated command + limitation text
- path: `scripts/check-evidence-amendments.py` | milestone: M40.12 | purpose: amendment semantics checks | status: STANDALONE_CHECKER | limitation: authority ambiguity remains needs-review | M41 action: integrate with immutability command flow

## Fixture Groups
- path: `tests/fixtures/private-evaluator/` | milestone: M40.7 | purpose: checklist checker fixtures | status: FIXTURE_ONLY | limitation: fixture scope only | M41 action: keep as CI regression inputs
- path: `tests/fixtures/canary-integrity/` | milestone: M40.7 | purpose: canary checker fixtures | status: FIXTURE_ONLY | limitation: no read telemetry coverage | M41 action: mark as smoke-level
- path: `tests/fixtures/process-trace/` | milestone: M40.7 | purpose: trace checker fixtures | status: FIXTURE_ONLY | limitation: static fixture trust | M41 action: map to strict fixture suite
- path: `tests/fixtures/evidence-binding/` | milestone: M40.7 | purpose: binding checker fixtures | status: FIXTURE_ONLY | limitation: no external authority | M41 action: keep clear non-approval note
- path: `tests/fixtures/m40-runtime-bypass/` | milestone: M40.10 | purpose: runtime bypass smoke inputs | status: FIXTURE_ONLY | limitation: simulation not production intercept | M41 action: dedicated runtime-bypass command
- path: `tests/fixtures/validator-authority/` | milestone: M40.11 | purpose: authority checker fixtures | status: FIXTURE_ONLY | limitation: metadata-driven | M41 action: integrate smoke route
- path: `tests/fixtures/role-separation/` | milestone: M40.11 | purpose: role checker fixtures | status: FIXTURE_ONLY | limitation: scenario coverage incomplete | M41 action: add user playbook examples later
- path: `tests/fixtures/evidence-immutability/` | milestone: M40.12 | purpose: immutability checker fixtures | status: FIXTURE_ONLY | limitation: baseline authority absent | M41 action: explicit M41.2 planning
- path: `tests/fixtures/evidence-amendments/` | milestone: M40.12 | purpose: amendment checker fixtures | status: FIXTURE_ONLY | limitation: authority semantics open | M41 action: keep needs-review branch explicit

## Runtime Bypass Smoke Harness
- path: `scripts/test-m40-runtime-bypass-smoke.py` | milestone: M40.10 | purpose: controlled bypass simulation | status: STANDALONE_CHECKER | limitation: not production-grade sandbox | M41 action: expose via CLI wrapper command

## CLI Integration Points
- path: `scripts/agentos-validate.py honest-pass` | milestone: M40.9 | purpose: proof/binding fixture and artifact mode | status: CLI_INTEGRATED | limitation: other integrity checks not unified | M41 action: add integrity command surface
- path: `scripts/agentos-validate.py all --strict` | milestone: M40.9 | purpose: include strict honest-pass stage | status: CLI_INTEGRATED | limitation: known baseline failure gap | M41 action: preserve as known gap until fixed

## Evidence Reports and Completion Reviews
- path: `reports/m40-6-*`..`reports/m40-13-*` | milestone: M40.x | purpose: evidence and status trail | status: REPORT_ONLY | limitation: narrative claim layer | M41 action: make discovery map and user guidance
