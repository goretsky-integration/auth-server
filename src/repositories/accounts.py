from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

import exceptions
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

    def create(self, *, name: str, login: str, password: str):
        account = Account(name=name, login=login, password=password)
        with self._session_factory() as session:
            try:
                with session.begin():
                    session.add(account)
            except IntegrityError:
                raise exceptions.AlreadyExistsInDatabase('Account already exists')
