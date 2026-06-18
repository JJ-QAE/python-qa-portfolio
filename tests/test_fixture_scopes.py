import pytest
import requests

@pytest.fixture(scope="function")
def api_function():
    print("\n>>> fixture function — before every test")
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")

@pytest.fixture(scope="session")
def api_session():
    print("\n>>> fixture session — only once")
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")

def test_function_1(api_function):
    assert api_function.status_code == 200

def test_function_2(api_function):
    assert api_function.status_code == 200

def test_session_1(api_session):
    assert api_session.status_code == 200

def test_session_2(api_session):
    assert api_session.status_code == 200