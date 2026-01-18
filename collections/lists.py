"""
Example
This program demonstrates basic list syntax and common list operations in Python.

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
print(f'Index [4]: {my_list[4]}')          # 50
print(f'Last element: {my_list[-1]}')      # 50
print(f'Penultimate element: {my_list[-2]}')  # 40

# Modifying list elements
my_list[1] = 200
print(f'\nElement at index [1] was modified: {my_list[1]}\n')

# Add a new element at the end of the list using append()
my_list.append(60)
print(f'{my_list} -> Element [60] was added at the end of the list\n')

# Add a new element at a specific index using insert()
my_list.insert(2, 150)
print(f'Element {my_list[2]} was added at index 2')
print(my_list)

# Remove list elements using remove method
my_list.remove(50)
print('\nRemove Method')
print(f'{my_list} -> 5 value was removed')

# Remove element by index with pop method
my_list.pop(1)
print('\nRemove index[1] with pop method')
print(f'{my_list} index [1] was removed')

# Remove element using word "del"
del my_list[2]
print('\nRemove index[2] with word "del"')
print(f'{my_list} index [2] was removed')

# Obtaining sublists
sublist = my_list[1:3] # 1 and 2
print(f'\nSublist[1:3]: {sublist}')

print(f'\n{"=" * 50}')
