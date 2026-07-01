# Решение

Переберите все повороты алфавита и найдите текст, похожий на формат flag.

## Шаги

1. Откройте `dist/ciphertext.txt` и скопируйте ciphertext.
2. Переберите все 26 сдвигов Caesar.
3. Остановитесь, когда plaintext содержит читаемый flag, начинающийся с `edu_ctf{`.

## Команда

```bash
python3 src/solve.py
```

Скрипт выводит:

```text
edu_ctf{mini_crypto_rotates}
```
