import pytest
from src.api.sportsify_client import fetch_sports_data

def test_fetch_sports_data_success(mocker):
    mock_response = {
        "data": [
            {"id": 1, "name": "Team A", "score": 100},
            {"id": 2, "name": "Team B", "score": 95}
        ]
    }
    mocker.patch('src.api.sportsify_client.requests.get', return_value=mock_response)

    result = fetch_sports_data()
    assert result == mock_response['data']

def test_fetch_sports_data_failure(mocker):
    mocker.patch('src.api.sportsify_client.requests.get', side_effect=Exception("API call failed"))

    with pytest.raises(Exception) as excinfo:
        fetch_sports_data()
    assert str(excinfo.value) == "API call failed"