"""
This code demonstrates how to combine tuples and lists.

Author: Lalo Téllez
"""

print(f'{"=" * 10} Tuples and Lists Combinations {"=" * 10}\n')

# We define a list that contains product tuples
products = [
    ('P001', 'T-shirt', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Hoodie', 40.00)
]

# Printing product info and calculating total price
total_price = 0

print("Product Details")
for product in products:

    id_product, description, price = product
    print(f'Product: id = {id_product}, description = {description}, price = ${price:.2f}')
    total_price += price

print(f'Total price of all products: ${total_price:.2f}')

print(f'\n{"=" * 50}')
