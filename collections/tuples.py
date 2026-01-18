"""
This code explains how tuples work in Python.

Author: Lalo Téllez
"""

print(f'{"=" * 20} Tuples in Python {"=" * 20}\n')

# Simple tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Tuples are immutable

# Iterating through the tuple elements
for element in my_tuple:
    print(element, end=' ')

# Creating a tuple to represent a coordinate
coordinate = (3, 5)

# Accessing elements of the tuple
print(f'\nCoordinates = {coordinate}')
print(f'Coordinate on the x-axis = {coordinate[0]}')
print(f'Coordinate on the y-axis = {coordinate[1]}')

# Creating a single-element tuple
element_tuple = (10,)
print(f'Single-element tuple: {element_tuple}')

# Nested tuples
nested_tuples = (1, (2, 3), (4, 5))
print(f'\nNested tuples: {nested_tuples}')
print(f'Second element in the nested structure: {nested_tuples[1]}')

print(f'\n{"=" * 50}')
