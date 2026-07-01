#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FLAG = (ROOT / "flag.txt").read_text(encoding="utf-8").strip()


def main() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    data = bytearray(b"\x00REV\x7fTRAINING\x00")
    for item in ["not_a_flag{demo}", "status=local-only", "подсказка: strings", FLAG, "end-of-blob"]:
        data += bytes([0, 3, 255]) + item.encode("utf-8") + b"\x00"
    data += bytes((i * 37 + 11) % 256 for i in range(64))
    (DIST / "strings_attached.bin").write_bytes(bytes(data))
    print(DIST / "strings_attached.bin")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
