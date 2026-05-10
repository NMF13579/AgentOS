# Milestone 22 - Markdown-to-Script Optimization Inventory

## Executive Summary
I inspected the canonical Markdown areas named in this task: `docs/`, `templates/`, `scripts/`, `reports/`, `examples/`, `tasks/`, `core-rules/`, `policies/`, `quality/`, `data/`, plus the bootstrap files used to orient the repo (`llms.txt`, `README.md`, `ROUTES-REGISTRY.md`, and the core runtime modules required by `llms.txt`).

The main duplication pattern is not random copy-paste. It is repeated rule language across safety docs, repeated status vocabularies across reports and checks, and repeated template structure across template packs, generated copies, and report families.

Markdown that explains meaning, policy, limitations, or human decision boundaries should stay in Markdown. Deterministic checks should move toward scripts when the rule can be stated as a fixed list, a fixed marker set, or a fixed structure.

What must not be automated in M22 is also clear: approval decisions, completion review decisions, release readiness decisions, ambiguous risk interpretation, active-task mutation, self-healing, SQLite, vector RAG, backend/service logic, and autonomous execution.

The derived index layer is still noisy: `data/index.json` currently fails validation, so it should stay clearly secondary until the source metadata is cleaned up.

## Observed Repository Coverage

| Path | Status | Notes |
|---|---|---|
| `docs/` | FOUND | Contains the main guardrail, policy, validation, and explanation docs |
| `templates/` | FOUND | Contains reusable template packs and derived template copies |
| `scripts/` | FOUND | Contains the current validators, audits, and wrappers |
| `reports/` | FOUND | Contains evidence reports, audits, smoke reports, and milestone reports |
| `examples/` | FOUND | Contains example scenarios and sample project material |
| `tasks/` | FOUND | Contains the active task, drafts, queue entries, and task contracts |
| `core-rules/` | FOUND | Contains the canonical governance module |
| `policies/` | FOUND | Contains policy data files used by checks |
| `quality/` | FOUND | Contains the canonical verification module |
| `data/` | FOUND | Contains derived config/index data used by validators |
| `state/` | FOUND | Required by bootstrap order and inspected for state rules |
| `workflow/` | FOUND | Required by bootstrap order and inspected for execution boundaries |
| `security/` | FOUND | Required by bootstrap order and inspected for security boundaries |
| `llms.txt` | FOUND | Canonical startup order file |
| `README.md` | FOUND | Root-level project overview |
| `ROUTES-REGISTRY.md` | FOUND | Canonical module ownership reference |
| `tasks/active-task.md` | FOUND | Current active task pointer and execution contract |

## Markdown Role Inventory

| File / Family | Current Role | Should Stay MD? | Scriptable Parts | Risk |
|---|---|---|---|---|
| `llms.txt` + `core-rules/MAIN.md` + `state/MAIN.md` + `workflow/MAIN.md` + `quality/MAIN.md` + `security/MAIN.md` | semantic source of truth | YES | Bootstrap order, module ownership, and presence checks | MEDIUM |
| `docs/*.md` policy and guardrail docs | semantic source of truth | YES | Required sections, boundary phrases, and status vocabulary | MEDIUM |
| `templates/*.md`, `tasks/templates/*.md`, `reports/templates/*.md` | template | YES | Required sections, required files, and template shape | LOW |
| `tasks/active-task.md` and `tasks/*/TASK.md` | task contract | YES | Frontmatter, required fields, and forbidden claim checks | HIGH |
| `tasks/*/REVIEW.md` and `tasks/*/TRACE.md` | verification record | YES | Required fields, review status checks, and forbidden phrases | HIGH |
| `reports/milestone-*.md`, `reports/*evidence*.md`, `reports/*audit*.md`, `reports/*smoke*.md`, `reports/verification.md` | evidence report / audit report / verification record | YES | Required sections, result markers, and command/result format | MEDIUM |
| `examples/**/*.md` | example | YES | Smoke-style checks and boundary claims | MEDIUM |
| `templates/dist/**` | generated or derived | YES | Rebuild checks and source alignment checks | MEDIUM |
| `data/index.json` and `data/required-sections.json` | derived navigation / derived config | NO | Schema checks and rebuild checks | MEDIUM |

## Markdown-to-Script Candidates

