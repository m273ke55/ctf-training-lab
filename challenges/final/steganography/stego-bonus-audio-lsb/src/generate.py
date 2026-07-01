#!/usr/bin/env python3
from pathlib import Path
import math, struct, wave
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip().encode()+b'\0'; bits=[(b>>i)&1 for b in flag for i in range(7,-1,-1)]
    rate=8000; frames=[]
    for i in range(max(1200,len(bits))):
        sample=int(500*math.sin(2*math.pi*220*i/rate))
        if i < len(bits): sample=(sample & ~1) | bits[i]
        frames.append(struct.pack('<h', sample))
    DIST.mkdir(exist_ok=True)
    with wave.open(str(DIST/'whisper.wav'),'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(b''.join(frames))
    return 0
if __name__=='__main__': raise SystemExit(main())
