import exceptions
import redis_db
from dodo_account import DodoAccount
from utils import logger

__all__ = (
    'update_account_cookies',
)


def update_account_cookies(account: DodoAccount, repeat_times: int = 5):
    try:
        cookies = account.get_auth_cookies()
        if not cookies:
            raise exceptions.UnsuccessfulAuthError
    except exceptions.UnsuccessfulAuthError:
        if repeat_times <= 0:
            logger.warning(f'Could not update account {account.name} cookies')
            return
        return update_account_cookies(account, repeat_times - 1)
    else:
        redis_db.set_cookies(account.name, cookies)
        logger.info(f'Account {account.name} cookies have been updated')
