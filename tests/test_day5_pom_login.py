from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_valid_login_navigates_to_inventory_page():
    # setup driver – później przeniesiemy to do fixture
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login_page = LoginPage(driver)

    try:
        # używamy POM zamiast klepać selektory w teście
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_on_inventory_page()
    finally:
        driver.quit()
