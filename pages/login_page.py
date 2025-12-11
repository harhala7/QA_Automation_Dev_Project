from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Otwiera stronę logowania."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        """Wpisuje dane i klika Login."""
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.clear()
        password_input.clear()

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def is_on_inventory_page(self) -> bool:
        """Sprawdza, czy jesteśmy na stronie z produktami."""
        return "inventory" in self.driver.current_url
