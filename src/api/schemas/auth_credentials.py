from typing import TypeAlias

from pydantic import constr, BaseModel

__all__ = ('AccountName', 'AccountCookies', 'AccountTokens')

AccountName: TypeAlias = constr(min_length=1, max_length=64)


class AccountTokens(BaseModel):
    account_name: str
    access_token: str
    refresh_token: str


class AccountCookies(BaseModel):
    account_name: str
    cookies: dict[str, str]
