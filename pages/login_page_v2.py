from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageV2(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_TITLE = (By.CLASS_NAME, "title")

    def open(self):
        self.open_url(self.URL)

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_on_inventory_page(self) -> bool:
        return self.is_element_visible(self.INVENTORY_TITLE)
