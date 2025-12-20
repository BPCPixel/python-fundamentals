# This program explains how compound assignment operators work
# They combine arithmetic operators with an assignment, making operations more concise

print(f'{"="*25} Compound Assignment Operators {"="*25}')

a, b = 10, 15
print(f'Initial value a: {a}, b: {b}\n')

# Compound operator of addition: +=
a += b  # a = a + b
print(f'Operator a += b = {a}')

# Compound operator of subtraction: -=
a = 10  # Reset a value
a -= b  # a = a - b
print(f'Operator a -= b = {a}')

# Compound operator of multiplication: *=
a = 10  # Reset a value
a *= b  # a = a * b
print(f'Operator a *= b = {a}')

# Compound operator of division: /=
a = 10  # Reset a value
a /= b  # a = a / b
print(f'Operator a /= b = {a:.2f}')

# Compound operator of floor division: //=
a = 10  # Reset a value
a //= b  # a = a // b
print(f'Operator a //= b = {a}')

print(f'{"="*60}')
