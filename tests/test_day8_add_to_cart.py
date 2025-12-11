import time
from pages.login_page_v2 import LoginPageV2
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_backpack_to_cart(driver):
    login_page = LoginPageV2(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # krok 1: logowanie
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_on_inventory_page()

    # krok 2: dodanie produktu do koszyka
    inventory_page.add_backpack_to_cart()
    time.sleep(2)

    # krok 3: przejście do koszyka
    inventory_page.go_to_cart()
    time.sleep(2)

    # krok 4: asercja w koszyku - TYLKO TA
    assert cart_page.has_product_with_name("Sauce Labs Backpack")
