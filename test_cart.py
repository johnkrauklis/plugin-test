import unittest

from cart import TAX_RATE, apply_member_discount, calculate_total

CART = [("Widget", 10.00, 2), ("Gadget", 25.00, 1)]  # subtotal 45.00


class CalculateTotalTest(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(calculate_total([]), 0)

    def test_no_discount_adds_tax(self):
        self.assertEqual(calculate_total(CART), 48.60)

    def test_quantity_multiplies_price(self):
        self.assertEqual(calculate_total([("Widget", 10.00, 3)]), 32.40)

    def test_discount_applied_before_tax(self):
        # Tax is charged on the discounted subtotal: 45 * 0.85 * 1.08.
        # Taxing the pre-discount subtotal would give 38.25 + 3.60 = 41.85.
        self.assertEqual(calculate_total(CART, discount_percent=15), 41.31)

    def test_full_discount_is_free(self):
        self.assertEqual(calculate_total(CART, discount_percent=100), 0)

    def test_rounds_to_cents(self):
        total = calculate_total([("Thing", 0.333, 1)])
        self.assertEqual(total, round(0.333 * (1 + TAX_RATE), 2))


class ApplyMemberDiscountTest(unittest.TestCase):
    def test_member_gets_ten_percent_before_tax(self):
        # 45 * 0.90 * 1.08. Taxing before the discount would give 44.10.
        self.assertEqual(apply_member_discount(CART), 43.74)

    def test_matches_calculate_total_with_ten_percent(self):
        self.assertEqual(
            apply_member_discount(CART), calculate_total(CART, discount_percent=10)
        )


if __name__ == "__main__":
    unittest.main()
