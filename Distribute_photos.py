import os
import shutil
import re

def distribute_photos(source_dir, base_dir):
    """
    Распределяет фото вида first_second_n.jpg по папкам:
    base_dir/first/second/
    
    :param source_dir: Папка, где лежат все фото
    :param base_dir: Корневая папка дерева директорий
    """
    # Регулярное выражение для извлечения first, second, n из имени файла
    pattern = re.compile(r"^(.+)_(.+)_([1-4])\.jpg$")

    for filename in os.listdir(source_dir):
        match = pattern.match(filename)
        if not match:
            print(f"Пропущен файл (не соответствует шаблону): {filename}")
            continue

        first_level = match.group(1)
        second_level = match.group(2)
        # n = match.group(3)  # можно использовать, если нужно проверять диапазон

        target_dir = os.path.join(base_dir, first_level, second_level)
        os.makedirs(target_dir, exist_ok=True)  # создаст, если ещё не существует

        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, filename)

        shutil.copy(src_path, dst_path)
        print(f"Перемещено: {filename} → {target_dir}")

# Пример использования
if __name__ == "__main__":
    source_directory = r"C:\Users\Shapaev\Downloads"      # где лежат все ваши .jpg
    base_directory = r"C:\Users\Shapaev\Capybara_passport\portraits"         # корень дерева папок

    distribute_photos(source_directory, base_directory)