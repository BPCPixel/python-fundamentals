# This program explains how assignment operators work
# We use assignments with the (=) operator

print(f'{"="*25} Assignment operators {"="*25}')

# 1. Assignment operator syntax: Variable = Value
number = 10
text = "Hello, world"
print(f'''
Number = {number}
Text   = {text}
''')

# 2. Multiple assignment syntax
variable1, variable2 = 2, 3
a, b, c = 10, "Hello", 14.6

print(f'''
Variable 1 = {variable1}
Variable 2 = {variable2}
a = {a}
b = {b}
c = {c}
''')

# Chained assignment operators
counter1 = counter2 = 0
print(f'''
Counter 1 = {counter1}
Counter 2 = {counter2}
''')

# Swapping variable values without temporary variable
x, y = 5, 10
print(f'Initial values: x = {x}, y = {y}')
x, y = y, x
print(f'Swapped values: x = {x}, y = {y}\n')

# Receive multiple values from user input
name, last_name = input("Type your name and last name separated by a comma: ").split(",")
print(f'''
Name: {name.strip().title()}
Last name: {last_name.strip().title()}
{"="*60}
''')
