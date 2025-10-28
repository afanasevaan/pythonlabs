# pythonlabs

## Лабораторная работа 1

### Задание 1

```
name = input('Имя:' )
age = int(input('Возраст:'))
next_age = age + 1
print(F"Привет, {name}! Через год тебе будет {next_age}")
```

![im01.png](/images/lab01/im01.png)

### Задание 2

```
n1 = input("a:")
n2 = input("b:")
if ',' in n1:
    n1 = n1.replace(',','.')
if ',' in n2:
    n2 = n2.replace(',','.')
n1 = float(n1)
n2 = float(n2)
sumc= n1 + n2
avg = sumc/2
print(F'sum = {'%.2f'%sumc}; avg = {'%.2f'%avg}')
```
![im02.png](/images/lab01/im02.png)

### Задание 3

```
p = float(input())
d = float(input())
v = float(input())
base = p * (1 - d/100)
v_amount = base * (v/100)
total = base + v_amount
print(F'База после скидки:{'%.2f'%base}')
print(F'НДС:{'%.2f'%v_amount}')
print(F'Итого к оплате:{'%.2f'%total}')
```

![im03.png](/images/lab01/im03.png)

### Задание 4

```
m = int(input('Минуты:'))
hour = m // 60
minutes = m % 60
print(F'{hour}:{minutes:02d}')
```

![im04.png](/images/lab01/im04.png)

### Задание 5

```
fn= input('ФИО:').split()
init = [i[0] for i in fn]
print(F'Инициалы: {''.join(init)}.')
print(F'Длина (символов): {len(''.join(fn))+2}')
```

![im06.png](/images/lab01/im06.png)


## Лабораторная работа 2

### Задание A1

```
def min_max(nums: list[float | int]):
    if not nums:
        raise TypeError ('Value Error')
    else:
        return min(nums), max(nums)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))


```

![im01.1.png](/images/lab02/im01.1.png)


### Задание A2

```
def unique_sorted(nums: list[float | int]):
    return (list(sorted(set(nums))))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print(unique_sorted([]))
```

![im01.2.png](/images/lab02/im01.2.png)

### Задание A3

```
def flatten(mat: list[list | tuple]):
    flattened_list =  []
    for row in mat:
        if isinstance(row, (list, tuple)):
            flattened_list.extend(row)
        else:
            raise TypeError ('TypeError')
    return (flattened_list)
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```

![im01.3.png](/images/lab02/im01.3.png)

### Задание B1

```
def transpose(mat: list[list[float | int]]):
    if len(mat)==0:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i) != len_s:
            raise TypeError ("ValueError")
    R = []
    for i in range(len(mat[0])):
        N = []
        for j in range(len(mat)):
             N.append(mat[j][i])
        R.append(N)
    return R
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1, 2], [3]]))
print(transpose([]))
```

![im02.1.png](/images/lab02/im02.1.png)

### Задание B2

```
def row_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i)!=len_s:
            raise TypeError ("ValueError")
    R = []
    for i in mat:
        R.append(sum(i))
    return R
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```

![im02.2.png](/images/lab02/im02.2.png)

### Задание B3

```
def col_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i)!= len_s:
            raise TypeError ("ValueError")
    R = []
    for i in range (len(mat[0])):
        sum_s = 0
        for j in range(len(mat)):
            sum_s += mat[j][i]
        R.append(sum_s)
    return R
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```

![im02.3.png](/images/lab02/im02.3.png)

## Лабораторная работа 3

### Задание A1

```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    s = text
    if casefold:
        s = s.casefold()
    if yo2e:
        s = s.replace('ё', 'е').replace('Ё', 'Е')
    s = s.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s
example_normalize1 = "ПрИвЕт\nМИр\t"
example_normalize2 = "ёжик, Ёлка"
example_normalize3 = "Hello\r\nWorld"
example_normalize4 = "  двойные   пробелы  "
res_normalise1 = normalize(example_normalize1)
res_normalise2 = normalize(example_normalize2)
res_normalise3 = normalize(example_normalize3)
res_normalise4 = normalize(example_normalize4)
print(res_normalise1, res_normalise2, res_normalise3, res_normalise4, sep='\n') 
```
![im01.1.png](/images/lab03/im01.1.png)

### Задание A2
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    s = text
    if casefold:
        s = s.casefold()
    if yo2e:
        s = s.replace('ё', 'е').replace('Ё', 'Е')
    s = s.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

import re # Библиотека регулярных выражений

def tokenize(text: str):
    # Регулярное выражение для захвата "слов", состоящих из букв, цифр, подчёркивания и дефисов внутри слова
    tokens = re.findall(r'\w+(?:-\w+)*', text) 
    return tokens

example_tokenize1 = "emoji 😀 не слово"
example_tokenize2 = "2025 год"
example_tokenize3 = "по-настоящему круто"
example_tokenize4 = "hello,world!!!"

res_tokenize1 = tokenize(example_tokenize1)
res_tokenize2 = tokenize(example_tokenize2)
res_tokenize3 = tokenize(example_tokenize3)
res_tokenize4 = tokenize(example_tokenize4)

