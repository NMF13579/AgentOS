# Process Trace Policy

## Purpose
Process trace records command execution evidence for PASS claims.

## Core Boundary
Agent-written trace is claim, not proof.
runner_generated: true must be set by runner, trusted validation wrapper, or approved validation entrypoint.
A trusted validation wrapper must not be created, modified, or invoked as authority by the execution agent itself.

## Minimal Trace Record
- command
- exit_code
- output_artifact
- output_hash
- generated_at
- runner_generated
- validation_source_id

## Trusted Trace Conditions
Trace is trusted only if:
- trace created by runner/approved wrapper
- output artifact exists
- output hash matches
- command exit code recorded
- writability limitation recorded if present
- evaluator can verify recorded hash

If runner-generated proof cannot be verified: HONEST_PASS_NEEDS_REVIEW

## Failure Classes
TRACE_MISSING, TRACE_INVALID, ARTIFACT_MISSING, HASH_MISMATCH, RUNNER_PROOF_NOT_VERIFIED

## MVP Limitations
No cryptographic timestamp authority.
