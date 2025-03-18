def generate_bill(items):
    """Calculate total bill from a list items (price list)"""
    return sum(items)


# Prices of items
items = [100, 200, 150] 
total = generate_bill(items)
print(f"Total bill amount: `{total}`")
