import requests

def test_response(api_post):
    assert api_post.status_code == 200

def test_content(api_post):
    assert "title" in api_post.json()

def test_post_id(api_post):
    assert "id" in api_post.json()
    assert api_post.status_code == 200

def test_nowy_post():
    nowy_post = {
        "title": "Mój test",
        "body": "flawless one",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=nowy_post
    )
    assert response.status_code == 201
    assert response.json() ["title"] == "Mój test"