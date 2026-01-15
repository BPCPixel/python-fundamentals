"""
This a program to practice my knowledge from the beginning to loops

Author: Lalo Téllez
"""

print(f'{"=" * 20} Mega Practice {"=" * 20}')

# Input data
name =  input("Type your name: ").strip()
age = input("Type your age: ").strip()

# String to Integer
age = int(age)

adult = None

# Validating age
if 100 > age >= 18:
    adult = True
elif 0 < age < 18:
    adult = False

# Printing the result of the age
if adult == True:
    print(f'Hello, {name.title()}.\nYou\'re an adult.\n')
elif adult == False:
    print(f'Hello, {name.title()}.\nYou\'re not an adult.\n')
else:
    print('Invalid age.\n')


valid_number = False

while valid_number == False:
    number = int(input('Type a number between 1 and 10: '))
    if 1 < number < 10:
        valid_number = True


print(f'{"=" * 50}')