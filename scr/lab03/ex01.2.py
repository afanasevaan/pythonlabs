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
