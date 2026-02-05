from src.api.base_client import BaseClient


class AuthAPI(BaseClient):
    def __init__(self):
        super().__init__("https://reqres.in")

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return self.post("/api/login", payload)
