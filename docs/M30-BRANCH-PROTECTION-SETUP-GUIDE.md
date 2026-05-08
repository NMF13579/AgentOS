# M30 Branch Protection Setup Guide

## Scope
- This guide does not configure GitHub settings automatically.
- Branch protection automation is out of scope for M30.7.

## Manual steps
- repository owner/admin should open Settings
- Branches / Branch protection rules
- create/edit rule for `main`
- create/edit rule for `dev`
- enable required status checks
- select Context Pipeline check by exact displayed name
- save and verify with test PR

## Boundaries
- Workflow existence is not branch protection.
- Do not claim required-check enforcement without evidence.
- Human Gate remains approval authority.

## sample-settings-summary.md should use this structure
- Branch: <main|dev|synthetic-branch>
- Observed check name: <check name shown by GitHub or unknown>
- Required check configured: <yes|no|unknown>
- Require branches up to date: <yes|no|unknown>
- Admin bypass policy: <allowed|restricted|unknown>
- Evidence source: <screenshot|copied settings summary|test PR|human confirmation|none>
- Expected verification status: <M30_REQUIRED_CHECK_*>
- Notes: <short explanation>

## admin-bypass-unclear
- Admin bypass uncertainty alone must not be upgraded to M30_REQUIRED_CHECK_CONFIGURED without warning.

- Workflow existence is not branch protection.
- This guide does not configure GitHub settings automatically.
- Branch protection automation is out of scope for M30.7.
