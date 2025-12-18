from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageV2(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_on_inventory_page(self) -> bool:
        return self.wait_for_url_contains("inventory.html")
