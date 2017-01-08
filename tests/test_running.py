import foobar, requests

def test_running():
    foo_recv = requests.get("localhost:80/foo")
    assert foo_recv.status_code == 200

    bar_recv = requests.get("localhost:80/bar")
    assert bar_recv.status_code == 200
