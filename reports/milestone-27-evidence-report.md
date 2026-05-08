# M27 Evidence Report

## Status
- Evidence report only.
- Not final completion review.
- Not approval.
- Not merge authorization.
- Not push authorization.
- Final milestone status is assigned only in `27.18.1`.

## Milestone Summary
- M27 implements Two-Level Agent Control.
- Level 1: Repo/Git Runtime Control (required).
- Level 2: GitHub Platform Control (optional).
- M26 checked and recorded policy/corridor boundaries.
- M27 adds blocking runtime enforcement boundaries.

## Level 1 Evidence Summary
Recorded evidence includes:
- runtime boundary contract
- permission state store
- command enforcement runtime
- write enforcement runtime
- commit/push runtime guard
- identity boundary policy
- token scope policy
- immutable audit log
- human gate checkpoint
- violation enforcement runtime
- retry enforcement runtime
- unified enforcement CLI
- Level 1 audit script
- Level 1 smoke fixtures
- full M27 audit script

## Level 1 Artifact Matrix
| Artifact | Status |
|---|---|
| `docs/M27-TWO-LEVEL-CONTROL-ARCHITECTURE.md` | PRESENT |
| `docs/M27-RUNTIME-BOUNDARY-CONTRACT.md` | MISSING |
| `docs/PERMISSION-STATE-STORE.md` | PRESENT |
| `docs/M27-COMMAND-ENFORCEMENT-RUNTIME.md` | PRESENT |
| `docs/M27-WRITE-ENFORCEMENT-RUNTIME.md` | PRESENT |
| `docs/M27-COMMIT-PUSH-RUNTIME-GUARD.md` | PRESENT |
| `docs/AGENT-IDENTITY-BOUNDARY-POLICY.md` | PRESENT |
| `docs/AGENT-TOKEN-SCOPE-POLICY.md` | PRESENT |
| `docs/IMMUTABLE-AUDIT-LOG-POLICY.md` | PRESENT |
| `docs/HUMAN-GATE-CHECKPOINT-POLICY.md` | PRESENT |
| `docs/M27-VIOLATION-ENFORCEMENT-RUNTIME.md` | PRESENT |
| `docs/M27-RETRY-ENFORCEMENT-RUNTIME.md` | PRESENT |
| `docs/M27-UNIFIED-ENFORCEMENT-CLI.md` | PRESENT |
| `docs/M27-AUDIT.md` | PRESENT |
| `scripts/agentos-permission-state.py` | PRESENT |
| `scripts/agentos-command-guard.py` | PRESENT |
| `scripts/agentos-write-guard.py` | PRESENT |
| `scripts/agentos-git-guard.py` | PRESENT |
| `scripts/agentos-audit-log.py` | PRESENT |
| `scripts/agentos-human-gate.py` | PRESENT |
| `scripts/agentos-violation-enforce.py` | PRESENT |
| `scripts/agentos-retry-enforce.py` | PRESENT |
| `scripts/agentos-enforce.py` | PRESENT |
| `scripts/audit-m27-level1.py` | PRESENT |
| `scripts/test-m27-level1-fixtures.py` | PRESENT |
| `scripts/audit-m27.py` | PRESENT |

## Level 1 Machine Verification Summary
Executed commands and observed outputs:

1. `python3 scripts/audit-m27-level1.py`  
Observed `RESULT: LEVEL_1_READY_WITH_WARNINGS`, exit `0`.

2. `python3 scripts/test-m27-level1-fixtures.py`  
Observed `RESULT: LEVEL_1_SMOKE_PASS`, exit `0`.

3. `python3 scripts/audit-m27.py --level-2-enabled false`  
Observed `RESULT: M27_LEVEL_1_READY_PLATFORM_OPTIONAL`, exit `0`.

Warnings observed:
- `docs/M27-RUNTIME-BOUNDARY-CONTRACT.md` reported missing by Level 1 audit.
- `scripts/agentos-enforce.py --help` check reported warning in Level 1 audit output.

