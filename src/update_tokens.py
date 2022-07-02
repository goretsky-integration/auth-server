import db
import dodo
import exceptions
from utils import logger


def main():
    accounts = db.get_accounts()
    office_manager_account_names = (account['name'] for account in accounts if account['name'].startswith('office'))
    for account_name in office_manager_account_names:
        try:
            refresh_token = db.local_storage.get_item(account_name)
        except exceptions.LocalStorageItemIsNotFoundError:
            logger.error(f'Account {account_name} refresh token is missing')
            continue
        try:
            new_auth_credentials = dodo.get_new_access_token(refresh_token)
        except exceptions.UnsuccessfulTokenRefreshError as error:
            logger.error(f'Could not update account {account_name} token:', str(error))
        else:
            access_token = new_auth_credentials['access_token']
            refresh_token = new_auth_credentials['refresh_token']
            db.set_token(account_name, access_token)
            db.local_storage.set_item(key=account_name, value=refresh_token)
            logger.info(f'Account {account_name} token has been updated')


if __name__ == '__main__':
    main()
