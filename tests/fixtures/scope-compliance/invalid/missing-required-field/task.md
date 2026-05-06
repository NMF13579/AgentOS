# Fixture

scope_control:
  allowed_paths:
    - docs/
  forbidden_paths:
    - scripts/
  allow_new_files: true
  allowed_new_files:
    - docs/
  forbidden_new_files:
    - scripts/
  allow_modify_existing: true
  allow_deletes: false
  sensitive_paths:
    - scripts/
