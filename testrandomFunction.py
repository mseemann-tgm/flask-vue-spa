import pytest
from run import app

@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client

def testaufrufRandom(client):
    res = client.get('/api/random')
    assert res.status_code == 200
