"""
This code is an example of how tuple unpacking works in Python.

Author: Lalo Téllez
"""

print(f'{"=" * 20} Tuple Unpacking {"=" * 20}\n')

product = ('P001', 'Shirt', 20.00)

# Unpacking the tuple called product
product_id, description, price = product

# Printing values
print(f'Complete tuple: {product}')

# Printing individual values
print(f'\nProduct: id = {product_id}, description = {description}, price = ${price:.2f}')

print(f'\n{"=" * 50}')
