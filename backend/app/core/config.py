from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Travel with Farmer API"
    app_env: str = "development"
    api_prefix: str = "/api/v1"

    database_url: str

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 1440

    openweather_api_key: str = ""
    openweather_url: str = "https://api.openweathermap.org/data/2.5/forecast"

    market_api_base_url: str = "https://api.data.gov.in"
    market_api_key: str = ""

    ndvi_api_base_url: str = "https://earth-search.aws.element84.com"
    ai_provider: str = "stub"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()
