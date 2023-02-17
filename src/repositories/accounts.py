from sqlalchemy import select

import models
from database.models import Account
from repositories.base import Repository

__all__ = ('AccountRepository',)


class AccountRepository(Repository):

    def get_all(self, *, limit: int, skip: int) -> list[models.Account]:
        statement = (
            select(Account)
            .order_by(Account.name.asc())
            .limit(limit)
            .offset(skip)
        )
        with self._session_factory() as session:
            accounts = session.scalars(statement).all()
        return [
            models.Account(
                name=account.name,
                login=account.login,
                password=account.password,
            ) for account in accounts
        ]
