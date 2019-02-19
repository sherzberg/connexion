
import pytest
import connexion
from flask import json

from hello import get_app


@pytest.fixture(scope='module')
def client():
    with get_app().app.test_client() as c:
        yield c



def test_greeting(client):
    response = client.post('/v1.0/greeting/asdf')

    assert response.status_code == 200
    assert json.loads(response.data)['greeting'] == 'Hello asdf'

