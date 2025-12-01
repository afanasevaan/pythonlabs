import re
from typing import Dict, List, Tuple
from pathlib import Path
from typing import Union


def normalize(text: str) -> str:
    if not text:
        return ""

    # Заменяем "ё" на "е"
    text = text.lower().replace("ё", "е")

    # Заменяем \n, \t, \r -> пробел
    text = re.sub(r"[\n\r\t]", " ", text)

    # Удаляем лишние пробелы
    text = re.sub(r"\s+", " ", text)

    # Убираем пробелы перед пунктуацией
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    # Убираем пробелы после пунктуации
    text = re.sub(r"([.,!?;:])\s+", r"\1 ", text)

    # Удаляем лишние пробелы в начале/конце
    return text.strip()


def tokenize(text: str) -> List[str]:
    """Разбивает текст на слова (токены)."""
    if not text:
        return []

    # Нормализуем текст
    normalized = normalize(text)
    if not normalized:
        return []

    # Удаляем пунктуацию для токенизации
    # Сохраняем только буквы, цифры и дефис внутри слов
    tokens = []
    for word in normalized.split():
        # Удаляем пунктуацию с начала и конца слова
        cleaned_word = re.sub(r"^[^a-zа-яё0-9]+|[^a-zа-яё0-9-]+$", "", word)

        # Если слово содержит дефис, разбиваем его
        if "-" in cleaned_word:
            parts = cleaned_word.split("-")
            # Добавляем только непустые части
            tokens.extend([part for part in parts if part])
        elif cleaned_word:  # Добавляем только если слово не пустое
            tokens.append(cleaned_word)

    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    """Подсчитывает частоту слов."""
    freq = {}
    for token in tokens:
        # Дополнительная очистка на всякий случай
        token_clean = token.lower().strip()
        if token_clean:
            freq[token_clean] = freq.get(token_clean, 0) + 1
    return freq


def top_n(freq: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """Возвращает n самых частых слов."""
    if not freq or n <= 0:
        return []

    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def ensure_parent_dir(path: Union[str, Path]):
    """Создает родительскую директорию для пути."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    test_text = "Привет, мир! Привет!!! Тест-тест проверка."
    print("Исходный текст:", test_text)

    norm_text = normalize(test_text)
    print("Нормализованный:", norm_text)

    tokens = tokenize(test_text)
    print("Токены:", tokens)

    freq = count_freq(tokens)
    print("Частоты:", freq)

    top_3 = top_n(freq, 3)
    print("Топ-3:", top_3)
