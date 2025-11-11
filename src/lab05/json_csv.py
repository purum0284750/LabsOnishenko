import json
import csv
import os
from typing import List, Dict, Any


def validate_json_file(json_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    if os.path.getsize(json_path) == 0:
        raise ValueError(f"JSON файл пустой: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    if not isinstance(data, list):
        raise ValueError(f"JSON должен содержать список на верхнем уровне. Получен: {type(data)}")

    if len(data) == 0:
        raise ValueError(f"JSON файл содержит пустой список: {json_path}")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    return data


def validate_csv_file(csv_path: str) -> List[str]:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    if os.path.getsize(csv_path) == 0:
        raise ValueError(f"CSV файл пустой: {csv_path}")

    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader, None)

        if headers is None:
            raise ValueError(f"CSV файл не содержит заголовков: {csv_path}")

        if not headers:
            raise ValueError(f"CSV файл содержит пустые заголовки: {csv_path}")

    return headers


def json_to_csv(json_path: str, csv_path: str) -> None:
    data = validate_json_file(json_path)
    output_dir = os.path.dirname(csv_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    fieldnames = sorted(all_keys)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for item in data:
            row = {key: str(item.get(key, '')) for key in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    validate_csv_file(csv_path)

    output_dir = os.path.dirname(json_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    data = []

    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(dict(row))

    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    samples_path = 'data/samples'
    out_path = 'data/out'

    test_cases = [
        (json_to_csv, f'{samples_path}/people.json', f'{out_path}/people_from_json.csv', "Нормальный JSON → CSV"),
        (csv_to_json, f'{samples_path}/people.csv', f'{out_path}/people_from_csv.json', "Нормальный CSV → JSON"),
    ]

    os.makedirs(out_path, exist_ok=True)

    for func, input_file, output_file, description in test_cases:

        try:
            func(input_file, output_file)
        except FileNotFoundError:
            print("FileNotFoundError")
        except ValueError:
            print("ValueError")

    try:
        print("JSON -> CSV")
        json_to_csv(f'{samples_path}/people.json', f'{out_path}/people_from_json.csv')

        print("CSV -> JSON")
        csv_to_json(f'{samples_path}/people.csv', f'{out_path}/people_from_csv.json')

    except FileNotFoundError:
        print("FileNotFoundError")
    except ValueError:
        print("ValueError")
    finally:
        print("Успешно")