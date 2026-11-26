# test_order_processor.py
from order_processor import calculate_order_total, validate_shipping_address

def test_calculate_order_total():
    items = [{"price": 10.0, "quantity": 2}, {"price": 5.0, "quantity": 1}]
    total = calculate_order_total(items, discount=2.0)
    assert total == 23.0

def test_validate_shipping_address():
    addr = {"street": "123 Main St", "city": "Springfield", "postal_code": "12345", "country": "US"}
    assert validate_shipping_address(addr) is True
