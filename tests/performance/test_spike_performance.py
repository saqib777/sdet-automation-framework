import time
import requests
from concurrent.futures import ThreadPoolExecutor


BASE_URL = "https://reqres.in/api/login"


def send_request():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    start = time.time()
    response = requests.post(BASE_URL, json=payload)
    duration = time.time() - start

    return response.status_code, duration


def test_login_spike_load():

    normal_users = 5
    spike_users = 50

    # Normal traffic
    with ThreadPoolExecutor(max_workers=normal_users) as executor:
        normal_results = list(executor.map(lambda _: send_request(), range(normal_users)))

    # Spike traffic
    with ThreadPoolExecutor(max_workers=spike_users) as executor:
        spike_results = list(executor.map(lambda _: send_request(), range(spike_users)))

    # Recovery traffic
    with ThreadPoolExecutor(max_workers=normal_users) as executor:
        recovery_results = list(executor.map(lambda _: send_request(), range(normal_users)))

    all_results = normal_results + spike_results + recovery_results

    status_codes = [r[0] for r in all_results]
    durations = [r[1] for r in all_results]

    avg_response = sum(durations) / len(durations)
    max_response = max(durations)

    assert all(code == 200 for code in status_codes), "Some requests failed during spike"
    assert avg_response < 2, f"Average response too high: {avg_response}"
    assert max_response < 5, f"Max response too high: {max_response}"