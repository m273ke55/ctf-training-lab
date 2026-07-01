# Решение

## Шаги

1. Проверяем тип файла:

```bash
file dist/report.pdf
```

2. Смотрим заголовок:

```bash
xxd -l 16 dist/report.pdf
```

3. Первые байты `50 4b 03 04` — это сигнатура ZIP. Распаковываем файл как архив:

```bash
unzip -l dist/report.pdf
unzip -p dist/report.pdf flag.txt
```

4. Получаем флаг `edu_ctf{magic_bytes_win}`.

## Проверка solver-скриптом

```bash
python3 src/solve.py
```
