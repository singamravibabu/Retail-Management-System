def apply_discount(price, discount):
    """Applies discount to a product price"""
    return price - (price * discount) / 100

# Example Usage
price = 1000
discount = 10
final_price = apply_discount(price, discount)
print(f"Final price after discount: {final_price}")
print("Discount logic updatedin main branch")
print("New discount rule added in discount-feature")
print("!!!")
