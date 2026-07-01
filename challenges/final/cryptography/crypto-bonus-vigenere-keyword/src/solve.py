#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; KEY='campus'
def dec(text):
    out=[]; j=0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base=65 if ch.isupper() else 97; shift=ord(KEY[j%len(KEY)])-97; j+=1
            out.append(chr((ord(ch)-base-shift)%26+base))
        else: out.append(ch)
    return ''.join(out)
def main(): print(dec((ROOT/'dist'/'ciphertext.txt').read_text().strip())); return 0
if __name__=='__main__': raise SystemExit(main())
