"""
Example of how break and continue loops work

Author: Lalo Tellez
"""

print(f'{"=" * 10} Break and Continue loops {"=" * 10}\n')

# Example with break
print('Break word')
for number in range(1,10):
    if number % 2 == 0: # Even
        print(number)
        break # Exit the program inmediatly

# Example with continue
print('\nContinue word')
for number in range(1,10):
    if number % 2 == 1:# Odd
        continue
    print(number)
print(f'\n{"=" * 45}')
