#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BLOB = ROOT / "dist" / "mini_blob.bin"
PATTERN = re.compile(rb"edu_ctf\{[A-Za-z0-9_!?@#.,:+-]+\}")

def main() -> int:
    match = PATTERN.search(BLOB.read_bytes())
    if not match:
        raise SystemExit("Флаг не найден. Сначала запустите src/generate.py.")
    print(match.group(0).decode("ascii"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
