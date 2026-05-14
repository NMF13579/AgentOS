# M41.1 Unified Integrity Command Plan

M41.1 proposes command integration only.
M41.1 does not modify agentos-validate.py.
Final `integrity` result token contract belongs to M41.2.
The `integrity` command must not erase domain-specific source tokens.

## Proposed Command Surface

### `python3 scripts/agentos-validate.py honest-pass`
- purpose: evaluate proof/trace/binding integrity using existing M40.9 mode
- current status: implemented
- integrate in M41: keep as base
- required inputs: `--fixtures` or artifact flags
- expected result tokens: `HONEST_PASS_OK`, `HONEST_PASS_VIOLATION`, `HONEST_PASS_NEEDS_REVIEW`
- strict behavior: requires trace + binding in artifact mode
- gate type: blocking
- integration risk: token translation ambiguity when aggregated

### `python3 scripts/agentos-validate.py runtime-bypass-smoke`
- purpose: run M40.10 smoke harness via unified CLI
- current status: standalone script only
- integrate in M41: yes
- required inputs: optional `--json`, `--keep-sandbox`
- expected result tokens: `BYPASS_TEST_*`
- strict behavior: advisory in default, blocking in strict integrity profile
- gate type: needs-review/blocking depending token
- integration risk: users may misread smoke as production enforcement

### `python3 scripts/agentos-validate.py validator-authority`
- purpose: run validator authority boundary checks
- current status: standalone checker only
- integrate in M41: yes
- required inputs: record path or fixture mode
- expected result tokens: `VALIDATOR_AUTHORITY_*`
- strict behavior: VIOLATION blocks, NEEDS_REVIEW blocks completion
- gate type: blocking
- integration risk: source trust metadata quality

### `python3 scripts/agentos-validate.py role-separation`
- purpose: run role separation checks
- current status: standalone checker only
- integrate in M41: yes
- required inputs: record path or fixture mode
- expected result tokens: `ROLE_SEPARATION_*`
- strict behavior: HIGH/CRITICAL violations always blocking
- gate type: blocking
- integration risk: confusion for LOW/MEDIUM exceptions

### `python3 scripts/agentos-validate.py evidence-immutability`
- purpose: run immutability checks
- current status: standalone checker only
- integrate in M41: yes
- required inputs: immutability record path
- expected result tokens: `EVIDENCE_IMMUTABILITY_*`
- strict behavior: VIOLATION blocks, LEGACY often NEEDS_REVIEW
- gate type: blocking/needs-review
- integration risk: overclaim risk without external baseline authority

### `python3 scripts/agentos-validate.py evidence-amendments`
- purpose: validate amendment semantics
- current status: standalone checker only
- integrate in M41: yes
- required inputs: amendment record path
- expected result tokens: `EVIDENCE_AMENDMENT_*`
- strict behavior: authority ambiguity blocks completion
- gate type: blocking/needs-review
- integration risk: reviewer metadata may be incomplete in practice

### `python3 scripts/agentos-validate.py integrity`
- purpose: aggregate integrity commands into one navigation layer
- current status: not implemented
- integrate in M41: proposed for M41.2
- required inputs: subcommand-specific or default fixture mode
- expected result tokens: proposed unified navigation status + source tokens
- strict behavior: include all strict-capable subchecks
- gate type: blocking when any source token is violation
- integration risk: accidental erasure of source-token meaning

### `python3 scripts/agentos-validate.py all --strict`
- purpose: overall validation plus strict integrity gate
- current status: implemented with known baseline failure gap
- integrate in M41: preserve behavior, improve explainability
- required inputs: repo state + active task context
- expected result tokens: existing `PASS/FAIL/...` plus embedded integrity source tokens in detail
- strict behavior: should include `integrity` stage after M41.2
- gate type: blocking
- integration risk: known unrelated failures can mask integrity signal

## Recommended M41.2 Action
Define `integrity` contract, output envelope, and token-preservation rules before wiring additional commands into `all --strict`.
