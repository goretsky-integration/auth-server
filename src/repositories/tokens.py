from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

import exceptions
import models
from database.models import AccountTokens, AccountCookies
from repositories.base import Repository

__all__ = ('AccountTokensRepository',)


class AccountTokensRepository(Repository):

    def get_by_account_name(self, account_name: str) -> models.AuthTokens:
        statement = select(AccountTokens).where(AccountTokens.account_name == account_name)
        with self._session_factory() as session:
            account_tokens = session.scalar(statement)
        if account_tokens is None:
            raise exceptions.DoesNotExistInDatabase('Tokens not found')
        return models.AuthTokens(
            account_name=account_name,
            access_token=account_tokens.access_token,
            refresh_token=account_tokens.refresh_token,
        )

    def update(self, *, account_name: str, access_token: str, refresh_token: str):
        statement = (
            insert(AccountTokens)
            .values(account_name=account_name, access_token=access_token, refresh_token=refresh_token)
            .on_conflict_do_update(
                index_elements=('account_name',),
                set_={
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                },
                where=(AccountTokens.account_name == account_name),
            )
        )
        with self._session_factory() as session:
            with session.begin():
                session.execute(statement)
