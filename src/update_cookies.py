import asyncio
from typing import Iterable

from dodolib import DatabaseClient, AuthClient

import dodo
import exceptions
import models
from config import get_crypt_settings
from security import CryptText
from utils import logger


async def get_accounts_cookies(accounts: Iterable[models.Account]) -> list[models.AuthCookies]:
    tasks = {account.name: asyncio.to_thread(dodo.get_new_auth_cookies, account_name=account.name,
                                             login=account.login, password=account.password)
             for account in accounts}
    all_accounts_cookies: list[models.AuthCookies] = []

    for _ in range(3):
        if not tasks:
            break

        accounts_cookies = await asyncio.gather(*tasks.values(), return_exceptions=True)

        for account_cookies in accounts_cookies:
            if isinstance(account_cookies, models.AuthCookies):
                tasks.pop(account_cookies.account_name)
                all_accounts_cookies.append(account_cookies)
    return all_accounts_cookies


async def main():
    crypt = CryptText(get_crypt_settings().secret_key)

    async with DatabaseClient() as db_client:
        accounts = await db_client.get_accounts()

    try:
        accounts = (models.Account(name=account.name, login=crypt.decrypt(account.login),
                                   password=crypt.decrypt(account.password))
                    for account in accounts)
    except exceptions.AuthCredentialsDecodeError:
        logger.critical('Could not decode auth credentials')
        return

    accounts_cookies = await get_accounts_cookies(accounts)

    async with AuthClient() as auth_client:
        tasks = (auth_client.update_cookies(account_cookies.account_name, account_cookies.cookies)
                 for account_cookies in accounts_cookies)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
