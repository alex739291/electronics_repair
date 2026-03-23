from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic will automatically look for this variable in the .env file
    DATABASE_URL: str

    # Configuration to tell Pydantic where the file is located
    model_config = SettingsConfigDict(env_file=".env")

# Creating a single instance of settings to use across the app
settings = Settings()