from pymongo import MongoClient

import config
import models
from utils import logger

__all__ = (
    'insert_account',
    'get_accounts',
    'update_tokens',
    'update_cookies',
    'close_mongo_db_connection',
)

_connection = MongoClient(config.MONGO_DB_URL)
_db = _connection.dodo


def insert_account(account: models.Account):
    _db.accounts.insert_one(account)


def get_accounts() -> tuple[models.Account, ...]:
    return tuple(_db.accounts.find({}, {'_id': 0}))


def update_tokens(access_token: str, refresh_token: str, account_name: str):
    query = {'account_name': account_name}
    update = {'$set': {'access_token': access_token, 'refresh_token': refresh_token}}
    _db.tokens.update_one(query, update, upsert=True)


def close_mongo_db_connection() -> None:
    _connection.close()
    logger.debug('Mongodb connection has been closed')


def update_cookies(cookies: dict[str, str], account_name: str):
    query = {'account_name': account_name}
    update = {'$set': {'cookies': cookies}}
    _db.cookies.update_one(query, update, upsert=True)
