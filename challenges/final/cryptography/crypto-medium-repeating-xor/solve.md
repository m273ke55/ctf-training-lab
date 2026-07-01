# Решение

В задаче используется repeating-key XOR. У XOR есть полезное свойство: если `cipher = plain XOR key`, то `key = cipher XOR plain`.

Так как каждый flag начинается с `edu_ctf{`, этот префикс можно использовать как known plaintext.

## Шаги

1. Прочитайте hex-ciphertext из `dist/ciphertext.hex`.
2. Преобразуйте его в bytes.
3. Попробуйте короткие длины ключа.
4. Восстановите байты ключа по известному префиксу там, где это возможно.
5. Расшифруйте данные и оставьте кандидат, похожий на `edu_ctf{...}`.

## Команда

```bash
python3 src/solve.py
```

Ожидаемый вывод:

```text
edu_ctf{xor_key_found}
```
