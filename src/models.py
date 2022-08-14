from dataclasses import dataclass
from typing import TypedDict


@dataclass(frozen=True, slots=True)
class Account:
    name: str
    login: str
    password: str


class AuthCredentials(TypedDict):
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str


@dataclass(frozen=True, slots=True)
class AuthCookies:
    account_name: str
    cookies: dict[str, str]
