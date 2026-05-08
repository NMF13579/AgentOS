# M29 Static Bypass Resistance Checker

## Purpose

Static bypass resistance checker is not approval.
Static bypass resistance checker does not authorize protected actions.
Static bypass resistance checker does not execute bypass attempts.
Static bypass resistance checker does not prove runtime blocking by execution.
Static bypass resistance checker does not weaken M27 runtime enforcement.
Static bypass resistance checker does not weaken M28 context control.
Static bypass resistance checker must never become a bypass guide.
BYPASS_DETECTED is a blocking signal, not a bypass guide.
Human Gate remains approval authority.

## CLI

- `python3 scripts/check-bypass-resistance.py`
- `python3 scripts/check-bypass-resistance.py --json`
- `python3 scripts/check-bypass-resistance.py --root <repo-root>`
- `python3 scripts/check-bypass-resistance.py --fixtures tests/fixtures/m29-m28-context-bypass`
- `python3 scripts/check-bypass-resistance.py --fixtures tests/fixtures/m29-m27-runtime-bypass`

## Result Values

- BYPASS_RESISTANCE_READY
- BYPASS_RESISTANCE_READY_WITH_WARNINGS
- BYPASS_RESISTANCE_INCOMPLETE
- BYPASS_RESISTANCE_NOT_READY
- BYPASS_RESISTANCE_NEEDS_REVIEW
- BYPASS_DETECTED

## Exit Semantics

- only `BYPASS_RESISTANCE_READY` => exit 0
- `BYPASS_RESISTANCE_READY_WITH_WARNINGS returns exit 1 by design`

## Relationship To Fixture Safety Checker

- safety checker is prerequisite
- if safety checker returns unsafe => not ready
- if invalid => incomplete
- if needs review => needs review
- if subprocess is used, use shell=False

## Fixture Roots

- `tests/fixtures/m29-m28-context-bypass`
- `tests/fixtures/m29-m27-runtime-bypass`
- fixture root exists but contains zero valid fixture directories => incomplete
- checked_fixtures = 0 must never produce BYPASS_RESISTANCE_READY

## Guardrail Mapping

Includes M27/M28/authority/source-of-truth category mappings to specific boundaries.
Finding category example: `guardrail_mapping_missing`.

Expected M27 guardrail search terms are used as hints for static evidence lookup.

## Guardrail Artifact Evidence

- records present/missing guardrail evidence
- does not invent missing M27 artifact paths
- missing evidence must not be treated as READY

## Expected Outcome Checks

Rejects `BYPASS_ALLOWED`, `APPROVED`, `AUTHORIZED`.

## Non-Authorization Claim Checks

Checker does not flag negated non-authorization statements as forbidden claims.

## BYPASS_DETECTED Safety Rule

BYPASS_DETECTED is blocking and must remain a safe high-level signal only.

## Reference Checker Fixtures

- `negated-non-auth-statement`
- `approval-claim`
- `bypass-allowed-status`
- `zero-fixtures-root`

## Findings

Includes categories such as:
- fixture_checked
- guardrail_mapping_found
- guardrail_mapping_missing
- guardrail_evidence_found
- guardrail_evidence_missing
- forbidden_status
- forbidden_authority_claim
- bypass_detected_signal
- needs_review

## JSON Output Behavior

JSON includes result, fixture roots, checked fixtures, mapped guardrails, warnings, errors, findings.
Paths are repository-relative.

## No-Write Behavior

Checker is static read-only and does not modify files.

## Non-Authorization Boundary

Static bypass resistance checker is not approval.
Static bypass resistance checker does not authorize commit, push, merge, release, deployment, or protected changes.
Static bypass resistance checker does not authorize bypassing AgentOS guardrails.
Static bypass resistance checker does not execute bypass attempts.
Static bypass resistance checker does not prove runtime blocking by execution.
Static bypass resistance checker does not weaken, disable, or reduce any guardrail.
Static bypass resistance checker must not weaken M27 runtime enforcement.
Static bypass resistance checker must not weaken M28 context control.
Human Gate remains approval authority.

## Limitations

Static analysis does not replace runtime proof.
