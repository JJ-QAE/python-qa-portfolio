import pytest
import requests

@pytest.fixture
def api_lista():
    return requests.get("https://jsonplaceholder.typicode.com/posts")

def test_status_code(api_lista):
    assert api_lista.status_code == 200

def test_respones_list(api_lista):
    data = api_lista.json()
    assert type(data) == list

def test_100_elements_list(api_lista):
    data = api_lista.json()
    assert len(data) == 100