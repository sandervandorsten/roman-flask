import pytest
from romanflask.flask_app import create_app


@pytest.fixture
def test_connection():
    return create_app().test_client()


def test_flask(test_connection):
    result = test_connection.get('/rom2num/MMMDCCCLVI')
    assert result.status_code == 200


def test_flask_shouldfail(test_connection):
    result = test_connection.get('/rom2num/XXMC')
    assert result.status_code == 404
