#!/usr/bin/env bash
set -euo pipefail

# Now delegates to the canonical thin dispatcher.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

exec "$PYTHON_BIN" "$SCRIPT_DIR/agentos-validate.py" all
