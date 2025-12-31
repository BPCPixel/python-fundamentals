"""
Customer Order and Access System

This is a practice program where the user can register in a Customer Order System.
The system validates age, generates an email, allows login, and simulates a purchase flow.

Author: Lalo Tellez
"""

import random

# CONSTANTS


EMAIL_DOMAIN = '@email.com.mx'
MIN_AGE = 18
MAX_AGE = 100

# Prices
TAX = 0.16
PRICE_TSHIRT = 20
PRICE_PANTS = 30
PRICE_SHOES = 40
PRICE_TENNIS = 50

# Discount
BULK_PURCHASE_DISCOUNT = 0.10

# SYSTEM HEADER

print(f'{"=" * 20} Customer Order System {"=" * 20}\n')

# REGISTRATION

print(f'{"-" * 10} Registration {"-" * 10}\n')

full_name = input('Enter your full name: ')

# Generate random ID for email
random_id = str(random.randint(0, 9999)).zfill(4)

# Generate email automatically
EMAIL = (full_name.strip().lower().replace(' ', '.') + '.' + random_id + EMAIL_DOMAIN)

# AGE VALIDATION

access_to_system = None

while access_to_system is None:
    age = int(input('Enter your age: '))

    if MAX_AGE >= age >= MIN_AGE:
        access_to_system = True
    elif MIN_AGE > age > 0:
        access_to_system = False

    if access_to_system is None:
        print('\nInvalid age')
        try_again = input('Do you want to try again (Y/N)? ').strip().upper()
        if try_again == 'N':
            access_to_system = False

    elif access_to_system is False:
        print('\nYou must be over 18 to register in the system\n')
        access_to_system = True

    else:
      
        # PASSWORD CREATION
       
        print('\nYour email is being generated...')
        PASSWORD = input('Create a password to access the system: ')

        print(f'''
Successful registration!

Welcome {full_name.title()}

New E-mail: [{EMAIL}]
New Password: [{PASSWORD}]
{"-" * 35}
''')

        # LOGIN

        print(f'{"-" * 5} Access to the system {"-" * 5}\n')

        access_to_purchase_summary = None

        while access_to_purchase_summary is None:
            input_email = input('Email: ')
            input_password = input('Password: ')

            valid_email = input_email == EMAIL
            valid_password = input_password == PASSWORD

            if not valid_email and not valid_password:
                print('\nIncorrect Email and Password')
            elif not valid_email:
                print('\nIncorrect Email')
            elif not valid_password:
                print('\nIncorrect Password')
            else:
                access_to_purchase_summary = True
                break

            try_again = input('Do you want to try again (Y/N)? ').strip().upper()
            if try_again == 'N':
                access_to_purchase_summary = False

        # PURCHASE SYSTEM
        
        if access_to_purchase_summary:
            purchase = None
            subtotal = 0
            total_items = 0

            # Counters
            tshirt_counter = 0
            pants_counter = 0
            shoes_counter = 0
            tennis_counter = 0

            discount_applied = False
            subtotal_discount = 0

            while purchase is None:
                print(f'''
{"-" * 35}

{"-" * 5} Purchase Menu {"-" * 5}

(1) T-SHIRT = $20
(2) PANTS = $30
(3) SHOES = $40
(4) TENNIS = $50
(5) EXIT

Subtotal: ${subtotal}
''')

                number_product = int(input('Enter the number of the product to buy it: '))

                if number_product == 5:
                    purchase = False

                elif number_product == 4:
                    tennis_counter += 1
                    total_items += 1
                    subtotal += PRICE_TENNIS
                    print(f'Number of tennis bought: {tennis_counter}')

                elif number_product == 3:
                    shoes_counter += 1
                    total_items += 1
                    subtotal += PRICE_SHOES
                    print(f'Number of shoes bought: {shoes_counter}')

                elif number_product == 2:
                    pants_counter += 1
                    total_items += 1
                    subtotal += PRICE_PANTS
                    print(f'Number of pants bought: {pants_counter}')

                elif number_product == 1:
                    tshirt_counter += 1
                    total_items += 1
                    subtotal += PRICE_TSHIRT
                    print(f'Number of t-shirts bought: {tshirt_counter}')

                else:
                    print('\nInvalid number, try again')

            # SUMMARY

            if total_items > 3:
                subtotal_discount = subtotal - (subtotal * BULK_PURCHASE_DISCOUNT)
                discount_applied = True
            else:
                subtotal_discount = subtotal

            total = subtotal_discount + (subtotal_discount * TAX)

            print(f'''
{"-" * 10} Purchase Summary {"-" * 10}

Products purchased: {total_items}
Subtotal: ${subtotal:.2f}

Discount applied (more than 3 items): {discount_applied}
Subtotal with discount: ${subtotal_discount:.2f}

Tax (16%): ${(subtotal_discount * TAX):.2f}
Total amount to pay: ${total:.2f}
''')

# EXIT

print('Exiting the system')
print(f'\n{"=" * 50}')
