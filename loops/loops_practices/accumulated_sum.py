"""
While Loop Practice

This code calculates the addition of the first 5 numbers
using a while loop.

Author: Lalo Tellez
"""

print(f'{"=" * 15} Addition of the first 5 numbers {"=" * 15}\n')

# Constant that defines the limit of the loop
MAX_VALUE = 5

# Variables initialization
addition = 0
number = 1

while number <= MAX_VALUE:
    # Show the current operation
    print(f'(Addition + Number) -> {addition} + {number}')
    
    addition += number
    number += 1
    
    # Show the partial cumulative result
    print(f'Cumulative partial addition: {addition}\n')

# Final result output
print(f'\nThe addition of the first 5 numbers = {addition}')

print(f'\n{"=" * 60}')

