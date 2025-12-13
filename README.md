QA Automation Dev Project – Saucedemo
Python + Selenium + pytest + Page Object Model (POM)

This project was created as part of my personal “QA Automation Upgrade” study program.
The goal was to build a clean, scalable, and fully working test automation framework for the demo e-commerce site saucedemo.com
 using:

Python 3.13+

Selenium WebDriver

pytest

webdriver-manager

Page Object Model (POM) architecture

🔧 Tech Stack
Component	Description
Python 3.13+  -	Main programming language
pytest  -	Test runner with fixtures and reports
Selenium WebDriver  -	Browser automation
webdriver-manager  -	Automatic ChromeDriver handling
POM (Page Object Model)  -	Clean and scalable project design

Project Structure

QA_Automation_Dev_Project/
│
├── pages/                     # Page Object Model classes
│   ├── base_page.py          # Base methods (click, type, waits)
│   ├── login_page_v2.py      # Improved login page
│   ├── inventory_page.py     # Products page interactions
│   └── cart_page.py          # Shopping cart methods
│
├── tests/
│   ├── test_day2_basics.py
│   ├── test_day3_basics.py
│   ├── test_day4_selenium_login.py
│   ├── test_day5_pom_login.py
│   ├── test_day7_inventory_page.py
│   └── test_day8_add_to_cart.py
│
├── conftest.py               # Browser fixture
├── requirements.txt
└── README.md

How to Run Tests

1.Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

2.Install dependencies:

pip install -r requirements.txt

3.Run all tests:

pytest -s

or run a specific test file:

pytest -s tests/test_day5_pom_login.py


Implemented Test Cases

✔ Basic Python tests
✔ Basic pytest assertions
✔ Selenium login test
✔ POM login test
✔ Reading product list from inventory
✔ (Work in progress) add-to-cart tests

Notes

This project is actively evolving as part of my QA Automation learning path.
Future improvements will include:

Allure reports

Retry plugin

Better waits

Class-level fixtures

CI/CD integration with GitHub Actions

Contact

If you want to see more of my work or collaborate, feel free to reach out through GitHub.

## Notes on CI vs Local Execution

This project contains two categories of tests:

### 1. Lightweight pytest tests (CI-friendly)
Basic Python and pytest tests (e.g. sanity checks and fundamentals)  
are executed automatically in **GitHub Actions**.

These tests do not require a browser and are intentionally used in CI
to ensure fast and stable pipeline execution.

### 2. Selenium WebDriver tests (local execution)
End-to-end browser tests (login, inventory, add-to-cart) are designed
to be executed **locally**.

Running Selenium tests in CI was intentionally avoided due to:
- browser and driver dependencies,
- environment instability on headless runners,
- Chrome security / password manager pop-ups affecting reliability.

This reflects real-world practice where UI E2E tests are often separated
from fast CI pipelines and executed in dedicated environments.

##  What This Project Demonstrates

- Ability to design a Selenium automation framework from scratch
- Practical use of Page Object Model (POM)
- Clean separation of test logic and page logic
- Pytest fixtures and test organization
- Debugging and handling real-world automation issues
- Conscious CI design decisions (speed vs stability trade-offs)