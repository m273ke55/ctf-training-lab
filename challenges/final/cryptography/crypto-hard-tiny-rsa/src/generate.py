#!/usr/bin/env python3
from pathlib import Path

FLAG = b"edu_ctf{tiny_rsa_done}"
P = 50_021
Q = 50_023
E = 65_537
BLOCK_SIZE = 4
ROOT = Path(__file__).resolve().parents[1]


def blocks(data: bytes, size: int):
    padded = data + b"\x00" * ((size - len(data) % size) % size)
    for i in range(0, len(padded), size):
        yield padded[i:i + size]


def main() -> None:
    n = P * Q
    phi = (P - 1) * (Q - 1)
    assert pow(E, -1, phi)
    ciphertext = [pow(int.from_bytes(block, "big"), E, n) for block in blocks(FLAG, BLOCK_SIZE)]
    out = ROOT / "dist"
    out.mkdir(parents=True, exist_ok=True)
    (out / "public.txt").write_text(
        "# Tiny RSA public data. Ciphertext is encrypted in 4-byte blocks.\n"
        f"n = {n}\n"
        f"e = {E}\n"
        "c = " + ",".join(str(x) for x in ciphertext) + "\n",
        encoding="utf-8",
    )
    print("wrote dist/public.txt")


if __name__ == "__main__":
    main()
