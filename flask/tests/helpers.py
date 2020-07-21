from .constants import CONTENT_TYPE
import json

def login_user(test_client, user):
    """
    logs a user into their account and returns the token.
    returns the json decoded response from the server.
    """
    login = test_client.post('/users/login',
                             data=json.dumps({
                                 'email': user.get('email'),
                                 'password': user.get('password')
                             }),
                       content_type=CONTENT_TYPE)

    login_data = json.loads(login.data.decode())
    return login_data


def marshall_raw_data(obj, fields):
    _obj = dict(zip(fields, obj))
    return _obj


