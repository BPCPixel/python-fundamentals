# This program simulates a sales ticket generator with discount

print(f'\n{"=" * 20} Sales Ticket Generator {"=" * 20}')

# User input
milk = float(input('Milk price?: $'))
bread = float(input('Bread price?: $'))
lettuce = float(input('Lettuce price?: $'))
bananas = float(input('Bananas price?: $'))
discount_percentage = float(input('Type a discount (%): '))

# Calculations
subtotal = milk + bread + lettuce + bananas
discount = subtotal * (discount_percentage / 100)
subtotal_with_discount = subtotal - discount
tax = subtotal_with_discount * 0.16
total = subtotal_with_discount + tax

# Ticket output
print(f'''
{'-' * 40}
Milk price:    ${milk:.2f}
Bread price:   ${bread:.2f}
Lettuce price: ${lettuce:.2f}
Bananas price: ${bananas:.2f}
{'-' * 40}
Subtotal:               ${subtotal:.2f}
Discount amount:        ${discount:.2f} ({discount_percentage}%)
Subtotal with discount: ${subtotal_with_discount:.2f}
Tax (16%):              ${tax:.2f}
Total:                  ${total:.2f}
{"=" * 60}
''')
