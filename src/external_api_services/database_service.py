import requests

import models

__all__ = ('DatabaseService',)


class DatabaseService:

    def __init__(self, *, base_url: str):
        self.__base_url = base_url.removesuffix('/')

    def get_accounts(self) -> list[models.Account]:
        url = f'{self.__base_url}/accounts/'
        response = requests.get(url)
        response_data = response.json()
        return [
            models.Account(
                name=account['name'],
                login=account['login'],
                password=account['password'],
            ) for account in response_data
        ]
