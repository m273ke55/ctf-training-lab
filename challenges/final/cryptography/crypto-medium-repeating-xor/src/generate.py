#!/usr/bin/env python3
from pathlib import Path
FLAG = 'edu_ctf{xor_key_found}'.encode()
KEY = b"owl"
ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    out = ROOT / "dist"
    out.mkdir(parents=True, exist_ok=True)
    ciphertext = bytes(b ^ KEY[i % len(KEY)] for i, b in enumerate(FLAG))
    (out / "ciphertext.hex").write_text(ciphertext.hex() + "\n", encoding="utf-8")
    (out / "note.txt").write_text("The plaintext is a standard edu_ctf flag encrypted with a short repeating XOR key.\n", encoding="utf-8")
    print("wrote dist/ciphertext.hex and dist/note.txt")
if __name__ == "__main__": main()
