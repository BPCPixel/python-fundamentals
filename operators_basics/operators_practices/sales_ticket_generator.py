# This program simulates a sales ticket generator
print(f'\n{"=" * 20} Sales Ticket Generator {"=" * 20}')
# User input
milk = float(input('Milk price?: '))
bread = float(input('Bread price?: '))
lettuce = float(input('Lettuce price?: '))
bananas = float(input('Bananas price?: '))

# Calculations
subtotal = milk + bread + lettuce + bananas
tax = subtotal * 0.16
total = subtotal + tax

# Ticket output
print(f'''
{'-' * 25}      
Milk price:    ${milk:.2f}
Bread price:   ${bread:.2f}
Lettuce price: ${lettuce:.2f}
Bananas price: ${bananas:.2f}
{'-' * 25}
Subtotal:   ${subtotal:.2f}
Tax (16%):  ${tax:.2f}
Total:      ${total:.2f}

{"=" * 60}
''')

