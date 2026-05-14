# Canary Files Policy

## Definition
Canary files are protected sentinel files used to detect tampering.

## Boundaries
- Canary file is not task context.
- Canary file is not source of truth.
- Canary file must not be used as task evidence.

## MVP Checks
canary modified -> FAIL
canary deleted -> FAIL
canary appears in changed-files -> FAIL
canary used as evidence -> FAIL

## Limitation
MVP does not claim reliable canary read detection.

## Deferred
- canary read detection
- sandbox-based read telemetry
- production-grade file access monitoring
