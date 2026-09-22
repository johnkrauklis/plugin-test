"""A tiny shopping cart calculator. Deliberately small and deliberately flawed —
used to test a two-person doc/review workflow, not as real code to admire."""

TAX_RATE = 0.08


def calculate_total(items, discount_percent=0):
    """items: list of (name, price, quantity). Returns the final charge."""
    subtotal = 0
    for name, price, quantity in items:
        subtotal += price * quantity

    # BUG: tax is calculated on the pre-discount subtotal, then the discount
    # is applied to the taxed amount. Customers get taxed on money they
    # never actually spent. Should discount first, then tax.
    tax = subtotal * TAX_RATE
    total_with_tax = subtotal + tax
    discount_amount = total_with_tax * (discount_percent / 100)
    total = total_with_tax - discount_amount

    return round(total, 2)


def apply_member_discount(items):
    """Members get 10% off."""
    return calculate_total(items, discount_percent=10)


if __name__ == "__main__":
    cart = [("Widget", 10.00, 2), ("Gadget", 25.00, 1)]
    print("Regular total:", calculate_total(cart))
    print("With 15% off:", calculate_total(cart, discount_percent=15))
    print("Member total:", apply_member_discount(cart))
