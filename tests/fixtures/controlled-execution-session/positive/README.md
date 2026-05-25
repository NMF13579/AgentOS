# Controlled Execution Session Positive Fixtures

## Purpose

This directory contains positive test fixture cases to validate the M58 Controlled Execution Session CLI (`check-controlled-execution-session.py`).

## Fixture Cases

The following fixture cases are defined:
1. `positive-clean-ready`: Happy-path controlled execution session readiness.
2. `positive-ready-with-warnings`: Valid readiness with non-blocking warning preserved.
3. `positive-closed-pending-m59`: Valid closed-pending-M59 handoff state.

## Expected Results

Expected outcomes are defined in the `expected.json` oracle for each case.

## Expected JSON as Oracle

Each fixture directory includes an `expected.json` which functions as the oracle for validation runner checks.

## Strict Mode Expectations

In strict mode, warning cases (such as `positive-ready-with-warnings`) are elevated to blockers, resulting in a blocked decision.

## Non-Authority Rules

- M58 positive fixtures do not open an execution session.
- M58 positive fixtures do not authorize task completion.
- M58 positive fixtures do not verify execution result.
- M58 positive fixtures do not create approval.
- M58 positive fixtures do not authorize merge, push, or release.
- M58 positive fixtures do not mutate lifecycle state.
- M58 positive fixtures only provide safe positive test data for the controlled execution session CLI.

## Relationship to 58.7 CLI

These fixtures are evaluated directly by the M58 CLI to verify correct implementation of preconditions and policy decisions.

## Relationship to 58.8.2 Negative Fixtures

While positive fixtures represent safe execution readiness states, 58.8.2 negative fixtures represent unsafe, contradictory, or malformed inputs that must be blocked.

## Relationship to 58.9 Fixture Runner

The 58.9 fixture runner executes the M58 CLI against all positive and negative fixture scenarios and verifies the outputs and exit codes match the respective `expected.json` oracle.
