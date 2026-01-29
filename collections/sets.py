"""
Example
This program demonstrates how sets work in Python.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Sets in Python {"=" * 20}\n')

# Creating the initial set (duplicates are removed automatically)
my_set = {1, 2, 3, 4, 5, 4}
print(f'My set: {my_set}\n')

# Adding new elements
my_set.add(6)
my_set.add(7)

# Trying to add a duplicated element
my_set.add(3)
print(f'Set after adding new elements: {my_set}\n')

# Removing an element
my_set.remove(4)
print(f'Set after removing element 4: {my_set}\n')

# Iterating over the set
print('Iterating over the set:')
for element in my_set:
    print(element, end=' ')

# Checking if a value exists in the set
print(f'\n\nDoes the value 4 exist in my set? {4 in my_set}')

# Obtaining the length of the set
print(f'\nThe length of my set is: {len(my_set)}')

print(f'\n{"=" * 50}')
