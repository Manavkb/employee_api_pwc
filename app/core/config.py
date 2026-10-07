"""
core/config.py - ONE place for application settings.

WHY : Values like the app name, version and API prefix are used in several
      files. Keeping them here means you change them once.
HOW : Read from environment variables, with sensible defaults for development.
"""
import os


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Enterprise Employee Management API")
    VERSION: str = os.getenv("APP_VERSION", "3.0.0")
    API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")


settings = Settings()
