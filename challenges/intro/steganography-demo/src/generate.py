#!/usr/bin/env python3
import struct
import zlib
from pathlib import Path

FLAG = "edu_ctf{stego_demo_comment}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "picture.png"


def chunk(kind: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(kind + data) & 0xFFFFFFFF
    return struct.pack("!I", len(data)) + kind + data + struct.pack("!I", crc)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    width, height = 2, 2
    ihdr = struct.pack("!IIBBBBB", width, height, 8, 2, 0, 0, 0)
    pixels = [(80, 140, 220), (90, 150, 230), (100, 160, 240), (110, 170, 250)]
    rows = []
    for y in range(height):
        rows.append(bytes([0]) + b"".join(bytes(p) for p in pixels[y * width:(y + 1) * width]))
    text = b"Comment" + bytes([0]) + ("Учебная скрытая заметка: " + FLAG).encode("utf-8")
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"tEXt", text) + chunk(b"IDAT", zlib.compress(b"".join(rows))) + chunk(b"IEND", b"")
    OUT.write_bytes(png)


if __name__ == "__main__":
    main()
