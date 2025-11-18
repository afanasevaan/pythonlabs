import argparse
import sys
from pathlib import Path

# Добавляем путь для импорта модулей
sys.path.append(str(Path(__file__).parent.parent))

def cat_command(args):
    """Вывод содержимого файла"""
    print(f"Пытаемся открыть файл: {args.input}")
    sys.stdout.flush()  
    
    file_path = Path(args.input)
    print(f"Полный путь: {file_path.absolute()}")
    sys.stdout.flush()  
    
    if not file_path.exists():
        print(f"❌ Файл не существует: {file_path.absolute()}")
        sys.stdout.flush()
        sys.exit(1)
    
    print(f"✅ Файл найден! Содержимое:")
    print("-" * 40)
    sys.stdout.flush() 
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.rstrip()
            if args.n:
                print(f"{i:>2}. {line}")
            else:
                print(line)
            sys.stdout.flush()

def stats_command(args):
    """Анализ частотности слов"""
    file_path = Path(args.input)
    
    if not file_path.exists():
        print(f"Ошибка: файл '{args.input}' не найден")
        sys.exit(1)
    
    text = file_path.read_text(encoding='utf-8')
    
    if not text.strip():
        print("Файл пуст")
        return
    
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Очистка слова от знаков препинания
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1
    
    # Сортировка по частоте
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:args.top]
    
    # Вывод результатов
    print(f"Топ-{args.top} слов в файле '{args.input}':")
    print("-" * 40)
    for word, count in top_words:
        print(f"{word:<15} {count:>3}")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилита для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Команда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    cat_parser.set_defaults(func=cat_command)

    # Команда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5, 
                            help="Количество топ-слов для вывода (по умолчанию: 5)")
    stats_parser.set_defaults(func=stats_command)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":  
    main()