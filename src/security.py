from cryptography.fernet import Fernet, InvalidToken

import exceptions

__all__ = (
    'CryptText',
)


class CryptText:

    def __init__(self, secret_key: str):
        self.__fernet = Fernet(secret_key)

    def encrypt(self, value: str) -> str:
        return self.__fernet.encrypt(value.encode('utf-8')).decode('utf-8')

    def decrypt(self, value: str) -> str:
        try:
            return self.__fernet.decrypt(value.encode('utf-8')).decode('utf-8')
        except InvalidToken:
            raise exceptions.AuthCredentialsDecodeError

    @staticmethod
    def generate_key() -> str:
        return Fernet.generate_key().decode('utf-8')
