from sqlalchemy.orm import sessionmaker

from database.engine import engine
from repositories import AccountRepository, AccountTokensRepository

__all__ = (
    'get_accounts_repository',
    'get_account_tokens_repository',
)


def get_accounts_repository() -> AccountRepository:
    return AccountRepository(sessionmaker(engine))


def get_account_tokens_repository() -> AccountTokensRepository:
    return AccountTokensRepository(sessionmaker(engine))
