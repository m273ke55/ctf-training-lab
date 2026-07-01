#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; KEY='campus'
def vig(text, enc=True):
    out=[]; j=0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base=65 if ch.isupper() else 97; shift=ord(KEY[j%len(KEY)])-97; j+=1
            if not enc: shift=-shift
            out.append(chr((ord(ch)-base+shift)%26+base))
        else: out.append(ch)
    return ''.join(out)
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip(); DIST.mkdir(exist_ok=True)
    (DIST/'ciphertext.txt').write_text(vig(flag)+'\n',encoding='utf-8')
    (DIST/'note.txt').write_text('Ключ рядом с местом, где проходит занятие. Вспомните английское слово для университетской территории.\n',encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
