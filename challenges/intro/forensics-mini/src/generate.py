#!/usr/bin/env python3
from pathlib import Path

FLAG = b"edu_ctf{mini_forensics_strings}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "artifact.bin"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = b"\x00\x13\x37CTF-LAB\x00" + bytes(range(32, 48)) + b"\xff\x00" + FLAG + b"\x00noise-end\n"
    OUT.write_bytes(data)


if __name__ == "__main__":
    main()
