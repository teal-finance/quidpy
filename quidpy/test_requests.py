import pytest
# from requests.exceptions import HTTPError
from . import QuidRequests
from .exceptions import QuidUnauthorizedException

"""
Before running the tests:

- Run a Quid server on localhost:8082 and create a "demo" namespace
- Create a user with name "demouser" and password "demouser"
- Run the Flask server in the example folder and set the key in
example/server.py
"""

quid_uri = "http://localhost:8082"
server_uri = "http://127.0.0.1:5000"
namespace = "demo"

request = QuidRequests(
    quid_uri,
    server_uri,
    namespace
)


def test_init():
    assert request.namespace == namespace
    assert request.quid_uri == quid_uri


def test_refresh_token():
    assert request.refresh_token is None
    request.getRequestToken("demouser", "demouser")
    assert type(request.refresh_token) == str
    assert len(request.refresh_token) > 0


def test_refresh_token_wrong():
    with pytest.raises(QuidUnauthorizedException):
        request.getRequestToken("demouser", "x")


def test_access_token():
    assert request.access_token is None
    request.getAccessToken()
    assert type(request.access_token) == str
    assert len(request.access_token) > 0


def test_request_get():
    request.get("/")
