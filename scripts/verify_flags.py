#!/usr/bin/env python3
"""Verify all challenge flags."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CHALLENGES = ROOT / "challenges"
FLAG_RE = re.compile(r"^edu_ctf\{[a-zA-Z0-9_!?@#.,:+-]+\}$")

def main() -> int:
    errors = []
    files = sorted(CHALLENGES.rglob("flag.txt"))
    if not files:
        print("[WARN] flag.txt files were not found in challenges/.")
        return 0
    for path in files:
        lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        rel = path.relative_to(ROOT)
        if len(lines) != 1:
            errors.append(f"{rel}: expected exactly one non-empty flag, found {len(lines)}")
            continue
        flag = lines[0]
        if not FLAG_RE.fullmatch(flag):
            errors.append(f"{rel}: invalid flag format: {flag!r}")
        else:
            print(f"[OK] {rel}: {flag}")
    if errors:
        print("\nFlag verification failed:")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"\nAll {len(files)} flag file(s) are valid.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
