def test_variables_and_types():
    username = "standard_user"
    age = 25
    height = 1.88
    is_logged_in = False

    print(username, type(username))
    print(age, type(age))
    print(height, type(height))
    print(is_logged_in, type(is_logged_in))

    assert isinstance(username, str)
    assert isinstance(age, int)
    assert isinstance(height, float)
    assert isinstance(is_logged_in, bool)
def test_product_price_math():
    price = 19.99
    quantity = 3
    total = price * quantity

    print("Total:", total)
    assert total == 59.97
def test_discount_price_rounding():
    price = 49.99
    discount_percent = 0.15  # 15% zniżki

    discounted_price = price * (1 - discount_percent)

    print("Discounted price:", discounted_price)

    assert round(discounted_price, 2) == 42.49
