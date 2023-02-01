import logging
import pathlib

import dodo
import exceptions
import models
from config import load_config, setup_logging
from external_api_services import DatabaseService, AuthService
from security import CryptText


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.toml'
    config = load_config(config_file_path)
    setup_logging(config.logging)

    crypt = CryptText(config.app.secret_key)

    database_service = DatabaseService(base_url=config.external_api.database_service_base_url)
    encrypted_accounts = database_service.get_accounts()
    decrypted_accounts = []
    for account in encrypted_accounts:
        try:
            decrypted_accounts.append(
                models.Account(
                    name=account.name,
                    login=crypt.decrypt(account.login),
                    password=crypt.decrypt(account.password),
                ),
            )
        except exceptions.AuthCredentialsDecodeError:
            logging.error('Could not decode auth credentials')

    accounts_cookies = []
    for account in decrypted_accounts:
        accounts_cookies.append(dodo.get_new_auth_cookies(account.name, account.login, account.password))

    auth_service = AuthService(base_url=config.external_api.auth_service_base_url)
    for account_cookies in accounts_cookies:
        auth_service.update_account_cookies(account_cookies)


if __name__ == '__main__':
    main()
