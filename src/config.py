from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

__all__ = (
    'get_app_settings',
    'get_crypt_settings',
    'get_oauth_settings',
)

load_dotenv()


class OAuthSettings(BaseSettings):
    client_id: str = Field(env='CLIENT_ID')
    client_secret: str = Field(env='CLIENT_SECRET')
    redirect_uri: str = Field(env='REDIRECT_URI')


class AppSettings(BaseSettings):
    debug: bool = Field(env='DEBUG')


class CryptSettings(BaseSettings):
    secret_key: str = Field(env='SECRET_KEY')


@lru_cache(maxsize=1)
def get_oauth_settings() -> OAuthSettings:
    return OAuthSettings()


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache(maxsize=1)
def get_crypt_settings() -> CryptSettings:
    return CryptSettings()
