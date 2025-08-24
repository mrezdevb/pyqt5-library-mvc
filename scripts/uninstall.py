import os
from typing import Optional, Tuple

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection as Psycopgconnection
from psycopg2.extensions import cursor as Psycopgcursor

load_dotenv()


default_db: Optional[str] = "postgres"
db_name: Optional[str] = os.getenv("DB_NAME")
db_user: Optional[str] = os.getenv("DB_USER")
db_password: Optional[str] = os.getenv("DB_PASSWORD")
db_host: Optional[str] = os.getenv("DB_HOST", "localhost")


def drop_database() -> None:
    connection: Psycopgconnection = psycopg2.connect(
        dbname=default_db, user=db_user, password=db_password, host=db_host
    )
    connection.autocommit = True
    cursor: Psycopgcursor = connection.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,))
    exists: Optional[Tuple] = cursor.fetchone()

    if exists:
        print(f"Dropping database {db_name} ...")
        cursor.execute(
            """SELECT pg_terminate_backend(pid) FROM pg_stat_activity
              WHERE datname = %s AND pid <> pg_backend_pid();""",
            (db_name,),
        )
        cursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database {db_name} dropped.")

    else:
        print(f"Database {db_name} not found.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    drop_database()
