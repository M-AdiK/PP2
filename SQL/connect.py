import psycopg2
from config import load_config

def connect():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            print("✅ Успех! Мы подключились к базе данных в Docker.")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(f" Ошибка подключения: {error}")

if __name__ == '__main__':
    connect()