print(res_tokenize1)
print(res_tokenize2)
print(res_tokenize3)
print(res_tokenize4)
```
![im01.2.png](/images/lab03/im01.2.png)

### Задание A3
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:n]

example_count_freq = ["bb","aa","bb","aa","cc"]
res_count_freq = count_freq(example_count_freq)
res_count_top_n = top_n(res_count_freq)
print(res_count_freq)
print(res_count_top_n)
```
![im01.3.png](/images/lab03/im01.3.png)

## Задание B
```
import sys
import os

# Добавляем путь к корневой папке проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def main():
    print("Введите текст (для завершения нажмите Ctrl+D на новой строке):")
    
    # Читаем весь ввод из stdin
    text = sys.stdin.read()
    
    if not text.strip():
        print("Вы не ввели текст!")
        return
    
    # Нормализуем текст
    normalized_text = normalize(text, casefold=True, yo2e=True)
    
    # Токенизируем
    tokens = tokenize(normalized_text)
    
    # Подсчитываем статистику
    total_words = len(tokens)
    unique_words = len(set(tokens))
    
    # Частоты и топ-5
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    # Вывод результатов
    print("\nРезультат:")
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
![im02.1.png](/images/lab03/im02.1.png) 


## Лабароторная 4

### задание A

```
from csv import writer
from pathlib import Path

def read_text(path: str, encoding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encoding)

def write_csv(rows: list, path: str, header: tuple = None) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = writer(f)
        if header:
            w.writerow(header)
        w.writerows(rows)
```
### Задание B
```
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

def validate_output_file(filename):
    path = Path(filename)
    if path.suffix.lower() != '.csv':
        raise ValueError()

def main():
    input_file = "scr/data/lab04/input.txt"  
    output_file = "scr/data/lab04/report.csv"  
    
    try:
        text = read_text(input_file)
        freq = count_freq(tokenize(normalize(text)))
        write_csv(sorted(freq.items(), key=lambda x: (-x[1], x[0])), 
                 output_file, header=("word", "count"))
        
        print(f"✓ Отчёт сохранён: {output_file}")
        print(f"Всего слов: {sum(freq.values())}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:", *[f"{w}:{c}" for w, c in top_n(freq, 5)])
        
    except FileNotFoundError:
        print(f"✗ Файл {input_file} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

![im01.png](/images/lab04/im01.png) 

# Лабораторная работа №5
## Задание А:
### Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный.

```
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path(json_path)
    csv_file = Path(csv_path)
    
    if not json_file.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")
    
    if json_file.suffix.lower() != '.json':
        raise ValueError("Неверный тип файла. Ожидается .json")
    
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка чтения JSON: {e}")
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    if data:
        first_item_keys = list(data[0].keys())
        remaining_keys = sorted(all_keys - set(first_item_keys))
        fieldnames = first_item_keys + remaining_keys
    else:
        fieldnames = sorted(all_keys)
    # Запись в CSV
    try:
        with csv_file.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                complete_row = {key: row.get(key, '') for key in fieldnames}
                writer.writerow(complete_row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")

def csv_to_json(csv_path: str, json_path: str) -> None:
  
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла. Ожидается .csv")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")
            
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    if not data:
        raise ValueError("Пустой CSV файл")

    try:
        with json_file.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")

json_to_csv("src/data/samples/people.json", "src/data/out/people_from_json.csv")
csv_to_json("src/data/samples/people.csv", "src/data/out/people_from_csv.json")
```
### Входные данные:
![im03.png](/images/lab05/im03.png)
## 
![im02.png](/images/lab05/im02.png)
##
### Выходные данные:
![im01.1.png](/images/lab05/im01.1.png)
##
![im01.2.png](/images/lab05/im01.2.png)
#
## Задание В:
### Установка зависимостей:
#### Через `requirements.txt`:
```
pip install -r requirements.txt
```
#### Напрямую
```
pip install openpyxl
```
```
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла. Ожидается .csv")
    
    # Чтение CSV
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    if not rows[0]:
        raise ValueError("CSV файл не содержит заголовка")
    
    # Создание XLSX
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        
        for row in rows:
            ws.append(row)
        
        
        for col_idx, column_cells in enumerate(ws.columns, 1):
            max_length = 8  
            column_letter = get_column_letter(col_idx)
            
            for cell in column_cells:
                try:
                    if cell.value:

                        cell_length = len(str(cell.value))
                        if cell_length > max_length:
                            max_length = cell_length
                except:
                    pass
            
            adjusted_width = max_length + 2
            ws.column_dimensions[column_letter].width = adjusted_width
        
        wb.save(xlsx_file)
        
    except Exception as e:
        raise ValueError(f"Ошибка создания XLSX: {e}")
    
csv_to_xlsx("src/data/samples/people.csv", "src/data/out/people.xlsx")
```
### Входные данные:
![im02.png](/images/lab05/im02.png)
### Выходные данные:
![im01.3.png](/images/lab05/im01.3.png)
## Вывод:
``` 
В ходе лабораторной работы разработан программный комплекс, предназначенный для автоматизированного сбора текстовой статистики. Система объединяет ранее созданные модули, позволяя выполнять чтение файлов, подсчёт частоты слов и сохранение результатов в формате CSV. Проект имеет модульную архитектуру, что облегчает повторное использование кода. Все элементы программы функционируют в полном соответствии с требованиями технического задания.
```