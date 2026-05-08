# M27 Platform Setup Session

- repository:
- setup_actor:
- setup_actor_role: UNKNOWN
- setup_started_at:
- setup_completed_at:
- level_2_requested:
- level_2_status: LEVEL_2_AVAILABLE
- ci_workflow_present:
- codeowners_present:
- placeholder_owners_replaced:
- target_branches:
- required_pr_enabled:
- required_status_checks_enabled:
- m27_enforcement_required:
- m25_validation_required_if_present:
- codeowners_review_required:
- force_push_disabled:
- branch_deletion_disabled:
- direct_push_restricted:
- bypass_permissions_restricted:
- secrets_shared_with_agent:
- platform_verification_result:
- known_gaps:
- next_required_action:
- non_authorization_warning:

Allowed `setup_actor_role` values:
- `REPOSITORY_OWNER`
- `REPOSITORY_ADMIN`
- `ORGANIZATION_ADMIN`
- `UNKNOWN`

Allowed `level_2_status` values:
- `SKIPPED_LEVEL_2_NOT_ENABLED`
- `LEVEL_2_AVAILABLE`
- `LEVEL_2_SETUP_IN_PROGRESS`
- `LEVEL_2_NEEDS_OWNER_ACTION`
- `PLATFORM_PARTIAL`
- `PLATFORM_ENFORCED`
- `NEEDS_REVIEW`

No secret values may be written into this template.
This setup session is not approval by itself.
This setup session does not authorize push, merge, release, or platform enforcement by itself.
PLATFORM_ENFORCED must not be claimed until 27.13.1 verifies it.
This setup session does not enable GitHub settings by itself.
