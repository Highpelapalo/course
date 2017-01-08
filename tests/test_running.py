import foobar, requests

def test_running():
    foo_recv = requests.get("localhost:5000/foo")
    assert foo_recv.status_code == 200

    bar_recv = requests.get("localhost:5000/bar")
    assert bar_recv.status_code == 200
