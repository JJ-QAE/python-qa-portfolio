# Python QA Portfolio 🐍

Automated tests written in Python, pytest and requests.
Built while learning QA Automation from scratch.

---

## 🧪 pytest — Unit Tests

| File | What it tests |
|------|--------------|
| `kalkulator.py` + `test_kalkulator.py` | Math functions with parametrize and fixtures |
| `api_test4.py` | BMI calculator — parametrize, raises, basic assert |
| `api_test5.py` | pytest fixture with dictionary |

---

## 🌐 API Tests — requests + pytest

| File | What it tests |
|------|--------------|
| `api_test2.py` | GET single post — status code, JSON structure |
| `api_test3.py` | GET list — type(), len() validation |
| `api_test4.py` | GET with parametrize — multiple endpoints |
| `api_test5.py` | POST — create new resource, status 201 |
| `api_test6.py` | conftest.py — shared fixture across files |
| `api_test7.py` | GET + POST combined in one file |
| `api_test8.py` | PUT and DELETE |
| `api_test9.py` | Error handling — 404, wrong endpoint, empty response |
| `test_posts_api.py` | **Mini project** — complete API test suite |

---

## ⚙️ Configuration

- `conftest.py` — shared fixtures available across all test files
- `pytest.ini` — pytest configuration, custom file discovery

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
- JSON structure validation
- pytest: assert, parametrize, fixture, raises
- conftest.py shared fixtures
- Error handling and negative test cases
