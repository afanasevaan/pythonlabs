import string
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