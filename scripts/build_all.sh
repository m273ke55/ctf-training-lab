#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f scripts/verify_flags.py || ! -f scripts/validate_web_services.py || ! -f scripts/verify_solvers.py ]]; then
  echo "[build][error] Скрипты проверки не найдены" >&2
  exit 1
fi

echo "[build] Генерация публичных dist-артефактов"
mapfile -t generators < <(find challenges -path '*/src/generate.py' -type f | sort)

if [[ ${#generators[@]} -eq 0 ]]; then
  echo "[build][warn] Генераторы не найдены"
else
  for generator in "${generators[@]}"; do
    echo "[build] Запуск: python3 ${generator}"
    python3 "$generator"
  done
fi

echo "[build] Проверка флагов"
python3 scripts/verify_flags.py

echo "[build] Проверка Web-сервисов"
python3 scripts/validate_web_services.py

echo "[build] Проверка solver-скриптов"
python3 scripts/verify_solvers.py

echo "[build] Проверки прошли"
echo "[build] Build завершён"
