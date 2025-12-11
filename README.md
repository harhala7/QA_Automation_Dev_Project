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