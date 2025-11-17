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