import requests

class BaseAPIClient:
    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout

    def get(self, endpoint, params=None):
        return self.session.get(
            self.base_url + endpoint,
            params=params,
            timeout=self.timeout
        )

    def post(self, endpoint, json=None, data=None):
        return self.session.post(
            self.base_url + endpoint,
            json=json,
            data=data,
            timeout=self.timeout
        )

    def put(self, endpoint, json=None):
        return self.session.put(
            self.base_url + endpoint,
            json=json,
            timeout=self.timeout
        )

    def delete(self, endpoint):
        return self.session.delete(
            self.base_url + endpoint,
            timeout=self.timeout
        )
