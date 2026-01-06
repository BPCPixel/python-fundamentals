"""
Example of how form field validation works.
The program will continue until the user enters a value.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Form Field Validation {"=" * 20}\n')

username = None

while not username:
    username = input('Enter your username: ')

print(f'Valid username: {username}')

print(f'\n{"=" * 50}')
