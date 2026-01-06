"""
Range Function Examples

This program demonstrates how the range function works using three examples:
1. A sequence of numbers with default start and increment.
2. A sequence of numbers with a custom start and default increment.
3. A sequence of numbers with custom start, end, and increment values.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Range Function {"=" * 20}\n')

print('Sequence of numbers from 0 to 4')

# Start = 0 (default)
# End = 5 - 1
# Increment = 1 (default)

for i in range(5):
    print(i, end=' ')

print('\n\nSequence of numbers from 10 to 20')
# Increment = 1 (default)
for i in range(10, 21):
    print(i, end=' ')

print('\n\nSequence of numbers from 20 to 30')
# Increment = 2
for i in range(20, 31, 2):
    print(i, end=' ')

print(f'\n\n{"=" * 50}')
