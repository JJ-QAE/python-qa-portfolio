# Python QA Portfolio 🐍

Automated tests written in Python using **pytest** and **requests**.  
Built while learning QA Automation from scratch.

## 📋 Project Overview

This repository contains my practice projects and exercises focused on **test automation** with Python and pytest.

### API Testing (using JSONPlaceholder)

| File                        | Description |
|----------------------------|-------------|
| `test_api_basic.py`        | Basic GET and POST tests |
| `test_posts_api.py`        | **Complete API test suite** – GET, POST, PUT, DELETE, error handling, parametrized tests |
| `test_users_api.py`        | Tests for users endpoint |
| `conftest.py`              | Shared fixtures for all tests |
| `archive/`                 | Previous versions of tests (learning history) |

### Other
- `src/kalkulator.py` – Simple calculator with unit tests

## 🛠️ Tech Stack

* Python 3.12
* pytest
* requests
* JSONPlaceholder


## 📈 Skills Demonstrated

- HTTP methods: GET, POST, PUT, DELETE
- Status code validation (200, 201, 404, etc.)
- JSON response structure and value validation
- pytest fixtures and `conftest.py`
- Parametrized tests (`@pytest.mark.parametrize`)
- Negative testing & error handling
- Clean project structure and organization


## ⚙️ How to Run Tests

```bash
# Install dependencies (if you create requirements.txt)
pip install -r requirements.txt

# Run all tests
pytest

# Run with verbose output
pytest -v --tb=short

# Run only API tests
pytest tests/ -k "api" -v

# Run with HTML report
pytest --html=report.html --self-contained-html