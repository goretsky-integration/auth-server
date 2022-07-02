import pathlib

from environs import Env

__all__ = (
    'COOKIES_LIFETIME',
    'REDIS_URL',
    'SECRET_KEY',
    'MONGO_DB_URL',
    'CLIENT_SECRET',
    'CLIENT_ID',
    'REDIRECT_URI',
    'DEBUG',
    'ROOT_PATH',
)

env = Env()
env.read_env()

COOKIES_LIFETIME: int = env.int('COOKIES_LIFETIME')
SECRET_KEY: str = env.str('SECRET_KEY')
MONGO_DB_URL: str = env.str('MONGO_DB_URL')
REDIS_URL: str = env.str('REDIS_URL')
CLIENT_ID: str = env.str('CLIENT_ID')
CLIENT_SECRET: str = env.str('CLIENT_SECRET')
REDIRECT_URI: str = env.str('REDIRECT_URI')
DEBUG: bool = env.bool('DEBUG')

ROOT_PATH = pathlib.Path(__file__).parent.parent
