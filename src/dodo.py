import requests

import exceptions

__all__ = (
    'get_new_auth_cookies',
)

LOGIN_URL = 'https://auth.dodopizza.ru/Authenticate/LogOn'
HEADERS = {'User-Agent': 'Goretsky-Band'}


def get_new_auth_cookies(login: str, password: str) -> dict:
    data = {'CountryCode': 'Ru', 'login': login, 'password': password}
    with requests.Session() as session:
        response = session.post(LOGIN_URL, headers=HEADERS, data=data)
        if not response.ok:
            raise exceptions.UnsuccessfulAuthError
        return session.cookies.get_dict()
