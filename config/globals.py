from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    TELEGRAM_TOKEN: str
    OPENAI_TOKEN: str
    MY_TELEGRAM_ID: int

    @property
    def sync_db_url(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")

config = Config()