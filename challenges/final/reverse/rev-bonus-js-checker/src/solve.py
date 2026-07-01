#!/usr/bin/env python3
from pathlib import Path
import ast, re
ROOT=Path(__file__).resolve().parents[1]
def main():
    text=(ROOT/'dist'/'checker.js').read_text(encoding='utf-8')
    key=int(re.search(r'KEY\s*=\s*(\d+)',text).group(1)); data=ast.literal_eval(re.search(r'DATA\s*=\s*(\[[^\]]+\])',text).group(1))
    print(''.join(chr(v^key) for v in data)); return 0
if __name__=='__main__': raise SystemExit(main())
