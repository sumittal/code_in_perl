from collections import namedtuple
from requests import Request, Session

PLIVO_API_URL = '/'.join(['https://api.plivo.com', 'v1/Account'])

AuthDetails = namedtuple('AuthDetails', 'auth_id auth_token')

# method to validate the account
def is_valid_account(account):
    account_str = str(account)
    if len(account_str) == 20 and account_str[:2] == 'MA':
        return True
    return False

# verify and get the credentials
def get_auth_credentials(auth_id, auth_token):

    if not (auth_id and auth_token):
        raise ValueError("Auth id and Auth tokens are required")

    if not is_valid_account(auth_id):
        raise ValueError('Invalid auth_id passed: %s' % auth_id)

    return AuthDetails(auth_id=auth_id, auth_token=auth_token)


class Client():
    def __init__(self, auth_id, auth_token, timeout=10):

        self.base_uri = PLIVO_API_URL
        self.timeout = timeout
        self.session = Session()
        self.session.headers.update({
            'User-Agent': 'Plivo Python API',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })
        self.session.auth = get_auth_credentials(auth_id, auth_token)


    def make_request(self, method, path=None, options=None):
        if path is not None:
            url = '/'.join([PLIVO_API_URL, self.session.auth[0], path])  + '/'
        else:
            url = '/'.join([PLIVO_API_URL, self.session.auth[0]])  + '/'

        if method == 'GET':
            req = Request('get', url, **({'params': options}))
        elif method == 'POST':
            req = Request('post', url, **({'json': options}))
        else:
            raise ValueError("Invalid method, should be GET or POST")

        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        if response.status_code not in [200, 202]:
            raise Exception(
                'status code {status_code} for the HTTP  call '
                '"{method}"'.format(
                    status_code=response.status_code, method=method))

        return response.json()

