#!/usr/bin/env python3
import ast
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TARGET=ROOT/'dist'/'tiny_checker.py'
def main():
    tree=ast.parse(TARGET.read_text(encoding='utf-8')); c={}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in {'SHIFT','DATA'}:
            c[n.targets[0].id]=ast.literal_eval(n.value)
    print(''.join(chr(v-c['SHIFT']) for v in c['DATA'])); return 0
if __name__=='__main__': raise SystemExit(main())
