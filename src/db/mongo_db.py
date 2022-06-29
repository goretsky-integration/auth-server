from pymongo import MongoClient

import config
import models
from utils import logger

__all__ = (
    'insert_account',
    'get_accounts',
    'close_mongo_db_connection',
)

_connection = MongoClient(config.MONGO_DB_URL)
_db = _connection.dodo


def insert_account(account: models.Account):
    _db.accounts.insert_one(account)


def get_accounts() -> tuple[models.Account, ...]:
    return tuple(_db.accounts.find({}, {'_id': 0}))


def close_mongo_db_connection() -> None:
    _connection.close()
    logger.debug('Mongodb connection has been closed')
