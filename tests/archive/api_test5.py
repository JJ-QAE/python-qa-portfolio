import requests

def test_post_nowy():
    nowy_post = {
        "title": "Mój test",
        "body": "To jest testowy post",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=nowy_post
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"]  == "Mój test"
    assert data["userId"] == 1