M42.1 plans regression fixtures only; it does not create them.

| Planned Check | Purpose | Future Target File or Command | Expected Result | Type | Priority | Milestone |
|---|---|---|---|---|---|---|
| command-exists-pass | Ensure command availability | `python3 scripts/agentos-validate.py integrity --help` | exit 0 | positive | P0 | M42.2 |
| json-output-valid-pass | Ensure machine-readable stability | `integrity --fixtures --json` | valid JSON | positive | P0 | M42.2 |
| source-token-preserved-pass | Guard token preservation | `integrity --fixtures --json` payload | source token fields preserved | positive | P0 | M42.2 |
| summary-output-boundary-pass | Guard summary boundary text | `integrity --fixtures --summary` | boundary phrase present | positive | P1 | M42.2 |
| warning-not-clean-pass | Guard warning semantics | strict summary + docs phrases | warning not clean PASS | positive | P0 | M42.2 |
| summary-json-conflict-fail | Guard mode conflict | `integrity --fixtures --summary --json` | non-zero blocked | negative | P0 | M42.2 |
| unknown-token-fail | Guard unknown explain token | `integrity --explain-result UNKNOWN_TOKEN` | non-zero + unknown-token message | negative | P0 | M42.2 |
| registry-recursion-fail | Guard recursion prevention | registry entry uses `integrity`/`all` | blocked result | negative | P0 | M42.3 |
| registry-missing-input-fail | Guard missing input path | registry non-null input path missing | blocked result | negative | P0 | M42.3 |
| false-approval-claim-fail | Guard false authority phrases | CLI/docs/report outputs | fail if approval phrases appear | negative | P0 | M42.2 |
| shell-true-fail | Guard forbidden subprocess style | static check: `grep shell=True scripts/agentos-validate.py` | fail if found | negative/static | P0 | M42.2 |
| all-strict-integrity-present-pass | Ensure strict integration stays present | `all --strict --json` checks include `integrity-strict-fixtures` | pass if present | positive | P0 | M42.3 |
| all-strict-json-known-gap-or-pass | Track json mode maturity | `all --strict --json` | pass if valid or mark documented known gap | mixed | P1 | M42.4+ |

Notes:
- `shell-true-fail` can stay as static grep-style check and does not require fixture directory initially.
- Use the baseline map as authoritative source for pass/fail wording, not as approval authority.
