# Лабораторная работа №6
## Модуль cli_text.py - работа с текстом
**Команда: cat**

**Описание:** Вывод содержимого файла с опциональной нумерацией

```bash
python src/lab06/cli_text.py cat --input src/data/samples/test.txt -n
```

**Вывод консоли**
![cat.png](/images/lab06/cat.png)

**Команда: stats**

**Описание:** Анализ частот слов в текстовом файле

```bash
python src/lab06/cli_text.py stats --input src/data/samples/test.txt -n
```

**Вывод консоли**
![stats.png](/images/lab06/stats.png)

**Команда: --help**

**Описание:** Помошник по работе с командой

```bash
python src/lab06/cli_text.py --help --input src/data/samples/test.txt -n
```
**Вывод консоли**
![help.png](/images/lab06/help.png)

## Модуль cli_convert.py - работа с текстом

**Команда: json2csv**

**Описание:** Конвертирует JSON файл в CSV формат

```bash
cd /Users/anastasiaafanaseva/Desktop/pythonLabs
python src/lab06/cli_convert.py json2csv --in src/data/samples/people.json --out src/data/out/people.csv
```

**Вывод консоли**
![j2c.png](/images/lab06/j2c.png)

**Выходной Файл**

![out_j2c](/images/lab06/out_j2c.png)

**Команда: csv2json**

**Описание:** Конвертирует CSV файл в JSON формат

```bash
cd /Users/anastasiaafanaseva/Desktop/pythonLabs
python src/lab06/cli_convert.py csv2json --in src/data/samples/people.csv --out src/data/out/people.json
```

**Вывод консоли**
![c2j.png](/images/lab06/c2j.png)

**Выходной Файл**
![2.png](images/lab06/2.png)

**Команда: csv2xlsx**

**Описание:** Конвертирует CSV файл в XLSX формат (Excel)

```bash
cd /Users/anastasiaafanaseva/Desktop/pythonLabs
python src/lab06/cli_convert.py csv2xlsx --in src/data/samples/people.csv --out src/data/out/people.xlsx
```

**Вывод консоли**
![1.3.png](/images/lab06/1.3.png)


**Выходной Файл**
![3.png][/images/lab06/3.png]

**Вывод:** В ходе работы созданы два CLI-модуля: для анализа текста и конвертации файлов.

Текстовая утилита выводит содержимое файлов и показывает статистику слов.

Конвертер преобразует данные между форматами JSON, CSV и XLSX.

Оба инструмента работают из командной строки с различными параметрами.