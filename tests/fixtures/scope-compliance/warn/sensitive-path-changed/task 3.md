# Fixture

scope_control:
  allowed_paths:
    - scripts/
  forbidden_paths:
    - .github/
  allow_new_files: false
  allowed_new_files:
    - scripts/
  forbidden_new_files:
    - .github/
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/
