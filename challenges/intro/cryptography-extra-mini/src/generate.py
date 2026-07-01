#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; KEY=0x2A
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip().encode(); DIST.mkdir(exist_ok=True)
    (DIST/'ciphertext.hex').write_text(bytes(b^KEY for b in flag).hex()+'\n',encoding='utf-8')
    (DIST/'readme.txt').write_text('Сообщение зашифровано single-byte XOR. Известно, что открытый текст является флагом формата edu_ctf{...}.\n',encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
