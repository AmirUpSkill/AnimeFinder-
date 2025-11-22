import os 
from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    # --- Project Metadata ---
    PROJECT_NAME: str = "AnimeFinder"
    API_V1_STR: str = "/api/v1"
    # --- Google Gemini AI ---
    GOOGLE_API_KEY: str 
    # --- Postgres DB --- 
    POSTGRES_SERVER: str 
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_DB: str 
    POSTGRES_PORT: str 
    # --- MinIO Object Storage --- 
    MINIO_ENDPOINT: str 
    MINIO_ACCESS_KEY: str 
    MINIO_SECRET_KEY: str 
    MINIO_BUCKET_NAME: str 
    MINIO_SECURE: bool 
    # --- Computed DB URL --- 
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )
# --- Settings Instance --- 
settings = Settings()