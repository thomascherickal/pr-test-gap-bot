from shop.pricing import subtotal


def test_subtotal_sums_prices():
    assert subtotal([1.10, 2.20]) == 3.30
