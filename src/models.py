from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Account:
    name: str
    login: str
    password: str


@dataclass(frozen=True, slots=True)
class AuthTokens:
    account_name: str
    access_token: str
    refresh_token: str


@dataclass(frozen=True, slots=True)
class AuthCookies:
    account_name: str
    cookies: dict[str, str]
