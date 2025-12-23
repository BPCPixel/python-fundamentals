# This program simulates a VIP discount system
# A supermarket offers a special discount to clients who buy 10 or more products
# AND are members of the store

print(f'{"=" * 20} VIP Discount System {"=" * 20}')

# Discount condition
min_products_for_discount = 10

# User input
quantity_products = int(input("How many products did you buy today? "))
membership = input("Do you have a store membership? (Y/N): ")

# Logical evaluation
eligible_for_discount = (quantity_products >= min_products_for_discount and membership.strip().upper() == "Y")

# Result
print(f'Do you have access to the VIP discount? {eligible_for_discount}')

print(f'{"=" * 60}')
