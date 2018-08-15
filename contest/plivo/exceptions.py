class PlivoError(Exception):
    pass

class InvalidRequestError(PlivoError):
    pass

class ServerError(PlivoError):
    pass

class AuthenticationError(PlivoError):
    pass


