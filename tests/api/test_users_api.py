import pytest
from api.users_api import UsersAPI
from api.validators import validate_user_object
from api.validators import validate_token_response




pytestmark = pytest.mark.api


@pytest.fixture
def users_api():
    return UsersAPI()


def test_get_users_success(users_api):
    response = users_api.get_users(page=2)

    assert response.status_code == 200

    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


def test_get_single_user(users_api):
    response = users_api.get_user_by_id(2)

    assert response.status_code == 200

    body = response.json()
    assert "data" in body
    validate_user_object(body["data"])


def test_get_user_not_found(users_api):
    response = users_api.get_user_by_id(9999)

    assert response.status_code == 404
