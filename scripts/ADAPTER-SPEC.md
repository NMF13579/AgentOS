# ADAPTER-SPEC — issue codes (validator v1.2.1)

Single reference for humans and tools. Codes match `scripts/validate-adapters.sh` JSON output.

| Code | Severity | auto_fixable | fix_type | Notes |
|------|----------|--------------|----------|--------|
| REQUIRED_ADAPTER_MISSING | error | false | — | Create file; minimal redirect to `llms.txt` and `LAYER-1/agent-rules.md`. |
| MISSING_LLMS_REDIRECT | error | true | insert | Add `llms.txt` redirect line. |
| MISSING_AGENT_RULES_REDIRECT | error | true | insert | Add `LAYER-1/agent-rules.md` line. |
| MISSING_META_ROLE | warning | true | insert | `<!-- ROLE: ADAPTER ENTRYPOINT -->` |
| MISSING_META_AUTHORITY | warning | true | insert | `<!-- AUTHORITY: NON-AUTHORITY -->` |
| MISSING_META_SOT | warning | true | insert | `<!-- SOURCE_OF_TRUTH: no -->` |
| ADAPTER_STATE_LEAK | error | false | — | Remove `STATE.md` reference from adapter. |
| ADAPTER_HANDOFF_LEAK | error | false | — | Remove `HANDOFF.md` reference. |
| ADAPTER_DECISIONS_LEAK | error | false | — | Remove `DECISIONS.md` reference. |
| ADAPTER_INTENT_LEAK | error | false | — | Remove `INTENT.md` reference. |
| ADAPTER_LAYER2_LEAK | error | false | — | Remove `LAYER-2` reference. |
| ALT_BOOTSTRAP_LANGUAGE | error | false | — | Remove competing bootstrap phrasing. |
| COMPETING_ROUTING_LIST | error | false | — | Remove competing file-order lists. |
| OPTIONAL_ADAPTER_PRESENT | warning | false | — | Review or remove optional adapter. |
| ZED_COMPAT_CONFLICT | warning | false | — | Keep one Zed-compatible instruction file from the compat list. |
