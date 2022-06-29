from redis import Redis

import config
from utils import logger

__all__ = (
    'set_cookies',
    'get_cookies_lifetime',
    'close_redis_connection',
)

_redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True
)


def set_cookies(account_name: str, cookies: dict):
    """Set cookies in redis.

    Args:
        account_name: Related to account unique cookies name.
        cookies: new cookies to be set.
    """
    _redis.hset(account_name, mapping=cookies)
    _redis.expire(account_name, config.COOKIES_LIFETIME)


def get_cookies_lifetime(account_name: str) -> int:
    """Get time in seconds before cookies will be expired.

    Args:
        account_name: Related to account unique cookies name.

    Returns:
        Time in seconds.
    """
    return _redis.ttl(account_name)


def close_redis_connection():
    _redis.close()
    logger.debug('Redis connection has been closed')
