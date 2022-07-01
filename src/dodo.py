import requests

import config
import exceptions
import models

__all__ = (
    'get_new_auth_cookies',
)

LOGIN_URL = 'https://auth.dodopizza.ru/Authenticate/LogOn'
TOKEN_URL = 'https://auth.dodois.io/connect/token'
HEADERS = {'User-Agent': 'Goretsky-Band'}


def get_new_auth_cookies(login: str, password: str) -> dict:
    data = {'CountryCode': 'Ru', 'login': login, 'password': password}
    with requests.Session() as session:
        response = session.post(LOGIN_URL, headers=HEADERS, data=data)
        if not response.ok:
            raise exceptions.UnsuccessfulAuthError
        return session.cookies.get_dict()


def get_new_access_token(refresh_token: str) -> models.AuthCredentials:
    data = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response_json = requests.post(TOKEN_URL, data=data).json()
    error_message = response_json.get('error')
    if error_message is not None:
        raise exceptions.UnsuccessfulTokenRefreshError(error_message)
    return response_json
