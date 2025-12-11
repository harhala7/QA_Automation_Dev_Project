from pages.login_page_v2 import LoginPageV2
from pages.inventory_page import InventoryPage


def test_inventory_products_visible(driver):
    login_page = LoginPageV2(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_on_inventory_page()
    assert inventory_page.get_products_count() > 0
