# Execution Verification Registry

## Purpose

Execution verification registry is a machine-readable index of M56–M60 execution-verification artifacts.

## Scope

This document explains the registry role, schema, builder, and checker. It does not change artifact authority.

## Inputs

- docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md
- schemas/execution-verification-registry.schema.json
- data/execution-verification-registry.json

## Components

- data/execution-verification-registry.json: registry data
- scripts/build-execution-verification-registry.py: builder/normalizer
- scripts/check-execution-verification-registry.py: validator/checker

## Role in M60

Registry supports navigation and validation for cleanup planning in M60.
It helps detect missing paths and metadata inconsistencies before later consolidation steps.

## Contract and Schema Relationship

- Contract defines semantics, boundaries, and conflict rules.
- Schema defines required JSON structure, enums, and field types.
- Checker enforces structure + core contract rules.
- Builder normalizes and writes deterministic registry JSON.

## Usage

Build/normalize:
```bash
python3 scripts/build-execution-verification-registry.py
```

Validate:
```bash
python3 scripts/check-execution-verification-registry.py --json
```

## Non-Authority Boundary

Registry is not approval.
Registry does not start cleanup execution.
Registry does not mutate lifecycle state.
Registry does not authorize merge, push, or release.
Registry does not change M56–M59 safety semantics.
Registry does not delete, rename, move, archive, deprecate, or consolidate artifacts.
Registry does not start M61 or M62.
Registry does not replace human review.

## Final Status

FINAL_STATUS: M60_REGISTRY_BUILDER_VALIDATOR_DEFINED
