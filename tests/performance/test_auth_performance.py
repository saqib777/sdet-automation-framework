import pytest
import time
import statistics
import concurrent.futures
from api.auth_api import AuthAPI
import statistics

pytestmark = pytest.mark.performance


@pytest.fixture
def auth_api():
    return AuthAPI()


def test_login_average_response_time(auth_api):
    """
    Measure average response time over multiple requests.
    """

    durations = []

    for _ in range(10):
        start = time.time()
        response = auth_api.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )
        end = time.time()

        assert response.status_code in (200, 400, 403)

        durations.append(end - start)

    avg_time = statistics.mean(durations)
    max_time = max(durations)

    print(f"\nAverage response time: {avg_time:.4f}s")
    print(f"Max response time: {max_time:.4f}s")

    assert avg_time < 1.0
    assert max_time < 2.0


def test_login_burst_stability(auth_api):
    """
    Send rapid sequential requests to ensure system stability.
    """

    for _ in range(20):
        response = auth_api.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )
        assert response.status_code in (200, 400, 403)


def test_login_concurrent_requests(auth_api):
    """
    Simulate small concurrent load.
    """

    def make_request():
        return auth_api.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(10)]
        responses = [f.result() for f in futures]

    end = time.time()
    total_duration = end - start

    for response in responses:
        assert response.status_code in (200, 400, 403)

    print(f"\nTotal duration for concurrent batch: {total_duration:.4f}s")

    assert total_duration < 5

def test_login_95th_percentile(auth_api):
    """
    Validate that 95% of requests complete under acceptable threshold.
    """

    durations = []

    for _ in range(30):
        start = time.time()
        response = auth_api.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )
        end = time.time()

        assert response.status_code in (200, 400, 403)
        durations.append(end - start)

    durations.sort()
    index_95 = int(len(durations) * 0.95) - 1
    p95 = durations[index_95]

    print(f"\n95th percentile response time: {p95:.4f}s")

    assert p95 < 1.5

def test_sustained_login_stability(auth_api):
    """
    Validate stability over sustained repeated execution.
    """

    failures = 0

    for _ in range(50):
        response = auth_api.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )

        if response.status_code not in (200, 400, 403):
            failures += 1

    print(f"\nUnexpected failures during sustained load: {failures}")

    assert failures == 0