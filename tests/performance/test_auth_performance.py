import pytest
import time
from api.auth_api import AuthAPI

pytestmark = pytest.mark.performance


@pytest.fixture
def auth_api():
    return AuthAPI()


def test_login_response_under_1_second(auth_api):
    start = time.time()
    response = auth_api.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )
    end = time.time()

    duration = end - start

    assert response.status_code in (200, 400, 403)
    assert duration < 1.0
