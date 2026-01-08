"""
Example
This program demonstrates basic list syntax in Python.

Author: Lalo Tellez
"""

print(f'{"=" * 20} List Example {"=" * 20}\n')

# Example 1: Showing different kinds of lists
numbers = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Cherry"]
mix = [1, "two", 3.0, [4, 5]]

# Printing the lists
print(f'Numbers -> {numbers}\n')
print(f'Fruits -> {fruits}\n')
print(f'Mix -> {mix}\n')

# Example list for basic operations
my_list = [10, 20, 30, 40, 50]
print(f'{my_list} -> Original list\n')

# Length of the list
print(f'List Length: {len(my_list)}\n')

# Accessing list items by index
print(f'Index [4]: {my_list[4]}')         # 50
print(f'Last element: {my_list[-1]}')     # 50
print(f'Penultimate element: {my_list[-2]}')  # 40

print(f'\n{"=" * 50}')
