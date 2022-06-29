from environs import Env

__all__ = (
    'COOKIES_LIFETIME',
    'COOKIES_UPDATE_THRESHOLD',
    'COOKIES_UPDATE_DELAY',
    'REDIS_DB',
    'REDIS_HOST',
    'REDIS_PORT',
    'SECRET_KEY',
    'MONGO_DB_URL',
)

env = Env()
env.read_env()

COOKIES_LIFETIME: int = env.int('COOKIES_LIVETIME')
COOKIES_UPDATE_DELAY: int = env.int('COOKIES_UPDATE_DELAY')
COOKIES_UPDATE_THRESHOLD: int = env.int('COOKIES_UPDATE_THRESHOLD')

REDIS_DB: int = env.int('REDIS_DB')
REDIS_HOST: str = env.str('REDIS_HOST')
REDIS_PORT: int = env.int('REDIS_PORT')

SECRET_KEY: str = env.str('SECRET_KEY')
MONGO_DB_URL: str = env.str('MONGO_DB_URL')
