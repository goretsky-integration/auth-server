import logging

import dodo
import exceptions
import models
from config import setup_logging, config
from external_api_services import AuthService
from security import CryptText


def main():
    setup_logging(config.logging)

    crypt = CryptText(config.app.secret_key)

    auth_service = AuthService(base_url=config.external_api.auth_service_base_url)
    encrypted_accounts = [
        account for account in auth_service.get_accounts()
        if account.name.startswith('office') or account.name.startswith('shift')
    ]
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
        accounts_cookies.append(dodo.get_new_auth_cookies(
            country_code=config.country_code,
            account_name=account.name,
            login=account.login,
            password=account.password,
        ))

    for account_cookies in accounts_cookies:
        auth_service.update_account_cookies(account_cookies)


if __name__ == '__main__':
    main()
