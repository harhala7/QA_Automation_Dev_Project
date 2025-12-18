from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Sauce Labs Backpack button
    BACKPACK_ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # inventory items list
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def get_cart_badge_count(self) -> int:
        if not self.is_visible(self.CART_BADGE):
            return 0
        text = self.get_text(self.CART_BADGE)
        return int(text)

    def get_products_count(self) -> int:
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))