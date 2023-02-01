class UnsuccessfulAuthError(Exception):
    pass


class UnsuccessfulTokenRefreshError(Exception):
    pass


class ForbiddenHostError(Exception):
    pass


class AuthCredentialsDecodeError(Exception):
    pass
