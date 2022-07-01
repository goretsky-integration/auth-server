import atexit

import accounts
import db
import dodo
import exceptions
from utils import logger


@atexit.register
def on_shutdown():
    db.close_mongo_db_connection()
    db.close_redis_connection()


def main():
    all_accounts = accounts.get_accounts()
    for account in all_accounts:
        try:
            cookies = dodo.get_new_auth_cookies(account['login'], account['password'])
        except exceptions.UnsuccessfulAuthError:
            logger.warning(f'Could not update {account["name"]} account')
        else:
            db.set_cookies(account['name'], cookies)
            logger.debug(f'Account {account["name"]} cookies have been updated')


if __name__ == '__main__':
    main()
