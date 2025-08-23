from pathlib import Path




env_content: str = """ DB_NAME=library_db
DB_USER=postgres
DB_PASSWORD=secret123
DB_HOST=localhost
MAX_BORROW_LIMIT=3
"""



def create_env() -> None:

	env_path: Path = Path(".env")


	if env_path.exists():
		print(" .env file already exists. No changes made.")

	else:
		with open(env_path, "w") as f:
			f.write(env_content)

		print(" .env file created with default values.")




if __name__ == "__main__":
	create_env()
