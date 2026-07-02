# Web-задачи

В проект интегрированы пять автономных учебных Web-задач. Вводная демонстрация находится в `challenges/intro/web-demo`, четыре финальные задачи — в `challenges/final/web/`.

| ID | Механика | Сложность | Локальный адрес |
|---|---|---:|---|
| `web-demo` | выполнение пользовательского Python-кода | intro | `http://127.0.0.1:5101` |
| `web-easy-method-head` | различие HTTP-методов и заголовков | easy | `http://127.0.0.1:5102` |
| `web-medium-command-injection` | command injection через newline | medium | `http://127.0.0.1:5103` |
| `web-hard-upload-include` | цепочка upload + local include | hard-but-fair | `http://127.0.0.1:5104` |
| `web-bonus-xxe-docx` | XXE в `word/document.xml` | medium bonus | `http://127.0.0.1:5105` |

## Локальный запуск

Требуются Docker Engine и Docker Compose v2.

```bash
docker compose -f docker-compose.web.yml up --build
```

Остановить и удалить контейнеры:

```bash
docker compose -f docker-compose.web.yml down --remove-orphans
```

Проверить структуру и метаданные без Docker:

```bash
python3 scripts/validate_web_services.py
```

После запуска контейнеров проверить intended solution path всех задач:

```bash
python3 scripts/smoke_web.py
```

В pull request эти же шаги автоматически выполняет workflow `.github/workflows/validate.yml`, включая реальную сборку пяти Docker-образов.

## Состав задачи

В корне каждой задачи находятся:

- `challenge.yml` — метаданные для будущего переноса в CTFd;
- `challenge.md` — публичное условие;
- `solve.md` — решение преподавателя;
- `flag.txt` — эталонный флаг;
- `Dockerfile` — воспроизводимая сборка контейнера;
- `src/` — исходники сервиса.

## Безопасность

Уязвимости в этих приложениях намеренные. Compose публикует сервисы только на `127.0.0.1`, помещает каждую задачу в отдельную внутреннюю Docker-сеть, ограничивает CPU, память и процессы, использует read-only root filesystem и временные writable-каталоги. Не публикуйте локальную конфигурацию напрямую в интернет и не размещайте внутри контейнеров реальные данные.
