import logging

import config

__all__ = (
    'logger',
)

log_level = logging.DEBUG if config.DEBUG else logging.INFO

logging.basicConfig(encoding='utf-8', level=log_level)
logger = logging.getLogger()
