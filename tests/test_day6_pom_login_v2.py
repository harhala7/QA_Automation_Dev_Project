from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page_v2 import LoginPageV2


def test_valid_login_navigates_to_inventory_page_v2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login_page = LoginPageV2(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_on_inventory_page()
    finally:
        driver.quit()
