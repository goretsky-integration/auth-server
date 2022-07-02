import redis

import config
from utils import logger

__all__ = (
    'set_cookies',
    'close_redis_connection',
    'set_token',
    'get_token',
)

_redis = redis.from_url(config.REDIS_URL, decode_responses=True)


def set_cookies(account_name: str, cookies: dict):
    """Set cookies in redis.

    Args:
        account_name: Related to account unique cookies name.
        cookies: new cookies to be set.
    """
    _redis.hset(account_name, mapping=cookies)
    _redis.expire(account_name, config.COOKIES_LIFETIME)


def set_token(account_name: str, access_token: str):
    _redis.hset('tokens', account_name, access_token)


def get_token(account_name: str) -> str:
    return _redis.hget('tokens', account_name)


def close_redis_connection():
    _redis.close()
    logger.debug('Redis connection has been closed')
