import os
import json
from pathlib import Path

# Конфигурация
PORTRAITS_DIR = "portraits"
OUTPUT_JSON = "portraits/portraits.json"

# Маппинг папок на русские названия для фронтенда
FOLDER_TO_RUSSIAN = {
    "capybara": "Капибары",
    "mushroom": "Грибовики",
    "bird": "Скебобы",
    "slipper": "Тапки",
    "neutral": "Нейтралы",
    "smile": "Смайлы",
    "pug": "Мопсы",
    "berserker": "Берсерки"
}

RANK_TO_RUSSIAN = {
    "president": "Президент",
    "pm": "Премьер-министр",
    "general": "Генерал",
    "diplomat": "Дипломат",
    "citizen": "Гражданин",
    "prisoner": "Заключенный"
}

def scan_portraits():
    """Сканирует папку portraits и создает структуру JSON"""
    portraits_data = {}
    total_files = 0
    
    # Проверяем существование папки
    if not os.path.exists(PORTRAITS_DIR):
        print(f"Создаю папку: {PORTRAITS_DIR}")
        os.makedirs(PORTRAITS_DIR, exist_ok=True)
    
    # Проходим по всем папкам первого уровня
    for first_level in os.listdir(PORTRAITS_DIR):
        first_level_path = os.path.join(PORTRAITS_DIR, first_level)
        
        # Пропускаем файлы, только папки
        if not os.path.isdir(first_level_path):
            continue
        
        # Получаем русское название религии
        religion_russian = FOLDER_TO_RUSSIAN.get(first_level, first_level)
        
        if religion_russian not in portraits_data:
            portraits_data[religion_russian] = {}
        
        # Проходим по папкам второго уровня
        for second_level in os.listdir(first_level_path):
            second_level_path = os.path.join(first_level_path, second_level)
            
            if not os.path.isdir(second_level_path):
                continue
            
            # Получаем русское название ранга
            rank_russian = RANK_TO_RUSSIAN.get(second_level, second_level)
            
            # Сканируем файлы в папке
            portraits_list = []
            
            # Проверяем файлы по шаблону first_level_second_level_n.jpg
            for n in range(1, 5):  # Проверяем номера 1-4
                filename = f"{first_level}_{second_level}_{n}.jpg"
                filepath = os.path.join(second_level_path, filename)
                
                if os.path.exists(filepath):
                    portraits_list.append({
                        "filename": filename,
                        "url": f"./portraits/{first_level}/{second_level}/{filename}",
                        "number": n
                    })
                    total_files += 1
            
            # Также проверяем другие возможные расширения
            for ext in [".jpeg", ".png", ".gif", ".webp"]:
                for n in range(1, 5):
                    filename = f"{first_level}_{second_level}_{n}{ext}"
                    filepath = os.path.join(second_level_path, filename)
                    
                    if os.path.exists(filepath):
                        portraits_list.append({
                            "filename": filename,
                            "url": f"./portraits/{first_level}/{second_level}/{filename}",
                            "number": n
                        })
                        total_files += 1
            
            # Сортируем по номеру
            portraits_list.sort(key=lambda x: x["number"])
            
            # Добавляем в структуру данных
            portraits_data[religion_russian][rank_russian] = portraits_list
    
    return portraits_data, total_files

def save_portraits_json(data, output_file):
    """Сохраняет данные в JSON файл"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"JSON файл сохранен: {output_file}")

    
def main():
    print("=" * 50)
    print("Генератор каталога портретов для В.И.В.К.")
    print("=" * 50)
    
    # Сканируем существующие портреты
    portraits_data, total_files = scan_portraits()
    
    print(f"✅ Найдено портретов: {total_files}")
    
    # Сохраняем JSON
    save_portraits_json(portraits_data, OUTPUT_JSON)
    
    # Выводим статистику
    print("\n📊 Статистика:")
    print("-" * 30)
    
    for religion, ranks in portraits_data.items():
        print(f"{religion}:")
        for rank, portraits in ranks.items():
            count = len(portraits)
            print(f"  ├─ {rank}: {count} портретов")
    
    print("\n📁 Структура файлов готова!")
    print("Для добавления новых портретов:")
    print("1. Поместите файлы в portraits/[религия]/[ранг]/")
    print("2. Назовите файлы по шаблону: religion_rank_n.jpg")
    print("3. Запустите этот скрипт снова")
    print(f"\nФайл каталога: {OUTPUT_JSON}")

if __name__ == "__main__":
    main()