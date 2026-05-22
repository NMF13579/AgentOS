# Fixture

scope_control:
  allowed_paths:
    - docs/
  forbidden_paths:
    - docs/private.md
  allow_new_files: false
  allowed_new_files:
    - docs/
  forbidden_new_files:
    - scripts/
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/
