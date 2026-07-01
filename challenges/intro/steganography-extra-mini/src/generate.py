#!/usr/bin/env python3
from pathlib import Path
import struct, math
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
def chunk(name, data):
    return name + struct.pack('<I', len(data)) + data + (b'\0' if len(data)%2 else b'')
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip()
    rate=8000; samples=[int(800*math.sin(2*math.pi*440*i/rate)) for i in range(400)]
    fmt=struct.pack('<HHIIHH',1,1,rate,rate*2,2,16)
    data=b''.join(struct.pack('<h',s) for s in samples)
    icmt=chunk(b'ICMT', f'Учебный комментарий WAV: {flag}'.encode('utf-8'))
    body=b'WAVE'+chunk(b'fmt ',fmt)+chunk(b'data',data)+chunk(b'LIST',b'INFO'+icmt)
    DIST.mkdir(exist_ok=True); (DIST/'comment.wav').write_bytes(b'RIFF'+struct.pack('<I',len(body))+body); return 0
if __name__=='__main__': raise SystemExit(main())
