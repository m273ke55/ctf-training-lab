#!/usr/bin/env python3
import struct, zlib
from pathlib import Path
FLAG = "edu_ctf{lsb_pixels_talk}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "pixels.png"
WIDTH, HEIGHT = 64, 8
def chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack("!I", len(data)) + kind + data + struct.pack("!I", zlib.crc32(kind + data) & 0xFFFFFFFF)
def bits_from_message(message: bytes):
    for byte in message:
        for shift in range(7, -1, -1): yield (byte >> shift) & 1
def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload_bits = list(bits_from_message((FLAG + "\0").encode("ascii")))
    pixels = bytearray((90 + (i * 37) % 120) for i in range(WIDTH * HEIGHT))
    for i, bit in enumerate(payload_bits): pixels[i] = (pixels[i] & 0xFE) | bit
    rows = [b"\x00" + bytes(pixels[y*WIDTH:(y+1)*WIDTH]) for y in range(HEIGHT)]
    ihdr = struct.pack("!IIBBBBB", WIDTH, HEIGHT, 8, 0, 0, 0, 0)
    OUT.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(b"".join(rows))) + chunk(b"IEND", b""))
if __name__ == "__main__": main()
