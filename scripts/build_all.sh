#!/usr/bin/env bash
set -euo pipefail

echo "[build] CTF Training Lab build placeholder"
if [[ ! -f scripts/verify_flags.py ]]; then
  echo "[build][error] scripts/verify_flags.py not found" >&2
  exit 1
fi

echo "[build] Verifying flags"
python3 scripts/verify_flags.py

echo "[build] Future task generators will be called here"
echo "[build] Done"
