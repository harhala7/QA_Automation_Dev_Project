from pages.login_page_v2 import LoginPageV2
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_backpack_to_cart(driver):
    login_page = LoginPageV2(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # logowanie
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_on_inventory_page()

    # dodanie produktu
    inventory_page.add_backpack_to_cart()

    # szybka asercja na badge, potwierdza że klik faktycznie zadziałał
    assert inventory_page.get_cart_badge_count() == 1

    # przejście do koszyka
    inventory_page.go_to_cart()

    # asercja po nazwie
    assert cart_page.has_product_with_name("Sauce Labs Backpack")
