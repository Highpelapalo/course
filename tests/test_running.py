import foobar, requests

def test_running():
    foo_recv = requests.get("http://127.0.0.1/foo")
    assert foo_recv.status_code == 200

    bar_recv = requests.get("http://127.0.0.1/bar")
    assert bar_recv.status_code == 200
