import psycopg2
from dotenv import load_dotenv
import os
from library_app.init_db import init_db

def main():
    load_dotenv()

    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')

    if not all([db_name, db_user, db_password]):
        print('Missing database config. Please enter manually:')
        db_name = input('DB Name: ')
        db_user = input('DB User: ')
        db_password = input('DB Password: ')

    def create_database():
        connection = psycopg2.connect(dbname='postgres', user=db_user, password=db_password, host=db_host)
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,))
        exists = cursor.fetchone()

        if exists:
            print(f'Database "{db_name}" already exists. Dropping it...')
            cursor.execute('''
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = %s AND pid <> pg_backend_pid();
            ''', (db_name,))
            cursor.execute(f'DROP DATABASE {db_name}')
            print(f'Database "{db_name}" dropped.')

        cursor.execute(f'CREATE DATABASE {db_name}')
        print(f'Database "{db_name}" created.')

        cursor.close()
        connection.close()

    create_database()
    init_db()
    print("✅ Database created and initialized.")
