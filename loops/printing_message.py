"""
Example: Printing a Message Using the Range Function

This example demonstrates how to print a message using the range function.
It shows two different ways to use a for loop with range.

Author: Lalo Tellez
"""

print(f'{"=" * 10} Print a Message with the Range Function {"=" * 10}\n')

message = input('Enter a message to repeat: ')
num_reps = int(input('Enter the number of repetitions: '))

# Iterate over the range of repetitions using the loop variable
for i in range(num_reps):
    print(f'{i + 1} - {message}')

print('\n')

# When the loop variable is not needed, it is common to use an underscore (_)
for _ in range(num_reps):
    print(message)

print(f'\n{"=" * 50}')

