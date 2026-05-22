Capability | M40 Coverage | M41 Operationalization | M42 Regression Protection | Limitation | Final Status
--- | --- | --- | --- | --- | ---
agent report as claim | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
runner proof as evidence | COMPLETE | COMPLETE | COMPLETE | evidence is validation signal only | COMPLETE
private evaluator mapping | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
canary integrity | COMPLETE | COMPLETE | COMPLETE | no production-grade claim | COMPLETE_WITH_LIMITATION
process trace | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
evidence binding | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
strict mode | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | baseline strict failures remain | COMPLETE_WITH_LIMITATION
failure response protocol | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
runtime bypass smoke | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | smoke only, not production sandbox | COMPLETE_WITH_LIMITATION
validator authority boundary | COMPLETE | COMPLETE | COMPLETE | no cryptographic authority claim | COMPLETE_WITH_LIMITATION
role separation | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
evidence immutability | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | metadata/hash limits documented | COMPLETE_WITH_LIMITATION
amendment flow | COMPLETE | COMPLETE | COMPLETE | none | COMPLETE
unified integrity CLI | DOCUMENTED_GAP | COMPLETE | COMPLETE | non-zero outcomes remain | COMPLETE_WITH_LIMITATION
fixture registry | DOCUMENTED_GAP | COMPLETE | COMPLETE | registry is navigation metadata | COMPLETE_WITH_LIMITATION
result UX | DOCUMENTED_GAP | COMPLETE | COMPLETE | advisory text is not authority | COMPLETE_WITH_LIMITATION
`all --strict` integrity integration | DOCUMENTED_GAP | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | strict remains non-zero | COMPLETE_WITH_LIMITATION
`all --strict --json` capability | DOCUMENTED_GAP | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | valid JSON with failing aggregate | COMPLETE_WITH_LIMITATION
regression runner | NOT_IMPLEMENTED | DEFERRED | COMPLETE_WITH_LIMITATION | known fails: summary-json-conflict, warning-not-clean-pass | COMPLETE_WITH_LIMITATION
negative regression fixtures | NOT_IMPLEMENTED | DEFERRED | COMPLETE | none | COMPLETE
official regression CLI wrapper | NOT_IMPLEMENTED | DEFERRED | COMPLETE_WITH_LIMITATION | mirrors known runner failures | COMPLETE_WITH_LIMITATION
recursion-safe strict path | NOT_IMPLEMENTED | DEFERRED | COMPLETE | skip-all-strict self-check only in safe path | COMPLETE
final authority boundary | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | COMPLETE_WITH_LIMITATION | human approval remains separate | COMPLETE_WITH_LIMITATION

COMPLETE does not mean human approval.
