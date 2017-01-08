import pytest
import requests
import foobar
from multiprocessing import Process

@pytest.fixture
def flapp(request):
    def set_up():
        foobar.flapp.run()
    p = Process(target=set_up)
    p.start()

    def kill_it():
        p.shutdown()
    request.addfinalizer(kil_it)


def test_app(flapp):
    request = requests.get('http://localost:5000/bar')
    assert request.status_code == 200
