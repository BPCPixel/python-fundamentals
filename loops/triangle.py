"""
Example: Printing a Message Using the Range Function

This program demonstrates how to create a symmetric triangle
using the range function and a for loop.

Author: Lalo Tellez
"""

print(f'{"=" * 10} Printing a Triangle {"=" * 10}\n')

# Ask the user for the number of rows
number_of_rows = int(input('Enter the number of rows: '))

# Generate the triangle
for row in range(1, number_of_rows + 1):
    blank_spaces = ' ' * (number_of_rows - row)
    asterisks = '*' * (2 * row - 1)
    print(f'{blank_spaces}{asterisks}')

print(f'\n{"=" * 50}')
