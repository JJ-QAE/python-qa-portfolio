import pytest
import requests

#false answear - it fakes real one
class FakeResponse:
    status_code = 200
    def json(self):
        return {"id": 1, "title": "Fake Post", "userId": 1}

    #monkeypatch changes requests.get into a function showing FakeResponse
def test_get_post(monkeypatch):
    def fake_post(url):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_post)

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Fake Post"