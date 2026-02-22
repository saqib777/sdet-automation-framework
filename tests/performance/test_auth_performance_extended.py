import pytest
import time
import concurrent.futures
from statistics import mean

from api.auth_api import AuthAPI

pytestmark = pytest.mark.performance


@pytest.fixture
def auth_api():
    return AuthAPI()


# --------------------------------------------------
# Single Request Threshold
# --------------------------------------------------

def test_login_single_request_under_threshold(auth_api):
    start = time.time()
    response = auth_api.login("eve.holt@reqres.in", "pistol")
    duration = time.time() - start

    assert response.status_code in (200, 400, 403)
    assert duration < 2.0


# --------------------------------------------------
# Average Response Time
# --------------------------------------------------

def test_login_average_response_time(auth_api):
    durations = []

    for _ in range(5):
        start = time.time()
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        durations.append(time.time() - start)

        assert response.status_code in (200, 400, 403)

    assert mean(durations) < 2.0


# --------------------------------------------------
# Maximum Response Time
# --------------------------------------------------

def test_login_max_response_time(auth_api):
    durations = []

    for _ in range(8):
        start = time.time()
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        durations.append(time.time() - start)

        assert response.status_code in (200, 400, 403)

    assert max(durations) < 3.0


# --------------------------------------------------
# Sequential Stability
# --------------------------------------------------

def test_login_sequential_stability(auth_api):
    for _ in range(10):
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        assert response.status_code in (200, 400, 403)


# --------------------------------------------------
# Concurrent Stability
# --------------------------------------------------

def test_login_concurrent_requests(auth_api):
    def make_request():
        return auth_api.login("eve.holt@reqres.in", "pistol")

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(10)]
        responses = [f.result() for f in futures]

    duration = time.time() - start

    for response in responses:
        assert response.status_code in (200, 400, 403)

    assert duration < 5.0


# --------------------------------------------------
# Negative Scenario Performance
# --------------------------------------------------

def test_invalid_login_response_time(auth_api):
    start = time.time()
    response = auth_api.login("invalid@email.com", "wrongpass")
    duration = time.time() - start

    assert response.status_code in (400, 401, 403)
    assert duration < 2.0
