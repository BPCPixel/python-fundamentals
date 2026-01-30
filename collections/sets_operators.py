"""
Example
This program demonstrates how set operators work in Python.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Set Operators {"=" * 20}\n')

# Define sets a and b
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Display set values
print(f'a = {a}')
print(f'b = {b}')

# Union of a and b
union = a | b
print(f'\nUnion (a | b): {union}')

# Intersection of a and b
intersection = a & b
print(f'Intersection (a & b): {intersection}')

# Difference of a and b
difference = a - b
print(f'Difference (a - b): {difference}')

print(f'\n{"=" * 50}')
