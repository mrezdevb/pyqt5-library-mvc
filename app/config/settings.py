from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    log_level: str = "DEBUG"
    max_borrow_limit: int

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}/{self.db_name}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding: str = "utf-8"
        extra = "ignore"


settings: Settings = Settings()  # type: ignore[call-arg]
