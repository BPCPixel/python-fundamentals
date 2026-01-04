"""
Practice: Password creation and validation

This program validates a password entered by the user.
The password must have at least 6 characters.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Password creation and validation {"=" * 20}\n')

password = input('Type a password (minimum 6 characters): ')

while len(password) < 6:
    print('Invalid password. It must have at least 6 characters.\n')
    password = input('Type a password (minimum 6 characters): ')
else:
    print('\nValid password')

print(f'\n{"=" * 50}')
