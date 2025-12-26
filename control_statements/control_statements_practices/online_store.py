# This code simulates an online store

print(f'{"=" * 20} Online Store {"=" * 20}\n')

# User input
amount = float(input("What was the purchase amount? $"))
member = input("Are you a member of the store (Y/N)? ").strip().upper()

# Validation with control statements
if amount > 1000 and member == 'Y':
    discount = amount * 0.10
    print(f'''\nCongratulations, you have obtained a 10% discount
Purchase amount: ${amount:.2f}
Purchase discount: ${discount:.2f}
Total amount: ${(amount - discount):.2f}''')

elif member == 'Y':
    discount = amount * 0.05
    print(f'''\nCongratulations, you have obtained a 5% discount
Purchase amount: ${amount:.2f}
Purchase discount: ${discount:.2f}
Total amount: ${(amount - discount):.2f}''')

else:
    print(f'''\nWe invite you to become a new member of the store
Total amount: ${amount:.2f}''')

print(f'\n{"=" * 50}')
