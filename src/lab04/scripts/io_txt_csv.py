from pathlib import Path
import csv


def read_text(path, encoding="utf-8"):
    path = Path(path)

    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_csv(
    rows,
    path,
    header=None,
):
    path = Path(path)

    if rows:
        first_length = len(rows[0])
        for row in rows:
            if len(row) != first_length:
                raise ValueError(
                    f"Строка имеет длину {len(row)}, ожидалось {first_length}"
                )

    if header and rows:
        if len(header) != len(rows[0]):
            raise ValueError(
                f"Заголовок имеет длину {len(header)}, а строки - {len(rows[0])}"
            )

    ensure_parent_dir(path)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header:
            writer.writerow(header)

        writer.writerows(rows)


def ensure_parent_dir(path):
    path = Path(path)
    parent_dir = path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)


try:
    content = read_text("src/lab04/data/input.txt", encoding="utf-8")
    print(content)
except FileNotFoundError:
    print("FileNotFoundError: Файл не найден")
except UnicodeDecodeError:
    print("UnicodeDecodeError: Ошибка кодировки")

write_csv([("test", 3)], "src/lab04/output/check.csv", header=("word", "count"))

print("=== ПРОВЕРКА ПУТЕЙ ===")
print(f"Текущая директория: {Path.cwd()}")

input_path = Path("src/lab04/data/input.txt")
print(f"Путь к input.txt: {input_path}")
print(f"Файл существует: {input_path.exists()}")

# Проверяем чтение
try:
    content = read_text("src/lab04/data/input.txt", encoding="utf-8")
    print("Файл найден! Содержимое:")
    print(content)
except FileNotFoundError:
    print("FileNotFoundError: Файл не найден")

    # Создаем тестовый файл
    print("Создаю тестовый файл...")
    ensure_parent_dir(input_path)
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("Привет, мир, привет !!!\n")
    print(f"Файл создан: {input_path}")

