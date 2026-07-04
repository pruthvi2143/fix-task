#!/bin/bash
set -euo pipefail

# Run the helper from wherever this script lives (never assumes a mount path).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${SCRIPT_DIR}/solve.py"
