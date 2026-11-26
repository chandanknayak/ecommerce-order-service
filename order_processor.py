# order_processor.py

# BREAKING SIGNATURE: renamed parameters, removed discount argument!
def calculate_order_total(cart_items: list[dict]) -> float:
    """Breaking change: signature completely modified without backward compatibility."""
    return sum(item.get("price", 0.0) * item.get("quantity", 1) for item in cart_items)

def validate_shipping_address(address: dict) -> bool:
    required = ["street", "city", "postal_code", "country"]
    return all(bool(address.get(f)) for f in required)
