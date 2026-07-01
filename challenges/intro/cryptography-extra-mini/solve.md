# Решение

## Идея

Ключ состоит из одного байта, поэтому вариантов всего 256. Формат флага известен заранее, значит правильный результат легко распознать.

## Шаги

1. Прочитать `dist/ciphertext.hex`.
2. Преобразовать hex в bytes.
3. Для каждого ключа от `0` до `255` выполнить XOR каждого байта.
4. Декодировать кандидат как текст.
5. Найти строку формата `edu_ctf{...}`.

Пример фрагмента:

```python
data = bytes.fromhex(hex_text)
for key in range(256):
    candidate = bytes(byte ^ key for byte in data).decode("utf-8", "ignore")
    if candidate.startswith("edu_ctf{") and candidate.endswith("}"):
        print(candidate)
```

Готовое решение находится в `src/solve.py`.

Финальный флаг: `edu_ctf{intro_xor_byte}`.

## Чему учит задача

Задача показывает, почему single-byte XOR слаб при известном формате plaintext, и тренирует простой brute force ключа.
