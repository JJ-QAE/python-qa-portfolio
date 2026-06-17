import requests

def test_put_post():
    zakutalizowany_post = {
        "title": "zaktualizowany tytuł",
        "body": "nowa treść",
        "user_id": 1
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=zakutalizowany_post
    )
    assert response.status_code == 200
    assert response.json()["title"] == "zaktualizowany tytuł"

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1",
    )
    assert response.status_code == 200