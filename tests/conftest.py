import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

# Ensure project root is on PYTHONPATH so "import pages" works from anywhere
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

@pytest.fixture
def driver():
    options = Options()

    # Stabilność, mniej popupów
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    # Wyłącza password manager i service od credentials (to robiło Ci popup i blokowało klik)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Jeśli kiedyś będziesz odpalał CI headless, dodasz:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)  # ważne: nie mieszamy implicit z explicit wait
    yield driver
    driver.quit()
