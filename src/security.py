import config
from cryptography.fernet import Fernet


fernet = Fernet(config.SECRET_KEY)


def encrypt(value: str) -> str:
    return fernet.encrypt(value.encode('utf-8')).decode('utf-8')


def decrypt(value: str) -> str:
    return fernet.decrypt(value.encode('utf-8')).decode('utf-8')
