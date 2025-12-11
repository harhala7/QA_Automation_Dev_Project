from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items_count(self) -> int:
        # liczymy po nazwach produktów, nie po wrapperach
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return len(elements)

    def has_product_with_name(self, expected_name: str) -> bool:
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        names = [el.text for el in elements]
        print("DEBUG CART NAMES:", names)
        return expected_name in names