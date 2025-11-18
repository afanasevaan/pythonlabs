import argparse
import sys
from pathlib import Path

# Добавляем путь для импорта модулей из других лабораторных
sys.path.append(str(Path(__file__).parent.parent))

try:
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Убедитесь, что модули lab05 существуют и содержат необходимые функции")
    sys.exit(1)


def json2csv_command(args):
    """Конвертация JSON → CSV"""
    try:
        json_to_csv(args.input, args.output)
        print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
    except Exception as e:
        print(f"❌ Ошибка конвертации JSON → CSV: {e}")
        sys.exit(1)


def csv2json_command(args):
    """Конвертация CSV → JSON"""
    try:
        csv_to_json(args.input, args.output)
        print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
    except Exception as e:
        print(f"❌ Ошибка конвертации CSV → JSON: {e}")
        sys.exit(1)


def csv2xlsx_command(args):
    """Конвертация CSV → XLSX"""
    try:
        csv_to_xlsx(args.input, args.output)
        print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
    except Exception as e:
        print(f"❌ Ошибка конвертации CSV → XLSX: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилита для конвертации данных между форматами",
        epilog="Примеры использования:\n"
               "  python cli_convert.py json2csv --in input.json --out output.csv\n"
               "  python cli_convert.py csv2json --in input.csv --out output.json\n"
               "  python cli_convert.py csv2xlsx --in input.csv --out output.xlsx"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    
    # Парсер для json2csv
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертация JSON → CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, 
                               help="Входной JSON файл")
    json2csv_parser.add_argument("--out", dest="output", required=True,
                               help="Выходной CSV файл")
    json2csv_parser.set_defaults(func=json2csv_command)
    
    # Парсер для csv2json
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертация CSV → JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True,
                               help="Входной CSV файл")
    csv2json_parser.add_argument("--out", dest="output", required=True,
                               help="Выходной JSON файл")
    csv2json_parser.set_defaults(func=csv2json_command)
    
    # Парсер для csv2xlsx
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертация CSV → XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True,
                               help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True,
                               help="Выходной XLSX файл")
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == "__main__":
    main()