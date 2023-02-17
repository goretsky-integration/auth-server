from sqlalchemy.orm import sessionmaker

from database.engine import engine
from repositories import AccountRepository

__all__ = ('get_accounts_repository',)


def get_accounts_repository() -> AccountRepository:
    return AccountRepository(sessionmaker(engine))
