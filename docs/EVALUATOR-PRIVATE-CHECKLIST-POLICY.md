# Evaluator Private Checklist Policy

## Policy
Do not hide requirements.
Hide evaluator traps.
Hidden checks allowed.
Hidden requirements forbidden.
Every hidden check must map to a public rule.

## What Agent May See
Public rules and expected behavior requirements.

## What Evaluator May Hide
Detection traps and anti-gaming checks that map to public rules.

## What Evaluator Must Not Hide
Any required behavior that is not publicly declared.

## Hidden Check vs Hidden Requirement
- Hidden check: private detection implementation of a public rule.
- Hidden requirement: undisclosed requirement. Forbidden.

## Allowed Private Checks
- Pattern checks for fake approval artifacts.
- Pattern checks for self-asserted authority.

## Forbidden Private Checks
- New mandatory behavior absent from public rules.
- Any rule with no mapping to public rule.

## Required Failure Classes
- `PRIVATE_CHECK_UNMAPPED`
- `HIDDEN_REQUIREMENT_DETECTED`

## Examples
A private check for fake approval text is allowed only when it maps to a public no-fake-approval rule.
