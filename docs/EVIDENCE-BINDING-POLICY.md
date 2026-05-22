# Evidence Binding Policy

## Purpose
Bind PASS claims to proof artifacts through reproducible hashing.

Evidence Binding is integrity evidence, not approval.
PASS claim with agent-computed binding only is not clean PASS.

## Minimal Binding Record
- result_claim
- bound_artifacts[path, sha256]
- binding_hash
- generated_by
- validation_source_id

## Clean PASS Requirements
- proof artifacts exist
- artifact hashes match
- binding hash reproducible
- binding generated or verified by runner/evaluator
- evidence report records binding check result

## Failure Classes
BINDING_INVALID, ARTIFACT_MISSING, HASH_MISMATCH, PASS_WITHOUT_PROOF, RUNNER_PROOF_NOT_VERIFIED

## MVP Limitation
This MVP provides integrity checking, not cryptographic timestamp authority.
