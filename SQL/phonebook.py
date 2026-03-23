import psycopg2
import csv
from config import load_config

def insert_from_csv(file_path):
    """Задача 1: Импорт из CSV"""
    sql = "INSERT INTO contacts(name, phone) VALUES(%s, %s) ON CONFLICT (phone) DO NOTHING;"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute(sql, row)
            print(f"✅ Данные из {file_path} загружены.")
    except Exception as e:
        print(f"❌ Ошибка импорта: {e}")

def add_contact(name, phone):
    """Задача 2: Ввод из консоли"""
    sql = "INSERT INTO contacts(name, phone) VALUES(%s, %s);"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
            print(f"✅ Контакт {name} добавлен.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def get_contacts(filter_type=None, value=None):
    """Задача 3: Поиск (Фильтрация)"""
    config = load_config()
    # Базовый запрос
    sql = "SELECT * FROM contacts"
    
    # Добавляем фильтр, если он передан
    if filter_type == 'name':
        sql += " WHERE name ILIKE %s" # ILIKE — поиск без учета регистра
        value = f"%{value}%" # Поиск по части имени
    elif filter_type == 'phone':
        sql += " WHERE phone LIKE %s"
        value = f"{value}%" # Поиск по префиксу

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (value,) if value else None)
                rows = cur.fetchall()
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
    except Exception as e:
        print(f"❌ Ошибка поиска: {e}")

def update_contact(contact_id, new_name=None, new_phone=None):
    """Задача 4: Обновление данных"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if new_name:
                    cur.execute("UPDATE contacts SET name=%s WHERE user_id=%s", (new_name, contact_id))
                if new_phone:
                    cur.execute("UPDATE contacts SET phone=%s WHERE user_id=%s", (new_phone, contact_id))
            print(f"✅ Контакт ID {contact_id} обновлен.")
    except Exception as e:
        print(f"❌ Ошибка обновления: {e}")

def delete_contact(identifier, by_name=False):
    """Задача 5: Удаление"""
    config = load_config()
    column = "name" if by_name else "phone"
    sql = f"DELETE FROM contacts WHERE {column} = %s"
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (identifier,))
            print(f"✅ Контакт {identifier} удален.")
    except Exception as e:
        print(f"❌ Ошибка удаления: {e}")

# Пример запуска для проверки:
if __name__ == '__main__':
    # 1. Загрузим из CSV
    insert_from_csv('contacts.csv')
    
    # 2. Посмотрим всех
    print("\n--- Список контактов ---")
    get_contacts()