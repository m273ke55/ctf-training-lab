# Финальные задачи: Steganography

Эта категория содержит безопасные локальные учебные задачи по стеганографии: поиск заметки в метаданных, извлечение сообщения из LSB PNG и анализ тонов на spectrogram WAV-файла.

## Реализованные задачи

| Challenge | Сложность | Баллы | Концепция |
| --- | --- | ---: | --- |
| `stego-easy-exif-note` | easy | 100 | поиск JPEG COM-комментария через `exiftool` или `strings` |
| `stego-medium-lsb-image` | medium | 200 | извлечение флага из младших битов пиксельных байтов PNG |
| `stego-hard-audio-spectrogram` | hard-but-fair | 300 | восстановление строки по последовательности частот в WAV/spectrogram |
| `stego-bonus-audio-lsb` | medium | 200 | bonus-извлечение флага из LSB 16-bit WAV-сэмплов |

Все публичные артефакты генерируются в каталог `dist/` каждой задачи скриптом `src/generate.py` и не хранятся в git, кроме `dist/.gitkeep`.
