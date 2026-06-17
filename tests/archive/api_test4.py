import pytest
import requests


@pytest.mark.parametrize("post_id", [1,2,3])
def test_posty_istnieja(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    assert "title" in response.json()
    assert "body" in response.json()