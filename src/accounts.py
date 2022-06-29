import db
import models
import security

__all__ = (
    'get_accounts',
    'insert_account',
)


def encrypt_account_info(account: models.Account) -> models.Account:
    return {
        'login': security.encrypt(account['login']),
        'password': security.encrypt(account['password']),
        'name': account['name'],
    }


def decrypt_account_info(account: models.Account) -> models.Account:
    return {
        'login': security.decrypt(account['login']),
        'password': security.decrypt(account['password']),
        'name': account['name'],
    }


def insert_account(account: models.Account):
    db.insert_account(encrypt_account_info(account))


def get_accounts() -> list[models.Account]:
    accounts = db.get_accounts()
    return [decrypt_account_info(account) for account in accounts]
