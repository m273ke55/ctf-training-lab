# Финальный чек-лист импорта в CTFd

Этот файл предназначен для преподавателя и коллеги, который переносит учебные задачи из репозитория в CTFd. Он фиксирует финальный порядок сборки, упаковки и ручной проверки перед занятием.

## Перед импортом задач

1. Убедитесь, что рабочая копия репозитория чистая или содержит только ожидаемые изменения документации.
2. Соберите публичные артефакты задач:

   ```bash
   bash scripts/build_all.sh
   ```

3. Упакуйте задачи для передачи в CTFd:

   ```bash
   python3 scripts/package_dist.py
   ```

4. Проверьте, что zip-архивы появились в каталоге `build/packages/`.

## Что переносить в CTFd

Для каждой задачи используйте данные из соответствующего `challenge.yml`:

- `name` — название задачи;
- `category` — категория;
- `difficulty` и `tags` — сложность и теги;
- `points` — баллы;
- `description` — описание;
- `flags` — флаг;
- `hints` — подсказки и их стоимость;
- `files` — публичные файлы из `dist/`.

В CTFd загружайте zip-архив конкретной задачи из `build/packages/` или публичные файлы, перечисленные в `files`.

## Что не загружать в CTFd

Не загружайте как публичные файлы:

- `solve.md`;
- `flag.txt`;
- `src/`;
- `.gitkeep`;
- `build/` целиком.

## Проверка флага

- Откройте `flag.txt` в каталоге задачи и убедитесь, что там ровно один флаг формата `edu_ctf{...}`.
- Сравните флаг с разделом `flags` в `challenge.yml`.
- При необходимости запустите `python3 src/solve.py` из корня репозитория или используйте общий прогон solver-скриптов.

## Проверка подсказок

- Перенесите все элементы из `hints` в `challenge.yml`.
- Проверьте, что стоимость подсказок в CTFd совпадает с `cost`.
- Убедитесь, что подсказки не раскрывают флаг напрямую.

## Проверка баллов и категорий

- Intro-задачи: `difficulty: intro`, `points: 0`.
- Final easy: `difficulty: easy`, `points: 100`.
- Final medium: `difficulty: medium`, `points: 200`.
- Final hard-but-fair: `difficulty: hard-but-fair`, `points: 300`.
- Допустимые категории: `Reverse`, `Forensics`, `Cryptography`, `Steganography`.

## Чек-лист intro-задач

- [ ] `reverse-demo`
- [ ] `reverse-mini`
- [ ] `forensics-demo`
- [ ] `forensics-mini`
- [ ] `cryptography-demo`
- [ ] `cryptography-mini`
- [ ] `steganography-demo`
- [ ] `steganography-mini`
- [ ] `reverse-extra-mini`
- [ ] `forensics-extra-mini`
- [ ] `cryptography-extra-mini`
- [ ] `steganography-extra-mini`

Для каждой intro-задачи проверьте название, категорию, нулевые баллы, флаг, подсказки и публичный файл из `dist/`.

## Чек-лист final-задач

- [ ] `rev-easy-strings-attached`
- [ ] `rev-medium-check-me`
- [ ] `rev-hard-pyc-lockbox`
- [ ] `forensics-easy-file-signature`
- [ ] `forensics-medium-hidden-archive`
- [ ] `forensics-hard-traffic-note`
- [ ] `crypto-easy-caesar-shift`
- [ ] `crypto-medium-repeating-xor`
- [ ] `crypto-hard-tiny-rsa`
- [ ] `stego-easy-exif-note`
- [ ] `stego-medium-lsb-image`
- [ ] `stego-hard-audio-spectrogram`
- [ ] `rev-bonus-js-checker`
- [ ] `forensics-bonus-log-timeline`
- [ ] `crypto-bonus-vigenere-keyword`
- [ ] `stego-bonus-audio-lsb`

Для каждой final-задачи проверьте сложность, баллы, флаг, подсказки и публичные файлы из `dist/`.

## Финальная проверка перед занятием

Перед открытием задач студентам выполните:

```bash
bash scripts/build_all.sh
python3 scripts/verify_flags.py
python3 scripts/package_dist.py
find build/packages -maxdepth 1 -type f -name '*.zip' | sort
```

Ожидаемый результат — 28 zip-архивов: 12 intro-задач и 16 final-задач. После загрузки в CTFd откройте каждую задачу в режиме предпросмотра, скачайте публичные файлы и убедитесь, что флаг принимается только в формате `edu_ctf{...}`.
