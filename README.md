# Python Foundation for Testing (SDET Journey)

This repository documents my hands-on journey from Python fundamentals to becoming a full-fledged **SDET (Software Development Engineer in Test)**. It is intentionally built step by step, focusing on *how real testing frameworks grow over time*, not just on writing passing tests.

The project covers **UI automation, API testing, performance basics, flaky test analysis, and test strategy**, all structured in a scalable and production-style layout.

---

## Why this repository exists

This is not a demo project.

This repository exists to:

* Practice **real SDET workflows**, not shortcuts
* Understand *why* frameworks are structured the way they are
* Build confidence in debugging, refactoring, and scaling test suites
* Simulate how testing evolves in real companies

Every failure, refactor, and design decision here is intentional and educational.

---

## Project Structure (High-Level)

```
Python_Foundation
│
├── src/
│   ├── api/                # API clients and API-level logic
│   │   ├── base_client.py  # Reusable HTTP client (requests wrapper)
│   │   ├── auth_api.py     # Authentication-related API actions
│   │   └── __init__.py
│   │
│   ├── pages/              # Page Object Model (UI automation)
│   │   ├── login_page.py
│   │   ├── dynamic_loading_page.py
│   │   ├── checkbox_page.py
│   │   └── google_home_page.py
│   │
│   ├── selenium_basics/    # Early Selenium learning experiments
│   └── utils/              # Shared helpers (strings, math, etc.)
│
├── tests/
│   ├── ui/                 # UI test cases (pytest + Selenium)
│   ├── api/                # API test cases (pytest + requests)
│   ├── performance/        # Performance & timing-related tests
│   └── test_strategy/      # Test design, notes, and strategy docs
│
├── conftest.py              # Shared pytest fixtures (browser, config)
├── pytest.ini               # Pytest config + markers
├── requirements.txt         # All dependencies
├── README.md                # You are here
└── .gitignore
```

---

## Core Testing Areas Covered

### 1. UI Automation (Selenium + Pytest)

* Page Object Model (POM)
* Explicit waits and synchronization
* Positive and negative test scenarios
* Marker-based execution (`smoke`, `regression`)
* Handling unstable UI tests (skipped/flaky tests)

Example scenarios:

* Login (positive & negative)
* Dynamic content loading
* Checkbox interactions
* Google Images exploration (kept for learning, marked unstable)

---

### 2. API Testing (Requests + Pytest)

This is where the project transitions from **tester** to **SDET**.

Key ideas:

* API tests do not depend on UI
* Logic is reusable and layered
* Failures are faster and more reliable

Design approach:

* `BaseAPIClient` handles:

  * HTTP methods (GET, POST, PUT, DELETE)
  * Headers
  * Timeouts
  * Response handling
* Feature-specific APIs (e.g. `auth_api.py`) extend this base

Planned API test coverage:

* Authentication success & failure
* Invalid payload handling
* Status code validation
* Schema / response structure checks
* Token-based flows

---

### 3. Performance & Stability Testing (Intro Level)

This section focuses on **test behavior**, not load testing tools yet.

Includes:

* Response time assertions
* Slow endpoint detection
* Identifying flaky tests
* Marking unstable tests intentionally

This mirrors how performance awareness starts in real QA teams.

---

### 4. Flaky Test Analysis

Instead of hiding flaky tests, this repo:

* Keeps them
* Marks them
* Documents why they are flaky

This teaches:

* When to fix
* When to quarantine
* When to skip with intent

---

### 5. Test Strategy & Design Thinking

The `test_strategy/` section focuses on *thinking like an SDET*:

* Why a test exists
* What risk it covers
* What layer it belongs to (UI vs API)
* When not to automate

This is where testing becomes engineering.

---

## Tooling & Tech Stack

* **Python 3.14+**
* **Pytest** – test framework
* **Selenium** – UI automation
* **Requests** – API testing
* **Git & GitHub** – version control
* **Virtual Environments** – dependency isolation

---

## How to Run the Project

### Setup

```
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Run all tests

```
pytest -v
```

### Run only smoke tests

```
pytest -m smoke -v
```

### Run headless (CI-style)

```
set HEADLESS=true
pytest -v
```

---

## Philosophy Behind This Repo

This repository is intentionally:

* Incremental
* Sometimes messy
* Frequently refactored

Because **real SDET work is exactly like that**.

The goal is not perfection.
The goal is *understanding, ownership, and growth*.

---

## Roadmap Ahead

* Expand API test suites (5+ tests per scenario)
* Add response schema validation
* Introduce basic mocking concepts
* Improve reporting
* Prepare CI integration

---

If you are reading this as a future version of me:

This is where the journey stopped being about tests —
and started being about engineering.
