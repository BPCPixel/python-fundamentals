"""
Practice: Guessing Game

This program simulates a guessing game where the user must guess
a randomly generated number within a limited number of attempts.

Author: Lalo Tellez
"""

import random

print(f'{"=" * 20} Guessing Game {"=" * 20}')

# Constants
MYSTERY_NUMBER = random.randint(1, 100)
MAX_ATTEMPTS = 5

# Control variables
attempts = 0
guess = None

print('Guess the correct number from 1 to 100')

while guess != MYSTERY_NUMBER and attempts < MAX_ATTEMPTS:
    guess = int(input('Number: '))
    attempts += 1

    if guess < MYSTERY_NUMBER:
        print('Greater...\n')
    elif guess > MYSTERY_NUMBER:
        print('Smaller...\n')

# Game result
if guess == MYSTERY_NUMBER:
    print(f'\nYOU WIN! Attempts used: {attempts}\n')
else:
    print(f'\nYOU LOSE. Attempts used: {attempts}')
    print(f'The mystery number was: {MYSTERY_NUMBER}\n')

print(f'{"=" * 55}')
