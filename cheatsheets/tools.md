# Шпаргалка по инструментам

| Команда | Назначение | Пример | Категории |
|---|---|---|---|
| `file` | Определить тип файла | `file sample.bin` | Все |
| `strings` | Найти читаемые строки | `strings app | grep edu_ctf` | Reverse, Forensics, Stego |
| `xxd` | Посмотреть hex | `xxd -l 64 file` | Forensics, Crypto |
| `grep` | Фильтр текста | `grep -n "flag" notes.txt` | Все |
| `unzip` | Распаковка ZIP | `unzip archive.zip` | Forensics |
| `binwalk` | Поиск вложений | `binwalk image.png` | Forensics, Stego |
| `exiftool` | Метаданные | `exiftool photo.jpg` | Stego, Forensics |
| `tshark` | PCAP в CLI | `tshark -r traffic.pcap` | Forensics |
| `python3` | Solver-скрипты | `python3 solve.py` | Crypto, Reverse |
| `objdump` | Дизассемблирование | `objdump -d app` | Reverse |
| `curl` | HTTP-запросы и заголовки | `curl -i http://target/` | Web |
| Browser DevTools | Просмотр Network/Storage/HTML | открыть вкладку Network | Web |
