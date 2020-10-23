import requests
from .exceptions import QuidMustLoginException, QuidUnauthorizedException, \
    QuidTooManyRetriesException


class QuidRequests:
    refresh_token = None
    access_token = None

    def __init__(self, quid_uri: str, server_uri: str,
                 namespace: str, timeouts={
                     "refresh_token": "24h",
                     "access_token": "20m"
                 }):
        self.quid_uri = quid_uri
        self.server_uri = server_uri
        self.namespace = namespace
        self.timeouts = timeouts
        self.headers = {}

    def get(self, uri: str):
        return self._requestWithRetry("get", uri)

    def post(self, uri, payload):
        return self._requestWithRetry("post", uri, payload)

    def getRequestToken(self, username: str, password: str,
                        token_ttl: str = None):
        ttl = self.timeouts["refresh_token"]
        if (token_ttl is not None):
            ttl = token_ttl
        uri = self.quid_uri+"/token/refresh/" + ttl
        payload = {
            "namespace": self.namespace,
            "username": username,
            "password": password,
        }
        r = requests.post(uri, payload)
        if r.status_code == requests.codes.ok:
            data = r.json()
            self.refresh_token = data["token"]
            # print("Refresh token", self.refresh_token)
        elif r.status_code == 401:
            raise QuidUnauthorizedException
        else:
            # print("Wrong status code", r.status_code)
            r.raise_for_status()

    def getAccessToken(self, token_ttl: str = None):
        if (self.refresh_token is None):
            raise QuidMustLoginException
        ttl = self.timeouts["access_token"]
        if (token_ttl is not None):
            ttl = token_ttl
        uri = self.quid_uri+"/token/access/" + ttl
        payload = {
            "namespace": self.namespace,
            "refresh_token": self.refresh_token,
        }
        r = requests.post(uri, payload)
        if r.status_code == requests.codes.ok:
            data = r.json()
            self.access_token = data["token"]
            self.headers = {
                'Authorization': "Bearer "+self.access_token
            }
            # print("Refresh token", self.access_token)
        elif r.status_code == 401:
            # the refresh token is probably expired
            raise QuidMustLoginException
        else:
            # print("Wrong status code", r.status_code)
            r.raise_for_status()

    def _requestWithRetry(self, method: str, uri: str,
                          payload=None, retries: int = 0):
        if (method == "get"):
            r = requests.get(self.server_uri+uri, headers=self.headers)
        else:
            r = requests.post(self.server_uri+uri, payload,
                              headers=self.headers)
        if r.status_code == requests.codes.ok:
            data = r.json()
            return data
        elif r.status_code == 401:
            retries += 1
            self.getAccessToken()
            if (retries < 3):
                self._requestWithRetry(method, uri, payload, retries)
            else:
                raise QuidTooManyRetriesException
        else:
            r.raise_for_status()
