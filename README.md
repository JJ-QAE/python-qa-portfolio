# Python QA Portfolio 🐍

Automated tests written in Python, pytest and requests.
Built while learning QA Automation from scratch.

---

## 🌐 API Tests — requests + pytest

| File | What it tests |
|------|--------------|
| `tests/archive/api_test.py` | GET single post — status code, title, userId, JSON value validation |
| `tests/archive/api_test2.py` | GET single post with fixture — status code, title, userId, id value |
| `tests/archive/api_test3.py` | GET list with fixture — status code, type(), len() == 100 |
| `tests/archive/api_test4.py` | GET with parametrize — status code, title and body validation |
| `tests/archive/api_test5.py` | POST — create new resource, status 201, data validation |
| `tests/archive/api_test6.py` | conftest.py shared fixture — GET status and title |
| `tests/archive/api_test7.py` | GET + POST combined — fixture for GET, requests.post() for POST |
| `tests/archive/api_test8.py` | PUT and DELETE — update and remove existing post |
| `tests/archive/api_test9.py` | Error handling — 404 not found, wrong endpoint, empty response |
| `tests/test_api_basic.py` | Basic API tests |
| `tests/test_posts_api.py` | **Mini project** — complete API test suite: GET, POST, PUT, DELETE, 404, parametrize |
| `tests/test_users_api.py` | Users endpoint — GET, parametrize, 404 |

---

## 🧪 pytest — Advanced Features

| File | What it tests |
|------|--------------|
| `tests/test_fixture_scopes.py` | Fixture scopes — function vs session |
| `tests/test_marker.py` | Markers — @pytest.mark.skip, @pytest.mark.slow |

---

## ⚙️ Configuration

- `tests/conftest.py` — shared fixtures available across all test files
- `pytest.ini` — pytest configuration, custom file discovery, registered markers

---

## 🛠️ Tech Stack

- Python 3.12
- pytest
- requests
- JSONPlaceholder API (https://jsonplaceholder.typicode.com)

---

## 📈 Skills demonstrated

- HTTP methods: GET, POST, PUT, DELETE
- Status code validation (200, 201, 404)
- JSON structure and value validation
- pytest: assert, parametrize, fixture, raises
- Fixture scopes: function vs session
- Custom markers: skip, slow
- conftest.py shared fixtures
- Error handling and negative test cases
- Clean project structure (src/, tests/, notes/)