import json

import requests

import exceptions
import models

__all__ = (
    'get_new_auth_cookies',
    'get_new_auth_tokens',
)

HEADERS = {'User-Agent': 'dodoextbot'}


def get_new_auth_cookies(country_code: str, account_name: str, login: str, password: str) -> models.AuthCookies:
    data = {'CountryCode': country_code, 'login': login, 'password': password}
    url = f'https://auth.dodopizza.{country_code}/Authenticate/LogOn'
    with requests.Session() as session:
        response = session.post(url, headers=HEADERS, data=data)
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
    response = requests.post('https://auth.dodois.io/connect/token', data=data, headers=HEADERS)
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
