#!/usr/bin/env python3
from pathlib import Path
import math
ROOT = Path(__file__).resolve().parents[1]
BLOCK_SIZE = 4

def parse_public(path: Path):
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, value = [part.strip() for part in line.split("=", 1)]
        values[name] = value
    return int(values["n"]), int(values["e"]), [int(x) for x in values["c"].split(",")]

def factor_trial_division(n: int):
    if n % 2 == 0:
        return 2, n // 2
    limit = math.isqrt(n)
    candidate = 3
    while candidate <= limit:
        if n % candidate == 0:
            return candidate, n // candidate
        candidate += 2
    raise ValueError("n appears to be prime")

def main() -> None:
    n, e, ciphertext = parse_public(ROOT / "dist" / "public.txt")
    p, q = factor_trial_division(n)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    plaintext = b"".join(pow(c, d, n).to_bytes(BLOCK_SIZE, "big") for c in ciphertext)
    print(plaintext.rstrip(b"\x00").decode("ascii"))
if __name__ == "__main__": main()
