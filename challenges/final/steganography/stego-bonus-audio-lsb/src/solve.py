#!/usr/bin/env python3
from pathlib import Path
import re, struct, wave
ROOT=Path(__file__).resolve().parents[1]
def main():
    with wave.open(str(ROOT/'dist'/'whisper.wav'),'rb') as w: raw=w.readframes(w.getnframes())
    bits=[struct.unpack_from('<h', raw, i)[0] & 1 for i in range(0,len(raw),2)]
    data=bytearray()
    for i in range(0,len(bits),8):
        byte=0
        for bit in bits[i:i+8]: byte=(byte<<1)|bit
        if byte==0: break
        data.append(byte)
        if byte==ord('}'): break
    print(re.search(rb'edu_ctf\{[^}]+\}', bytes(data)).group(0).decode()); return 0
if __name__=='__main__': raise SystemExit(main())
