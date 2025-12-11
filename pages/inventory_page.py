from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    BACKPACK_ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")

    def get_products_count(self) -> int:
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        self.wait_and_click(self.BACKPACK_ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_ICON)
