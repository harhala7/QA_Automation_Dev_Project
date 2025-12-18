from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self) -> int:
        items = self.find_all(self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self) -> list[str]:
        name_elements = self.find_all(self.CART_ITEM_NAMES)
        return [el.text for el in name_elements]

    def has_product_with_name(self, expected_name: str) -> bool:
        return expected_name in self.get_cart_item_names()
