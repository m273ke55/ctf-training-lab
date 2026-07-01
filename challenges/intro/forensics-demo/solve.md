# Решение

Файл называется `mystery.jpg`, но расширение не является доказательством типа файла.

## Шаги

1. Проверяем тип файла:

```bash
file dist/mystery.jpg
```

2. Смотрим первые байты:

```bash
xxd -l 64 dist/mystery.jpg
```

3. Видим читаемый текст и строку с флагом. Файл можно открыть обычным `cat`:

```bash
cat dist/mystery.jpg
```

4. Флаг: `edu_ctf{forensics_demo_magic}`.

## Проверка solver-скриптом

```bash
python3 src/solve.py
```
