# Решение

В `holiday_photo.jpg` находится корректный небольшой JPEG, а после него приклеен ZIP-архив.

## Путь через binwalk

1. Проверяем файл:

```bash
file dist/holiday_photo.jpg
```

2. Ищем вложенные данные:

```bash
binwalk dist/holiday_photo.jpg
```

3. Извлекаем найденный ZIP или вырезаем данные по показанному смещению, затем читаем `note.txt`:

```bash
unzip -p extracted.zip note.txt
```

## Путь без binwalk, только Python

1. Найдите сигнатуру ZIP `PK\x03\x04` в байтах файла.
2. Возьмите все данные от найденного смещения до конца.
3. Откройте получившийся поток как ZIP и прочитайте `note.txt`.

Это делает solver:

```bash
python3 src/solve.py
```

Флаг: `edu_ctf{archive_inside}`.
