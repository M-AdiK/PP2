import psycopg2
from config import load_config

def create_tables():
    """ Создаем таблицу contacts в базе данных """
    # SQL-запрос для создания таблицы
    command = """
    CREATE TABLE IF NOT EXISTS contacts (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    )
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Выполняем SQL-команду
                cur.execute(command)
            # Фиксируем изменения (commit происходит автоматически при выходе из with conn)
            print("✅ Таблица 'contacts' успешно создана или уже существует.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"❌ Ошибка при создании таблицы: {error}")

if __name__ == '__main__':
    create_tables()