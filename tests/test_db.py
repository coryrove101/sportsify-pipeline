import pytest
from src.db.postgres_client import PostgresClient

@pytest.fixture
def db_client():
    client = PostgresClient()
    yield client
    client.close()

def test_insert_data(db_client):
    test_data = {'id': 1, 'name': 'Test Team', 'score': 100}
    db_client.insert_data('sports_data', test_data)
    result = db_client.get_data('sports_data', {'id': 1})
    assert result['name'] == 'Test Team'
    assert result['score'] == 100

def test_update_data(db_client):
    test_data = {'id': 1, 'name': 'Test Team', 'score': 100}
    db_client.insert_data('sports_data', test_data)
    updated_data = {'score': 150}
    db_client.update_data('sports_data', {'id': 1}, updated_data)
    result = db_client.get_data('sports_data', {'id': 1})
    assert result['score'] == 150

def test_delete_data(db_client):
    test_data = {'id': 1, 'name': 'Test Team', 'score': 100}
    db_client.insert_data('sports_data', test_data)
    db_client.delete_data('sports_data', {'id': 1})
    result = db_client.get_data('sports_data', {'id': 1})
    assert result is None

def test_get_data(db_client):
    test_data = {'id': 1, 'name': 'Test Team', 'score': 100}
    db_client.insert_data('sports_data', test_data)
    result = db_client.get_data('sports_data', {'id': 1})
    assert result['name'] == 'Test Team'