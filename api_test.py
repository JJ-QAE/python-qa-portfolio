import requests

def test_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_odpowiedz_ma_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert "title" in data

def test_userid():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert "userId" in data

def test_userid_output():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1