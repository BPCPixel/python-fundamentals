# This program explains how comparison operators work
# The result is always a boolean value (True or False), depending on the condition

print(f'{"=" * 20} Comparison (Relational) Operators {"=" * 20}')

a, b = 7, 5
print(f'Initial value of a: {a}, initial value of b: {b}')

# Equal operator
result = (a == b)
print(f'Result of a == b: {result}')  # False

# Not equal operator
result = (a != b)
print(f'Result of a != b: {result}')  # True

# Greater than 
result = (a > b)
print(f'Result of a > b: {result}')  # True

# Less than 
result = (a < b)
print(f'Result of a < b: {result}')  # False

# Greater than or equal to
result = (a >= b)
print(f'Result of a >= b: {result}')  # True

# Less than or equal to
result = (a <= b)
print(f'Result of a <= b: {result}')  # False
