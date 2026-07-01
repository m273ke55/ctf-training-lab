#!/usr/bin/env python3
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist" / "check_me.py"

def main() -> int:
    tree = ast.parse(TARGET.read_text(encoding="utf-8"))
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in {"KEY", "DATA"}:
                constants[node.targets[0].id] = ast.literal_eval(node.value)
    flag = "".join(chr(value ^ constants["KEY"]) for value in constants["DATA"])
    print(flag)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
