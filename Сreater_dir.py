import os

def create_directory_tree(base_dir, first_level_dirs, second_level_dirs):
    """
    Создаёт дерево директорий:
    base_dir/
        ├── dir1/
        │   ├── sub1/
        │   ├── sub2/
        │   └── ...
        ├── dir2/
        │   ├── sub1/
        │   ├── sub2/
        │   └── ...
        └── ...

    :param base_dir: Корневая директория (строка)
    :param first_level_dirs: Список имён папок 1-го уровня
    :param second_level_dirs: Список имён папок 2-го уровня (общий для всех)
    """
    for first in first_level_dirs:
        first_path = os.path.join(base_dir, first)
        for second in second_level_dirs:
            full_path = os.path.join(first_path, second)
            os.makedirs(full_path, exist_ok=True)
            print(f"Создана директория: {full_path}")

# Пример использования:
if __name__ == "__main__":
    # Укажите здесь свои данные
    base_directory = r"C:\Users\Shapaev\Capybara_passport\portraits"
    first_level = ["capybara", "mushroom", "bird", "slipper", "neutral", "smile", "pug", "berserker"]
    second_level = ["president", "pm", "general", "diplomat", "citizen", "prisoner"]

    create_directory_tree(base_directory, first_level, second_level)
    