from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By



def test_open_saucedemo_homepage():
    # uruchom Chrome przez webdriver_manager (nie musisz ręcznie ściągać drivera)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # otwórz stronę SauceDemo
        driver.get("https://www.saucedemo.com/")

        # prosta asercja - tytuł strony powinien zawierać "Swag Labs"
        assert "Swag Labs" in driver.title

        # chwila pauzy, żebyś zobaczył stronę, zanim okno się zamknie
        time.sleep(3)
    finally:
        # zawsze zamknij przeglądarkę
        driver.quit()
def test_valid_login_navigates_to_inventory_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://www.saucedemo.com/")

        # znajdź pola login i hasło
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # wprowadź poprawne dane logowania
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # prosta asercja: po poprawnym logowaniu URL zawiera "inventory"
        assert "inventory" in driver.current_url
    finally:
        driver.quit()
