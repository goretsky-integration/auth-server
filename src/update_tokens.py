import asyncio

from dodolib import DatabaseClient, AuthClient
from dodolib.models import AuthToken
from dodolib.utils.convert_models import UnitsConverter

import dodo
import exceptions
import models
from config import get_oauth_settings


async def main():
    oauth_settings = get_oauth_settings()
    async with (
        DatabaseClient() as db_client,
        AuthClient() as auth_client,
    ):
        units = UnitsConverter(await db_client.get_units())
        tasks = (auth_client.get_tokens(account_name) for account_name in units.account_names)
        accounts_tokens: tuple[AuthToken, ...] = await asyncio.gather(*tasks)

        tasks = (dodo.get_new_auth_tokens(account_tokens.account_name, oauth_settings.client_id,
                                          oauth_settings.client_secret, account_tokens.refresh_token)
                 for account_tokens in accounts_tokens)

        accounts_new_tokens: tuple[models.AuthTokens, ...] = await asyncio.gather(*tasks, return_exceptions=True)

        tasks = (auth_client.update_tokens(new_tokens.account_name, new_tokens.access_token, new_tokens.refresh_token)
                 for new_tokens in accounts_new_tokens
                 if not isinstance(new_tokens, exceptions.UnsuccessfulTokenRefreshError))
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
