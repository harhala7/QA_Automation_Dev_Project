from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def click(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def wait_and_click(self, locator: tuple[By, str], timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator: tuple[By, str], text: str):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator: tuple[By, str]) -> str:
        return self.driver.find_element(*locator).text

    def is_element_visible(self, locator: tuple[By, str]) -> bool:
        return len(self.driver.find_elements(*locator)) > 0

