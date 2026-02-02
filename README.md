#  Python UI Automation Framework (Pytest + Selenium)

This repository documents my hands-on journey into **UI automation testing using Python, Pytest, and Selenium**.
It is not just a collection of scripts — it is a **learning-first automation framework** built step by step with real problems, failures, fixes, and improvements.

The goal of this project is simple:

> Build a clean, maintainable, and scalable UI automation framework the way it is done in real-world QA / SDET teams.

---

##  What this project demonstrates

* Page Object Model (POM) from scratch
* Pytest-based test structure
* Clean separation of tests and page logic
* Reusable fixtures using `conftest.py`
* Headless and non-headless browser execution
* Test categorization using Pytest markers
* Handling flaky / unstable UI tests safely
* Debugging real Selenium issues (timeouts, locators, waits)

This repo reflects **practical learning**, not tutorial copy-paste.

---

## Project Structure

```
Python_Foundation/
│
├── src/
│   ├── pages/                # Page Object classes
│   │   ├── login_page.py
│   │   ├── checkbox_page.py
│   │   ├── dynamic_loading_page.py
│   │   └── google_home_page.py
│   │
│   ├── selenium_basics/       # Browser setup & helpers
│   └── utils/                 # Utility functions
│
├── tests/
│   ├── ui/                    # UI test cases
│   │   ├── test_login_positive.py
│   │   ├── test_login_negative.py
│   │   ├── test_checkboxes.py
│   │   ├── test_dynamic_loading.py
│   │   └── test_dynamic_loading_content.py
│   │
│   └── conftest.py            # Shared Pytest fixtures
│
├── pytest.ini                 # Pytest configuration & markers
├── requirements.txt           # Dependencies
├── README.md
└── .gitignore
```

---

##  Architecture Overview

### Page Object Model (POM)

* Each page has **one responsibility**
* Locators stay inside page classes
* Tests never directly touch Selenium locators
* UI changes require updates in **one place only**

Example (conceptual):

* `LoginPage` → knows *how* to login
* Test → knows *what* to verify

---

##  How to Run the Tests

### 1️ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️ Run all tests

```bash
pytest -v
```

### 3️ Run only smoke tests

```bash
pytest -m smoke -v
```

### 4️ Run regression suite

```bash
pytest -m regression -v
```

---

##  Pytest Markers Used

Markers help control execution and prevent unstable tests from blocking progress.

```ini
smoke       → critical core flows
regression  → full test suite
flaky       → unstable UI tests (kept for learning)
```

Example usage:

```python
@pytest.mark.smoke
def test_valid_login():
    ...
```

---

##  Headless Execution

The framework supports **headless Chrome execution** using an environment variable.

### Normal mode (browser visible)

```bash
pytest -v
```

### Headless mode

**PowerShell:**

```powershell
$env:HEADLESS="true"
pytest -v
```

**Linux / macOS:**

```bash
HEADLESS=true pytest -v
```

This is handled centrally inside `conftest.py`.

---

##  Handling Unstable Tests

Some UI flows (e.g. Google Images) are intentionally **kept but skipped**:

```python
@pytest.mark.skip(reason="Google UI is unstable – kept for learning")
```

Why?

* Shows real-world flakiness
* Demonstrates responsible test management
* Prevents CI noise

---

##  What I Learned Building This

* Why Page Objects matter long-term
* How small design mistakes cause test flakiness
* How Pytest collection works
* Why explicit waits beat sleep
* Why not every test should block the pipeline
* How real automation frameworks evolve over time

---

##  Future Improvements

Planned next steps:

* GitHub Actions CI pipeline
* HTML test reports
* Better wait abstractions
* Data-driven tests
* Cross-browser execution

---

##  Final Note

This repository represents **growth**, not perfection.

Every failure, fix, and refactor here reflects how automation is actually learned and built in real projects.

If you are learning Selenium + Pytest and want a **clean, honest reference**, this repo is for you.
