import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"


class ProductionConfig(Config):
    DEBUG = False