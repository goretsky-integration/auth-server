import db
import dodo
import exceptions
from utils import logger


def main():
    accounts = db.get_accounts()
    office_manager_account_names = (account['name'] for account in accounts if account['name'].startswith('office'))
    for account_name in office_manager_account_names:
        auth_credentials = db.get_token(account_name)
        refresh_token = auth_credentials['refresh_token']
        try:
            new_auth_credentials = dodo.get_new_access_token(refresh_token)
        except exceptions.UnsuccessfulTokenRefreshError as error:
            logger.error(f'Could not update account {account_name} token:', str(error))
        else:
            db.set_token(account_name, new_auth_credentials)
            logger.info(f'Account {account_name} token has been updated')


if __name__ == '__main__':
    main()
