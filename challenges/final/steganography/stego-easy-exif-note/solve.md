# Решение

Флаг находится в JPEG COM-сегменте: это комментарий файла, похожий на метаданные изображения.

## Путь через exiftool

```bash
exiftool dist/photo.jpg
```

В выводе найдите комментарий со строкой `edu_ctf{exif_note_seen}`.

## Fallback через strings

```bash
strings dist/photo.jpg
```

Так как комментарий хранится текстом, `strings` тоже показывает флаг.

## Проверка solver-скриптом

```bash
python3 src/solve.py
```
