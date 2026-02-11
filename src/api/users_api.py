from api.base_client import BaseAPIClient


class UsersAPI:
    def __init__(self):
        self.client = BaseAPIClient(
            base_url="https://reqres.in/api",
            headers={"Content-Type": "application/json"}
        )

    def get_users(self, page=1):
        return self.client.get("/users", params={"page": page})

    def get_user_by_id(self, user_id):
        return self.client.get(f"/users/{user_id}")
