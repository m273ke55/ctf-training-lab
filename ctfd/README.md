# Перенос задач в CTFd

Для каждой задачи перенесите название, категорию, описание, баллы, флаг и подсказки. Для файловых задач добавьте публичные файлы из `dist/`; для Web-задач укажите URL развернутого сервиса. Файлы `solve.md` и `flag.txt` нельзя публиковать. `challenge.yml` используется как внутренняя карточка.

Финальный workflow перед загрузкой в CTFd:

```bash
bash scripts/build_all.sh
python3 scripts/package_dist.py
docker compose -f docker-compose.web.yml up --build -d
python3 scripts/smoke_web.py
```

После выполнения команд zip-архивы лежат в `build/packages/`, а пять Web-сервисов доступны на локальных портах 5101–5105. В боевой CTFd-конфигурации замените локальные адреса на адреса учебной инфраструктуры.

Перед импортом пройдите финальный чек-лист: [`final_import_checklist.md`](final_import_checklist.md).
