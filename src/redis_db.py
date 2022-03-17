import contextlib
from typing import Generator

from redis import Redis

import config

__all__ = (
    'set_cookies',
    'get_cookies_lifetime',
)


@contextlib.contextmanager
def redis_connection() -> Generator[Redis, None, None]:
    redis = Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True,
    )
    try:
        yield redis
    finally:
        redis.close()


def set_cookies(account_name: str, cookies: dict):
    with redis_connection() as redis:
        redis.hset(account_name, mapping=cookies)
        redis.expire(account_name, config.COOKIES_LIFETIME)


def get_cookies_lifetime(account_name: str) -> int:
    with redis_connection() as redis:
        return redis.ttl(account_name)
