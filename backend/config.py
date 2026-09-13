from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Jaldhara backend"
    
    # DB
    DATABASE_URL: str = Field("postgresql+asyncpg://postgres:postgres@localhost:5432/jaldhara", env="DATABASE_URL")
    
    # Redis
    REDIS_URL: str = Field("redis://localhost:6379/0", env="REDIS_URL")
    
    # MinIO
    MINIO_ENDPOINT: str = Field("localhost:9000", env="MINIO_ENDPOINT")
    MINIO_ACCESS_KEY: str = Field("minioadmin", env="MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY: str = Field("minioadmin", env="MINIO_SECRET_KEY")
    MINIO_SECURE: bool = Field(False, env="MINIO_SECURE")
    
    # Keycloak
    KEYCLOAK_URL: str = Field("http://localhost:8080/auth/", env="KEYCLOAK_URL")
    KEYCLOAK_REALM: str = Field("jaldhara", env="KEYCLOAK_REALM")
    KEYCLOAK_CLIENT_ID: str = Field("jaldhara-backend", env="KEYCLOAK_CLIENT_ID")
    KEYCLOAK_CLIENT_SECRET: Optional[str] = Field(None, env="KEYCLOAK_CLIENT_SECRET")
    
    # Auth Dev Mode
    AUTH_DEV_MODE: bool = Field(True, env="AUTH_DEV_MODE")

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
