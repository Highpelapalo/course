import pytest
import time
import requests
import foobar
from multiprocessing import Process

def set_up():
    foobar.flapp.run()
@pytest.fixture
def flask_obj(request):
    p = Process(target=set_up)
    p.start()
    time.sleep(3)
    def kill_it():
        p.terminate()
    request.addfinalizer(kill_it)


def test_app(flask_obj):
    request = requests.get('http://localhost:5000/bar')
    assert request.status_code == 200
