# discount.py
def apply_discount(price, discount_percent):
	"""Apply discount to a price and return the final amount."""
	discount = price * (discount_percent / 100)
	return price * discount

# Example Usage
final_price = apply_discount(1000, 10)
print(f"Final Price after discount: {final_price}")
