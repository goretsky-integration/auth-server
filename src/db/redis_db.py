import redis

import config
import models
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


def set_token(account_name: str, auth_credentials: models.AuthCredentials):
    name = f'token_{account_name}'
    _redis.hset(name, mapping=auth_credentials)
    _redis.expire(name, auth_credentials['expires_in'])


def get_token(account_name: str) -> models.AuthCredentials:
    return _redis.hgetall(f'token_{account_name}')


def close_redis_connection():
    _redis.close()
    logger.debug('Redis connection has been closed')
