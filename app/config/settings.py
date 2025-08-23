from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	db_user: str
	db_password: str
	db_name: str
	db_host: str = 'localhost'
	log_level: str = 'DEBUG'
	max_borrow_limit: int

	@property
	def db_url(self) -> str:
		return f'postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}'



	class Config:
		env_file: str = '.env'
		env_file_encoding: str = 'utf-8'

settings = Settings()
