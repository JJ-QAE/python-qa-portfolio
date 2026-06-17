import pytest
import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert len(response.json()) > 5

@pytest.mark.parametrize("id", [1, 2, 3])
def test_users_exist(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    assert response.status_code == 200

def test_user_not_there():
    response = requests.get("https://jsonplaceholder.typicode.com/users/lolabunny")
    assert response.status_code == 404