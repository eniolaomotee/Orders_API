from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_name: str
    database_username: str
    database_password: str
    secret_key: str
    access_token_expires_minutes: int
    algorithm: str
    
    class Config:
        env_file = ".env"
        



settings = Settings()