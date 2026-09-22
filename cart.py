"""A tiny shopping cart calculator. Deliberately small and deliberately flawed —
used to test a two-person doc/review workflow, not as real code to admire."""

TAX_RATE = 0.08


def calculate_total(items, discount_percent=0):
    """items: list of (name, price, quantity). Returns the final charge."""
    subtotal = 0
    for name, price, quantity in items:
        subtotal += price * quantity

    discount_amount = subtotal * (discount_percent / 100)
    discounted_subtotal = subtotal - discount_amount
    tax = discounted_subtotal * TAX_RATE
    total = discounted_subtotal + tax

    return round(total, 2)


def apply_member_discount(items):
    """Members get 10% off."""
    return calculate_total(items, discount_percent=10)


if __name__ == "__main__":
    cart = [("Widget", 10.00, 2), ("Gadget", 25.00, 1)]
    print("Regular total:", calculate_total(cart))
    print("With 15% off:", calculate_total(cart, discount_percent=15))
    print("Member total:", apply_member_discount(cart))
