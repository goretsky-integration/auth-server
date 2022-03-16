from http.cookies import BaseCookie

import aiohttp

import exceptions


class DodoAuthenticator:
    _login_url = 'https://auth.dodopizza.ru/Authenticate/LogOn'
    _headers = {
        'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'),
    }

    __slots__ = ('__login', '__password')

    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password

    @property
    def auth_data(self) -> dict:
        return {
            'CountryCode': 'Ru',
            'login': self.__login,
            'password': self.__password,
        }

    @staticmethod
    def parse_cookies(cookies: BaseCookie) -> dict:
        return {cookie.key: cookie.value for key, cookie in cookies.items()}

    async def get_auth_cookies(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self._login_url, headers=self._headers,
                                    data=self.auth_data) as response:
                if not response.ok:
                    raise exceptions.UnsuccessfulAuthError
                cookies = session.cookie_jar.filter_cookies(self._login_url)
                return self.parse_cookies(cookies)
