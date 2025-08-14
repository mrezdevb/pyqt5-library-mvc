import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()
defualt_db = 'postgres'
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST', 'localhost')




def drop_database():
	connection = psycopg2.connect(dbname=defualt_db, user=db_user, password=db_password, host=db_host)
	connection.autocommit = True
	cursor = connection.cursor()

	cursor.execute('SELECT 1 FROM pg_database WHERE datname=%s', (db_name,))
	exists = cursor.fetchone()
	
	
	if exists:
		print(f'Dropping database {db_name} ...')
		cursor.execute(f'SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s AND pid <> pg_backend_pid();', (db_name,))
		cursor.execute(f'DROP DATABASE {db_name}')
		print(f'Database {db_name} dropped.')
	else:
		print(f'Database {db_name} not found.')

	cursor.close()
	connection.close()

if __name__ == '__main__':
	drop_database()
