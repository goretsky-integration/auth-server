from typing import TypedDict


class Account(TypedDict):
    login: str
    name: str
    password: str
    account_name: str


class AuthCredentials(TypedDict):
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str
