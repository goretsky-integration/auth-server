import logging

__all__ = (
    'logger',
)

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()
