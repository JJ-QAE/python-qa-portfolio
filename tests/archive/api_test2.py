import pytest
import requests

@pytest.fixture
def api_response():
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")

def test_status_code(api_response):
    assert api_response.status_code == 200

def test_ma_title(api_response):
    assert "title" in api_response.json()

def test_userid(api_response):
    assert "userId" in api_response.json()

def test_userid_output(api_response):
    data = api_response.json()
    assert data["id"] == 1