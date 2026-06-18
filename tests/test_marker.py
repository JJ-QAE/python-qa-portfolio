import pytest
import requests

@pytest.mark.skip(reason='APi is unavailable')
def test_skipped():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

@pytest.mark.slow
def test_slow():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/")
    assert response.status_code == 200

def test_normal():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200