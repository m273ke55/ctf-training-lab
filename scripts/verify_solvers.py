#!/usr/bin/env python3
"""Run every file-based challenge solver and compare it with flag.txt."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHALLENGES = ROOT / "challenges"
EXPECTED_SOLVER_COUNT = 28


def main() -> int:
    failures: list[str] = []
    solvers = sorted(CHALLENGES.rglob("src/solve.py"))
    if len(solvers) != EXPECTED_SOLVER_COUNT:
        failures.append(
            f"expected {EXPECTED_SOLVER_COUNT} solver scripts, found {len(solvers)}"
        )
    for solver in solvers:
        challenge = solver.parent.parent
        flag_path = challenge / "flag.txt"
        if not flag_path.is_file():
            failures.append(f"{solver.relative_to(ROOT)}: missing flag.txt")
            continue
        expected = flag_path.read_text(encoding="utf-8").strip()
        try:
            completed = subprocess.run(
                [sys.executable, str(solver)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{solver.relative_to(ROOT)}: timed out after 30 seconds")
            continue
        output = completed.stdout + completed.stderr
        if completed.returncode != 0 or expected not in output:
            failures.append(
                f"{solver.relative_to(ROOT)}: exit={completed.returncode}, expected flag not found"
            )
        else:
            print(f"[OK] {solver.relative_to(ROOT)}")

    if failures:
        print("\nSolver verification failed:")
        for failure in failures:
            print(f"[ERROR] {failure}")
        return 1
    print(f"\nAll {len(solvers)} file-based solver(s) returned the expected flag.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
