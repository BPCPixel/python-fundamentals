"""
Example of how the form field validation works.
The instruction will continue until the user enters a value

Author: Lalo Tellez
"""

print(f'{"=" * 20} Form Field Validation {"=" * 20}\n')

name_user = None

while not name_user:
    name_user = input('Enter your username: ')

print(f'Valid Username: {name_user}')

print(f'\n\n{"=" * 50}')
