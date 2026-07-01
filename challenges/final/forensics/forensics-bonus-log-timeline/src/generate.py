#!/usr/bin/env python3
from pathlib import Path
import base64
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip(); payload=base64.b64encode(flag.encode()).decode()
    lines=[]
    for i in range(1,61):
        if i==37: lines.append(f'2026-04-18T10:{i:02d}:00Z level=DEBUG service=api event=debug_note user=trainer payload={payload}')
        else: lines.append(f'2026-04-18T10:{i:02d}:00Z level=INFO service=web event=request status=200 path=/lesson/{i%7}')
    DIST.mkdir(exist_ok=True); (DIST/'server.log').write_text('\n'.join(lines)+'\n',encoding='utf-8'); return 0
if __name__=='__main__': raise SystemExit(main())
