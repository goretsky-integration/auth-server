import pathlib

from environs import Env

__all__ = (
    'COOKIES_LIFETIME',
    'COOKIES_UPDATE_THRESHOLD',
    'COOKIES_UPDATE_DELAY',
    'TELEGRAM_MESSAGES_QUEUE',
    'SRC_DIR',
    'ACCOUNTS_FILE_PATH',
    'LOG_FILE_PATH',
)

env = Env()
env.read_env()

COOKIES_LIFETIME: int = env.int('COOKIES_LIVETIME')
COOKIES_UPDATE_DELAY: int = env.int('COOKIES_UPDATE_DELAY')
COOKIES_UPDATE_THRESHOLD: int = env.int('COOKIES_UPDATE_THRESHOLD')

SRC_DIR = pathlib.Path(__file__).parent
ACCOUNTS_FILE_PATH = pathlib.Path.joinpath(SRC_DIR.parent, 'accounts.json')
LOG_FILE_PATH = pathlib.Path.joinpath(SRC_DIR.parent, 'logs.log')
