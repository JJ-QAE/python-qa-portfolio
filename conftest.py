import pytest
import requests

@pytest.fixture
def api_post():
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")

