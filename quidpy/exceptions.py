class QuidMustLoginException(Exception):
    """
    The refresh token is invalid or expired
    """


class QuidUnauthorizedException(Exception):
    """
    The server responded with unauthorized 401 status code
    """


class QuidTooManyRetriesException(Exception):
    """
    Request retried too many times
    """
