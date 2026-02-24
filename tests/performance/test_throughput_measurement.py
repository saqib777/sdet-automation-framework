def test_login_throughput():

    users = 30

    start = time.time()

    with ThreadPoolExecutor(max_workers=users) as executor:
        results = list(executor.map(lambda _: send_request(), range(users)))

    total_time = time.time() - start
    throughput = users / total_time

    assert throughput > 5, f"Throughput too low: {throughput} req/sec"