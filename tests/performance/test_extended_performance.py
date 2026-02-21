import pytest
import time
from statistics import mean

from api.auth_api import AuthAPI

pytestmark = pytest.mark.performance


@pytest.fixture
def auth_api():
    return AuthAPI()


def test_login_response_time_threshold(auth_api):
    """
    Validates that a single login request responds under 2 seconds.
    This acts as a regression guard for performance degradation.
    """
    start = time.time()
    response = auth_api.login("eve.holt@reqres.in", "pistol")
    end = time.time()

    duration = end - start

    assert response.status_code in (200, 400, 403)
    assert duration < 2.0


def test_multiple_login_average_response_time(auth_api):
    """
    Executes multiple login requests and validates
    the average response time stays under threshold.
    """
    durations = []

    for _ in range(5):
        start = time.time()
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        end = time.time()

        durations.append(end - start)
        assert response.status_code in (200, 400, 403)

    avg_time = mean(durations)
    assert avg_time < 2.0


def test_sequential_request_stability(auth_api):
    """
    Ensures repeated requests do not fail under sequential execution.
    This is not load testing — this validates stability.
    """
    for _ in range(10):
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        assert response.status_code in (200, 400, 403)


def test_response_time_percentile(auth_api):
    """
    Measures response time distribution and validates
    that worst-case execution remains acceptable.
    """
    durations = []

    for _ in range(8):
        start = time.time()
        response = auth_api.login("eve.holt@reqres.in", "pistol")
        end = time.time()

        durations.append(end - start)
        assert response.status_code in (200, 400, 403)

    max_duration = max(durations)
    assert max_duration < 3.0


def test_negative_login_performance(auth_api):
    """
    Validates performance behavior for invalid credentials.
    Even error responses should return quickly.
    """
    start = time.time()
    response = auth_api.login("invalid@email.com", "wrongpass")
    end = time.time()

    duration = end - start

    assert response.status_code in (400, 401, 403)
    assert duration < 2.0
