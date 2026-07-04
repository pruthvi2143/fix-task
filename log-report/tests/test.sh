#!/bin/bash
# pytest and pytest-json-ctrf are baked into the environment image.
# This script must always exit 0; the pass/fail signal lives in reward.txt.
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA \
  --ctrf /logs/verifier/ctrf.json
rc=$?

if [ "$rc" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit 0
