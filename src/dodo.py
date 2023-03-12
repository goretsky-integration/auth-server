import json

import requests

import exceptions
import models

__all__ = (
    'get_new_auth_cookies',
    'get_new_auth_tokens',
)

LOGIN_URL = 'https://auth.dodopizza.ru/Authenticate/LogOn'
TOKEN_URL = 'https://auth.dodois.io/connect/token'
HEADERS = {'User-Agent': 'dodoextbot'}


def get_new_auth_cookies(account_name: str, login: str, password: str) -> models.AuthCookies:
    data = {'login': login, 'password': password}
    with requests.Session() as session:
        response = session.post(LOGIN_URL, headers=HEADERS, data=data)
        if response.status_code == 403:
            raise exceptions.ForbiddenHostError('It is not allowed to login from this host')
        if not response.ok:
            raise exceptions.UnsuccessfulAuthError
        cookies = session.cookies.get_dict()
        return models.AuthCookies(account_name=account_name, cookies=cookies)


def get_new_auth_tokens(
        account_name: str,
        client_id: str,
        client_secret: str,
        refresh_token: str
) -> models.AuthTokens:
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(TOKEN_URL, data=data, headers=HEADERS)
    try:
        response_json = response.json()
    except json.JSONDecodeError:
        raise exceptions.UnsuccessfulTokenRefreshError('Could not decode response JSON')
    error_message = response_json.get('error')
    if response.status_code == 403:
        raise exceptions.ForbiddenHostError('It is not allowed to login from this host')
    if error_message is not None:
        raise exceptions.UnsuccessfulTokenRefreshError(error_message)
    return models.AuthTokens(access_token=response_json['access_token'],
                             refresh_token=response_json['refresh_token'],
                             account_name=account_name)
