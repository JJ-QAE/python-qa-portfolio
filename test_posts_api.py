import pytest
import requests

def test_posts_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_new_posts_api():
    new_post = {"title": "Test", "body": "Content", "userId": 1}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post,)
    assert response.status_code == 201
    assert response.json()["title"] == "Test"

def test_actualzie_api():
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_delete_posts_api():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/looool")
    assert response.status_code == 404

@pytest.mark.parametrize("post_id", [4, 2, 3])
def test_posts_exist(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200