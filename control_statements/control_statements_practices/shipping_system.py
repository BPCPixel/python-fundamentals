"""
Shipping System

This program simulates a shipping system that calculates
the cost of a package based on its destination and weight.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Shipping System {"=" * 20}\n')

# Constants
NATIONAL = 10
INTERNATIONAL = 20

print(f'''Shipping Cost:
National = $10 x kilo
International = $20 x kilo
''')

# User input
destination = input('Destination (National / International): ').strip().upper()
weight = float(input('Insert the weight of your package (kg): '))

# Calculating shipping cost
shipping_cost = None

if destination == 'NATIONAL':
    shipping_cost = NATIONAL * weight
elif destination == 'INTERNATIONAL':
    shipping_cost = INTERNATIONAL * weight
else:
    print('Unknown destination. Please enter National or International.')

# Output
if shipping_cost is not None:
    print(f'\nThe shipping cost is ${shipping_cost:.2f}')

print(f'\n{"=" * 60}')