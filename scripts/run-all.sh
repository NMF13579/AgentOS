#!/usr/bin/env bash
# =============================================================
# LEGACY SCRIPT - do not use for M12+ flow
# This script validates tasks/active-task.md as a TASK contract
# and is incompatible with active-pointer format.
# Now delegates to the canonical thin dispatcher.
# =============================================================
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

exec "$PYTHON_BIN" scripts/agentos-validate.py all
