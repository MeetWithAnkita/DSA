# Task: Write Python code to:
# 1. Sort products by price in ascending order.
# 2. Sort products by price in descending order.

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]
a = sorted(products, key = lambda x: x["price"])
b = sorted(products, key = lambda x: x["price"], reverse = True)

print(a)
print(b)

