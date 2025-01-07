from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False, env_file='.env', env_file_encoding='utf-8')
    
    RAPIDAPI_KEY: str
    RAPIDAPI_HOST: str
    RAPIDAPI_URL: str
    WEBSITE_URL: str
    GCP_PROJECT_ID: str
    GCP_BQ_DATASET: str
    GCP_BQ_TABLE: str
    
    
config = Settings()