| Rule / Pattern | Current Markdown Locations | Candidate Script | Why Scriptable | Priority |
|---|---|---|---|---|
| Required section checks | `templates/`, `reports/`, `tasks/`, `docs/` | `scripts/validate-required-sections.py` | The required heading list is fixed and testable | HIGH |
| Status marker checks | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `docs/RELEASE-READINESS-AUDIT.md`, `reports/` | `scripts/validate-status-semantics.py` | The allowed marker set is finite | HIGH |
| Forbidden claim checks | `docs/BOUNDARY-CLAIMS.md`, `docs/HUMAN-APPROVAL-EVIDENCE.md`, `docs/SAFETY-BOUNDARIES.md`, `docs/TEMPLATE-PACKAGING-AUDIT.md` | `scripts/validate-boundary-claims.py` | The banned phrases can be matched directly | HIGH |
| Boundary statement checks | `llms.txt`, `docs/SAFETY-BOUNDARIES.md`, `docs/BOUNDARY-CLAIMS.md`, `quality/MAIN.md` | Future `scripts/validate-boundary-statements.py` | Boundary language is fixed enough to check with a phrase list | MEDIUM |
| Frontmatter presence and field checks | `tasks/`, `reports/verification.md`, `reports/*evidence*.md`, `templates/`, `examples/` | `scripts/validate-frontmatter.py` | Required fields and allowed values are finite | HIGH |
| Template structure checks | `templates/`, `tasks/templates/`, `reports/templates/` | `scripts/check-template-integrity.py` | The file set and required shapes are fixed | HIGH |
| Source-of-truth reference checks | `llms.txt`, `docs/SOURCE-OF-TRUTH-MAP.md`, canonical `*/MAIN.md` files | Future `scripts/validate-source-of-truth-map.py` | Owner links and canonical references can be verified mechanically | HIGH |
| Index consistency checks | `data/index.json`, `docs/INDEX-SCHEMA.md`, `docs/SOURCE-OF-TRUTH-MAP.md` | `scripts/validate-index.py` and `scripts/build-index.py` | Derived index fields can be compared against source Markdown | MEDIUM |
| Evidence format checks | `reports/*evidence*.md`, `reports/*completion-review*.md`, `reports/verification.md` | Future `scripts/validate-evidence-report.py` | Report sections and command/result tables are deterministic | MEDIUM |

## Meaningful Markdown to Preserve

| Markdown Area | Why It Should Stay MD | Automation Boundary |
|---|---|---|
| Architecture explanations | They explain why the system exists in a certain shape | Scripts may check presence, not rewrite meaning |
| Guardrail philosophy | It defines how the system stays safe | Scripts may check phrasing, not decide policy |
| Risk model rationale | It explains risk categories and why they exist | Scripts may check allowed labels only |
| Approval policy rationale | It explains when human approval is needed | Scripts may not issue approval |
| Completion decision logic | It explains the line between evidence and completion | Scripts may prepare evidence, not finish the task |
| Release decision logic | It explains the line between evidence and release readiness | Scripts may report, not approve release |
| Limitations | It preserves the explicit limits of the system | Scripts may check that the section exists |
| Usage docs | They are for people reading the repo | Scripts may check links and structure only |
| Troubleshooting | It captures known failure patterns in plain language | Scripts may not replace the diagnosis text |
| Lessons | It records human learning from incidents | Scripts may check format only |
| Human decisions | They remain a human responsibility | Scripts must never take over the decision |
| Evidence reports | They summarize checks and gaps | Scripts may validate format, not outcome authority |

## Duplication Audit

