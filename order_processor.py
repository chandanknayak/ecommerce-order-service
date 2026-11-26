# order_processor.py

def calculate_order_total(items: list[dict], discount: float = 0.0) -> float:
    """Calculate the final order total including item pricing and discount."""
    subtotal = sum(item.get("price", 0.0) * item.get("quantity", 1) for item in items)
    final_amount = max(0.0, subtotal - discount)
    return round(final_amount, 2)

def validate_shipping_address(address: dict) -> bool:
    """Ensure required address fields are present."""
    required = ["street", "city", "postal_code", "country"]
    return all(bool(address.get(f)) for f in required)
