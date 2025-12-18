# This program shows how the function random works

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f'Random number between 1 and 10: {random_number}')

# Simulate a 6-sided die
die_roll = random.randint(1, 6)
print(f'Result of rolling a die: {die_roll}')