| Repeated Content | Locations | Duplication Type | Risk | Recommendation |
|---|---|---|---|---|
| Core guardrail and governance language | `llms.txt`, `core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, `security/MAIN.md` | safe duplication | MEDIUM | Keep the repeated boundary language, but make sure each file keeps its own owner role clear |
| Status vocabulary and result markers | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `docs/RELEASE-READINESS-AUDIT.md`, `reports/*`, `scripts/validate-status-semantics.py` | scriptable duplication | HIGH | Centralize the marker set in validators and keep the docs as explanation |
| Boundary phrases about human control | `docs/BOUNDARY-CLAIMS.md`, `docs/HUMAN-APPROVAL-EVIDENCE.md`, `docs/SAFETY-BOUNDARIES.md`, `docs/TEMPLATE-PACKAGING-AUDIT.md` | safe duplication | MEDIUM | Preserve the repeated safety language, then enforce it with one validator |
| Template structure reused across packs | `templates/agentos-minimal/**`, `templates/agentos-full/**`, `templates/dist/**`, `tasks/templates/**`, `reports/templates/**` | safe duplication | LOW | Keep the reuse because it makes the packs consistent and rebuildable |
| Report section patterns | `reports/milestone-*.md`, `reports/*evidence*.md`, `reports/*completion-review*.md`, `reports/verification.md` | scriptable duplication | MEDIUM | Use section-profile checks instead of hand-reviewing every variant |

Total dangerous duplications found: 0
Total scriptable duplications found: 2

## MD-to-Agent Gap Audit

| Gap Type | Example | Current Protection | Missing Check | Priority |
|---|---|---|---|---|
| Rule gap | A report can say `PASS` without making clear that this is only a check result | Boundary docs and status docs | One repo-wide forbidden-claim check for reports | HIGH |
| Structure gap | Different report families use different required sections | Templates and local conventions | Profile-based required-section validation | HIGH |
| Status gap | `PASS`, `READY`, `APPROVED`, and `COMPLETED` can be mixed up | `docs/STATUS-SEMANTICS.md` | Context-aware status validation | HIGH |
| Source-of-truth gap | Derived navigation can drift away from the Markdown source | `llms.txt` and `docs/SOURCE-OF-TRUTH-MAP.md` | Source-of-truth map validation | HIGH |
| Context gap | Observation and recommendation can blend together in reports | Human review | Observation-vs-recommendation lint | MEDIUM |
| Execution gap | A runner can look like an executor even when it is only reporting | Read-only notes in docs and scripts | Read-only contract checks for scripts | MEDIUM |
| Verification gap | A command result can be mistaken for completion | Validation docs and evidence docs | Result-to-decision boundary checks | HIGH |
| Human-review gap | Approval language can be implied by a check result | Approval evidence docs | Claim checks for approval language | HIGH |

## Status and Boundary Semantics

| Status / Boundary | Current Meaning | Locations | Drift Risk | Recommendation |
|---|---|---|---|---|
| `PASS` | The check succeeded | `docs/STATUS-SEMANTICS.md`, `docs/VALIDATION.md`, `reports/` | MEDIUM | Keep the meaning tied to the specific check, not to final approval |
| `FAIL` | The check found a problem | `docs/STATUS-SEMANTICS.md`, `reports/` | MEDIUM | Keep a short reason next to every failure |
| `WARN` | The check found a non-blocking concern | `docs/STATUS-SEMANTICS.md`, `docs/RELEASE-READINESS-AUDIT.md`, `reports/` | MEDIUM | Use WARN only for known, non-blocking issues |
| `NOT_RUN` | The check was not executed | `docs/STATUS-SEMANTICS.md`, `docs/VALIDATION.md`, `reports/` | HIGH | Require a reason whenever a check was not run |
| `ERROR` | The tool failed before it could finish | `docs/STATUS-SEMANTICS.md`, `docs/RELEASE-READINESS-AUDIT.md`, `reports/` | HIGH | Separate tool failure from a normal FAIL result |
| `READY` | The item looks eligible for the next step | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `tasks/*` | HIGH | Always pair READY with the next allowed action |
| `NEEDS_REVIEW` | A human review is needed | `docs/STATUS-SEMANTICS.md`, `reports/` | LOW | Keep it as a human-controlled status |
| `APPROVED` | A human approved the action | `docs/HUMAN-APPROVAL-EVIDENCE.md`, `approvals/`, `tasks/*` | HIGH | Keep approval evidence explicit and file-based |
| `BLOCKED` | The item cannot proceed yet | `docs/STATUS-SEMANTICS.md`, `tasks/*`, `state/` docs | HIGH | Require the blocker to be named |
| `COMPLETED` | Completion was recorded | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `reports/` | HIGH | Keep completion separate from proof of correctness |
| `FAILED` | Failure was recorded | `docs/STATUS-SEMANTICS.md`, `state/` docs, `reports/` | MEDIUM | Keep failure and recovery evidence together |
| Boundary: validation does not equal approval | A check can pass without giving permission | `docs/BOUNDARY-CLAIMS.md`, `docs/HUMAN-APPROVAL-EVIDENCE.md`, `docs/SAFETY-BOUNDARIES.md` | HIGH | Keep this rule visible in every approval-related doc |
| Boundary: Markdown stays primary | Markdown defines the meaning; derived data only helps navigation | `llms.txt`, `docs/SOURCE-OF-TRUTH-MAP.md`, `docs/INDEX-SCHEMA.md` | HIGH | Keep the derived layer clearly secondary |
| Boundary: audit does not approve release | Audit only reports evidence | `docs/RELEASE-READINESS-AUDIT.md`, `docs/VALIDATION.md` | HIGH | Keep release authority with the human reviewer |

## Script Readiness Map

| Script / Future Script | Purpose | Source-of-Truth Needed | Read-only? | Priority |
|---|---|---|---|---|
| `scripts/validate-required-sections.py` | Check required headings | `data/required-sections.json` | CONFIRMED | HIGH |
| `scripts/validate-status-semantics.py` | Check status vocabulary and unsafe phrases | `docs/STATUS-SEMANTICS.md` | CONFIRMED | HIGH |
| `scripts/validate-boundary-claims.py` | Check forbidden boundary claims | `docs/BOUNDARY-CLAIMS.md` | CONFIRMED | HIGH |
| `scripts/validate-frontmatter.py` | Check required frontmatter fields | `docs/FRONTMATTER-STANDARD.md` once finalized | CONFIRMED | HIGH |
| `scripts/check-template-integrity.py` | Check template and pack structure | Template tree contract | CONFIRMED | HIGH |
| `scripts/validate-index.py` | Check derived index consistency | `data/index.json` and source Markdown | CONFIRMED | MEDIUM |
| `scripts/build-index.py` | Build the derived index | Source Markdown frontmatter | NOT_CONFIRMED | MEDIUM |
| `scripts/test-template-integrity.py` | Self-test the template integrity checker | Template fixture set | CONFIRMED | MEDIUM |
| `scripts/test-negative-fixtures.py` | Check rejection behavior | Negative fixture set | NOT_CONFIRMED | MEDIUM |
| `scripts/audit-template-packaging.py` | Read-only packaging audit | Template packaging docs and examples | CONFIRMED | MEDIUM |
| `scripts/audit-agentos.py` | Aggregate audit runner | Validation suite outputs | NOT_CONFIRMED | HIGH |
| Future `scripts/validate-source-of-truth-map.py` | Check canonical ownership links | `llms.txt` and source-of-truth map | YES | HIGH |
| Future `scripts/validate-evidence-report.py` | Check evidence report shape | Evidence report profile | YES | MEDIUM |
| Future `scripts/validate-boundary-statements.py` | Check boundary phrases | Boundary language profile | YES | MEDIUM |

## Frontmatter Readiness

| File Family | Useful Metadata | Benefit | Risk |
|---|---|---|---|
| `tasks/**` | `task_id`, `state`, `risk_level`, `activated_at` | Makes task state and scope easier to check | A bad field can make a task look more complete than it is |
| `reports/milestone-*.md` | `task_id`, `result`, `verified_at`, `scope` | Makes evidence reports easier to validate | The metadata must not replace the report text |
| `reports/*evidence*.md` | `task_id`, `commands`, `evidence_status` | Makes command coverage easier to track | The result must stay evidence, not approval |
| `templates/*.md` | `template_type`, `version`, `required_sections` | Makes template reuse easier to check | The template must stay readable to people |
| `docs/*.md` | `module`, `authority`, `status` | Makes ownership and role clearer | Ownership must not be guessed when it is unclear |
| `examples/**/*.md` | `scenario`, `purpose`, `expected_behavior` | Makes example families easier to index | Examples must stay examples, not rules |

## Index Readiness

| Entity | Fields Needed | Consumer | Priority |
|---|---|---|---|
| Canonical modules | `path`, `module`, `authority`, `status` | Validators and audit tools | HIGH |
| Task contracts | `task_id`, `state`, `risk_level`, `activated_at` | Task health and execution checks | HIGH |
| Reports | `report_type`, `task_id`, `result`, `created_at` | Evidence navigation and audit | MEDIUM |
| Templates | `template_name`, `required_sections`, `version` | Template integrity checks | MEDIUM |
| Examples | `path`, `scenario`, `purpose` | Example navigation and smoke checks | LOW |
| Derived index entries | `path`, `type`, `module`, `status`, `authority`, `created`, `last_validated` | `data/index.json` consumer tools | HIGH |

`data/index.json` must be derived - Markdown stays the primary source text.
The index must be rebuildable from Markdown at any time.
The index must not store approval, completion, or release decisions as authority.

## Do Not Automate Yet

- approval decisions
- completion review decisions
- release readiness decisions
- ambiguous policy interpretation
- ambiguous risk classification
- active-task mutation
- self-healing
- SQLite
- vector RAG
- backend/service layer
- autonomous execution

## Recommended Next M22 Tasks

| # | Task | Status | Reason |
|---|---|---|---|
| 1 | Markdown Role Classification | CONFIRMED | The repo already shows clear document families and role boundaries |
| 2 | Source-of-Truth Map | CONFIRMED | Ownership and boundary language need one clearer map |
| 3 | Frontmatter Standard | ADJUSTED | This should follow the source-of-truth map so the fields stay aligned |
| 4 | Frontmatter Validator | ADJUSTED | The validator should use the approved standard, not guess the schema |
| 5 | Status Semantics Validator | CONFIRMED | Status drift is already visible across docs and reports |
| 6 | Required Sections Validator | CONFIRMED | Section profiles are already repetitive enough to check mechanically |
| 7 | Boundary Claims Validator | CONFIRMED | Human-control language needs a repo-wide check |
| 8 | Index Schema | ADJUSTED | The index should stay derived and rebuildable |
| 9 | Build Index | ADJUSTED | Build only after the schema and ownership map are stable |
| 10 | Validate Index | ADJUSTED | Validate the derived layer only after the rebuild rules are fixed |
| 11 | Audit Uses Index | DEFERRED | The source docs need to settle first |
| 12 | Negative Fixtures | CONFIRMED | Negative cases are needed for the deterministic checks |
| 13 | Evidence Report | CONFIRMED | Evidence reports need one repeatable format |
| 14 | Completion Review | CONFIRMED | Final completion decisions must remain human-controlled |

## Validation Evidence

| Command | Status | Output Summary | Notes |
|---|---|---|---|
| `bash scripts/run-all.sh` | PASS | `PASS: task validation passed`; `PASS: verification validation passed` | Read-only command, confirmed by source inspection |
| `python3 scripts/check-template-integrity.py --strict` | PASS | `TEMPLATE_INTEGRITY_RESULT: PASS` | Read-only command, confirmed by source inspection |
| `python3 scripts/test-template-integrity.py` | PASS | `fixture-suite: PASS`; `Result: PASS` | Read-only command, confirmed by source inspection |
| `python3 scripts/test-negative-fixtures.py` | NOT_RUN | Not run in this pass | Mutation risk could not be ruled out fully |
| `python3 scripts/audit-template-packaging.py` | PASS | `TEMPLATE_PACKAGING_AUDIT_RESULT: PASS` | Read-only command, confirmed by source inspection |
| `python3 scripts/validate-required-sections.py reports/milestone-22-markdown-to-script-inventory.md --profile markdown_to_script_inventory` | PASS | `all required headings present` | Required sections are present |
| `python3 scripts/validate-status-semantics.py reports/milestone-22-markdown-to-script-inventory.md` | PASS | `status semantics valid` | The report avoids unsafe status claims |
| `python3 scripts/validate-boundary-claims.py reports/milestone-22-markdown-to-script-inventory.md` | PASS | `no forbidden boundary claims found` | The report keeps decision boundaries intact |
| `python3 scripts/validate-index.py --index data/index.json --root .` | FAIL | `15` invalid status entries and many unknown-metadata warnings | The derived index still needs cleanup |
| `python3 scripts/audit-agentos.py` | NOT_RUN | Not run | It writes `reports/audit.md`, so it is not safe for this task |

## Final Inventory Result

**READY_WITH_WARNINGS**

The repo already has enough structure to move into Markdown role classification and source-of-truth mapping. The main caution is repeated status and boundary language across several docs and reports, which can drift if it is not checked mechanically. The derived index also fails validation right now, so it should stay secondary until the metadata is cleaned up. There is no fundamental blocker, but the next step should focus on ownership and role boundaries before more metadata or index work is added.

Highest-priority recommended next task: **Markdown Role Classification**