## Level 2 Evidence Summary
- `level_2_enabled`: no (skip path) and yes (evidence fixtures path) were both tested.
- Skip status verified: `SKIPPED_LEVEL_2_NOT_ENABLED`.
- Partial status verified: `PLATFORM_PARTIAL`.
- Enforced status verified from provided platform fixture evidence: `PLATFORM_ENFORCED`.
- Level 2 disabled does not fail Level 1.

## Level 2 Artifact Matrix
| Artifact | Status |
|---|---|
| `.github/workflows/m27-enforcement.yml` | PRESENT |
| `.github/CODEOWNERS` | PRESENT |
| `docs/M27-GITHUB-CI-GATE.md` | PRESENT |
| `docs/M27-CODEOWNERS-POLICY.md` | PRESENT |
| `docs/M27-BRANCH-PROTECTION-POLICY.md` | PRESENT |
| `docs/M27-GITHUB-PLATFORM-SETUP-GUIDE.md` | PRESENT |
| `scripts/check-github-platform-enforcement.py` | PRESENT |
| `templates/github-platform-enforcement-record.md` | PRESENT |
| `reports/milestone-27-platform-enforcement-evidence.md` | PRESENT |

## Level 2 Machine Verification Summary
Executed commands and observed outputs:

1. `python3 scripts/check-github-platform-enforcement.py check --level-2-enabled false`  
Observed `RESULT: SKIPPED_LEVEL_2_NOT_ENABLED`, exit `0`.

2. `python3 scripts/check-github-platform-enforcement.py check --level-2-enabled true --platform-state tests/fixtures/github-platform-enforcement/platform-enforced/state.json`  
Observed `RESULT: PLATFORM_ENFORCED`, exit `0`.

3. `python3 scripts/check-github-platform-enforcement.py check --level-2-enabled true --platform-state tests/fixtures/github-platform-enforcement/m27-check-not-required/state.json`  
Observed `RESULT: PLATFORM_PARTIAL`, exit `1`.

4. `python3 scripts/audit-m27.py --level-2-enabled true --platform-state tests/fixtures/github-platform-enforcement/platform-enforced/state.json`  
Observed `RESULT: M27_LEVEL_2_PLATFORM_ENFORCED`, exit `0`.

Owner/admin setup performed status:
- Not directly verified in this report (evidence-based/fixture-based check path used).

PLATFORM_ENFORCED verified:
- Yes, for provided enforcement fixture evidence.

## M25 / M26 Relationship
- M27 does not bypass M25.
- M27 does not replace M25 merge gates.
- M27 preserves M26 corridor boundaries.
- This M27 evidence report does not authorize merge.
- This M27 evidence report does not authorize push.

## Known Gaps and Warnings
- Level 1 warning: `docs/M27-RUNTIME-BOUNDARY-CONTRACT.md` reported missing by `audit-m27-level1.py`.
- Level 1 warning: `scripts/agentos-enforce.py --help` warning reported by `audit-m27-level1.py`.
- Level 2 is optional; disabled state is valid and may remain `SKIPPED_LEVEL_2_NOT_ENABLED`.
- If Level 2 is enabled incompletely, owner/admin action is required (`PLATFORM_PARTIAL` / `NEEDS_OWNER_ACTION` path).
- Known gap from `27.10.1`: time-based retry window validation is not implemented; `--now` reserved for future time-window checks.

## Handoff to 27.18.1
- `27.18.1` assigns final M27 completion status.
- This report provides evidence only.
- Final status must be selected in completion review using allowed M27 completion statuses.
- This report must not self-declare final completion.

## Non-Authorization Clauses
- This report is not approval.
- This report does not authorize commit.
- This report does not authorize push.
- This report does not authorize merge.
- This report does not authorize release.
- This report does not override M25.
- This report does not override M26.
- This report does not override M27 runtime guards.
- This report does not assign final M27 completion status.
