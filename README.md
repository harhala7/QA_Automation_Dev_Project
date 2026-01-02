[![Selenium Tests (CI-safe)](https://github.com/harhala7/QA_Automation_Dev_Project/actions/workflows/python-tests.yml/badge.svg)](https://github.com/harhala7/QA_Automation_Dev_Project/actions/workflows/python-tests.yml)

# Selenium Test Automation – Saucedemo

UI test automation framework built with Selenium, pytest, and Page Object Model.
The project demonstrates a clean, scalable approach to browser-based test automation.

## What this project demonstrates
- Designing a Selenium automation framework from scratch
- Practical use of Page Object Model (POM)
- Separation of test logic and page logic
- Pytest fixtures and test organization
- Handling real-world UI automation challenges
- Conscious CI vs local execution decisions

## Tech stack
- Python
- Selenium WebDriver
- pytest
- webdriver-manager

## Project structure
pages/        # Page Object Model classes
tests/        # UI test cases (login, inventory, cart)
conftest.py   # Browser and test fixtures

## How to run tests locally
```bash
python -m venv venv
venv\Scripts\activate #windows
# source venv/bin/activate #Linux/MacOS

pip install -r requirements.txt
pytest -s
```

## CI vs Local execution
- Lightweight pytest tests are executed in CI
- Selenium UI tests are intended for local execution
- This avoids browser instability on shared CI runners
- Reflects common real-world QA practice

## API testing
API and contract testing are covered in a separate dedicated repository:
https://github.com/harhala7/QA_API_Contracts_Project