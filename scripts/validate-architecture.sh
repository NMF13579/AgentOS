#!/usr/bin/env bash
set -euo pipefail

# Now delegates to the canonical thin dispatcher.
# =============================================================
PYTHON_BIN="${PYTHON_BIN:-python3}"

exec "$PYTHON_BIN" scripts/agentos-validate.py all
