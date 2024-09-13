from os import environ
from pydantic import BaseSettings

class Settings(BaseSettings):
    GITHUB_API_KEY: str
    FIRESTORE_PROJECT_ID: str
    EMAIL_SENDER: str
    EMAIL_RECIPIENT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Initialize settings
settings = Settings()

# HUMAN ASSISTANCE NEEDED
# The following block might need adjustments based on specific requirements:
# - Additional environment variables might be needed
# - Default values or validation rules for the variables could be added
# - The .env file path might need to be adjusted based on the project structure
