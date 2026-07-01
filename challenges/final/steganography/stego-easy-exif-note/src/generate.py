#!/usr/bin/env python3
import struct
from pathlib import Path
FLAG = "edu_ctf{exif_note_seen}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "photo.jpg"
def segment(marker: int, data: bytes) -> bytes:
    return bytes([0xFF, marker]) + struct.pack("!H", len(data) + 2) + data
def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    comment = ("Учебный JPEG-комментарий: " + FLAG).encode("utf-8")
    app0 = b"JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00"
    OUT.write_bytes(b"\xff\xd8" + segment(0xE0, app0) + segment(0xFE, comment) + b"\xff\xd9")
if __name__ == "__main__":
    main()
