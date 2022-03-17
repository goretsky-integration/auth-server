import json

from loguru import logger

import config

__all__ = (
    'logger',
)

logger.add(config.LOG_FILE_PATH, retention='3 days')


def read_accounts_file() -> list[dict]:
    with open(config.ACCOUNTS_FILE_PATH, encoding='utf-8') as accounts_file:
        return json.load(accounts_file)
