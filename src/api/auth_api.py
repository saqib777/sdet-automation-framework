from api.base_client import BaseAPIClient



class AuthAPI:
    def __init__(self):
        self.client = BaseAPIClient(
            base_url="https://reqres.in/api",
            headers={"Content-Type": "application/json"}
        )

    def login(self, email=None, password=None):
        payload = {}
        if email:
            payload["email"] = email
        if password:
            payload["password"] = password

        return self.client.post("/login", json=payload)

    def register(self, email, password):
      return self.client.post(
         "/register",
         json={
             "email": email,
             "password": password
         }
    )


