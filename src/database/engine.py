from sqlalchemy import create_engine

from config import config

__all__ = ('engine',)

engine = create_engine(config.database.url)
