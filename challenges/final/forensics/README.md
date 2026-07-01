# Финальные задачи: Forensics

Эта категория содержит безопасные локальные учебные задачи по цифровой криминалистике: определение типа файла по содержимому, поиск приклеенных архивов и анализ небольшого сетевого дампа.

## Реализованные задачи

| Challenge | Сложность | Баллы | Концепция |
| --- | --- | ---: | --- |
| `forensics-easy-file-signature` | easy | 100 | определение ZIP-архива по magic bytes несмотря на неверное расширение |
| `forensics-medium-hidden-archive` | medium | 200 | поиск ZIP-архива, приклеенного к концу JPEG-файла |
| `forensics-hard-traffic-note` | hard-but-fair | 300 | анализ PCAP, поиск HTTP-ответа и декодирование base64-заметки |
| `forensics-bonus-log-timeline` | medium | 200 | bonus-анализ server.log, поиск debug_note и декодирование base64 payload |

Все публичные артефакты генерируются в каталог `dist/` каждой задачи скриптом `src/generate.py`.
