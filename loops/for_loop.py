"""
For Loop Example

This program demonstrates how a for loop works
by iterating over the letters of a string
and the elements of a fruit list.

Author: Lalo Tellez
"""

print(f'{"=" * 20} For Loop Example {"=" * 20}\n')

# Example 1: Iterate a string

print('Iterate the letters of a string')

# Declare a string to iterate
string_word = 'Hello World'

# The characters are iterated one by one
for letter in string_word:
    print(letter, end=' ')

# Example 2: Iterate a list

print('\n\nIterate the fruits of a fruit list')

# Declare a list to iterate
fruits = ['Banana', 'Apple', 'Orange']

# The list elements are iterated
for fruit in fruits:
    print(fruit, end=' ')

print(f'\n\n{"=" * 50}')
