"""
Customer order and access system



Author: Lalo Tellez
"""

import random

print(f'{"=" * 20} Customer Order System {"=" * 20}\n')

print(f'{"-"*10} Registration {"-"*10}\n')
full_name = input('Enter your full name: ')
domain = '@email.com.mx'
random_ID = str(random.randint(0,9999)).zfill(4)
EMAIL = full_name.strip().lower().replace(' ','.') + '.' +random_ID + domain

adult_user = None
while adult_user == None:
    age = int(input('Enter your age: '))
    if 100 >= age >= 18:
        adult_user = True
    elif 18 > age > 0:
        adult_user = False

    if adult_user is None:
        print("\nInvalid age")
        try_again = input('Do you want to try again (Y/N)? ').strip().upper()
        if try_again == 'N':
            adult_user = False
    elif adult_user is False:
        print("\nYou must be over 18 to register in the the system\n")
        adult_user = True
    else:
        # Create a Password for the user
        print('\nYour email is being generated...')
        PASSWORD = input('Create a password to access the system: ')
        print(f'''\nSuccessful registration!
\nWelcome {full_name.title()}\n
New E-mail: [{EMAIL}]
New Password: [{PASSWORD}]
{"-"*35}\n''') 

print("Exiting the system")
print(f'\n{"=" * 50}')