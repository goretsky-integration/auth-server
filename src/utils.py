import json

from loguru import logger

import config

__all__ = (
    'logger',
)


def read_accounts_file() -> list[dict]:
    with open(config.ACCOUNTS_FILE_PATH, encoding='utf-8') as accounts_file:
        return json.load(accounts_file)
