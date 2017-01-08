import pytest
import requests
from multiprocessing import Process

@pytest.fixture
def flapp(request):
    def set_up():
        flapp.run()
    p = Process(target=set_up)
    p.start()

    def kill_it():
        p.shutdown()
    request.addfinalizer(kill_it)


def test_app(flapp):
    request = requests.get('http://localost:5000/bar')
    assert request.status_code == 200
