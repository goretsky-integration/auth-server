import json

import config
import exceptions
import security

__all__ = (
    'LOCAL_STORAGE_PATH',
    'get_item',
    'set_item',
)

LOCAL_STORAGE_PATH = config.ROOT_PATH / 'local_storage.json'


def set_item(key: str, value: str) -> None:
    data_to_be_written = {key: security.encrypt(value)}
    if LOCAL_STORAGE_PATH.exists():
        with open(LOCAL_STORAGE_PATH, encoding='utf-8') as file:
            data_to_be_written = json.load(file) | data_to_be_written
    with open(LOCAL_STORAGE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data_to_be_written, file)


def get_item(key: str) -> str:
    with open(LOCAL_STORAGE_PATH, encoding='utf-8') as file:
        storage_data = json.load(file)
    try:
        value = storage_data[key]
    except KeyError:
        raise exceptions.LocalStorageItemIsNotFoundError(key=key)
    return security.decrypt(value)
