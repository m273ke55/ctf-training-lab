#!/usr/bin/env python3
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip(); DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(DIST/'unknown.dat','w',zipfile.ZIP_DEFLATED) as z: z.writestr('note.txt',f'Учебная заметка. Флаг: {flag}\n')
    return 0
if __name__=='__main__': raise SystemExit(main())
