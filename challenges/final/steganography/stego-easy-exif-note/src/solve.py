#!/usr/bin/env python3
import re, struct
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "photo.jpg"
def jpeg_comments(blob: bytes):
    pos = 2
    while pos + 4 <= len(blob):
        if blob[pos] != 0xFF:
            pos += 1; continue
        marker = blob[pos + 1]
        if marker == 0xD9: break
        length = struct.unpack("!H", blob[pos + 2:pos + 4])[0]
        data = blob[pos + 4:pos + 2 + length]
        if marker == 0xFE: yield data
        pos += 2 + length
def main() -> None:
    text = b"\n".join(jpeg_comments(DATA.read_bytes())).decode("utf-8", errors="ignore")
    match = re.search(r"edu_ctf\{[^}]+\}", text)
    if not match: raise SystemExit("Флаг в JPEG COM-сегменте не найден")
    print(match.group(0))
if __name__ == "__main__": main()
