import logging

from config import get_app_settings

__all__ = (
    'logger',
)

log_level = logging.DEBUG if get_app_settings().debug else logging.INFO

logging.basicConfig(encoding='utf-8', level=log_level)
logger = logging.getLogger()
