# Platform Required Checks Evidence

<!-- ROLE: EVIDENCE_REPORT -->
<!-- AUTHORITY: NON-AUTHORITY -->
<!-- SOURCE_OF_TRUTH: no -->

## Human Summary

Platform branch protection evidence for AgentOS repository.
This report captures the state of branch protection rules on `main` branch.
Evidence collected: 2026-05-06.
Human verifier: NMF13579.

---

## Platform Evidence

- branch: main
- ruleset configured: YES
- ruleset type: Branch ruleset (GitHub Rulesets)
- required check: agentos-validate (GitHub Actions)
- require PR before merging: YES
- block force pushes: YES
- restrict deletions: YES
- required approvals: 0
- human verifier: NMF13579
- verification date: 2026-05-06
- final platform enforcement status: PLATFORM_ENFORCED

---

## Required Check Details

- check name: agentos-validate
- check provider: GitHub Actions
- check confirmed on main: YES
- bypass permissions on main: NO
- admin bypass allowed on main: NO

---

## Branch Protection Rules Active on `main`

- Restrict deletions: YES
- Block force pushes: YES
- Require a pull request before merging: YES
- Require status checks to pass: YES
- Status check required: agentos-validate

---

## Evidence Source

- method: manual GitHub Settings → Rulesets → AgentOS
- configured by: NMF13579 (repository owner)
- date: 2026-05-06
- screenshot evidence: YES (captured during configuration)

---

## Validation

- file existence check: PASS
- platform enforcement status: PLATFORM_ENFORCED
- human verifier: NMF13579
- evidence complete: YES

---

## Non-Authority Boundaries

This report is evidence only.
This report does not approve execution.
This report does not replace human review.
Platform enforcement is active on main branch.
