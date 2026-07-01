#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
    data=bytes.fromhex((ROOT/'dist'/'ciphertext.hex').read_text().strip())
    for key in range(256):
        text=bytes(b^key for b in data).decode('utf-8','ignore')
        m=re.fullmatch(r'edu_ctf\{[^}]+\}', text)
        if m: print(m.group(0)); return 0
    return 1
if __name__=='__main__': raise SystemExit(main())
