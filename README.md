# Python QA Portfolio 🐍

Automated tests written in Python, pytest and requests. Built while learning QA Automation from scratch.

## 🌐 API Tests — requests + pytest

| File                    | What it tests |
|------------------------|---------------|
| api_test.py            | GET single post — status code, title, userId, JSON value validation |
| api_test2.py           | GET single post with fixture — status code, title, userId, id value |
| api_test3.py           | GET list with fixture — status code, type(), len() == 100 |
| api_test4.py           | GET with parametrize — status code, title and body validation |
| api_test5.py           | POST — create new resource, status 201, data validation |
| api_test6.py           | conftest.py shared fixture — GET status and title |
| api_test7.py           | GET + POST combined — fixture for GET, requests.post() for POST |
| api_test8.py           | PUT and DELETE — update and remove existing post |
| api_test9.py           | Error handling — 404 not found, wrong endpoint, empty response |
| **test_posts_api.py**  | **Mini project** — complete API test suite GET POST PUT DELETE ... |

## ⚙️ Configuration

- `conftest.py` — shared fixtures available across all test files
- `pytest.ini` — pytest configuration, custom file discovery

## 🛠️ Tech Stack

- Python 3.12
- pytest
- requests
- JSONPlaceholder API[](https://jsonplaceholder.typicode.com)

## 📈 Skills demonstrated

- HTTP methods: GET, POST, PUT, DELETE
- Status code validation (200, 201, 404)
- JSON structure and value validation
- pytest: assert, parametrize, fixture, raises
- conftest.py shared fixtures
- Error handling and negative test cases
- Clean project structure
