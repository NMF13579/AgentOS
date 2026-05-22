Command contract map records expected behavior; it does not authorize state transitions.

| Command | Expected Mode | Expected Output | Expected Exit Semantics | Stable Fields | Known Gap | Regression If Broken |
|---|---|---|---|---|---|---|
| `integrity --help` | help text | human-readable usage | exit 0 | n/a | none | command missing or parse failure |
| `integrity --list-fixtures --json` | registry list | JSON | exit 0 or 1 if blocked | suite,result,exit_code,generated_at,details | none | invalid JSON / command missing |
| `integrity --fixtures --json` | fixture execution | JSON | 0 for OK/WARNING, 1 for VIOLATION/NEEDS_REVIEW/BLOCKED | suite,result,exit_code,generated_at,details,subchecks | warning remains non-clean-pass | source-token loss / invalid JSON |
| `integrity --strict --fixtures --json` | strict fixture execution | JSON | same semantics as above | same as above | none | strict path missing / invalid JSON |
| `integrity --fixtures --summary` | summary UX | human-readable summary | mirrors JSON exit semantics | summary fields list from M41.4 | none | summary implies approval |
| `integrity --strict --fixtures --summary` | strict summary UX | human-readable summary | mirrors strict JSON exit semantics | summary fields + warning phrase | none | hides warning / clean-pass claim |
| `integrity --explain-results` | explanation | human-readable token map | exit 0 | n/a | none | missing boundary phrase |
| `integrity --explain-result INTEGRITY_WARNING` | explanation single-token | human-readable | exit 0 | n/a | none | invented or changed meaning |
| `integrity --explain-result UNKNOWN_TOKEN` | unknown-token guard | human-readable error | non-zero | n/a | none | unknown token accepted with fake meaning |
| `integrity --fixtures --summary --json` | conflict guard | blocked message | non-zero | result/message if JSON path used | none | conflict no longer blocked |
| `all --strict` | strict aggregate | human-readable aggregate | currently non-zero in repo due known baseline failures | checks include integrity-strict-fixtures | known baseline failures | integrity check dropped silently |
| `all --strict --json` | strict aggregate JSON | JSON aggregate | currently non-zero in repo due known baseline failures | result, counts, checks[] | KNOWN_GAP_IF_DOCUMENTED (aggregate-style envelope) | invalid JSON / missing integrity check |

Contract status summary:
- `integrity` command family: STABLE
- `all --strict`: STABLE with KNOWN_GAP_IF_DOCUMENTED for baseline failures
- `all --strict --json` envelope shape: NEEDS_REVIEW / DEFERRED_TO_M42 for dedicated envelope semantics
