def test_all_prices_positive():
    prices = [4.99, 12.50, 1.00, 7.75]

    for price in prices:
        if price <= 0:
            assert False, f"Price {price} is invalid"

def test_all_products_have_names():
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    
    for product in products:
        if product == "":
            assert False, "product name is missing"
