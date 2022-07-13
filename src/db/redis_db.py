import json

import redis

import config
from utils import logger

__all__ = (
    'set_cookies',
    'close_redis_connection',
    'set_token',
)

_redis = redis.from_url(config.REDIS_URL, decode_responses=True)


def set_cookies(account_name: str, cookies: dict):
    """Set cookies in redis.

    Args:
        account_name: Related to account unique cookies name.
        cookies: new cookies to be set.
    """
    cookies_json = json.dumps(cookies)
    key = f'cookies_{account_name}'
    _redis.set(key, cookies_json)
    _redis.expire(key, config.COOKIES_LIFETIME)


def set_token(account_name: str, access_token: str):
    _redis.set(f'token_{account_name}', access_token)


def close_redis_connection():
    _redis.close()
    logger.debug('Redis connection has been closed')
