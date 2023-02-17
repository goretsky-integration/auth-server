from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

import exceptions
import models
from database.models import AccountCookies
from repositories.base import Repository

__all__ = ('AccountCookiesRepository',)


class AccountCookiesRepository(Repository):

    def get_by_account_name(self, account_name: str) -> models.AuthCookies:
        statement = select(AccountCookies).where(AccountCookies.account_name == account_name)
        with self._session_factory() as session:
            account_cookies = session.scalar(statement)
        if account_cookies is None:
            raise exceptions.DoesNotExistInDatabase('Cookies not found')
        return models.AuthCookies(account_name=account_name, cookies=account_cookies.cookies)

    def update(self, *, account_name: str, cookies: dict[str, str]):
        statement = (
            insert(AccountCookies)
            .values(account_name=account_name, cookies=cookies)
            .on_conflict_do_update(
                index_elements=('account_name',),
                set_={'cookies': cookies},
                where=(AccountCookies.account_name == account_name),
            )
        )
        with self._session_factory() as session:
            with session.begin():
                session.execute(statement)
