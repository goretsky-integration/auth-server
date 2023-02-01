import requests

import models

__all__ = ('AuthService',)


class AuthService:

    def __init__(self, *, base_url: str):
        self.__base_url = base_url.removesuffix('/')

    def get_account_tokens(self, account_name: str) -> models.AuthTokens:
        url = f'{self.__base_url}/auth/token/'
        request_query_params = {'account_name': account_name}
        response = requests.get(url, params=request_query_params)
        response_data = response.json()
        return models.AuthTokens(
            account_name=response_data['account_name'],
            access_token=response_data['access_token'],
            refresh_token=response_data['refresh_token'],
        )

    def update_account_tokens(self, account_tokens: models.AuthTokens) -> None:
        url = f'{self.__base_url}/auth/token/'
        request_data = {
            'account_name': account_tokens.account_name,
            'access_token': account_tokens.access_token,
            'refresh_token': account_tokens.refresh_token,
        }
        requests.patch(url, json=request_data)

    def update_account_cookies(self, account_cookies: models.AuthCookies) -> None:
        url = f'{self.__base_url}/auth/cookies/'
        request_data = {
            "account_name": account_cookies.account_name,
            "cookies": account_cookies.cookies,
        }
        requests.patch(url, json=request_data)
