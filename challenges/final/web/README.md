# Финальные задачи: Web

Категория содержит локальные HTTP-сервисы по базовым Web-механикам.

| Challenge | Сложность | Баллы | Концепция |
|---|---|---:|---|
| `web-easy-method-head` | easy | 100 | HTTP HEAD и анализ заголовков |
| `web-medium-command-injection` | medium | 200 | command injection и обход blacklist через newline |
| `web-hard-upload-include` | hard-but-fair | 300 | цепочка file upload + local include |
| `web-bonus-xxe-docx` | medium bonus | 200 | внешняя XML-сущность внутри DOCX |

Все сервисы запускаются командой `docker compose -f docker-compose.web.yml up --build -d` и проверяются через `python3 scripts/smoke_web.py`.
