#!/usr/bin/env python3
from pathlib import Path
import string
ROOT = Path(__file__).resolve().parents[1]
KNOWN = b"edu_ctf{"
PRINTABLE = set(bytes(string.printable, "ascii"))

def repeating_xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def main() -> None:
    ciphertext = bytes.fromhex((ROOT / "dist" / "ciphertext.hex").read_text(encoding="utf-8").strip())
    for key_len in range(1, 9):
        key = [None] * key_len
        ok = True
        for i, plain_b in enumerate(KNOWN):
            pos = i % key_len
            recovered = ciphertext[i] ^ plain_b
            if key[pos] is not None and key[pos] != recovered:
                ok = False
                break
            key[pos] = recovered
        if not ok or any(v is None for v in key):
            continue
        key_bytes = bytes(key)
        candidate = repeating_xor(ciphertext, key_bytes)
        if all(b in PRINTABLE for b in candidate):
            text = candidate.decode("ascii")
            if text.startswith("edu_ctf{") and text.endswith("}"):
                print(text)
                return
    raise SystemExit("flag was not found")
if __name__ == "__main__": main()
