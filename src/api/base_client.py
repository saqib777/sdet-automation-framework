import requests


class BaseApiClient:
    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url
        self.session = requests.Session()

        # Default headers
        self.session.headers.update(headers or {
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _full_url(self, endpoint: str) -> str:
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, **kwargs):
        return self.session.get(self._full_url(endpoint), **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.session.post(self._full_url(endpoint), **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.session.put(self._full_url(endpoint), **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.session.delete(self._full_url(endpoint), **kwargs)
