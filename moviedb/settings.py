from sqlalchemy.engine.url import URL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config("common.env")

APP_HOST = config("APP_HOST", default="0.0.0.0")
APP_PORT = config("APP_PORT", cast=int, default=8080)
DEBUG = config("DEBUG", cast=bool, default=False)
TESTING = config("TESTING", cast=bool, default=False)
SECRET_KEY = config("SECRET_KEY", cast=Secret)
OMDBAPI_KEY = config("OMDBAPI_KEY", default="45e90d75")
OMDBAPI_URL = "http://www.omdbapi.com/"
MEDIA_ROOT = config("MEDIA_ROOT", default="media")
DB_CONFIG = {
    "drivername": "postgresql",
    "host": config("DB_HOST", default="moviedb_db_1"),
    "port": config("DB_PORT", default="54321"),
    "username": config("DB_USER", default="moviedb"),
    "password": config("DB_PASSWORD", default="moviedb"),
    "database": config("DB_DATABASE", default="moviedb"),
}
DB_URL = URL(**DB_CONFIG)
