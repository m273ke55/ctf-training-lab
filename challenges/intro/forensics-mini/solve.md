# Решение

## Шаги

1. Извлеките читаемые строки из бинарного файла:

```bash
strings dist/artifact.bin
```

2. Среди служебных фраз найдите строку формата `edu_ctf{...}`.

3. Флаг: `edu_ctf{mini_forensics_strings}`.

## Проверка solver-скриптом

```bash
python3 src/solve.py
```
