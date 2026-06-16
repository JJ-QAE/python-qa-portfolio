import requests

def test_404():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/99999"
    )
    assert response.status_code == 404

def test_wrong_endpoint():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/deosntexsist"
    )
    assert response.status_code == 404

def test_blank_response():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/deosntexsist"
    )
    assert response.status_code == 404
    assert response.json() == {}

